
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
        print(username)
        print(password)

        
        conn = mysql.connect()
        cursor = conn.cursor()
        

        cursor.callproc('sp_validateLogin',(username,))
        data = cursor.fetchall()

        print(data)

        if len(data) > 0:
            if check_password_hash(str(data[0][3]),password):
                print('ok')
                # session['user'] = data[0][0]
                return redirect('/home')
                # return render_template('signin.html', error="OK")
            else:
                return render_template('signin.html', error="wrong email or password")
        else:
            return render_template('signin.html', error="wrong email or password")

    except Exception as e:
        return render_template('signin.html', error="All fields are required !")
    # finally:
    #     cursor.close()
    #     conn.close()

if __name__ == "__main__":
    app.run()
