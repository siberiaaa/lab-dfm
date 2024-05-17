from flask import request, render_template, redirect, url_for, flash, g
from bson.objectid import ObjectId
from modules.db import instructions 
from datetime import datetime


def list_instruction():

    instructionlist = instructions.find({})

    return render_template("instruction/list_instruction.html", instructionlist=instructionlist, username=g.get("session"))


def add_instruction():

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
        
        instructions.insert_one(object)
        
        return redirect(url_for('instructions'))

    return render_template("instruction/add_instruction.html", username=g.get("session"))

def read_instruction(id):

    oid = ObjectId(id)
    element = instructions.find_one({"_id": oid})

    return render_template("instruction/read_instruction.html", instruction = element, username=g.get("session"))

def update_instruction(id):

    oid = ObjectId(id)
    element = instructions.find_one({"_id": oid})

    if request.method == 'POST':
        oid = ObjectId(id)
        new_element = request.form
        
        instructions.replace_one({"_id": oid},
        {
         "name": new_element["name"],
         "description": new_element["description"],
         "modify_date": datetime.now(),
         "modify_user": g.get("session")
         })
        
        return redirect(url_for('instructions'))

    return render_template("instruction/update_instruction.html", instruction = element, username=g.get("session"))

def delete_instruction(id):
    oid = ObjectId(id)
    instructions.delete_one({"_id": oid})

    return redirect(url_for('instructions'))

