from flask import Flask, render_template

app = Flask('Grandma tracker')
_COLOR_PALETTE = ('#3D8D7A', '#B3D8A8', '#FBFFE4', '#A3D1C6')
@app.route('/')
def hello_world():
    return render_template('index.html')


