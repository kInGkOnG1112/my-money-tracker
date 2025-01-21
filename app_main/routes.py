"""
importing all the libraries and modules dependencies
"""
from flask import render_template
from app import app
from utils.helpers import get_global_context


@app.route("/")
def home():
    """
    Renders the home page
    :return: .html with its context
    """
    context = {
        "title": "Dashboard",
        "page": "dashboard"
    }
    context = get_global_context(context)
    return render_template("pages/home.html", context_data=context)


@app.route("/records")
def records():
    """
    Renders the records page
    :return: .html with its context
    """
    context = {
        "title": "Records",
        "page": "records"
    }
    context = get_global_context(context)
    return render_template("pages/home.html", context_data=context)


@app.route("/analysis")
def analysis():
    """
    Renders the analysis page
    :return: .html with its context
    """
    context = {
        "title": "Analysis",
        "page": "analysis"
    }
    context = get_global_context(context)
    return render_template("pages/home.html", context_data=context)


@app.route("/accounts")
def accounts():
    """
    Renders the accounts page
    :return: .html with its context
    """
    context = {
        "title": "Accounts",
        "page": "accounts"
    }
    context = get_global_context(context)
    return render_template("pages/home.html", context_data=context)


@app.route("/categories")
def categories():
    """
    Renders the categories page
    :return: .html with its context
    """
    context = {
        "title": "Categories",
        "page": "categories"
    }
    context = get_global_context(context)
    return render_template("pages/home.html", context_data=context)
