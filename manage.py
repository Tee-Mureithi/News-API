# from flask import Flask, render_template
# from newsapi import NewsApiClient

# app = Flask(__name__)

# @app.route('/')
# def Index():
#     newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
#     topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

#     articles = topheadlines['articles']

#     desc = []
#     news = []
#     img = []
#     url = []

#     for i in range(len(articles)):
#         myarticles = articles[i]

#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         url.append(myarticles['url'])

#     mylist = zip(news, desc, img)

#     return render_template('index.html', context = mylist)


# @app.route('/bbc')
# def bbc():
#     newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
#     topheadlines = newsapi.get_top_headlines(sources="bbc-news")

#     articles = topheadlines['articles']

#     desc = []
#     news = []
#     img = []
#     url = []

#     for i in range(len(articles)):
#         myarticles = articles[i]

#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         url.append(myarticles)['url']



#     mylist = zip(news, desc, img)

#     return render_template('bbc.html', context=mylist)



# if __name__ == "__main__":
#     app.run(debug=True)



# # from flask import Flask, render_template
# # from app import app

# # app= Flask (__name__)

# # if __name__ == '___main__':
# #     app.run(debug=True)
from app import create_app
from flask_script import Manager,Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


if __name__ == '__main__':
    manager.run()

