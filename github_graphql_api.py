import requests
from dotenv import load_dotenv
import os

# Load environment veraibles from .env file
load_dotenv()

API_URL = 'https://api.github.com/graphql'
TOKEN = os.getenv('TOKEN')

headers = {"Authorization": f"Bearer {TOKEN}"}


def fetch_repositories(user_login):
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
    variables = {"login": user_login}
    response = requests.post(API_URL, json={"query": query, "variables": variables}, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['user']['repositories']['nodes']
    else:
        raise Exception(f"Query failed with status code\
                        {response.status_code}: {response.text}")


if __name__ == '__main__':
    user_input = input("Enter GitHub username: ")
    try:
        repos = fetch_repositories(user_input)
        for repo in repos:
            print(f"Repo: {repo['name']},\
                  Stars: {repo['stargazerCount']}, URL: {repo['url']}")
    except Exception as e:
        print(e)
