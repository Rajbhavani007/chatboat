import os

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__, template_folder='templets')  # still relative to module

chatbot = ChatBot('Ryan')
trainer = ListTrainer(chatbot)

for _file in os.listdir('data'):
     chats = open('data/' + _file, 'r').readlines()
     trainer.train(chats)

@app.route("/")
def index():
 return render_template("htmlfile.html")

@app.route("/get")
def get_bot_response():
     usertext = request.args.get('msg')
     return str(chatbot.get_response(usertext))


if __name__ == "__main__":
        app.debug = True
        app.run()



