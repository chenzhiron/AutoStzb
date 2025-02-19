import sqlite3


class LogDb:
    def __init__(self, dbname):
        self.dbname = dbname
        self._init_db()

    def _init_db(self):
        # 仅在需要时创建连接（线程/进程安全）
        conn = sqlite3.connect(self.dbname, timeout=10)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now', 'localtime')),
                leave INT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()

    def get_conn(self):
        return self.connect

    def init_conn(self):
        self.connect = sqlite3.connect(self.dbname, timeout=10)

    def write(self, content, leave=0):
        conn = self.get_conn()
        conn.execute(
            "INSERT INTO log (content, leave) VALUES (?, ?)",
            (content, leave),
        )
        conn.commit()

    def select(self, maxlen=100):
        conn = self.get_conn()
        r = conn.execute(
            """
            SELECT * FROM (
                SELECT * FROM log
                ORDER BY id DESC
                LIMIT ?
                )
                ORDER BY id ASC
            """,
            (maxlen,),
        )
        return r.fetchall()


if __name__ == "__main__":
    # 测试代码
    ldb = LogDb("log.db")
    ldb.init_conn()
    # ldb.write('12345',6)
    r = ldb.select()
    for v in r:
        print(v)
