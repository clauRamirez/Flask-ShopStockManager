import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def run_sql(sql, values = None):
    results = []
    conn = None
    try:
        conn = psycopg2.connect(f"dbname={getenv('DATABASE_NAME')}")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return results
        else:
            return None
