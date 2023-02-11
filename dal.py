import sqlite3 as sl

con = sl.connect('horizon.db')

def openDB():
    con = sl.connect('horizon.db')
def closeDB():
    con.close()

def setup():
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY, key TEXT, value TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, url TEXT)')
    con.commit()

# secret data
def setSecret(key, value):
    cur = con.cursor()
    cur.execute("INSERT INTO secrets (key, value) VALUES (?, ?)", (key, value,))
    con.commit()

def getSecret(key):
    cur = con.cursor()
    cur.execute("SELECT value FROM secrets WHERE key=?", (key,))
    result = cur.fetchall()
    return result

# news data
def setNews(url):
    cur = con.cursor()
    cur.execute("INSERT INTO news (url) VALUES (?)", (url,))
    con.commit()

def getNews(url):
    cur = con.cursor()
    cur.execute("SELECT url FROM news WHERE url=?", (url,))
    result = cur.fetchall()
    return result
def getAllNews():
    cur = con.cursor()
    cur.execute("SELECT url FROM news")
    result = cur.fetchall()
    return result
def clearNews():
    cur = con.cursor()
    cur.execute(" DELETE FROM news")
    con.commit()

