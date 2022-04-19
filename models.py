from settings import *
import json

db = SQLAlchemy(app)

class Genres(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    movies = db.relationship('Movies', backref='genres')

    def json(self):
        return {'id': self.id, 'name': self.name}
    
    def add_genre(_name):
        new_genre = Genres(name=_name)
        db.session.add(new_genre)
        db.session.commit()

    def get_all_genres():
        return [Genres.json(genre) for genre in Genres.query.all()]
    
    def get_genre(_id):
        return [Genres.json(Genres.query.filter_by(id=_id).first())]

    def update_genre(_id, _name):
        genre = Genres.query.filter_by(id=_id).first()
        genre.name = _name
        db.session.commit()
    
    def delete_genre(_id):
        Genres.query.filter_by(id=_id).delete()
        db.session.commit()

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

    def json(self):
        return {'id': self.id, 'title': self.title, 'year': self.year, 'genre_id': self.genre_id}
    
    def add_movie(_title, _year, _genre_id):
        new_movie = Movies(title=_title, year=_year, genre_id=_genre_id)
        db.session.add(new_movie)
        db.session.commit()

    def get_all_movies():
        return [Movies.json(movie) for movie in Movies.query.all()]
    
    def get_movie(_id):
        return [Movies.json(Movies.query.filter_by(id=_id).first())]

    def update_movie(_id, _title, _year, _genre_id):
        movie = Movies.query.filter_by(id=_id).first()
        movie.title = _title
        movie.year = _year
        movie.genre_id = _genre_id
        db.session.commit()
    
    def delete_movie(_id):
        Movies.query.filter_by(id=_id).delete()
        db.session.commit()