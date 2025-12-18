from flask import Flask,request,render_template,redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
client = MongoClient(os.getenv("Mongo_uri"))
db=client['test']
collection=db['Flask']
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/add',methods=['POST'])
def index():
    error=None
    try:
        name=request.form['name']
        password=request.form['password']
        collection.insert_one({'name':name,'password':password})
        return redirect('/success')
    except Exception as e:
        error="Insertion Failed"
        return render_template('index.html',error=error)
@app.route('/success',methods=['GET'])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)

