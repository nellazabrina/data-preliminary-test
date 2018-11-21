import json
from flask import Flask
from flask import request
from models import UserReview
from flask_restful import Api, Resource, reqparse
from peewee import IntegrityError

class UserReviewHandler(Resource):
    def get(self, id=None):
        if request.method == 'GET':
            model = UserReview()
            results = model.select().where(id = id)
            for result in results:
                if (id == result['id']):
                    return result.as_json(), 200
                return "user_review not found", 404
        else:
            return "method not allowed", 405

    def post(self, id=None):
        if request.method == 'POST':
            parser = reqparse.RequestParser()
            parser.add_argument("order_id")
            parser.add_argument("product_id")
            parser.add_argument("user_id")
            parser.add_argument("rating")
            parser.add_argument("review")
            args = parser.parse_args()
            try:
                data = {
                    "order_id" : int(args["order_id"]),
                    "product_id" : int(args["product_id"]),
                    "user_id" : args["user_id"],
                    "rating" : float(args["rating"]),
                    "review" : args["review"]
                }
                created = UserReview.create(**data)
                return created.as_json(), 201
            except ValueError:
                return None, 400
            except IntegrityError:
                return {
                    "message": "Order with id {} already exists".format(args["order_id"])
                }, 400
        else:
            return "method not allowed", 405

    def put(self, id=None):
        if request.method == 'PUT':
            model = UserReview()
            parser = reqparse.RequestParser()
            parser.add_argument("order_id")
            parser.add_argument("product_id")
            parser.add_argument("user_id")
            parser.add_argument("rating")
            parser.add_argument("review")
            args = parser.parse_args()
            results = model.select()
            for result in results:
                if (id == result.id):
                    updated = UserReview.update(rating = args["rating"], review = args["review"]).where(id == id)
                    print(updated)
                    return updated.as_json(), 200                
            try:
                data = {
                    "order_id" : int(args["order_id"]),
                    "product_id" : int(args["product_id"]),
                    "user_id" : args["user_id"],
                    "rating" : float(args["rating"]),
                    "review" : args["review"]
                }
                created = UserReview.create(**data)
                return created.as_json(), 201
            except ValueError:
                return None, 400
        else:
            return "method not allowed", 405

    def delete(self, id=None):
        if request.method == 'DELETE':
            model = UserReview()
            results = model.select()
            for result in results:
                if (id == result.id):
                    result.delete_instance(recursive=False)
                    return "{} is deleted".format(id), 200
            return "The requested resource is no longer available at the server", 410
        else:
            return "method not allowed", 405