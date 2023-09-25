from flask import Flask,request
import csv
from static import detect2

app = Flask(__name__)

def scores(data):
    f = open ("static\leaderboard.csv","a")
    cw = csv.writer(f)
    cw.writerow(data)
    f.close()
    leaderboard()
    
def leaderboard():
    f = open ("static\leaderboard.csv","r")
    cr = csv.reader(f)
    namelist = []
    for i in cr:
        if i==[]:
            pass
        else:
            namelist.append(i)
    f.close()

    l = len(namelist)

    for i in range(0, l):
        for j in range(0, l-i-1):
            if (namelist[j][1] > namelist[j + 1][1]):
                tempo = namelist[j]
                namelist[j] = namelist[j + 1]
                namelist[j + 1] = tempo
    
    print (namelist)


@app.route("/")
def hello_world():
    detect2.Time()
    return ("<div>\
            <link rel= \"stylesheet\" type= \"text/css\" href= \"static/style.css\">\
            <ul class=\"nav\">  <li>Home</li> <li>Leaderboard</li> <li>About</li>  </ul>\
            <p style=\"color:blue;\" id=\"test\"></p>\
            <h1 class=\"title\">Where's Biryani?</h1>\
            <p class=\"sass\">Think you can beat a computer? </p>\
            <p class = \"rules\">Try spotting this plate of biryani as quickly as you can and see how you fare against a computer and other players!<br></p>\
            <p class=\"starting\">Click on the biryani to start :D</p>\
            <script src=\"static/click.js\"></script>\
            </div>")

@app.route("/score", methods=['POST'])
def receive_data():
    time = request.get_json()
    time1 = [time["username"],time["time"]]
    scores (time1)
    return ("<p>success!</p>")


