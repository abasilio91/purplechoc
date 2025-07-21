from flask import Flask
import config

app = Flask(__name__)
app.secret_key=config.SECRET_KEY

from views import *

if __name__ == '__main__':
    app.run(debug=True)