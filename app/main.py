from flask import Blueprint

main: Blueprint = Blueprint("main", __name__)


@main.route("/home")
def home():
    return "<h1>Hello</h1>"
