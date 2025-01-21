from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

books = [
{"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
{"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
{"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
{"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
{"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/api/v1/qui-suis-je', methods=["GET", "POST"])
def qui_suis_je():
    return "Je suis Othmane!"

@app.route('/api/v1/qui-suis-je/<name>', methods=["GET", "POST"])
def getNameDynamic (name):
    return name

@app.route('/api/v1/addition/<a>/<b>', methods=["GET", "POST"])
def addition (a,b):
    return str(int(a)+int(b))

@app.route('/api/v1/books', methods=['GET'])
def get_books_by_author():
    author = request.args.get('author')
    if author:
        result = [book for book in books if book['author'].lower() == author.lower()]
        return jsonify(result)
    return jsonify([])

@app.route('/search', methods=['GET'])
def search_form():
    query = request.args.get('query')
    if query:
        result = [book for book in books if query.lower() in book['author'].lower()]
        if result:
            return render_template('search_results.html', books=result)
        else:
            return render_template('search_results.html', error="Aucun livre trouvé pour cet auteur.")
    return render_template('search.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)




