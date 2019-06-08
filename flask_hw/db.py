import psycopg2

from db_config import DB_CONFIG as DB


def get_fruits():
    conn = psycopg2.connect(**DB)
    with conn.cursor() as cur:
        cur.execute("""SELECT definition
                       FROM fruits
                       ORDER BY fruit_id desc
                    """)
        return [fruit for fruit_tuple in cur.fetchall() for fruit in fruit_tuple]


def add_fruit(definition=None):
    if len(definition) > 0:
        con = psycopg2.connect(**DB)
        sql_query = """INSERT INTO fruits(definition)
                       VALUES ('{}')""".format(definition)
        print(sql_query)
        con.cursor().execute(sql_query)
        con.commit()


def remove_fruit(definition=None):
    if definition is not None:
        con = psycopg2.connect(**DB)
        sql_query = """DELETE FROM fruits
                                WHERE lower(definition) = lower('{}')""".format(definition)
        print(sql_query)
        con.cursor().execute(sql_query)
        con.commit()


def get_vegetables():
    conn = psycopg2.connect(**DB)
    with conn.cursor() as cur:
        cur.execute("""SELECT definition
                       FROM vegetables
                       ORDER BY vegetable_id DESC
                    """)
        return [vegetable for vegetable_tuple in cur.fetchall() for vegetable in vegetable_tuple]


def add_vegetable(definition=None):
    if definition is not None:
        con = psycopg2.connect(**DB)
        sql_query = """INSERT INTO vegetables(definition)
                                VALUES ('{}')""".format(definition)
        con.cursor().execute(sql_query)
        con.commit()


def remove_vegetable(definition=None):
    if definition is not None:
        con = psycopg2.connect(**DB)
        sql_query = """DELETE FROM vegetables
                                WHERE lower(definition) = lower('{}')""".format(definition)
        con.cursor().execute(sql_query)
        con.commit()
