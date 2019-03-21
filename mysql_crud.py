#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

print("Start CRUD Programming by Python")

con = pymysql.connect('localhost', 'root', 'p@ssw0rd2535', 'testdb')

# SHOW VERSION
with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    print("Database version: {}".format(version[0]))
print('----------------------')

# SHOW LIST DATA
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))

print('----------------------')

# SHOW DATA WITH HEADER
con = pymysql.connect(
    host='localhost',
    user='root',
    password='p@ssw0rd2535',
    db='testdb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    row = cur.fetchall()
    desc = cur.description

    print("{0:>3} {1:>10}".format(desc[0][0], desc[1][0]))

    for row in rows:
        print("{0:3} {1:>10}".format(row[0], row[2]))

print('----------------------')
# FETCH DATA MAP
myId = 4
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars WHERE id=%s", myId)

    Id, Name, Price = cur.fetchone()
    print(Id, Name, Price)
print('----------------------')

# LENGTH DATA
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars WHERE id IN(1,2,3)")
    print("The query affected {} rows".format(cur.rowcount))
print('----------------------')

# INSERT DATA
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO Cars VALUES(8, 'Toyota', 1934034)")
print('----------------------')

# UPDATE DATA
with con:
    cur = con.cursor()
    cur.execute("UPDATE Cars SET price=9000 WHERE id=8")
print('----------------------')

# DELETE DATA
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM Cars WHERE id=8")
print('----------------------')
