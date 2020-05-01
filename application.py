from flask import Flask, render_template
import requests

app = Flask(__name__)

"""Fetch the latest post for embedded context"""
def get_post_embed():
    request = requests.get('https://life.lunatech.com/wp-json/wp/v2/posts/?context=embed&per_page=1')
    post = request.json()[0]
    return {'link': post['link'], 'title': post['title']['rendered'], 'featured_media': post['featured_media'], 'featured_media_url':  post['jetpack_featured_media_url']}

@app.route('/')
def home():
    pe = get_post_embed()
    return render_template('home.html', title=pe['title'], link=pe['link'], image=pe['featured_media_url'])

if __name__ == "__main__":
    app.run()
