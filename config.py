from decouple import config

QUEUE_NAME = config('QUEUE_NAME')
RABBITMQ_HOST = config('RABBITMQ_HOST')
RABBITMQ_USER_SUB = config('RABBITMQ_USER_SUB')
RABBITMQ_PASSWORD_SUB = config('RABBITMQ_PASSWORD_SUB')
RABBITMQ_USER_PUB = config('RABBITMQ_USER_PUB')
RABBITMQ_PASSWORD_PUB = config('RABBITMQ_PASSWORD_PUB')