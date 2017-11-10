# encoding: utf-8


import sqlite3

con = sqlite3.connect('d:/tmp/test.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE t_test (name char(10))')
cursor.execute('INSERT INTO t_test VALUES (?)', ['zhang'])
cursor.execute('SELECT * FROM t_test')
for row in cursor.fetchall():
    print(row)
con.commit()
