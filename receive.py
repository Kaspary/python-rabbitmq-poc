import config
from rabbitmq import RabbitMQ

class Receiver:
    
    RABBITMQ = {
        'host': config.RABBITMQ_HOST,
        'user': config.RABBITMQ_USER_SUB,
        'password': config.RABBITMQ_PASSWORD_SUB,
        'queue': config.QUEUE_NAME
    }

    def start_consuming(self):
        with RabbitMQ(**self.RABBITMQ) as rmq:
            rmq.start_consuming(self.callback)
    
    def callback(self, ch, method, properties, body):
        print("Received: %r" % body.decode())


if __name__ == '__main__':
    s = Receiver()
    try:
        s.start_consuming()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
