from flask import Flask, redirect, render_template, request
from database import delete_book, fetch_book, insert_book, fetch_all_books, update_book

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        book_name = request.form["book_name"]
        date_started = request.form["date_started"]
        date_ended = request.form["date_ended"]
        rating = request.form["rating"]

        insert_book(book_name, date_started, date_ended, rating)

    books = fetch_all_books()
    return render_template("index.html", books=books)

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    if request.method == "POST":
        book_name = request.form["book_name"]
        date_started = request.form["date_started"]
        date_ended = request.form["date_ended"]
        rating = request.form["rating"]

        update_book(book_id, book_name, date_started, date_ended, rating)

        return redirect("/")
    
    book = fetch_book(book_id)
    return render_template("edit.html", book=book)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    delete_book(book_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
