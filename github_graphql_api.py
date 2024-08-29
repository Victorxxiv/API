import requests

API_URL = 'https://api.github.com/graphql'
TOKEN = 'your_github_token'

headers = {"Authorization": f"Bearer {TOKEN}"}

def fetch_repositories(username):
    query = """
    query($login: String!) {
        user(login: $login) {
            repositories(first: 10) {
                nodes {
                    name
                    url
                    description
                    stargazerCount
                }
            }
        }
    }
    """
    variables = {"login": username}
    response = requests.post(API_URL, json={"query": query, "variables": variables}. headers=headers)
    if response.status_code == 200:
        return response.json()['data']['user']['repositories']['nodes']
    else:
        raise Exception(f"Query failed with status code")
    