from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'books-rating'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

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

        cursor.callproc('sp_validateLogin',(username,))
        data = cursor.fetchall()

        # if len(data) > 0:
        #     #check pwd
        # else:
        #     return render_template('signin.html', errors="wrong")

    except Exception as e:
        return render_template('signin.html', error="All fields are required !")


if __name__ == "__main__":
    app.run()
