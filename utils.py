"""
Module to hold useful utils.
"""
import csv
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import yaml


def config():
    """
    Loads config yaml file.
    :return: (dict) of config
    """
    cwd = os.getcwd()
    config_path = f"{cwd}/config.yml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def dict_to_yaml(dict_to_convert, filename):
    """
    Converts dict to a yaml file.
    :param dict_to_convert:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        f.write(yaml.dump(dict_to_convert))


def create_csv(header: str, data: list, filename="movies.csv"):
    """

    :param header: csv header row values (str)
    :param data: list of lists that needs to be writen as rows
    :param filename: the filename you wish to save the file as defaults to movies.csv
    :return: csv file of movie data
    """
    with open(filename, 'w') as movies_csv:
        movies_csv.writelines(f"{header}\n")
        moviewriter = csv.writer(movies_csv, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        for row in data:
            # print(row)
            moviewriter.writerow(row)


def multithreading(func, args,
                   workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)

    return list(res)


def multiprocessing(func, args,
                    workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)
