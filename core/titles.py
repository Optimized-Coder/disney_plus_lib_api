from .extensions import db

class Title(db.Model):
    __tablename__ = 'data'
    id = db.Column('id', db.String, primary_key=True)
    title = db.Column('title', db.String)
    content_type = db.Column('type', db.String)
    description = db.Column('description', db.String)
    release_year = db.Column('release_year', db.Integer)
    age_certification = db.Column('age_certification', db.String)
    runtime = db.Column('runtime', db.Integer)
    genre = db.Column('genres', db.String)
    production_countries = db.Column('production_countries', db.String)
    seasons = db.Column('seasons',db.Integer)
    imdb_id = db.Column('imdb_id', db.String)
    imdb_votes = db.Column('imdb_votes', db.String)
    imdb_rating = db.Column('imdb_score', db.Float)
    tmdb_rating = db.Column('tmdb_popularity', db.Float)
    tmdb_score = db.Column('tmdb_score', db.Float)

    def format_genres(self):
        x = self.genre
        new_genre = x.replace('[', '').replace(']', '').replace("'", '').title()
        return new_genre

    def format_production_countries(self):
        x = self.production_countries
        new_countries = x.replace('[', '').replace(']', '').replace("'", '')
        return new_countries
    
    def get_genres_as_list(self):
        return self.format_genres().split(',')
    
    def convert_year_to_decade(self):
        decade = self.release_year // 10
        decade = decade * 10
        return decade

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content_type': self.content_type.lower(),
            'description': self.description,
           'release_year': self.release_year,
            'age_certification': self.age_certification,
            'runtime_mins': self.runtime,
            'genre': self.format_genres(),
            'production_countries': self.format_production_countries(),
            'seasons': self.seasons,
            'imdb_id': self.imdb_id,
            'imdb_votes': self.imdb_votes,
            'imdb_rating': self.imdb_rating,
            'tmdb_rating': self.tmdb_rating,
            'tmdb_score': self.tmdb_score
        }
    

    
    
