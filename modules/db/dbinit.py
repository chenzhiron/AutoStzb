import sqlite3
import json
from modules.config import tasks_config
from modules.db.dbexecute import (
    CREATE_DB_TABLE,
    DROP_DB_TABLE,
    INSERT_DB_DATA,
    SELECT_DB_ALL,
    SELECT_DB_WHERE_NAME,
    UPDATE_DB_DATA,
)


class Db:
    def __init__(self, dbname):
        self.dbname = dbname
        self._init_db()

    def _init_db(self):
        # 仅在需要时创建连接（线程/进程安全）
        conn = sqlite3.connect(self.dbname, timeout=10)
        conn.execute(CREATE_DB_TABLE)
        conn.commit()
        conn.close()

    def init_write_data(self):
        con.init_config(tasks_config)

    def remove_table(self):
        conn = self.get_conn()

        conn.execute(DROP_DB_TABLE)
        conn.commit()

    def init_config(self, configdict: dict[str, dict]):
        self.remove_table()
        self._init_db()
        for key, value in configdict.items():
            self.write(key, value)

    def get_conn(self):
        return sqlite3.connect(self.dbname, timeout=10)

    def write(self, name, config):
        conn = self.get_conn()

        conn.execute(
            INSERT_DB_DATA,
            (name, json.dumps(config)),
        )
        conn.commit()

    def update(self, name, config):
        conn = self.get_conn()

        conn.execute(UPDATE_DB_DATA, (json.dumps(config), name))
        conn.commit()

    def select(self, name=None):
        conn = self.get_conn()

        if name:
            cursor = conn.execute(SELECT_DB_WHERE_NAME, (name,))
        else:
            cursor = conn.execute(SELECT_DB_ALL)
        rows = cursor.fetchall()
        conn.close()
        return self.postprocessing(rows, name)

    def postprocessing(self, rows, name=None):
        result = {}
        for row in rows:
            if name:
                result.update({name: json.loads(row[0])})
            else:
                result.update({row[0]: json.loads(row[1])})
        return result

    def select_task_execute(self):
        conn = self.get_conn()
        cursor = conn.execute(SELECT_DB_ALL)
        rows = cursor.fetchall()
        return self.postprocessing(rows)

    def select_format(self, name):
        conn = self.get_conn()

        cursor = conn.execute(SELECT_DB_WHERE_NAME, (name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return json.loads(row[0])
        return None


if __name__ == "__main__":
    # 测试代码
    con = Db("task.db")
    con.remove_table()
    con.init_config(tasks_config)
    v = con.select()
    for k, v in v.items():
        print(k, v)
    v2 = con.select_task_execute()
    for k, v in v2.items():
        print(k, v)
