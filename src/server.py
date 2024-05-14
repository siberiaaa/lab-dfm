from flask import Flask
from modules.home import homes
# import modules.home as home
import modules.category as category

app = Flask(__name__, template_folder="./templates")
app.config["SECRET_KEY"] = "wao"


@app.route("/", methods=["GET"])
def home():
    return homes()

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


if __name__ == "__main__":
    app.run(debug=True)