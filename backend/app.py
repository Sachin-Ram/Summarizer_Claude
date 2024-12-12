from flask import Flask,request,jsonify
import os
import anthropic
"""
1.get the api key
2.Initialize the api key
3.create an anthropic object
4.initialize conversation using message api
5.return response
"""
app=Flask(__name__)

@app.route("/")
def function():
    data=""
    return data


if __name__ =='main':
     
    app.run(debug=True)