from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

def route1(app:Flask) -> None:

    @app.route("/r1")
    def r1():
        return jsonify({"msg":"ok",
        "data":"route1"})