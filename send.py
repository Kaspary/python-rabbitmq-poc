import pika

def send():
    credentials = pika.PlainCredentials('user', 'password')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=credentials
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    message = input('\nMessage: ')
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    connection.close()


if __name__ == '__main__':
    try:
        send()
    except Exception as e:
        print('Exit with error ', str(e))