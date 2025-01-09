import sys
import logging
import os.path
import os
import ctypes
import subprocess
import time
import json
import signal
import jaro
from neo4j import GraphDatabase

current_dir = os.path.dirname(__file__)

def handle_timeout(sig, frame):
        raise TimeoutError('took too long')

signal.signal(signal.SIGALRM, handle_timeout)

class ExecutionEvaluator:
    def __init__(self):
        self.log = open('./exc_eval.log', 'w+')
        # import datasets to 2 different data folder
        dataset_list = os.listdir(f"{current_dir}/datasets")
        self.dataset_list = dataset_list
        try:
            # iterate through all dataset folder under ./datasets
            for dataset in dataset_list:
                # import data to data folder for ground truth with cli command
                self.process = subprocess.run([
                    'sh',
                    f'{current_dir}/datasets/{dataset}/import.sh',
                    f'{current_dir}/server/server_gold/lgraph_db', f'{dataset}'
                ], stdout=self.log, stderr=self.log, close_fds=True)

                # import data to data folder for predicted result with cli command
                self.process = subprocess.run([
                    'sh',
                    f'{current_dir}/datasets/{dataset}/import.sh',
                    f'{current_dir}/server/server_predict/lgraph_db', f'{dataset}'
                ], stdout=self.log, stderr=self.log, close_fds=True)
        except Exception as e:
            logging.debug(e)

        # start 2 seperate tugraph-db server
        try:
            # start server for ground truth with cli command
            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_gold/start.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)
            time.sleep(10)

            # start server for predcited result with cli command
            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_predict/start.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)
            time.sleep(10)
        except Exception as e:
            logging.debug(e)

        # setup driver for ground truth
        self.url_gold = f"bolt://localhost:9092"
        self.driver_gold = GraphDatabase.driver(self.url_gold, auth=("admin", "73@TuGraph"))
        self.driver_gold.verify_connectivity()

        # setup driver for predicted result
        self.url_predict = f"bolt://localhost:9094"
        self.driver_predict = GraphDatabase.driver(self.url_predict, auth=("admin", "73@TuGraph"))
        self.driver_predict.verify_connectivity()

        self.session_pool = {}
        for dataset in self.dataset_list:
            self.session_pool[dataset] = []
            self.session_pool[dataset].append(self.driver_gold.session(database=dataset))
            self.session_pool[dataset].append(self.driver_predict.session(database=dataset))

    def __del__(self):
        # stop 2 seperate tugraph-db server
        try:
            # stop server for ground truth with cli command
            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_gold/stop.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)

            # stop server for predicted result with cli command
            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_predict/stop.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)
        except Exception as e:
            logging.debug(e)
    
    def restart_predict_server(self):
        try:
            # restart server for predicted result with cli command
            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_predict/start.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)
            time.sleep(10)

            # setup driver for predicted result
            self.driver_predict = GraphDatabase.driver(self.url_predict, auth=("admin", "73@TuGraph"))
            self.driver_predict.verify_connectivity()
            for dataset in self.dataset_list:
                self.session_pool[dataset][1] = self.driver_predict.session(database=dataset)
        except Exception as e:
            logging.debug(e)

    def evaluate(self, query_predict, query_gold, db_id):
        if db_id not in self.session_pool.keys():
            return 0

        # run cypher on the server for ground truth
        ret_gold = True
        try:
            res_gold = self.session_pool[db_id][0].run(query_gold).data()
        except Exception as e:
            ret_gold = False
            res_gold = e

        # run cypher on the server for predict result
        ret_predict = True
        try:
            signal.alarm(10)
            res_predict = self.session_pool[db_id][1].run(query_predict).data()
            signal.alarm(0)
        except TimeoutError as e:
            ret_predict = False
            res_predict = e
            self.restart_predict_server()
        except Exception as e:
            ret_predict = False
            res_predict = e
            if "Couldn't connect to localhost:9094 (resolved to ()):" in str(e):
                self.restart_predict_server()
        
        if ret_gold == False:
            return -1
        else:
            if ret_predict == True:
                if "SKIP" in query_gold or "LIMIT" in query_gold:
                    # if SKIP or LIMIT in cypher, only compare the size of query result
                    if len(res_gold) == len(res_predict):
                        return 1
                    else:
                        return 0
                else:
                    # else, sort all query results then compare if two results are same
                    for i in range(len(res_gold)):
                        res_gold[i] = str(res_gold[i])
                    res_gold.sort()
                    for i in range(len(res_predict)):
                        res_predict[i] = str(res_predict[i])
                    res_predict.sort()
                    if res_predict == res_gold:
                        return 1
                    else:
                        return 0
            else:
                return 0
