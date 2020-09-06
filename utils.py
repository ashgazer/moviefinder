"""
Module to hold useful utils.
"""
import os

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
