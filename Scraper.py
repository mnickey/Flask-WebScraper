from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/scraper/', methods=['GET', 'POST'])
def scraper():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        links = []
        site = request.form['myUrl']
        r = requests.get("http://" + site)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all('a'):
            if 'href' in link.attrs:
                links.append(link)
        return render_template('links.html', site=site, links=links)

if __name__ == '__main__':
    app.run(debug=True)
