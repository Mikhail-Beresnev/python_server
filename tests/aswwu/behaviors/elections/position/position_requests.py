import requests
from settings import keys, testing

POSITION_URL = testing['base_url'] + ':' + str(testing['port']) + '/' + 'elections/position'


def get_position(position=None, election_type=None, active=None):
    optional_parameters = {
        'position': position,
        'election_type': election_type,
        'active': active
    }
    resp = requests.get(POSITION_URL, optional_parameters)
    return resp


def post_position(session, position, election_type, active, order):
    post_data = {
      'position': position,
      'election_type': election_type,
      'active': active == 'True',
      'order': int(order)
    }
    resp = session.post(POSITION_URL, json=post_data)
    return resp


def get_specified_position(position_id):
    url = POSITION_URL + '/' + position_id
    resp = requests.get(url)
    return resp


def put_specified_position(session, position_id, position, election_type, active, order):
    url = POSITION_URL + '/' + position_id
    put_data = {
        'position': position,
        'election_type': election_type,
        'active': active == 'True',
        'order': int(order)
    }
    resp = session.put(url, put_data)
    return resp
