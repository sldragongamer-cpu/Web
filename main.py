from flask import Flask
from vercel_python_wsgi import handler

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

handler = handler(app)

from Website  import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
