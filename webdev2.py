from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def firstPath():
    name = 'Mehvish'
    return render_template('webdev2.html', name = name)

app.run()