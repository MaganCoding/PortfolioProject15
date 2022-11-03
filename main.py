import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

limit = 100


all_facts = []

headers = {
'X-Api-Key': 'qYcKROAW3ZnDdSy/wCxAuA==9EZQ5TK35jHdWUwq',
}


response = requests.get(f'https://api.api-ninjas.com/v1/facts?limit={limit}', headers=headers)
facts = response.json()
for _ in facts:
    all_facts.append(_['fact'])






@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fact/")
def fact():
    data = random.choice(all_facts)
    all_facts.remove(data)
    return render_template("facts.html", data=data)













if __name__ == "__main__":
    app.run(debug=True)