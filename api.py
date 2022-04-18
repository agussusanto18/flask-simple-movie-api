from movies import *

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
    Movies.add_movie(request_data['title'], request_data['year'], request_data['genre'])
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


if __name__ == '__main__':
    app.run(port=8001, debug=True)