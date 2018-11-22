import json
from flask import Flask
from flask import request
from models import UserReview
from flask_restful import Api, Resource, reqparse
from peewee import IntegrityError

class UserReviewHandler(Resource):
    def get(self, id=None):
        if request.method == 'GET':
            if (id==None):
                return None, 400
            else:
                results = UserReview().select().where(UserReview.id == id)
                for result in results:
                    if (id == result.id):
                        return result.as_json(), 200
                return {
                    "message" : "user_review not found"
                }, 404
        else:
            return {
                "message" : "method not allowed"
            }, 405

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
            return {
                "message" : "method not allowed"
            }, 405

    def put(self, id=None):
        if request.method == 'PUT':
            if (id==None):
                return None
            else:
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
                    query  = UserReview().select().where(UserReview.id == id)
                    if (len(query) == 0):
                        return {
                            "message" : "user_review not found"
                        }, 404                        
                    if ((query[0].order_id) == data["order_id"] and (query[0].user_id) == data["user_id"] and (query[0].product_id) == data["product_id"]):
                        UserReview().update(**data).where(UserReview.id == id).execute()
                        return query[0].as_json(), 200
                    else:
                        raise IntegrityError
                except ValueError:
                    return None, 400
                except IntegrityError:
                    query  = UserReview().select().where(UserReview.id == id)
                    if ((query[0].user_id) != data["user_id"]):
                        return {
                            "message": "id user_review {} is not owned by {}".format(id, args["user_id"])
                        }, 400
                    elif ((query[0].order_id) != data["order_id"]):
                        return {
                            "message": "id user_review {} doesn't match with order_id {}".format(id, args["order_id"])
                        }, 400
                    elif ((query[0].product_id) != data["product_id"]):
                        return {
                            "message": "id user_review {} doesn't match with product_id {}".format(id, args["product_id"])
                        }, 400       
        else:
            return {
                "message" : "method not allowed"
            }, 405

    def delete(self, id=None):
        if request.method == 'DELETE':
            model = UserReview()
            results = model.select()
            for result in results:
                if (id == result.id):
                    result.delete_instance(recursive=False)
                    return {
                        "message" : "{} is deleted".format(id)
                    }, 200
            return {
                "message" : "The requested resource is no longer available at the server"
            }, 410
        else:
            return {
                "message" : "method not allowed"
            }, 405