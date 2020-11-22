import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_ads")
def get_ads():
    ads = list(mongo.db.ads.find())
    return render_template("ads.html", ads=ads)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    ads = list(mongo.db.ads.find({"$text": {"$search": query}}))
    return render_template("ads.html", ads=ads)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("login"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session'cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username existst in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect User or/and Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username doesn't exist")
            return redirect(url_for("register"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.users.remove({'_id': ObjectId(username)})
    flash("Profile Successfully Deleted")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/post_ad", methods=["GET", "POST"])
def post_ad():
    if request.method == "POST":
        ad = {
            "category_name": request.form.get("category_name"),
            "ad_title": request.form.get("ad_title"),
            "ad_description": request.form.get("ad_description"),
            "photo_url": request.form.get("photo_url"),
            "price": request.form.get("price"),
            "condition_type": request.form.get("condition_type"),
            "area_name": request.form.get("area_name"),
            "email": request.form.get("email"),
            "telephone": request.form.get("telephone"),
            "posted_by": session["user"]
        }
        mongo.db.ads.insert_one(ad)
        flash("Ad Successfully Posted")
        return redirect(url_for("get_ads"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    conditions = mongo.db.conditions.find().sort("condition_type", 1)
    ireland_areas = mongo.db.ireland_areas.find().sort("area_name", 1)
    n_ireland_areas = mongo.db.n_ireland_areas.find().sort("area_name", 1)
    return render_template("post_ad.html", categories=categories,
                        conditions=conditions,
                        ireland_areas=ireland_areas,
                        n_ireland_areas=n_ireland_areas)


@app.route("/edit_ad/<ad_id>", methods=["GET", "POST"])
def edit_ad(ad_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "ad_title": request.form.get("ad_title"),
            "ad_description": request.form.get("ad_description"),
            "photo_url": request.form.get("photo_url"),
            "price": request.form.get("price"),
            "condition_type": request.form.get("condition_type"),
            "area_name": request.form.get("area_name"),
            "email": request.form.get("email"),
            "telephone": request.form.get("telephone"),
            "posted_by": session["user"]
        }
        mongo.db.ads.update({"_id": ObjectId(ad_id)}, submit)
        flash("Ad Successfully Updated")

    ad = mongo.db.ads.find_one({"_id": ObjectId(ad_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    conditions = mongo.db.conditions.find().sort("condition_type", 1)
    ireland_areas = mongo.db.ireland_areas.find().sort("area_name", 1)
    n_ireland_areas = mongo.db.n_ireland_areas.find().sort("area_name", 1)
    return render_template("edit_ad.html", ad=ad, categories=categories,
                        conditions=conditions,
                        ireland_areas=ireland_areas,
                        n_ireland_areas=n_ireland_areas)


@app.route("/delete_ad/<ad_id>")
def delete_ad(ad_id):
    mongo.db.ads.remove({"_id": ObjectId(ad_id)})
    flash("Ad Successfully Deleted")
    return redirect(url_for("get_ads"))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Your message has been sent")
        return redirect(url_for("get_ads"))

    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
