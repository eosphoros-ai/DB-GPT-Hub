# -*- encoding: utf-8 -*-
import yaml
import json
import os

from dbgpt_hub.data_process.connections.mysql_connector import MySQLConnector
from dbgpt_hub.data_process.table_meta_data_processor import TableMetaDataProcessor


def get_config(path):
    config = None
    config_file_path = os.path.join(path, "db_config.yaml")
    with open(config_file_path, encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    return config


if __name__ == '__main__':
    current_path = os.path.split(os.path.realpath(__file__))[0]

    config_data = get_config(current_path)

    # 生成mysql 工具对象
    connect = None

    # 暂时只实现mysql，其他版本数据库，后续扩展
    if config_data["database"]["dbtype"] == "mysql":
        connect = MySQLConnector(host=config_data["database"]["host"], port=config_data["database"]["port"],
                                 user=config_data["database"]["user"], passwd=config_data["database"]["passwd"],
                                 db=config_data["database"]["db"])
    else:
        raise ()

    processor = TableMetaDataProcessor(connect, config_data)
    meta = processor.generate_spider_table_metadata();

    with open(os.path.join(current_path, "tables.json"), "w") as file:
        json.dump(meta, file, ensure_ascii=False, indent=1)
