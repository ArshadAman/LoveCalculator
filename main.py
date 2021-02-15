from flask import Flask, request
from flask.templating import render_template
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6z'


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/calculate', methods=["POST"])
def calculate():
    print(request.method)
    if request.method == 'POST':
        your_name = request.form["your_name"]
        crush_name = request.form["crush_name"]
        your_name = your_name.lower()
        crush_name = crush_name.lower()
        combined_string = your_name + crush_name

        #Total TRUE:
        totalT = combined_string.count("t")
        totalR = combined_string.count("r")
        totalU = combined_string.count("u")
        totalEt = combined_string.count("e")

        total_true = totalT+totalR+totalU+totalEt

        #Total Love:

        totalL = combined_string.count("l")
        totalO = combined_string.count("o")
        totalV = combined_string.count("v")
        totalEl = combined_string.count("e")

        total_love = totalL+totalO+totalV+totalEl

        score = int(str(total_true) + str(total_love))
        
        if score < 80 and score>75:
            score+=5
        elif score >60 and score<75:
            score+=10
        elif score >40 and score<60:
            score+=20
        else:
            score+=40

        return render_template("result.html", score=score)


if __name__ == '__main__':
    app.run(debug=True)