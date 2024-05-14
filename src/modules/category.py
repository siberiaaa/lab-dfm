from flask import request, render_template, redirect, url_for, flash
from bson.objectid import ObjectId
import modules.db as db 

def list_category():

    listamaterias = db.collection.find()

    return render_template("listarmaterias.html", listamaterias=listamaterias)


def add_category():

    if request.method == 'POST':

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        cedula = request.form["cedula"]
        nombremateria = request.form["nombremateria"]
        objetivomateria = request.form["objetivomateria"]
        horasmaterias = request.form["horasmaterias"]
        nota = request.form["nota"]

        object = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "nombremateria": nombremateria,
            "objetivomateria": objetivomateria,
            "horasmaterias": horasmaterias,
            "nota": nota
        }
        
        db.collection.insert_one(object)
        
        return redirect(url_for('listarmaterias'))

    return render_template("agregarmateria.html")

def read_category(id):
    oid = ObjectId(id)
    element = db.collection.find_one({"_id": oid})

    return render_template("detallemateria.html", materia = element)

def update_category(id):
    oid = ObjectId(id)
    element = db.collection.find_one({"_id": oid})

    if request.method == 'POST':
        oid = ObjectId(id)
        new_element = request.form
        
        db.collection.replace_one({"_id": oid},
        {
         "nombre": new_element["nombre"],
         "apellido": new_element["apellido"],
         "cedula": new_element["cedula"],
         "nombremateria": new_element["nombremateria"],
         "objetivomateria": new_element["objetivomateria"],
         "horasmaterias": new_element["horasmaterias"],
         "nota": new_element["nota"]
         })
        
        return redirect(url_for('listarmaterias'))

    return render_template("actualizarmateria.html", materia = element)

def delete_category(id):
    oid = ObjectId(id)
    db.collection.delete_one({"_id": oid})

    return redirect(url_for('listarmaterias'))

