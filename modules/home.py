from flask import render_template, request, make_response, redirect, url_for, session
from modules.db import users 
from bson.objectid import ObjectId


def homes():
    username = check_cookie()

    return render_template("base.html", username=username)

def check_cookie():
    username = ""

    if 'session' in session:
        session_id = session['session']

        try:
            oid = ObjectId(session_id)
            user = users.find_one({"_id": oid})

            if user == None: #cookie invalida
                session.pop('session', None)
                return redirect(url_for("home"))
            else:
                username = user["name"]

        except:
            session.pop('session', None)
            return redirect(url_for("home"))
        
    return username