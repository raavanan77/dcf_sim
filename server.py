from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/chart',methods=['GET','POST'])
def chart():
    return render_template('chart.html')