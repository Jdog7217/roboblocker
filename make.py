import sqlite3 as sl

acc = sl.connect('main.db')

with acc: 
    acc.execute("""
        CREATE TABLE server (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serverid INTEGER NOT NULL,
            verify BOOLEAN, 
            method INTEGER,
            channel INTEGER,
            role INTEGER,
            disabled BOOLEAN DEFAULT False
        );
    """)  
with acc:
    acc.execute("""
        CREATE TABLE logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serverid INTEGER NOT NULL,
            userid INTEGER, 
            operatorid INTEGER,
            event STRING,
            time INTEGER
        );
    """)  