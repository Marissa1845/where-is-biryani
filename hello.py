from flask import Flask,request, render_template
import csv
from static import detect1

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
            if (float(namelist[j][1]) > float (namelist[j + 1][1])):
                tempo = namelist[j]
                namelist[j] = namelist[j + 1]
                namelist[j + 1] = tempo
    print (namelist)
    
    f = open ("static\sortedleaderboard.csv","w")
    cw = csv.writer(f)
    cw.writerow(['#', 'Name','Time'])
    for i in range(0,l):
        ut = int(namelist[i][1])
        ut = ut/1000
        cw.writerow([i+1,namelist[i][0],ut])
    
    f.close()



@app.route("/")
def hello_world():
    compTimes = detect1.Time()
    for i in range(0, len(compTimes)):
        compTimes[i] = round(compTimes[i], 6)
        compTimes[i] = str(compTimes[i]) + 's'
    return ("<div>\
            <link rel= \"stylesheet\" type= \"text/css\" href= \"static/style.css\">\
            <ul class=\"nav\">  <li id='navlb'><a href='/'>Home</a></li> <li id='navlb' ><a href='/leaderboard'>Leaderboard</a></li> <li id='navlb'><a href='/about'>About</li></a></ul>\
                <div id=\"startPage\">\
                <p style=\"color:blue;\" id=\"test\"></p>\
                <h1 class=\"title\">Where's Biryani?</h1>\
                <p class=\"sass\">Think you can beat a computer? </p>\
                <p class = \"rules\">Try spotting this plate of biryani as quickly as you can and see how you fare against a computer and other players!<br></p>\
                <img id=\"imgstart\" src=\"static/b.png\">\
                <p class=\"starting\">Click on the biryani to start :D</p>\
                <script src=\"static/click.js\"></script>\
                </div>\
            <div id=\"takingName\">\
                <input type=\"text\" id='name' placeholder=\"Enter Name...\">\
                <img id=\"potato\" src=\"static/tater.gif\">\
            </div>\
            <div id='game'><img class='birbir' src='static/biryani-full.jpg'></div>\
            <div id='game2'><img class='birbir' src='static/birbir2.png'></div>\
            <div id='game3'><img class='birbir' src='static/birbir3.png'></div>\
            <div id='game4'><img class='birbir' src='static/birbir4.png'></div>\
            <div id='comp'>\
                <p id='comptime' >The computer did it in<br></p>\
                <div id='times'>\
                <div><img id='fb1' src='static/found_biryani1.png'>\
                <p id='comptime1'>"+str(compTimes[0])+"</p>\
                </div>\
                <div><img id='fb2' src='static/found_biryani2.png'>\
                <p id='comptime2'>"+str(compTimes[1])+"</p>\
                </div>\
                <div><img id='fb3' src='static/found_biryani3.png'>\
                <p id='comptime3'>"+str(compTimes[2])+"</p>\
                </div>\
                <div><img id='fb4' src='static/found_biryani4.png'>\
                <p id='comptime4'>"+str(compTimes[3])+"</p>\
                </div></div>\
                <p id='navlead1'><br>Click <a href='/leaderboard' id='here1'>here</a> to view the leaderboard</p>\
                <p id='navlead2'>Click <a href='/about' id='here1'>here</a> to know more about \"Where's Biryani?\"</p>\
            </div>\
            </div>\
            <div id='success1'>\
                <h1 id='msg'>\"You found the biryani!\"</h1>\
                <p id='usertime1'></p>\
                <p class='levelchange'>Click <span id='herel2'>here</span> to proceed to Level 2!</p>\
                <img class='dance1' src='static\\tchik.gif'>\
                <img class='dance2' src='static\\tchik.gif'>\
            </div>\
            <div id='success2'>\
                <h1 id='msg'>\"You found the biryani!\"</h1>\
                <p id='usertime2'></p>\
                <p class='levelchange'>Click <span id='herel3'>here</span> to proceed to Level 3!</p>\
                <img class='dance1' src='static\\tchik.gif'>\
                <img class='dance2' src='static\\tchik.gif'>\
            </div>\
            <div id='success3'>\
                <h1 id='msg'>\"You found the biryani!\"</h1>\
                <p id='usertime3'></p>\
                <p class='levelchange'>Click <span id='herel4'>here</span> to proceed to the Final Level!</p>\
                <img class='dance1' src='static\\tchik.gif'>\
                <img class='dance2' src='static\\tchik.gif'>\
            </div>\
            <div id='success'>\
                <h1 id='msg'>\"You found the biryani!\"</h1>\
                <p id='usertime4'></p>\
                <img id='snake' src='static/snake.jpeg'>\
                <p id='snark'>Now <span id='watch'>watch</span> me <br>do it!\
            </div>\
            <div id='progressing'> <div class='color'></div>\
            </div>\
            </div>")

@app.route("/score", methods=['POST'])
def receive_data():
    data = request.get_json()
    time1 = [data["username"],data["time"]]
    scores (time1)
    return ("<p>success!</p>")
@app.route("/leaderboard")
def show_leaderboard():
    return("<div>\
           <ul class=\"nav fix1\">\
             <li id='navlb'><a href='/'>Home</a></li>\
             <li id='navlb' ><a href='/leaderboard'>Leaderboard</a></li>\
             <li id='navlb'><a href='/about'>About</li> </a> </ul>\
           <div id='lb'>\
                <link rel= \"stylesheet\" type= \"text/css\" href= \"static/style.css\">\
                <h1 id='lbHead'>LEADERBOARD</h1>\
                <table id='table-container'></table>\
                <script src='static/leaderboard.js'></script>\
            </div>\
           </div>")

@app.route("/about")
def show_about():
    return ("<div>\
            <ul class=\"nav fix2\">\
             <li id='navlb'><a href='/'>Home</a></li>\
             <li id='navlb' ><a href='/leaderboard'>Leaderboard</a></li>\
             <li id='navlb'><a href='/about'>About</li></a></ul>\
            <div id='sideNav'><ul>\
                <li class='sn'><a href='#intro'>Introduction</a></li> \
                <li class='sn'><a href='#cv'>Computer Vision</a></li>\
                <li class='sn'><a href='#or'>Object Recognition</a></li>\
                <li class='sn'><a href='#opencv'>OpenCV</a></li>\
                <li class='sn'><a href='#us'>Our Project</a></li>\
            </ul></div>\
            <div id='ab'>\
                <link rel= \"stylesheet\" type= \"text/css\" href= \"static/style.css\">\
            <div id='intro'>\
                <h1 id='hintro'>Introduction</h1>\
                <p id='pintro'> 'Where's Biryani?' is our brainchild for presenting object recognition in a simple and entertaining manner.\
                    We chose this topic not only because we found it interesting, but also because object recognition is being \
                    used on a regular basis in various industries like retail, security, healthcare, and more. <br> To know more \
                    about the technicalities of our project, read on! </p>\
            </div>\
            <div id='cv'>\
                <h1 class='sheadings'>Computer Vision</h1>\
                <p class='sparas'> Computer vision is a field of AI that works with deriving meaningful information from digital images,\
                    videos and other visual media. Computer vision enables computers to see and comprehend visual inputs.<br>\
                    It is being used in industries ranging from energy and utilities to manufacturing. Automotive giants like \
                    Tesla, Audi, and BMW make use of computer vision in self-driving cars. It is projected to reach $41.11 \
                    billion by 2030.\
                </p>\
            </div>\
            <div id='or'>\
                <h1 class='sheadings'>Object Recognition</h1>\
                <p class='sparas'> Object recognition is a type of technology that is a part of computer vision. It is capable of locating \
                    objects in images and other visual inputs.<br>\
                    Real-life applications include face and vehicle recognition, pedestrian counting, self-driving vehicles, \
                    security systems, and more.\
                <img class='imgs' src='static/or1.png'>\
                </p>\
            </div>\
            <div id='opencv'>\
                <h1 class='sheadings'>OpenCV</h1>\
                <p class='sparas'> OpenCV is a widely used library for real-time computer vision and image processing. \
                    It is often used in factory product inspection, medical imaging, and security analysis.\
                </p>\
            </div>\
            <div id='us'>\
                <h1 class='sheadings'>Our Project</h1>\
                <p class='sparas'> We make use of template matching, a method in digital image processing available in opencv for searching and \
                    locating a template image in a source image. \
                    <img class='imgs' src='static/opencv.png'> <br>\
                    <br>To recognise the template image, we have to compare it against the source image by sliding it, which means \
                    moving the patch one pixel at a time.<br>\
                    <br>At every location, a metric will be calculated to represent how similar the patch is to our template image. \
                    The metric is stored in a result matrix (a two-dimensional array, with values for x and y coordinates). \
                    The function minMaxLoc is used to locate the highest value (or lowest, depending on the type of matching \
                    method) in the result matrix.\
                </p>\
                <img class='hehe' src='static/sliding.png'>\
            </div>\
            </div>")