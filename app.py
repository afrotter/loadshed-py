from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://loadshedding.eskom.co.za/LoadShedding/GetStatus'
    response = requests.get(url)

    if response.status_code == 200:
        loadshedding_status = response.json()
    else:
        loadshedding_status = 'Error: ' + str(response.status_code)

    return render_template('index.html', loadshedding_status=loadshedding_status)


