import sys
from scrape import *

if __name__ == '__main__':
    try:
        checkup()
    except KeyboardInterrupt:
        print("no")
