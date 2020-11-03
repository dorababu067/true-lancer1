from django.db import connection

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()
    ]

def my_query():
    cursor = connection.cursor()
    #sql = "SELECT * FROM mydb1.app1_submitedassets;"
    # sql = "SELECT userid, asset_name, timeremaining, count(id) as totalcount, Max(submittime) AS latestsubmit FROM app1_submitedassets WHERE submitdate=DATE(NOW()) group by userid;"

    # sql = "SELECT userid, asset_name, timeremaining, count(id) as totalcount, Max(submittime) AS latestsubmit FROM app1_submitedassets  group by userid;"

    sql = "SELECT asset_name, userid, timeremaining, count(id) as totalcount, Max(submittime) AS latestsubmit FROM app1_submitedassets  group by asset_name;"
 
    cursor.execute(sql)
    r = dictfetchall(cursor)
    # print("my query results:", r)
    return r