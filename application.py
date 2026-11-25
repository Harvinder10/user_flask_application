from flask import Flask, request, jsonify,render_template
import mysql.connector
import jwt
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps


app= Flask(__name__)

app.config["SECRET_KEY"] = "abcd"

def connector():
    db=mysql.connector.connect(host ="localhost",user="root",password="Harry1@@7",database="student_management")
    cursor = db.cursor(dictionary=True)
    return db,cursor
 
@app.route("/signup",methods=["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Please provide data"})

    fields =["fname","email","dob"]
    for i in fields:
        if i not in data:
            return jsonify({"error": f"key {i} is missing"})

    fname = data["fname"]
    lname = data["lname"]
    email = data["email"]
    dob = data["dob"]

    required_fields =["fname","email"]
    for i in required_fields:
        if not data[i]:
            return jsonify({"error": f"{i} is required"})

    db,cursor = connector()
    cursor.execute("select * from user where email = %s",(email,))
    existing_user = cursor.fetchone()
    cursor.close()
    db.close()

    if existing_user:
        return jsonify({"message": "User already exists"})


    db,cursor = connector()
    cursor.execute("insert into user ( fname, lname, email, dob) values (%s,%s,%s,%s)",(fname,lname,email,dob))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "signup successful"})

if __name__ == "__main__":
    app.run(debug=True)


