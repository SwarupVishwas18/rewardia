import sqlite3 as sql
from colorama import Fore


class DB:
    def __init__(self) -> None:
        self.conn = sql.connect("database.db")

        print(Fore.GREEN)

        self.conn.execute(
            """
            CREATE TABLE users IF NOT EXISTS(
                     id INT PRIMARY KEY NOT NULL, 
                     username VARCHAR(255)  NOT NULL, 
                     password VARCHAR(255)  NOT NULL, 
                     points INT  DEFAULT 0, 
                     key TEXT NOT NULL
            );
        """
        )

        self.conn.execute(
            """
            CREATE TABLE tasks IF NOT EXISTS(
                     id INT PRIMARY KEY NOT NULL, 
                     task VARCHAR(255)  NOT NULL, 
                     status INT  NOT NULL, 
                     points INT  NOT NULL, 
                     user_id INT NOT NULL
            );
        """
        )

        self.conn.execute(
            """
            CREATE TABLE rewards IF NOT EXISTS(
                     id INT PRIMARY KEY NOT NULL, 
                     title VARCHAR(255)  NOT NULL, 
                     points INT  NOT NULL,
                     status INT  NOT NULL, 
                     user_id INT NOT NULL

            );
        """
        )

        print("Database Initialized 100%")

    def user_exists(self, username):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users")
        result = cur.fetchall()
        for user in result:
            if user[1] == username:
                return user[0]

        return False

    def get_password(self, user_id):
        cur = self.conn.cursor()
        cur.execute("SELECT password FROM users WHERE id=?", (user_id))
        return cur.fetchone()[0]

    def get_key(self, user_id):
        cur = self.conn.cursor()
        cur.execute("SELECT key  FROM users WHERE id=?", (user_id))
        return cur.fetchone()[0]

    def insert_user(self, username, pwd, key):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO (username, password, key) VALUES(?,?, ?)", (username, pwd, key)
        )

    def get_points(self, user_id):
        cur = self.conn.cursor()
        cur.execute("SELECT points FROM users WHERE id=?", (user_id))
        return cur.fetchone()[0]

    def update_points(self, user_id, points):
        cur = self.conn.cursor()
        new_pts = self.getPoints(user_id) + points
        cur.execute("UPDATE users SET points = ? WHERE id=?", (new_pts, user_id))

    def get_tasks(self, user_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id=? AND status=?", (user_id, 0))
        return cur.fetchall()

    def update_task_status(self, id, new_val):
        cur = self.conn.cursor()
        cur.execute("UPDATE tasks SET status = ? WHERE id=?", (new_val, id))
        cur = self.conn.cursor()
        cur.execute("SELECT points FROM tasks WHERE id=?", (id))
        return cur.fetchone()[0]

    def add_task(self, title, points, user_id):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO tasks(task, points, status,user_id) VALUES(?,?,?,?)",
            (title, points, 0, user_id),
        )
        return True

    def get_rewards(self, user_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM rewards WHERE user_id=?", (user_id))
        return cur.fetchall()

    def delete_rewards(self, rew_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM rewards WHERE id=?", (rew_id))
        pts = cur.fetchone()[2]
        cur = self.conn.cursor()
        cur.execute("DELETE FROM rewards WHERE id=?", (rew_id))
        return pts
