import logging

logging.basicConfig(filename="data/app.log", format='[%(levelname)s] - [%(asctime)s] - [%(name)s]  %(message)s',
                    level=logging.INFO)

console = logging.StreamHandler()
console.setFormatter(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)s] - [%(asctime)s] - [%(name)s]  %(message)s')
console.setFormatter(formatter)

logging.getLogger("").addHandler(console)


def get_logger(name):
    return logging.getLogger(name)
