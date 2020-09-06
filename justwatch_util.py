"""
Helper tool for reading from justwatch api
"""

from justwatch import JustWatch


class JWQueryTool:

    def __init__(self, config):
        self.just_watch = JustWatch(country='GB')
        self.provider_data = self.just_watch.get_providers()
        self.config = config

    def create_provider_id_lookup(self, row_name):
        return {row['id']: row.get(row_name, 0) for row in self.provider_data}

    @staticmethod
    def get_score(score_list: list, provider_name: str):
        score_list = [score['value'] for score in score_list if score.get('provider_type') == f'{provider_name}:score']
        return score_list[0] if score_list else 0

    def get_titles(self, query):
        provider_to_id = self.create_provider_id_lookup('short_name')
        provider_lookup = self.create_provider_id_lookup('technical_name')
        titles = []
        rs = self.just_watch.search_for_item(monetization_types=['flatrate'],
                                             query=query, content_types=['movie'], providers=self.config['providers'])
        for item in rs['items']:

            for offer in item['offers']:
                if offer['monetization_type'] in ['flatrate', 'free']:  # not in ['rent', 'buy', 'cinema']:
                    imdb_score = self.get_score(item['scoring'], "imdb")

                    tmdb_score = self.get_score(item['scoring'], "tmdb")

                    if provider_to_id.get(offer['provider_id'], 'nfx') in self.config['providers'] and offer[
                        'urls'].get(
                            'presentation_type', 'hd') == 'hd':
                        titles.append(
                            [query, item['title'], provider_lookup.get(offer['provider_id'], offer['provider_id']),
                             imdb_score, tmdb_score, offer['urls']['standard_web']])

        return titles
