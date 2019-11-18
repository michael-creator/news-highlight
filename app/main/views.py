# from app import app
from flask import render_template,request, redirect ,url_for
from . import main
from ..request import get_news

@main.route('/')
def index():

    output = get_news()

    return render_template('index.html', name = output)

@main.route('/news/sources')
def news():

    output = get_news()
    return render_template('news.html')