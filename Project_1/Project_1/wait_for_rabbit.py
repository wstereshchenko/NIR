import os
import time
import pika


AMQP_CREDENTIALS = pika.PlainCredentials(os.getenv('RABBITMQ_DEFAULT_USER', 'guest'),
                                         os.getenv('RABBITMQ_DEFAULT_PASS', 'guest'))
AMQP_PARAMETERS = pika.ConnectionParameters(host=os.getenv('RABBITMQ_HOST', 'rabbitmq'),
                                            port=int(os.getenv('RABBITMQ_PORT', 5672)),
                                            virtual_host=os.getenv('RABBITMQ_DEFAULT_VHOST', '/'),
                                            credentials=AMQP_CREDENTIALS)
time.sleep(15)
# wait while RABBITMQ is not ready
while True:
    try:
        print('Trying to connect to RABBITMQ...')
        amqp_connection = pika.BlockingConnection(parameters=AMQP_PARAMETERS)
        print('RABBITMQ connection SUCCESS')
        amqp_connection.close()
        break
    except pika.exceptions.AMQPConnectionError as err:
        print(err)
        print('RABBITMQ connection FAIL')
        time.sleep(5)
