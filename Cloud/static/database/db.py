import pymysql


db_host = 'database-1.cjuee6yaqisf.us-west-2.rds.amazonaws.com'
db_user = 'brian'
db_password = '12345678'


def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password
            )
            print ("Successfull")
    except:
        print("Falla")