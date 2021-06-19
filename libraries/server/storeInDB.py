import sqlite3
from sqlite3 import Error

def convert_into_binary(file_path):
  with open(file_path, 'rb') as file:
    binary = file.read()
  return binary

def insert_into_database(file_path_name, file_blob, file_checksum): 
  try:
    conn = sqlite3.connect('app.db')
    print("[INFO] : Successful DB connection!")
    cur = conn.cursor()
    sql_insert_file_query = '''INSERT INTO uploads(file_name, file_blob, file_checksum)
      VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql_insert_file_query, (file_path_name, file_blob, file_checksum))
    conn.commit()
    print("[INFO] : The blob for ", file_path_name, " is in the database!") 
    last_updated_entry = cur.lastrowid
    return last_updated_entry
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "[ERROR : DB Error]"




