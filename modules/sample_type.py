from flask import request, render_template, redirect, url_for, flash, g
from bson.objectid import ObjectId
from modules.db import sample_types
from datetime import datetime


def list_sample_type():

    sample_typelist = sample_types.find({})

    return render_template("sample_type/list_sample_type.html", sample_typelist=sample_typelist, username=g.get("session"))


def add_sample_type():

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
        
        sample_types.insert_one(object)
        
        return redirect(url_for('sample_types'))

    return render_template("sample_type/add_sample_type.html", username=g.get("session"))

def read_sample_type(id):

    oid = ObjectId(id)
    element = sample_types.find_one({"_id": oid})

    return render_template("sample_type/read_sample_type.html", sample_type = element, username=g.get("session"))

def update_sample_type(id):

    oid = ObjectId(id)
    element = sample_types.find_one({"_id": oid})

    if request.method == 'POST':
        oid = ObjectId(id)
        new_element = request.form
        
        sample_types.replace_one({"_id": oid},
        {
         "name": new_element["name"],
         "description": new_element["description"],
         "modify_date": datetime.now(),
         "modify_user": g.get("session")
         })
        
        return redirect(url_for('sample_types'))

    return render_template("sample_type/update_sample_type.html", sample_type = element, username=g.get("session"))

def delete_sample_type(id):
    oid = ObjectId(id)
    sample_types.delete_one({"_id": oid})

    return redirect(url_for('sample_types'))

