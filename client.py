"""
Main entry file for program to run and create csv file.
"""
import itertools

from justwatch_util import JWQueryTool
from tmdb import TMDBQueryTool
from utils import config, create_csv

# Setup config as constant
CONFIG = config()


def create_film_list():
    film_list = []
    for director in CONFIG['directors']:
        works = TMDBQueryTool(director).find_artists_work("Director")
        for row in JWQueryTool(CONFIG).get_titles(director):
            if row[1] in works:
                film_list.append(row)
    film_list.sort()
    return [film_list for film_list, _ in itertools.groupby(film_list)]


if __name__ == '__main__':
    movies = create_film_list()
    csv_header = "Director,Title,Platform,IMDB,TMDB,URL"
    create_csv(csv_header, movies, "movies.csv")
