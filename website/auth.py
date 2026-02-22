import pymysql as  mariadb
import sys

def load_secrets(filepath):
    secrets = {}
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            secrets[key.strip()] = value.strip()
    return secrets

def get_db_connection():
    try:
        secrets = load_secrets("/var/www/flaskapp/website/secrets.txt")
        conn = mariadb.connect(
            user=secrets["DB_USER"],
            password=secrets["DB_PASSWORD"],
            host="localhost",
            database=secrets["DB_NAME"]
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None


def authenticate_user(name, password):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM submissions WHERE name='{name}' AND password='{password}'")
        #cur.execute("SELECT * FROM submissions WHERE name=? AND password=?", (name, password))
        user = cur.fetchone()
        conn.close()
        return user
    return None
