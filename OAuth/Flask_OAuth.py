from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

# Create Flask app and blueprint for GitHub
app = Flask(__name__)
app.secret_key = 'your_secret_key'
github_blueprint = make_github_blueprint(client_id='your_github_client_id', client_secret='your_github_client_secret')
app.register_blueprint(github_blueprint, url_prefix='/github_login')

# User redirected to GitHub to authenticate
@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for('github.login'))
    resp = github.get('/user')
    assert resp.ok, resp.text
    return 'You are logged in as: {}'.format(resp.json()['login'])


if __name__ == '__main__':
    app.run(debug=True)