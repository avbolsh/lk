from . import main

@main.route("/")
def index():
    return "<h1>Main blueprint</h1>"