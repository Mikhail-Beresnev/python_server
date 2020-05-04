from settings import keys, testing
import requests

ELECTION_URL = testing['base_url'] + ':' + str(testing['port']) + '/' + 'elections/election/'


def post_candidate(session, election_id, position, username, display_name):
    """elections/election"""
    post_data = {
        'position': position,
        'username': username,
        'display_name': display_name
    }
    url = ELECTION_URL + election_id + '/candidate'
    resp = session.post(url, json=post_data)
    return resp


def get_candidate(election_id, position=None, username=None, display_name=None):
    optional_parameters = {
        'position': position,
        'username': username,
        'display_name': display_name
    }
    url = ELECTION_URL + election_id + '/candidate'
    resp = requests.get(url, params=optional_parameters)
    return resp


def get_specified_candidate(election_id, candidate_id):
    url = ELECTION_URL + election_id + '/candidate/' + candidate_id
    resp = requests.get(url)
    return resp

# (r"/elections/election/(.*)/candidate/(.*)", elections.SpecifiedCandidateHandler)
# get, put, delete
