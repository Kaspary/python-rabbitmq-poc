import multiprocessing
import time

from receive import Receiver
from send import Sender

"""
https://x-team.com/blog/set-up-rabbitmq-with-docker-compose/
https://stackoverflow.com/a/63271763/13154919
"""

def main():
    receiver = Receiver()
    proc = multiprocessing.Process(target=receiver.start_consuming)
    proc.start()
    time.sleep(0.5)
    try:
        proc.terminate()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')

def read_messages():
    sender = Sender()
    while True:
        message = input('Message: ')
        sender.send_message(message)


if __name__ == '__main__':
    main()
