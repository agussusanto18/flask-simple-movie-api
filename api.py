from models import *

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'movies': Movies.get_all_movies()})

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    result_movie = Movies.get_movie(id)
    return jsonify(result_movie)

@app.route('/movies', methods=['POST'])
def add_movie():
    request_data = request.get_json()
    Movies.add_movie(request_data['title'], request_data['year'], request_data['genre_id'])
    response = Response("Movie added", 201, mimetype='application/json')
    return response

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    request_data = request.get_json()
    Movies.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response('Movie updated', 200, mimetype='application/json')
    return response

@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    Movies.delete_movie(id)
    response = Response('Movie deleted', 200, mimetype='application/json')
    return response


# Genre -----------------------------------------------------------------------------


@app.route('/genres', methods=['GET'])
def get_genres():
    return jsonify({'genres': Genres.get_all_genres()})

@app.route('/genres/<int:id>', methods=['GET'])
def get_genre_by_id(id):
    result_genre = Genres.get_genre(id)
    return jsonify(result_genre)

@app.route('/genres', methods=['POST'])
def add_genre():
    request_data = request.get_json()
    Genres.add_genre(request_data['name'])
    response = Response("Genre added", 201, mimetype='application/json')
    return response

@app.route('/genres/<int:id>', methods=['PUT'])
def update_genre(id):
    request_data = request.get_json()
    Genres.update_genre(id, request_data['name'])
    response = Response('Genre updated', 200, mimetype='application/json')
    return response

@app.route('/genres/<int:id>', methods=['DELETE'])
def remove_genre(id):
    Genres.delete_genre(id)
    response = Response('Genre deleted', 200, mimetype='application/json')
    return response




if __name__ == '__main__':
    app.run(port=8080, debug=True)