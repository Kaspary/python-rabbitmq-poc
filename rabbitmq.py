import traceback
from pika import (
    PlainCredentials,
    ConnectionParameters,
    BlockingConnection
)


class RabbitMQ:

    def __init__(self, host, user, password, queue):
        self.connection_parameters = ConnectionParameters(
            host=host,
            credentials=PlainCredentials(user, password)
        )
        self.queue = queue
        self.connection = BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        print('Close rabbitmq connection')
        self.connection.close()

    def declare_queue(self, queue):
        self.channel.queue_declare(queue=queue)

    def add_consumer(self, queue, callback):
        print(f"Add condumer to {queue}")
        self.channel.basic_consume(
            queue=queue,
            auto_ack=True,
            on_message_callback=lambda ch, method, properties, body: callback(body, queue),
        )

    def start_consuming(self):
        print('Waiting for messages...')
        self.channel.start_consuming()

    def read_messages(self, queue, callback):
        method, body = self.get_message(queue)
        if not method:
            return
        start_message_count = method.message_count + 1
        while method is not None:
            try:
                print(f"({queue}) {start_message_count - method.message_count} from {start_message_count}")
                callback(body, queue)
                self.confirm_receipt(method.delivery_tag)
            except Exception as e:
                print(f"{e.__class__.__name__}: {traceback.format_exc()}")
            method, body = self.get_message(queue)

    def get_message(self, queue):
        method, properties, body = self.channel.basic_get(queue)
        return method, body

    def confirm_receipt(self, delivery_tag):
        self.channel.basic_ack(delivery_tag)

