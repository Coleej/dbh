from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def home(username=None):
    return render_template("index.html", username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for {form.username.data}, remember me={form.remember_me.data}"
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/map")
def map():
    return render_template("map.html")
