"""
TMDB Helper module. To help making calls to tmdb module easier.
"""

import tmdbsimple as tmdb

tmdb.API_KEY = ""


class DirectorNotFound(Exception):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class TMDBQueryTool:
    """
    Helper class for querying TMDB.
    """

    def __init__(self, name):
        """

        :param name: (str) of director/artist
        """
        self.name = name
        self.person_id = self.get_person_id()

    def get_person_id(self):
        """

        :return: (int) person_id value in tmdb database.
        """
        search = tmdb.Search()
        res = search.person(query=self.name)
        try:
            return res['results'][0]['id']
        except IndexError:
            raise DirectorNotFound(f"could not find director when searching tmdb: {self.name}")

    def get_person_credits(self, job_title):
        """

        :param job_title: Credits type to filter on e.g actor, crew, director
        :return: (list) filter list of credits for person_id
        """
        person = tmdb.People(id=self.person_id)
        person_credits = person.movie_credits()['crew']

        # Generator version of code
        # for row in person_credits:
        #     if row['job'] == job_title:
        #         yield row['title']

        return [row['title'] for row in person_credits if row['job'] == job_title]

    def find_artists_work(self, job_title):
        """

        :param job_title: Credits type to filter on e.g actor, crew, director
        :return: (list) of all film titles
        """
        return self.get_person_credits(job_title)
