from http.client import INTERNAL_SERVER_ERROR
from flask import Flask, render_template

#Creating a flask instance
app=Flask(__name__)  #This helps flask find all our directories

#Create a decorator, which is a route for the URL
@app.route('/')

# def index():
#     return "<H1>Hello World</H1>"

def index():
    pizza = ["pepporoni", "cheese", "mushrooms", "nadan",41]
    first_name="John"
    stuff = "This is <strong>Bold</strong> Text"
    return render_template("index.html", first_name=first_name, stuff=stuff, pizza=pizza)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


#The next section will be jinja2, this is a templating


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500



