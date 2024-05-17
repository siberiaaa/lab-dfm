from flask import request, render_template, redirect, url_for, flash, g
from bson.objectid import ObjectId
from modules.db import tests, categories, sample_types, instructions
from datetime import datetime

def list_test():
    categorylist = -1
    sampletypelist = -1

    if categories.count_documents({}) != 0:
        categorylist = categories.find()
        
    
    if sample_types.count_documents({}) != 0:
        sampletypelist = sample_types.find()

    testlist = tests.find()

    if request.method == 'POST':
        category = request.form["category"]
        sampletype = request.form["sampletype"]

        testlist = filter_test(category, sampletype)

        return render_template("test/list_test.html", testlist=testlist, categorylist=categorylist, sampletypelist=sampletypelist, username=g.get("session"))


    return render_template("test/list_test.html", testlist=testlist, categorylist=categorylist, sampletypelist=sampletypelist, username=g.get("session"))

def filter_test(category, sampletype):
    if category != "" and sampletype != "":
        tests_filtered = tests.find({"category":category, "sampletype":sampletype})
    elif category != "":
        tests_filtered = tests.find({"category":category})
    elif sampletype != "":
        tests_filtered = tests.find({"sampletype":sampletype})
    else:
        tests_filtered = tests.find()

    return tests_filtered


def add_test():

    categorylist = -1
    sampletypelist = -1
    instructionlist = -1


    if categories.count_documents({}) != 0:
        categorylist = categories.find()
        
    
    if sample_types.count_documents({}) != 0:
        sampletypelist = sample_types.find()
        
 
    if instructions.count_documents({}) != 0:
        instructionlist = instructions.find()


    if request.method == 'POST':
        name = request.form["name"]
        description = request.form["description"]
        category = request.form["category"]
        sampletype = request.form["sampletype"]
        price = request.form["price"]
        instruction = request.form["instruction"]
        
        if category == "":
            flash("You must select a category, if it doesn't exist, add it.")
   
        if sampletype == "":
            flash("You must select a sample type, if it doesn't exist, add it.")
        
        if instruction == "":
            flash("You must select a instruction, if it doesn't exist, add it.")

        if instructions != "" and sampletype != "" and category != "":
            object = {
                "name": name,
                "description": description,
                "category": category,
                "sampletype": sampletype,
                "price": price,
                "instruction": instruction,
                "creation_date": datetime.now(),
                "creation_user": g.get("session"),
                "modify_date": datetime.now(),
                "modify_user": g.get("session")
            }
            
            tests.insert_one(object)
            
            return redirect(url_for('tests'))

    return render_template("test/add_test.html", categorylist=categorylist, sampletypelist=sampletypelist, instructionlist=instructionlist, username=g.get("session"))

def read_test(id):

    oid = ObjectId(id)
    element = tests.find_one({"_id": oid})

    category = categories.find_one({"_id": element["category"]})
    sampletype = sample_types.find_one({"_id": element["sampletype"]})
    instruction = instructions.find_one({"_id": element["instruction"]})

    if category == None:
        category_name = "Not found"
    else:
        category_name = category["name"]

    if sampletype == None:
        sampletype_name = "Not found"
    else:
        sampletype_name = sampletype["name"]

    if instruction == None:
        instruction_name = "Not found"
    else:
        instruction_name = instruction["name"]

    
    
    

    return render_template("test/read_test.html", test = element, category_name=category_name, sampletype_name=sampletype_name, instruction_name=instruction_name, username=g.get("session"))

def update_test(id):
    categorylist = -1
    sampletypelist = -1
    instructionlist = -1


    if categories.count_documents({}) != 0:
        categorylist = categories.find()
        
    
    if sample_types.count_documents({}) != 0:
        sampletypelist = sample_types.find()
        
 
    if instructions.count_documents({}) != 0:
        instructionlist = instructions.find()

    oid = ObjectId(id)
    element = tests.find_one({"_id": oid})

    if request.method == 'POST':
        oid = ObjectId(id)
        new_element = request.form

        if new_element["category"] == "" or new_element["sampletype"] == "" or new_element["instruction"] == "":
            #flash
            return

        
        tests.replace_one({"_id": oid},
        {
         "name": new_element["name"],
         "description": new_element["description"],
         "category": new_element["category"],
         "sampletype": new_element["sampletype"],
         "price": new_element["price"],
         "instruction": new_element["instruction"],
         "modify_date": datetime.now(),
         "modify_user": g.get("session")
         })
        
        return redirect(url_for('tests'))

    return render_template("test/update_test.html", test = element, categorylist=categorylist, sampletypelist=sampletypelist, instructionlist=instructionlist, username=g.get("session"))

def delete_test(id):
    oid = ObjectId(id)
    tests.delete_one({"_id": oid})

    return redirect(url_for('tests'))

