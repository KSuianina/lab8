import pymysql


def connect():
    host = "localhost"
    user = "root"
    password = ""
    connection = pymysql.connect(host=host, user=user, password=password)
    connection.cursor().execute("USE laba")
    return connection
