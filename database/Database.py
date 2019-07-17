import pymysql


class Database:

    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "password"
        db = "chat"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)

    def get_users(self):
        with self.con.cursor() as cursor:
            sql = "SELECT * FROM `user`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def add_user(self, username, password):
        with self.con.cursor() as cursor:
            sql = "INSERT INTO  `user` (`username`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
            self.con.commit()