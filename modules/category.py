from flask import request, render_template, redirect, url_for, flash,g
from bson.objectid import ObjectId
from modules.db import categories 
from datetime import datetime


def list_category():

    categorylist = categories.find({})

    return render_template("category/list_category.html", categorylist=categorylist, username=g.get("session"))


def add_category():

    if request.method == 'POST':

        name = request.form["name"]
        description = request.form["description"]

        object = {
            "name": name,
            "description": description,
            "creation_date": datetime.now(),
            "creation_user": g.get("session"),
            "modify_date": datetime.now(),
            "modify_user": g.get("session")
        }
        
        categories.insert_one(object)
        
        return redirect(url_for('categories'))

    return render_template("category/add_category.html", username=g.get("session"))

def read_category(id):

    oid = ObjectId(id)
    element = categories.find_one({"_id": oid})

    return render_template("category/read_category.html", category = element, username=g.get("session"))

def update_category(id):

    oid = ObjectId(id)
    element = categories.find_one({"_id": oid})

    if request.method == 'POST':
        oid = ObjectId(id)
        new_element = request.form
        
        categories.replace_one({"_id": oid},
        {
         "name": new_element["name"],
         "description": new_element["description"],
         "modify_date": datetime.now(),
         "modify_user": g.get("session")
         })
        
        return redirect(url_for('categories'))

    return render_template("category/update_category.html", category = element, username=g.get("session"))

def delete_category(id):
    oid = ObjectId(id)
    categories.delete_one({"_id": oid})

    return redirect(url_for('categories'))

