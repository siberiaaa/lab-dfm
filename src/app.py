from flask import Flask, g, request, redirect, url_for
from modules.home import homes, check_cookie
import modules.category as category
import modules.test as test
import modules.sample_type as sample_type
import modules.instruction as instruction
import modules.authentication as authentication
import modules.reports as reports

app = Flask(__name__, template_folder="./templates")
app.config["SECRET_KEY"] = "wao"


@app.before_request
def middleware():
    session = check_cookie()
    g.setdefault("session", session)

    allowedendpoints = ["home", "login", "signup", "logout", "tests", "categories", "sample_types", "instructions", "static"] #static :(
    if session == "" and request.endpoint not in allowedendpoints:
        return redirect(url_for('login'))

@app.route("/", methods=["GET"])
def home():
    return homes()

# ----------------- Tests ----------------- 
@app.route("/tests", methods=["GET", "POST"])
def tests():
    return test.list_test()

@app.route("/tests/add", methods=["GET", "POST"])
def add_test():
    return test.add_test()

@app.route("/tests/<id>", methods=["GET"])
def read_test(id):
    return test.read_test(id)

@app.route("/tests/update/<id>", methods=["GET", "POST"])
def update_test(id):
    return test.update_test(id)

@app.route("/tests/delete/<id>", methods=["GET"])
def delete_test(id):
    return test.delete_category(id)


# ----------------- Categories ----------------- 
@app.route("/categories", methods=["GET"])
def categories():
    return category.list_category()

@app.route("/categories/add", methods=["GET", "POST"])
def add_category():
    return category.add_category()

@app.route("/categories/<id>", methods=["GET"])
def read_category(id):
    return category.read_category(id)

@app.route("/categories/update/<id>", methods=["GET", "POST"])
def update_category(id):
    return category.update_category(id)

@app.route("/categories/delete/<id>", methods=["GET"])
def delete_category(id):
    return category.delete_category(id)


# ----------------- sample_types ----------------- 
@app.route("/sample_types", methods=["GET"])
def sample_types():
    return sample_type.list_sample_type()

@app.route("/sample_types/add", methods=["GET", "POST"])
def add_sample_type():
    return sample_type.add_sample_type()

@app.route("/sample_types/<id>", methods=["GET"])
def read_sample_type(id):
    return sample_type.read_sample_type(id)

@app.route("/sample_types/update/<id>", methods=["GET", "POST"])
def update_sample_type(id):
    return sample_type.update_sample_type(id)

@app.route("/sample_types/delete/<id>", methods=["GET"])
def delete_sample_type(id):
    return sample_type.delete_sample_type(id)


# ----------------- Instructions ----------------- 
@app.route("/instructions", methods=["GET"])
def instructions():
    return instruction.list_instruction()

@app.route("/instructions/add", methods=["GET", "POST"])
def add_instruction():
    return instruction.add_instruction()

@app.route("/instructions/<id>", methods=["GET"])
def read_instruction(id):
    return instruction.read_instruction(id)

@app.route("/instructions/update/<id>", methods=["GET", "POST"])
def update_instruction(id):
    return instruction.update_instruction(id)

@app.route("/instructions/delete/<id>", methods=["GET"])
def delete_instruction(id):
    return instruction.delete_instruction(id)


# ----------------- Authentication ----------------- 
@app.route("/login", methods=["GET", "POST"])
def login():
    return authentication.login()

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return authentication.signup()

@app.route("/logout", methods=["GET"])
def logout():
    return authentication.logout()


# ----------------- Authentication ----------------- 
@app.route("/reports/tests_in_categories", methods=["GET"])
def tests_in_categories():
    return reports.tests_in_categories()

@app.route("/reports/common_instruction", methods=["GET"])
def common_instruction():
    return reports.common_instruction()

@app.route("/reports/tests_by_price", methods=["GET"])
def tests_by_price():
    return reports.tests_by_price()



if __name__ == "__main__":
    app.run(debug=True)