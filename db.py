import psycopg2

db = psycopg2.connect(
    dbname='store_api',
    user='machel',
    password=',./,./',
    host='localhost',
    port='5432'
)
