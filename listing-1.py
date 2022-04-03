#!/usr/bin/python2.7
import sys
import json
import psycopg2
data = json.loads(sys.argv)
if (data["tablename"] == 'test' and
        (data["rowinfo"]["sourcerow"]["id"] == data["rowinfo"]["targetrow"]["id"])):
    conn_db1 = psycopg2.connect(database="testdb", user="test",
        password="123", host="192.168.217.161", port=5432)
    cur_db1 = conn_db1.cursor()    cur_db1.execute("DELETE FROM test WHERE id = %s" % data["rowinfo"]["targetrow"]["id"])    print(data["sourcename"])
else:
    print(data["sourcename"])
