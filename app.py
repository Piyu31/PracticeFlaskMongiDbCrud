from flask import Flask ,render_template
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app=Flask(__name__)


connection=MongoClient("mongodb+srv://priyanka:piyu31@cluster0.mdba4.mongodb.net/Users?retryWrites=true&w=majority")
db = connection["Users"]
colletions=db["Details"]

@app.route('/')
def signup():
  return render_template('signup.html')


#adding one entry to database

colletions.insert_one({"name": "John" ,"password":"ydeam"})
colletions.insert_one({"name": "John" ,"password":"ydeam"})
#adding many  entry to database

data1={"name": "rama" ,"password":"2526RTQG"}
data2={"name": "krishna" ,"password":"1028IOJ"}
data3={"name": "radha" ,"password":"1616GHQ1"}

colletions.insert_many([data1,data2,data3])

#deleting from database

colletions.delete_one({"name": "John" ,"password":"ydeam"})

#fecthing from database
@app.route("/details",methods=["GET"])
def get_details():
    users_details=list(colletions.find({}))
    return json.dumps(users_details,default=json_util.default)


#signup
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST'
        existing_user = colletions.find_one({'name' : request.form['name']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pwd'].encode('utf-8'), bcrypt.gensalt())
            colletions.insert({'name' : request.form['name'], 'password' : hashpass})
            session['name'] = request.form['name']
            return redirect(url_for('signup'))

        return 'That username already exists!'

    return render_template('signup.html')

if __name__ == '__main__':
   app.run()