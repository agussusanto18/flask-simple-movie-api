from settings import *
import json

db = SQLAlchemy(app)

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title, 'year': self.year, 'genre': self.genre}
    
    def add_movie(_title, _year, _genre):
        new_movie = Movies(title=_title, year=_year, genre=_genre)
        db.session.add(new_movie)
        db.session.commit()

    def get_all_movies():
        return [Movies.json(movie) for movie in Movies.query.all()]
    
    def get_movie(_id):
        return [Movies.json(Movies.query.filter_by(id=_id).first())]

    def update_movie(_id, _title, _year, _genre):
        movie = Movies.query.filter_by(id=_id).first()
        movie.title = _title
        movie.year = _year
        movie.genre = _genre
        db.session.commit()
    
    def delete_movie(_id):
        Movies.query.filter_by(id=_id).delete()
        db.session.commit()