from flask import request, render_template, redirect, url_for, flash, make_response, g
from bson.objectid import ObjectId
from modules.db import users 
from datetime import datetime

def login():
    if request.method == 'POST':

        user = request.form["user"]
        password = request.form["password"]
        
        user = users.find_one({"user": user, "password": password})

        if user == None:
            flash("Username or password incorrect.")
        else:
            resp = make_response(redirect(url_for("home")))
            resp.set_cookie("session", str(user["_id"]))
            return resp

    return render_template("authentication/login.html", username=g.get("session"))

def signup():

    if request.method == 'POST':

        user = request.form["user"]
        name = request.form["name"]
        password = request.form["password"]
        password2 = request.form["password2"]

        if password != password2:
            flash("Enter same password")
        else:
            object = {
                "user": user,
                "name": name,
                "password": password,
                "singup_date": datetime.now()
            }
            
            users.insert_one(object)
            
            return redirect(url_for('login'))

    return render_template("authentication/signup.html", username=g.get("session"))


def logout():

    resp = make_response(redirect(url_for("home")))
    resp.set_cookie('session', '', expires=0)

    return resp