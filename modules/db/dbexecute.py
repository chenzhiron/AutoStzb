CREATE_DB_TABLE = """
            CREATE TABLE IF NOT EXISTS Task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                config TEXT NOT NULL
            )
            """
DROP_DB_TABLE = "DROP TABLE IF EXISTS Task"

INSERT_DB_DATA = "INSERT OR IGNORE INTO Task (name, config) VALUES (?, ?)"

UPDATE_DB_DATA = "UPDATE Task SET config = ? WHERE name = ?"

SELECT_DB_WHERE_NAME = "SELECT config FROM Task WHERE name = ?"

SELECT_DB_ALL = "SELECT name, config FROM Task"
