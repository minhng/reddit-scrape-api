from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import praw
import os
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

application = Flask(__name__)
CORS(application)
api = Api(application)
reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent=os.getenv('REDDIT_USER_AGENT'))


class Posts(Resource):
    def __init__(self):
        self.subreddit_name = parser.parse_args().get('subreddit_name', None)

    def get(self):
        hot, new = [], []
        hot_posts = reddit.subreddit(self.subreddit_name).hot(limit=10)
        new_posts = reddit.subreddit(self.subreddit_name).new(limit=10)

        for h in hot_posts:
            hot.append({'title': h.title, 'num_comments': h.num_comments,
                        'id': h.id, 'score': h.score, 'url': h.url})
        for n in new_posts:
            new.append({'title': n.title, 'num_comments': n.num_comments,
                        'id': n.id, 'score': n.score, 'url': n.url})
        return jsonify(hottest=hot, newest=new)


api.add_resource(Posts, "/posts")
parser = reqparse.RequestParser()
parser.add_argument('subreddit_name', type=str, required=True, help='subrredit_name is required')

### Deveploment server only
# if __name__ == '__main__':
#     application.run(debug=True)
