"""
Main entry file for program to run and create csv file.
"""
import itertools

from justwatch_util import JWQueryTool
from tmdb import TMDBQueryTool
from utils import config, create_csv, multithreading

# Setup config as constant
CONFIG = config()
FILM_LIST = []


def create_film_list(director):
    works = TMDBQueryTool(director).find_artists_work("Director")
    for row in JWQueryTool(CONFIG).get_titles(director):
        if row[1] in works:
            FILM_LIST.append(row)


if __name__ == '__main__':
    csv_header = "Director,Title,Platform,IMDB,TMDB,URL"
    multithreading(create_film_list, CONFIG['directors'], CONFIG['noOfThreads'])

    # removes duplicates
    movies = [film_l for film_l, _ in itertools.groupby(sorted(FILM_LIST))]

    create_csv(csv_header, movies, CONFIG['csvfilename'])
