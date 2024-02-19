import os
import openai

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
openai.api_key = "sk-XXX"

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/openai/<question>', methods=['GET'])
def callchatgpt(id: int):
  response = openai.ChatCompletion.create(
        model="gpt-4",
        stream=True,
        messages=
        [{
          "role": "user",
          "content": question
        }]
    )
  for chunk in response:
   if 'content' in chunk.choices[0].delta:
     return (chunk.choices[0].delta.content,end="")

  
if __name__ == '__main__':
   app.run()
