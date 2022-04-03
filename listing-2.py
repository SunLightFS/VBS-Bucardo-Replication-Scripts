#!/usr/bin/python2.7
import sys
import json
import psycopg2
data = json.loads(sys.argv)
if data["tablename"] == 'test' and (data["rowinfo"]["sourcerow"]["id"] == data["rowinfo"]["targetrow"]["id"]):
    query = "SELECT MAX(id) FROM test"
    conn_db1 = psycopg2.connect(database="testdb", user="test",
        password="123", host="192.168.217.161", port=5432)
    cur_db1 = conn_db1.cursor()    conn_db2 = psycopg2.connect(database="testdb", user="test",
        password="123", host="192.168.217.162", port=5432)
    cur_db2 = conn_db1.cursor()    max_db1 = cur_db1.execute(query)[0]
    max_db2 = cur_db2.execute(query)[0]    if max_db1 >= max_db2:
        next_id = max_db1 + 1
    else:
        next_id = max_db2 + 1    cur_db1.execute("INSERT INTO test VALUES(%s, %s)" % (next_id, data["rowinfo"]["targetrow"]["sometext"]))
    cur_db2.execute("DELETE FROM test WHERE id = %s" % data["rowinfo"]["targetrow"]["id"])    print(data["sourcename"])
else:
    print(data["sourcename"])
