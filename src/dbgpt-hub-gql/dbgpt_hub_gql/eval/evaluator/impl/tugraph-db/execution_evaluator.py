import sys
import logging
import os.path
import os
import ctypes
import subprocess
import time
import json
from neo4j import GraphDatabase

current_dir = os.path.dirname(__file__)

class ExecutionEvaluator:
    def __init__(self):
        self.log = open('./exc_eval.log', 'w+')
        # import datasets to 2 different data folder
        dataset_list = os.listdir(f"{current_dir}/datasets")
        try:
            # iterate through all dataset folder under ./datasets
            for dataset in dataset_list:
                # import data in ci command
                self.process = subprocess.run([
                    'sh',
                    f'{current_dir}/datasets/{dataset}/import.sh',
                    f'{current_dir}/server/server_gold/lgraph_db', f'{dataset}'
                ], stdout=self.log, stderr=self.log, close_fds=True)

                self.process = subprocess.run([
                    'sh',
                    f'{current_dir}/datasets/{dataset}/import.sh',
                    f'{current_dir}/server/server_predict/lgraph_db', f'{dataset}'
                ], stdout=self.log, stderr=self.log, close_fds=True)
        except Exception as e:
            # in dev environment, start server before run tests
            logging.debug(e)

        # python start 2 seperate tugraph-db server
        try:
            # start server in ci command
            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_gold/start.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)
            time.sleep(10)

            self.process = subprocess.run([
                'sh',
                f'{current_dir}/server/server_predict/start.sh'
            ], stdout=self.log, stderr=self.log, close_fds=True)
            time.sleep(10)
        except Exception as e:
            # in dev environment, start server before run tests
            logging.debug(e)

        self.url_gold = f"bolt://localhost:9092"
        self.url_predict = f"bolt://localhost:9094"
        # driver for ground truth
        self.driver_gold = GraphDatabase.driver(self.url_gold, auth=("admin", "73@TuGraph"))
        self.driver_gold.verify_connectivity()
        # driver for predict result
        self.driver_predict = GraphDatabase.driver(self.url_predict, auth=("admin", "73@TuGraph"))
        self.driver_predict.verify_connectivity()

        self.session_pool = {}
        for dataset in dataset_list:
            self.session_pool[dataset] = []
            self.session_pool[dataset].append(self.driver_gold.session(database=dataset))
            self.session_pool[dataset].append(self.driver_predict.session(database=dataset))


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
            res_predict = self.session_pool[db_id][1].run(query_predict).data()
        except Exception as e:
            ret_predict = False
            res_predict = e
        
        if ret_gold == False:
            return 0
        else:
            if ret_predict == True:
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
