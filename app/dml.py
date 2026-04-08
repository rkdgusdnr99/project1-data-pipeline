from db import get_connection

def get_all_user_ids():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users")
    ids = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return ids

def get_all_user_countries():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT country FROM users")
    countries = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return countries