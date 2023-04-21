from flask import Blueprint, jsonify
from ..titles import Title

api = Blueprint('api', __name__, url_prefix='/api')

def check_title_exists(title_id):
    title = Title.query.filter_by(id=title_id).first()
    if title is None:
        return False
    return True

'''
***********
API ENDPOINTS
***********
'''

@api.route('/')
def get_all_titles():
    all_titles = Title.query.all()

    return jsonify([title.to_dict()\
                    for title in all_titles])

@api.route('/title/<title_id>/')
def get_title(title_id):
    title_exists = check_title_exists(title_id)
    title = Title.query.filter_by(id=title_id).first()
    if not title_exists:
        return 'Title Not Found'
    else:
        return jsonify(title.to_dict())
    
@api.route('/movies/')
def get_all_movies():
    all_movies = Title.query.filter_by(content_type='MOVIE')
    return jsonify([movie.to_dict()\
                    for movie in all_movies])

@api.route('/shows/')
def get_all_shows():
    all_shows = Title.query.filter_by(content_type='SHOW')
    return jsonify([show.to_dict()\
                    for show in all_shows])

@api.route('/top-20/')
def get_top_20_titles():
    all_titles = Title.query.order_by(Title.tmdb_rating.desc()).limit(20)
    return jsonify([title.to_dict()\
                    for title in all_titles])

@api.route('/top-100/')
def get_top_100_titles():
    all_titles = Title.query.order_by(Title.tmdb_rating.desc()).limit(100)
    return jsonify([title.to_dict()\
                    for title in all_titles])

@api.route('/genre/<genre>/')

def get_title_by_genre(genre):
    selected_titles = []
    
    all_titles = Title.query.all()
    for title in all_titles:
        genres = title.get_genres_as_list()
        if genre.title() in genres:
            selected_titles.append(title.to_dict())
    return jsonify(selected_titles)

@api.route('/decade/<int:decade>')

def get_title_by_decade(decade):
    selected_titles = []

    all_titles = Title.query.all()
    for title in all_titles:
        if title.convert_year_to_decade() == decade:
            selected_titles.append(title.to_dict())
    return jsonify(selected_titles)
