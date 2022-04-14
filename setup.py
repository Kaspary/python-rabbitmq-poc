import multiprocessing
import time

from receive import main as main_receive
from send import send

proc = multiprocessing.Process(target=main_receive, args=())
proc.start()

def main():
    print('To exit press CTRL+C')
    
    time.sleep(0.5)
    while True:
        send()
    
    print('\nEnd proccess...')
    proc.terminate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        proc.terminate()
        print('\nInterrupted!')
