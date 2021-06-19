
import sqlite3
from sqlite3 import Error


def isFileInDb(checksum):
    try:
        conn = sqlite3.connect('app.db')
        cur = conn.cursor()
        print("[INFO] : Connected to SQLite to read_blob_data")
        sql_fetch_blob_query = """SELECT true from uploads where file_checksum = ?"""
        cur.execute(sql_fetch_blob_query, (checksum,))
        record = cur.fetchall()
        cur.close()
    except sqlite3.Error as error:
        print("[INFO] : Failed to read blob data from sqlite table", error)
    finally:
        if conn:
            conn.close()
    if len(record):
        return True
    else:
        return False
