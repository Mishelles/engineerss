from flask import render_template, request, redirect, url_for, abort, current_app, flash
from . import main
from .. import db
from flask import jsonify
from .models import Post, Tag

@main.route("/news", methods=['GET'])
def news_page():
    tags = Tag.objects().all()
    return render_template('news-page.html', tags=tags)

@main.route("/news/loadmore/<int:last_id>")
def load_more_news(last_id):
    if last_id == 0:
        next_chunk_of_news = Post.objects().all().order_by('-date')[:10]
    else:
        next_chunk_of_news = Post.objects(_id__lt=last_id).order_by('-date')[:10]
    print(len(next_chunk_of_news))
    return jsonify({'news' : next_chunk_of_news})
