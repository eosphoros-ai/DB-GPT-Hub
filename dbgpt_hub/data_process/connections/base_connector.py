# -*- encoding: utf-8 -*-
from abc import ABC, abstractmethod


class BaseConnector(ABC):
    """
    基础连接接口
    """

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
        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._db = db
        # 需要子类定义
        self._conn = None
        self._cursor = None

    def __del__(self):
        """析构函数"""
        if self._cursor:
            self._cursor.close()

        if self._conn:
            self._conn.close()

    @abstractmethod
    def get_connect(self):
        """获取连接"""
        pass

    @abstractmethod
    def get_cursor(self, cursor=None):
        """获取游标"""
        pass

    @abstractmethod
    def select_db(self, db):
        """选择数据库"""
        pass

    @abstractmethod
    def get_all_tables(self, args=None):
        """查询所有表"""
        pass

    @abstractmethod
    def execute(self, sql, args=None):
        """获取SQL执行结果"""
        pass

    @abstractmethod
    def get_version(self, args=None):
        """获取MySQL版本"""
        pass

    @abstractmethod
    def get_all_table_metadata(self, args=None):
        """查询所有表的元数据信息"""
        pass

    @abstractmethod
    def get_table_metadata(self, db, table, args=None):
        """查询表字段的元数据信息"""
        pass

    @abstractmethod
    def get_table_field_metadata(self, db, table, args=None):
        """查询表字段的元数据信息"""
        pass
