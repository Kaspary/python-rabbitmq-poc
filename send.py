import config
from rabbitmq import RabbitMQ

class Sender:
    
    RABBITMQ = {
        'host': config.RABBITMQ_HOST,
        'user': config.RABBITMQ_USER_PUB,
        'password': config.RABBITMQ_PASSWORD_PUB,
        'queue': config.QUEUE_NAME
    }

    def send_message(self, message):
        with RabbitMQ(**self.RABBITMQ) as rmq:
            rmq.send_message(message)


if __name__ == '__main__':
    s = Sender()
    message = input('Message: ')
    s.send_message(message)