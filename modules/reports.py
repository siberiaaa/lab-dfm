from flask import request, render_template, g, flash
from bson.objectid import ObjectId
from modules.db import tests, categories, instructions


def tests_in_categories():
    testlist = -1
    categorylist = -1
    categories_dictionary = -1

    if tests.count_documents({}) != 0:
        testlist = list(tests.find())
    
    if categories.count_documents({}) != 0:
        categorylist = list(categories.find())

    if testlist == -1 or categorylist == -1:
        flash("Add more tests with existent categories to generate report.")
    else:   
        categories_dictionary = {}

        for category in categorylist:
            repetitions = 0

            for test in testlist:
                if str(test["category"]) == str(category["_id"]):
                    repetitions += 1
            
            categories_dictionary[category["name"]] = repetitions

    return render_template("reports/tests_in_categories.html", testlist=testlist, categorylist=categorylist, categories_dictionary=categories_dictionary, username=g.get("session"))

def common_instruction():
    testlist = -1
    instructionlist = -1
    instructions_dictionary = -1

    if tests.count_documents({}) != 0:
        testlist = list(tests.find())
    
    if instructions.count_documents({}) != 0:
        instructionlist = list(instructions.find())

    if testlist == -1 or instructionlist == -1:
        flash("Add more tests with existent instructions to generate report.")
    else:
        instructions_dictionary = {}

        for instruction in instructionlist:
            repetitions = 0

            for test in testlist:
                if str(test["instruction"]) == str(instruction["_id"]):
                    repetitions += 1
            
            instructions_dictionary[instruction["name"]] = repetitions

    return render_template("reports/common_instruction.html", testlist=testlist, instructionlist=instructionlist, instructions_dictionary=instructions_dictionary, username=g.get("session"))

def tests_by_price():
    testlist = -1
    testprice_dictionary = -1

    if tests.count_documents({}) != 0:
        testlist = tests.find()

    if testlist == -1:
        flash("Add more tests to generate report.")
    else:
        testprice_dictionary = {"1-100": [], "101-200": [], "201-300": [], "301-500": [], "+501": []}
        testpricequantity_dictionary = {"1-100": 0, "101-200": 0, "201-300": 0, "301-500": 0, "+501": 0}

        for test in testlist:
            if int(test["price"]) >= 1 and int(test["price"]) <= 100:
                testprice_dictionary["1-100"].append(test)
                testpricequantity_dictionary["1-100"] += 1
            elif int(test["price"]) >= 101 and int(test["price"]) <= 200:
                testprice_dictionary["101-200"].append(test)
                testpricequantity_dictionary["101-200"] += 1
            elif int(test["price"]) >= 201 and int(test["price"]) <= 300: 
                testprice_dictionary["201-300"].append(test)
                testpricequantity_dictionary["201-300"] += 1
            elif int(test["price"]) >= 301 and int(test["price"]) <= 500: 
                testprice_dictionary["301-500"].append(test)
                testpricequantity_dictionary["301-500"] += 1
            elif int(test["price"]) >= 501: 
                testprice_dictionary["+501"].append(test)
                testpricequantity_dictionary["+501"] += 1
         

    return render_template("reports/tests_by_price.html", testlist=testlist, testprice_dictionary=testprice_dictionary, testpricequantity_dictionary=testpricequantity_dictionary, username=g.get("session"))