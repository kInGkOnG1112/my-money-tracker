"""
importing all the libraries and modules dependencies
"""
from flask import render_template, Blueprint
from utils.helpers import get_global_context

main = Blueprint('main', __name__)


@main.route("/")
def dashboard():
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


@main.route("/records")
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
    return render_template("pages/records.html", context_data=context)


@main.route("/analysis")
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
    return render_template("pages/analysis.html", context_data=context)


@main.route("/accounts")
def accounts():
    """
    Renders the accounts page
    :return: .html with its context
    """
    icon_list: list[str] = [
        '/static/images/account_logo/bank.png',
        '/static/images/account_logo/debit-card.png',
        '/static/images/account_logo/master-card.jpg',
        '/static/images/account_logo/money.png',
        '/static/images/account_logo/paypal.jpg',
        '/static/images/account_logo/piggy-bank.jpg',
        '/static/images/account_logo/visa-card.png',
        '/static/images/account_logo/wallet.png'
    ]
    context = {
        "title": "Accounts",
        "page": "accounts",
        "icon_list": icon_list
    }
    context = get_global_context(context)
    return render_template("pages/accounts.html", context_data=context)


@main.route("/categories")
def categories():
    """
    Renders the categories page
    :return: .html with its context
    """
    icon_list: list[str] = [
        '/static/images/car.jpg',
        '/static/images/clothing.jpg',
        '/static/images/food.jpg',
        '/static/images/health.jpg',
        '/static/images/money-tag.jpg',
        '/static/images/gas.jpg',
        '/static/images/baby.jpg',
        '/static/images/bills.jpg',
        '/static/images/education.jpg',
        '/static/images/savings.jpg',
        '/static/images/cart.jpg',
        '/static/images/movie.jpg',
        '/static/images/sports.jpg',
        '/static/images/gym.jpg',
        '/static/images/medication.jpg',
        '/static/images/plain-orange.jpg',
        '/static/images/plain-yellow.jpg',
        '/static/images/plain-red.jpg',
        '/static/images/plain-purple.jpg',
        '/static/images/plain-darkblue.jpg',
        '/static/images/plain-blue.jpg',
        '/static/images/plain-indigo.jpg',
        '/static/images/plain-green.jpg',
        '/static/images/plain-darkgreen.jpg'
    ]

    context = {
        "title": "Categories",
        "page": "categories",
        "icon_list": icon_list
    }
    context = get_global_context(context)
    return render_template("pages/categories.html", context_data=context)
