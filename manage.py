from flask import Flask, render_template
from app import app
from flask_script import Manager

if __name__ == "__main__":
    app.run(debug=True)

    