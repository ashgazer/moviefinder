from utils import create_unique_list_of_lists

dummy_data = [['Noah Baumbach', 'Mistress America', 'netflix', 6.7, 6.6, 'http://www.netflix.com/title/80037275'],
              ['Noah Baumbach', 'Mistress America', 'netflix', 6.7, 6.6, 'http://www.netflix.com/title/80037275']]


def test_create_unique_list_of_lists():
    result = create_unique_list_of_lists(dummy_data)
    assert result == [
        ['Noah Baumbach', 'Mistress America', 'netflix', 6.7, 6.6, 'http://www.netflix.com/title/80037275']]
