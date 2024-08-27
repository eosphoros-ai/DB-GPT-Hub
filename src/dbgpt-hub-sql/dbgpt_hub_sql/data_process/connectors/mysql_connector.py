# -*- encoding: utf-8 -*-
from abc import ABC

import pymysql
from dbgpt_hub_sql.data_process.connections.base_connector import BaseConnector


class MySQLConnector(BaseConnector, ABC):
    def __init__(
        self,
        host="127.0.0.1",
        port=3306,
        user=None,
        passwd=None,
        db=None,
        charset="utf8",
        *args,
        **kwargs
    ):
        super().__init__(host, port, user, passwd, db, charset, args, kwargs)
        self._conn = pymysql.connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset=charset
        )
        self._cursor = self._conn.cursor()

    def __del__(self):
        """析构函数"""
        super().__del__()

    def get_connect(self):
        """获取连接"""
        return self._conn

    def get_cursor(self, cursor=None):
        """获取游标"""
        return self._conn.cursor(cursor)

    def select_db(self, db):
        """选择数据库"""
        self._conn.select_db(db)

    def get_all_tables(self, args=None):
        """查询所有表"""
        self._cursor.execute("SHOW TABLES", args)
        tables = []
        for table in self._cursor.fetchall():
            tables.append(table[0])
        return tables

    def execute(self, sql, args=None):
        """获取SQL执行结果"""
        self._cursor.execute(sql, args)
        return self._cursor.fetchall()

    def get_version(self, args=None):
        """获取MySQL版本"""
        self._cursor.execute("SELECT VERSION()", args)
        version = self._cursor.fetchone()
        print("MySQL Version : %s" % version)
        return version

    def get_all_table_metadata(self, args=None):
        """查询所有表的元数据信息"""
        sql = "SELECT * FROM information_schema.TABLES WHERE TABLE_TYPE !='SYSTEM VIEW' AND TABLE_SCHEMA NOT IN ('sys','mysql','information_schema','performance_schema')"
        self._cursor.execute(sql, args)
        return self._cursor.fetchall()

    def get_table_metadata(self, db, table, args=None):
        """查询指定表的元数据信息"""
        sql = (
            'SELECT TABLE_NAME ,TABLE_COMMENT  FROM information_schema.TABLES WHERE TABLE_NAME="'
            + table
            + '" AND TABLE_SCHEMA="'
            + db
            + '"'
        )
        self._cursor.execute(sql, args)
        return self._cursor.fetchall()

    def get_table_field_metadata(self, db, table, args=None):
        """查询表字段的元数据信息"""
        db = "'" + db + "'"
        table = "'" + table + "'"
        sql = """
        SELECT 
            ORDINAL_POSITION , COLUMN_NAME , DATA_TYPE , COLUMN_COMMENT
        FROM 
            information_schema.COLUMNS 
        WHERE 
            table_schema = %s AND table_name = %s;
        """ % (
            db,
            table,
        )
        self._cursor.execute(sql, args)
        return self._cursor.fetchall()
