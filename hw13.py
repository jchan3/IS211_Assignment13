#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: hw13.py"""


import sqlite3 as lite
import sys


con = lite.connect('hw13.db')


with con:

    cur = con.cursor()

    sql = """CREATE TABLE student (id INTEGER PRIMARY KEY ASC,
                first_name TEXT, last_name TEXT);"""

    cur.execute(sql)

    sql2 = """CREATE TABLE quiz (id INTEGER PRIMARY KEY ASC,
		subject TEXT, num_questions INTEGER, date DATE);"""

    cur.execute(sql2)

    sql3 = """CREATE TABLE results (score INTEGER, quiz_id INTEGER,
                student_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz(id),				
                FOREIGN KEY (student_id) REFERENCES student(id));"""

    cur.execute(sql3)
