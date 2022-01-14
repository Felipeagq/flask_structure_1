from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask import Blueprint

r2_b = Blueprint( 'r2', __name__)

@r2_b.route('/r2')
def r2():
    return jsonify({"msg":"ok",
        "data":"route2"})


# def route2(app:Flask) -> None:

#     @app.route("/r2")
#     def r2():
#         return jsonify({"msg":"ok",
#         "data":"route2"})