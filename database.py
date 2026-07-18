import sqlite3

from config import DATABASE_NAME


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                post_url TEXT PRIMARY KEY,
                title TEXT,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.commit()

    def is_post_exists(self, post_url: str) -> bool:
        self.cursor.execute(
            "SELECT 1 FROM posts WHERE post_url=?",
            (post_url,)
        )
        return self.cursor.fetchone() is not None

    def add_post(self, post_url: str, title: str):
        self.cursor.execute(
            "INSERT OR IGNORE INTO posts(post_url, title) VALUES(?, ?)",
            (post_url, title)
        )
        self.conn.commit()

    def total_posts(self):
        self.cursor.execute("SELECT COUNT(*) FROM posts")
        return self.cursor.fetchone()[0]


db = Database()
