from app import create_app
from flask_cors import CORS, cross_origin
import os
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()


app = create_app( os.getenv("FLASK_CONFIG") or "default")

CORS(app)


@app.route("/")
def index():
    return jsonify({"version":"v0.0.1"})

if __name__ == "__main__":
    app.run(host="0.0.0.0")