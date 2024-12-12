from flask import Flask,request,jsonify
import os
from dotenv import load_dotenv 
load_dotenv()
import anthropic
"""
1.get the api key
2.Initialize the api key
3.create an anthropic object
4.initialize conversation using message api
5.return response
"""
app=Flask(__name__)

api_key=os.getenv('api_key')

client=anthropic.Anthropic(api_key=api_key)

@app.route("/",methods=['GET','POST'])
def function():
    data=request.form.get('data')
    text=client.messages.create(
        model="Claude 3.5 Sonnet 2024-10-22",
        max_tokens=300,
        system="You are a text summarizer and when asked to summarize a text, send back the summary",
        messages=[
            {
                'role':"user",
                'content':f"summarize this text : {data}"
            }
        ]
    )

    summary = text.get("content")

    return summary

if __name__ =="__main__":
     
    app.run(debug=True)