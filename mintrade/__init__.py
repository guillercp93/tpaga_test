try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    print('--->not import pymysql<----')