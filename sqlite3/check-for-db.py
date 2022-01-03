
import sqlite3 as sl
import os


DATABASE_PATH = "data/files/localdata.db"

if not os.path.isfile('data/files/localdata.db'):
  print(f"[ERROR] [sqlite3 database] database file ({DATABASE_PATH}) not found!")
  print(f"[sqlite3 database] Creating database file in {DATABASE_PATH}")
  pass

DATABASE_LOCALDATE = sl.connect('{}'.format(DATABASE_PATH))
DATABASE_LOCALDATE_CURSOR = DATABASE_LOCALDATE.cursor()




def check_db_table_(name):
  listOfTables = DATABASE_LOCALDATE_CURSOR.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='{}'; """.format(name)).fetchall()
  if listOfTables == []:
    return False
  else:
    return True

def create_db_table_(name):
  resl = check_db_table_(name)
  if resl == False:
    DATABASE_LOCALDATE_CURSOR.execute("""CREATE TABLE {} (id integer, type text)""".format(name))
    DATABASE_LOCALDATE.commit()
    return True
  else:
    return False

def db_add_(dbname, userid, typ):
  g = check_db_table_(dbname)
  if g == False:
    return False
  userid = int(userid)
  typ = str(typ)
  g = db_check_value_(dbname,userid,typ,0)
  if g == True:
    return False
  DATABASE_LOCALDATE_CURSOR.execute("INSERT INTO {} VALUES ({}, '{}')".format(dbname, userid, typ))
  DATABASE_LOCALDATE.commit()
  return True

def db_remove_(dbname,userid,typ):
  g = check_db_table_(dbname)
  if g == False:
    return False
  userid = int(userid)
  typ = str(typ)
  g = db_check_value_(dbname,userid,typ,0)
  if g == False:
    return False
  DATABASE_LOCALDATE_CURSOR.execute("DELETE from {} WHERE id={} AND type='{}'".format(dbname, userid, typ))
  DATABASE_LOCALDATE.commit()
  return True

def db_check_value_(dbname,userid,typ,resp):
  g = check_db_table_(dbname)
  if g == False:
    return False
  userid = int(userid)
  typ = str(typ)
  resl = DATABASE_LOCALDATE_CURSOR.execute("SELECT * FROM {} WHERE id={} AND type='{}'".format(dbname, userid, typ)).fetchall()
  if resl==[]:
    return False
  else:
    if resp == 1:
      return resl
    else:
      return True

def db_listkey_(dbname,typ):
  g = check_db_table_(dbname)
  if g == False:
    return False
  typ = str(typ)
  dblist = DATABASE_LOCALDATE_CURSOR.execute("SELECT * FROM {} WHERE type='{}'; ".format(dbname,typ)).fetchall()
  return dblist



d = 123
typa = "tban"
nam = "asd"
g = create_db_table_(nam)
print(g)
i = db_listkey_(nam,typa)
print(i)
a = db_check_value_(nam,d,typa,1)
print(a)
a = db_add_(nam,d,typa)
print(a)
a = db_add_(nam,d,typa)
print(a)
a = db_check_value_(nam,d,typa,1)
print(a)
a = db_remove_(nam,d,typa)
print(a)
a = db_check_value_(nam,d,typa,1)
print(a)
i = db_listkey_(nam,typa)
print(i)

