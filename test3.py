from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/profile/<username>')
def profile(username):
    return render_template('demo.html',username=username,isActive=False)

@app.route('/books')
def book():
    books = [{'name':'book1','author':'abc','cover':'https://visme.co/blog/wp-content/uploads/2021/06/the-godfather-book-cover.png'},{'name':'book2','author':'abc2','cover':'https://visme.co/blog/wp-content/uploads/2021/06/the-godfather-book-cover.png'},{'name':'book3','author':'abc3','cover':'https://visme.co/blog/wp-content/uploads/2021/06/the-godfather-book-cover.png'},]
    return render_template('book.html', books=books)


app.run(debug=True)