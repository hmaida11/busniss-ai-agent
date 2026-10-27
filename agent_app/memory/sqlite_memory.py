import sqlite3
from typing import List, Tuple

class SQLiteMemory:
    def __init__(self, db_path: str = "agent_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                "CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, role TEXT, content TEXT)"
            )

    def add_message(self, role: str, content: str):
        with self.conn:
            self.conn.execute("INSERT INTO history (role, content) VALUES (?, ?)", (role, content))

    def get_history(self) -> List[Tuple[str, str]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT role, content FROM history ORDER BY id ASC")
        return cursor.fetchall()
