import logging

if __name__ == '__main__':
    logging.basicConfig(filename='./debug/example.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
