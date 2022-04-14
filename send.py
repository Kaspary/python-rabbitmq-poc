import pika

def send(message='Hello RabbitMQ!'):
    credentials = pika.PlainCredentials('user', 'password')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=credentials
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f"[x] Sent '{message}'")
    connection.close()


if __name__ == '__main__':
    send()