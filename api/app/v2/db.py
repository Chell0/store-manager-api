import psycopg2

db = psycopg2.connect(
    dbname='store_api'
    dbuser='machel'
    dbpswd='this-is-my-favorite-password'
    dbhost='localhost'
    dbport='5432'
)
