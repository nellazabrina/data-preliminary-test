import user_review
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(user_review.UserReviewHandler, '/api/usr-review/', '/api/usr-review/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

app.run()