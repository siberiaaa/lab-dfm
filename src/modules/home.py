from flask import render_template, request, make_response, redirect, url_for
from modules.db import users 
from bson.objectid import ObjectId


def homes():
    username = check_cookie()

    return render_template("base.html", username=username)

def check_cookie():
    username = ""

    if 'session' in request.cookies:
        session_id = request.cookies.get('session')

        try:
            oid = ObjectId(session_id)
            user = users.find_one({"_id": oid})

            if user == None: #cookie invalida
                resp = make_response(redirect(url_for('home')))
                resp.set_cookie('session', '', expires=0)
                return resp
            else:
                username = user["name"]

        except:
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('session', '', expires=0)
            return resp
        
    return username