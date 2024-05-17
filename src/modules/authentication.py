from flask import request, render_template, redirect, url_for, flash, make_response, g, session
from bson.objectid import ObjectId
from modules.db import users 
from datetime import datetime, timedelta

def login():
    if request.method == 'POST':

        user = request.form["user"]
        password = request.form["password"]
        
        user = users.find_one({"user": user, "password": password})

        if user == None:
            flash("Username or password incorrect.")
        else:
            session.permanent = True
            session['session'] = str(user["_id"])
            return redirect(url_for("home"))

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
    session.pop('session', None)
    return redirect(url_for("home"))
