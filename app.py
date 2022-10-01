
from flask import Flask, render_template, request, json, redirect, session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.secret_key = "This is my secret"

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'books-rating'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/signup")
def displaySignup():
    return render_template("signup.html")


@app.route("/api/signup", methods=['POST'])
def signup():
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    if name and email and password:
        hashed_password = generate_password_hash(password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser', (name, email, hashed_password))

        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully ! '})
        else:
            return json.dumps({"error": str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields !</span>'})


@app.route('/signin')
def displaySignin():
    test = "hello"
    return render_template('signin.html', test=test)


@app.route('/api/validateLogin', methods=['POST'])
def validateLogin():
    try:
        username = request.form['inputEmail']
        password = request.form['inputPassword']

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.callproc('sp_validateLogin', (username,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][3]), password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('signin.html', error="wrong email or password")
        else:
            return render_template('signin.html', error="wrong email or password")

    except Exception as e:
        return render_template('signin.html', error="All fields are required !")
    # finally:
    #     cursor.close()
    #     conn.close()


@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return redirect("/signin")


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('signin')


@app.route('/showAddBook')
def displayAddBook():
    if session.get('user'):
        return render_template('addBook.html')
    else:
        redirect('/signin')


@app.route('/addBook', methods=['POST'])
def addBook():
    if session.get('user'):
        title = request.form['inputTitle']
        author = request.form['inputAuthor']
        category = request.form['inputCategory']
        rating = request.form['inputRating']
        comments = request.form['inputComments']
        user = session.get('user')

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_addBook', (title, author,
                        category, rating, comments, user))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return redirect('/userHome')
        else:
            return render_template('addBook.html', error='error')
    else:
        return redirect('/signin')


@app.route("/getBooks")
def getBooks():
    if session.get('user'):
        user = session.get('user')

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.callproc('sp_getBooksByUser', (user,))
        books = cursor.fetchall()

        books_dict = []
        for book in books:
            book_dict = {
                "id": book[0],
                "title": book[1],
                "author": book[2],
                "category": book[3],
                "rating": book[4],
                "comments": book[5]
            }
            books_dict.append(book_dict)

        return json.dumps(books_dict)

    else:
        redirect('/signin')


@app.route("/getBookById", methods=['POST'])
def getBookById():
    if session.get('user'):

        user = session.get('user')
        # print(user)
        data = request.get_json(force=True)
        # data = json.loads(data)
        id = data['id']
        # print(id)

        conn = mysql.connect()
        cursor = conn.cursor()
        print('id', id)
        print('user', user)
        cursor.callproc('sp_getBookById', (user, id,))

        book = cursor.fetchall()
        print(book)


        for item in book:
            book_dict = {
                "id": item[0],
                "title": item[1],
                "author": item[2],
                "category": item[3],
                "rating": item[4],
                "comments": item[5]
            }



        return json.dumps(book_dict)

    else:
        redirect('/signin')


if __name__ == "__main__":
    app.run()
