import sqlite3
import json


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

    def get_conn(self):
        return sqlite3.connect(self.dbname, timeout=10)

    def write(self, name, config):
        conn = self.get_conn()
        try:
            conn.execute(
                "INSERT OR IGNORE INTO Task (name, config) VALUES (?, ?)",
                (name, json.dumps(config)),
            )
            conn.commit()
        finally:
            conn.close()

    def update(self, name, config):
        conn = self.get_conn()
        try:
            conn.execute(
                "UPDATE Task SET config = ? WHERE name = ?", (json.dumps(config), name)
            )
            conn.commit()
        finally:
            conn.close()

    def select(self, name=None):
        conn = self.get_conn()
        try:
            if name:
                cursor = conn.execute("SELECT config FROM Task WHERE name = ?", (name,))
            else:
                cursor = conn.execute("SELECT config FROM Task")
            return cursor.fetchall()
        finally:
            conn.close()

    def select_format(self, name):
        conn = self.get_conn()
        try:
            cursor = conn.execute("SELECT config FROM Task WHERE name = ?", (name,))
            for v in cursor:
                return json.loads(v[-1])
        finally:
            conn.close()


if __name__ == "__main__":
    # 测试代码
    con = Db("task.db")

    con.write("simulator", {"address": "127.0.0.1:7885"})
    
    # 查询数据
    r = con.select_format("simulator")
    print(r)
    # 更新数据
    con.update("simulator", {"address": "127.0.0.1:10086"})

    # 再次查询数据
    r2 = con.select_format("simulator")
    print(r2)
    con.write("simulator", {"address": "127.0.0.1:9999"})
