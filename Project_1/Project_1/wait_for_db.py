import os
import time
import psycopg2
import redis


DB_NAME = os.getenv('POSTGRES_DB', 'postgres')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
DB_HOST = os.getenv('POSTGRES_HOST', 'db')
DB_PORT = os.getenv('POSTGRES_PORT', 5432)

# # wait while cache is not ready
# while True:
#     try:
#         print('Trying to connect to cache...')
#         cache_client = redis.StrictRedis(host='redis', port=6379)
#         result = cache_client.get('categories')
#         print(result)
#         print('Cache connection SUCCESS')
#         break
#     except redis.ConnectionError as err:
#         print(err)
#         print('Cache connection FAIL')
#         time.sleep(5)

# wait while DB is not ready
time.sleep(15)
while True:
    try:
        print('Trying to connect to DB...')
        db_connection = psycopg2.connect(dbname=DB_NAME,
                                         user=DB_USER,
                                         password=DB_PASSWORD,
                                         host=DB_HOST,
                                         port=DB_PORT)
        print('DB connection SUCCESS')
        db_connection.close()
        break
    except psycopg2.OperationalError as err:
        print(err)
        print('DB connection FAIL')
        time.sleep(5)
