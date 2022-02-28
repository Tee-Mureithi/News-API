from importlib.resources import contents
from flask import render_template,request,redirect,url_for
from ..requests import main_all_articles , main_article
from .import app





@app.route('/')
def index():
        # news_all.append(main_all_articles['title'])
        # desc_all.append(main_all_articles['description'])
        # img_all.append(main_all_articles['urlToImage'])
        # p_date_all.append(main_all_articles['publishedAt'])
        # url_all.append(main_article['url'])
        
        # all = zip( news_all,desc_all,img_all,p_date_all,url_all)


         return render_template('index.html')