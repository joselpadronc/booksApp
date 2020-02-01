from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/books')
def books_list():
  return render_template('books_list.html')


if __name__ == "__main__":
    app.run(debug=True)
