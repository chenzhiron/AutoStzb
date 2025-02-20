import sqlite3
import json
from config import tasks_config


class Db:
    def __init__(self, dbname):
        self.dbname = dbname
        self._init_db()

    def _init_db(self):
        # 仅在需要时创建连接（线程/进程安全）
        conn = sqlite3.connect(self.dbname, timeout=10)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                config TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()
        
    def init_write_data(self):
        con.init_config(tasks_config)

    def remove_table(self):
        conn = self.get_conn()

        conn.execute("DROP TABLE IF EXISTS Task")
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
            "INSERT OR IGNORE INTO Task (name, config) VALUES (?, ?)",
            (name, json.dumps(config)),
        )
        conn.commit()

    def update(self, name, config):
        conn = self.get_conn()

        conn.execute(
            "UPDATE Task SET config = ? WHERE name = ?", (json.dumps(config), name)
        )
        conn.commit()

    def select(self, name=None):
        conn = self.get_conn()

        if name:
            cursor = conn.execute("SELECT config FROM Task WHERE name = ?", (name,))
        else:
            cursor = conn.execute("SELECT config FROM Task")
        return cursor.fetchall()

    def select_format(self, name):
        conn = self.get_conn()

        cursor = conn.execute("SELECT config FROM Task WHERE name = ?", (name,))
        for v in cursor:
            return json.loads(v[-1])


if __name__ == "__main__":
    # 测试代码
    con = Db("task.db")
    con.remove_table()
    con.init_config(tasks_config)
    v = con.select()
    for r in v:
        print(r)
