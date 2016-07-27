import os
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'Method used: %s' % request.method
    
@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "you are using post"
    else:
        return"you are probably using GET"
    


if __name__ == "__mai2__":
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
    