# -*- encoding: utf-8 -*-
class TableMetaDataProcessor:
    def __init__(self, conn, config_data):
        self.__conn = conn
        self.__config_data = config_data

    # 生成表元数据信息
    def _generate_table_meta_data(self, db, tables, pks, fks):
        table_names_original = tables
        column_names = [[-1, "*"]]
        column_names_original = [[-1, "*"]]
        column_types = []
        foreign_keys = []
        primary_keys = []
        table_names = []
        for i in range(len(tables)):
            table_meta = self.__conn.get_table_metadata(db, tables[i])
            table_names.append(table_meta[0][1])
            meta_data = self.__conn.get_table_field_metadata(db, tables[i])
            for md in meta_data:
                column_names.append([i, md[3]])
                column_names_original.append([i, md[1]])
                if md[2] == "varchar" or md[2] == "text":
                    column_types.append("text")
                elif md[2] == "timestamp" or md[2] == "datetime":
                    column_types.append("time")
                else:
                    column_types.append("number")
                # 解析主键
                if pks[tables[i]] == md[1]:
                    primary_keys.append(len(column_names_original))

        # 解析外键
        if fks:
            for key, fk in fks.items():
                fk_item = []
                for item in fk:
                    for k, f in item.items():
                        table_index = table_names_original.index(k)
                        # 遍历 column_names_original
                        for cno in range(len(column_names_original)):
                            if column_names_original[cno][0] == table_index and column_names_original[cno][1] == f:
                                fk_item.append(cno)
                                break
                foreign_keys.append(fk_item)

        return {"column_names": column_names, "column_names_original": column_names_original,
                "column_types": column_types,
                "db_id": db, "foreign_keys": foreign_keys, "primary_keys": primary_keys, "table_names": table_names,
                "table_names_original": table_names_original}

    def generate_spider_table_metadata(self):
        table_configs = self.__config_data["table-configs"]

        # 结果列表
        result = []
        db_id = self.__config_data["database"]["db"]
        for key, value in table_configs.items():
            tables = value["tables"]
            primary_keys = value["primary_keys"]
            foreign_keys = value["foreign_keys"]

            # 表元数据
            table_meta_data = self._generate_table_meta_data(db_id, tables, primary_keys, foreign_keys)
            result.append(table_meta_data)

        return result
