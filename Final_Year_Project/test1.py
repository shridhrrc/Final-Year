from flask import Flask, render_template,request
import bot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        req = request.form['vehicle_number']
        bot.vehicle_enum(req)
    return render_template('index.html')
    return render_template('support.html')
