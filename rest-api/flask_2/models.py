import sqlite3 as sql

def insert_account_holder(email,username,phone,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)", (email,username,phone,password))
    con.commit()
    con.close()

def insert_contact(name,phone,username,email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contact (name,phone,username,email) VALUES (?,?,?,?)", (name,phone,username,email))
    con.commit()
    con.close()

def select_account_holder(params=()):
    con = sql.connect("database.db")
    cur = con.cursor()
    if params==():
        cur.execute("select * from account_holder")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from account_holder"

        result = cur.execute(string)
        con.close()
        return result.fetchall()

def select_contact(params=()):
    con = sql.connect("database.db")
    cur = con.cursor()
    if params==():
        cur.execute("select * from contact")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from contact"

        result = cur.execute(string)
        con.close()
        return result.fetchall()