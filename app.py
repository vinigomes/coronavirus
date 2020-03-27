from flask import Flask, render_template
import pandas as pd
import copy
import ssl
import services


app = Flask(__name__)

ssl._create_default_https_context = ssl._create_unverified_context


# Download dataset when start the application
covid = pd.read_csv('https://query.data.world/s/oma46o2n6g7odze4j6ainduilu7liq')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/brazil', methods=['GET'])
def brazil():
    covid_brazil = copy.copy(covid)
    fig_brazil = services.show_confirmed_coronavirus_cases_in_brazil(covid_brazil)
    fig_brazil.show()
    return render_template('index.html')


@app.route('/world', methods=['GET'])
def world():
    covid_world = copy.copy(covid)
    fig_world = services.show_confirmed_coronavirus_cases_in_world(covid_world)
    fig_world.show()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
