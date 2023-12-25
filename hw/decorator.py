# * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
import time
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def printing_decorator(target_function):
    logging.info(f'Init for {target_function.__name__}')

    def inner_func(*args,**kwargs):
        start = time.time()
        logging.info(f'Start: {start}')
        result = target_function(*args,**kwargs)
        end = time.time()
        logging.info(f'End: {end}')
        print(f'Calc"s  time method ({target_function.__name__}):  ', end - start)
        logging.info(f'Calc"s  time method ({target_function.__name__}): {end-start}')
        return result

    return inner_func