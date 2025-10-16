import sqlite3 as sql


def listExtension():

    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute('SELECT * FROM extension').fetchall()
    con.close()
    return data


def listStory():

    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    storydata = cur.execute(
        'SELECT name,author,clas,wordcount,story FROM Story '
        'WHERE storyID < 4').fetchall()
    con.close()
    return storydata


def listFictionStory():

    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    fictionstorydata = cur.execute(
        'SELECT name,author,clas,wordcount,story FROM '
        'Story WHERE clas LIKE "fiction"').fetchall()
    con.close()
    return fictionstorydata


def listNonFictionStory():

    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    nonfictionstorydata = cur.execute(
        'SELECT name,author,clas,wordcount,story FROM '
        'Story WHERE clas LIKE "non-fiction"').fetchall()
    con.close()
    return nonfictionstorydata


def listuserdata():

    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    userdata = cur.execute(
        'SELECT username,email,password FROM '
        'userdata').fetchall()
    con.close()
    return userdata


def listusersstorydata():

    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    usersstorydata = cur.execute('SELECT name,clas,wordcount,rating,pageperuser,story FROM Story WHERE userID LIKE "1"').fetchall()
    con.close()
    return usersstorydata

def insertuserdata(username, email, password, Gender):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO userdata ('username','email','password','Gender') VALUES (?,?,?,?)", (username, email, password, Gender))
        con.commit()
        con.close


def insertstorydata(name, clas, author, story):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Story ('name','clas','author','story') VALUES (?,?,?,?)", (name, clas, author, story))
        con.commit()
        con.close



def userIDcheckuserdata():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    emailcheckuserdata = cur.execute("SELECT DISTINCT userID FROM userdata").fetchall()
    row_countuserID = cur.rowcount
    con.close()
    return row_countuserID

def emailcheckuserdata():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    emailcheckuserdata = cur.execute("SELECT DISTINCT email FROM userdata").fetchall()

    con.close()
    return emailcheckuserdata

def usernamecheckuserdata():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    usernamecheckuserdata = cur.execute("SELECT DISTINCT username FROM userdata").fetchall()
    row_countemail = cur.rowcount
    con.close()
    return usernamecheckuserdata


