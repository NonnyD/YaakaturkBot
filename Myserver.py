from flask import Flask
from threading import thread

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def server_on():
    t = thread(target=run)
    t.start()