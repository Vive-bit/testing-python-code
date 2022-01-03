def check_db_(name):
  listOfTables = DATABASE_LOCALDATE_CURSOR.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='{}'; """.format(name)).fetchall()
  if listOfTables == []:
    return False
  else:
    return True

def create_db_table_(name):
  resl = check_db_(name)
  if resl == False:
    DATABASE_LOCALDATE_CURSOR.execute("""CREATE TABLE {} (id integer, type text)""".format(name))
    return True
  else:
    return False


g = create_db_table_("asd")
print(g)
