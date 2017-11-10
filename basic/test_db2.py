# encoding: utf-8


import sqlite3

con = sqlite3.connect('d:/tmp/test.db')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS t_test1 (name char(10), job char(10))')
cursor.execute('INSERT INTO t_test1 VALUES (?, ?)', ['zhang', 'dev'])
cursor.execute('SELECT * FROM t_test1')
colnames = next(zip(*cursor.description))
# list(zip(*cursor.description))[0] 如果只要第一个元素，那么用next
# In Python 2, zip returned a list. In Python 3, zip returns an iterable object. But you can make it into a list just by calling list, e.g. list(zip(*ngram))
# 输出数据是这样的 (('name', None, None, None, None, None, None),)
# 用*传参和不加*，不一样
print(colnames)
for row in cursor.fetchall():
    print(row)
con.commit()
print('你好')