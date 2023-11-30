from flask import Flask, render_template, send_from_directory, make_response, request

import database as db
import util

app = Flask(__name__)


@app.route("/images/<img>")
def images_img(img):
    return send_from_directory("templates/images", img)


@app.route("/assets/<file>")
def assets_file(file):
    return send_from_directory("templates/assets", file)


@app.route("/assets/<resource>/<file>")
def assets_resource_file(resource, file):
    return send_from_directory(f"templates/assets/{resource}", file)


@app.route("/")
def homepage():  # put application's code here
    return render_template("index.html")


@app.route("/")
def hint():
    return render_template("hint.html")


@app.route("/")
def tasks():
    return render_template("tasks.html")


@app.route("/test")
def test():  # put application's code here
    user_id, needs_cookie = util.get_make_user(request)
    resp = make_response(render_template("hint.html"))
    resp.set_cookie("scvgr_user_id", str(user_id), 365 * 24 * 60 * 60)
    print(f"Tasks for {user_id}: {util.get_tasks(user_id)}")
    print(f"Hints for {user_id}: {util.get_hints(user_id)}")
    return resp


@app.route("/hint")
def hints():  # put application's code here
    user_id, needs_cookie = util.get_make_user(request)
    resp = make_response(render_template("hint.html"))
    resp.set_cookie("scvgr_user_id", str(user_id), 365 * 24 * 60 * 60)
    print(f"Tasks for {user_id}: {util.get_tasks(user_id)}")
    print(f"Hints for {user_id}: {util.get_hints(user_id)}")
    return resp


if __name__ == "__main__":
    app.run()
