def setup():
    size(1280, 720)
    background (0)
    global tut, hi, gg, var, f, numlist, numstring, numint, screen, var4, menu, big, menuimg, space, asteroids, asteroid, astnumlist, speed, score, astcount, x, y,astcoordx,astcoordy, ff, boom, m, n, hiscores, listlines, read
    tut = loadImage("tut.png")
    hi = loadImage("highscore.png")
    menuimg = loadImage ("home.png")
    gg = loadImage("gg.png")
    space = loadImage("Space.png")
    asteroid = loadImage("asteroid.png")
    var = 480
    f = createFont ("Arial", 100, True)
    boom = loadImage("boom.png")
    asteroids = []
    numlist = []
    numstring = ""
    numint = 0
    screen = 0
    var4 = 0
    menu = 0
    astnumlist = []
    speed = 2
    astcoordx = []
    astcoordy = []
    score = ("N/A")
    astcount = 0
    x = 0
    y = 0
    m = 0
    big = 0
    n = 0
    
    read = open("highscores.txt", "r+")
    listlines = read.readlines()
    
    
def keyPressed():
    loopvar = 0
    var2 = 0
    global var, f, numlist, numstring, numint
    if key == "0":
        numlist.append(0)
    elif key == "1":
        numlist.append(1)
    elif key == "2":
        numlist.append(2)
    elif key == "3":
        numlist.append(3) 
    elif key == "4":
        numlist.append(4)
    elif key == "5":
        numlist.append(5)
    elif key == "6":
        numlist.append(6)
    elif key == "7":
        numlist.append(7)
    elif key == "8":
        numlist.append(8)
    elif key == "9":
        numlist.append(9)
    elif key == BACKSPACE:
        if numlist == []:
            loopvar = 0
        else:
            numlist.pop
            last = len(numstring)
            numstring = numstring[:last-1]
            var2 = 1
    else:
        loopvar = 1
    if loopvar == 0:
        if numlist == []:
            loopvar = 0
        else:
            if var2 == 0:
                numstring += str(numlist[-1])
                
def keyTyped():
    if key == ENTER:
        if menu == 1:
            for x in range (10):
                global var, numstring, x, y, numlist, var4, astnumlist, asteroids, score, astcount, boom, m, n, big
                if len(asteroids) == 1:
                    if numstring == str(int(astnumlist[0] + astnumlist[1])):
                        big = 150
                        m = 1
                        n = 1
                elif len(asteroids) == 2:
                    if numstring == str(int(astnumlist[2] + astnumlist[3])):
                        big = 150                        
                        m = 2
                        n = 2
                elif len(asteroids) == 3:
                    if numstring == str(int(astnumlist[4] + astnumlist[5])):
                        big = 150                        
                        m = 3
                        n = 3
                elif len(asteroids) == 4:
                    if numstring == str(int(astnumlist[6] + astnumlist[7])):
                        big = 150
                        m = 4
                        n = 4
                elif len(asteroids) == 5:
                    if numstring == str(int(astnumlist[8] + astnumlist[9])):
                        big = 150
                        m = 5
                        n = 5
                del numlist [:-1]
                numstring = ""
    
                
        
def draw():
    global var, f, numlist, hiscores, numstring, numint, screen,var4, menu, menuimg, space, asteroid, asteroids, astnumlist, speed, astcoordx, astcoordy, score, astcount, ff, big, m, n, read, listlines
    if menu == 0:
        clear()
        background (menuimg)
    elif menu == 1:
        textAlign(CENTER,CENTER)
        background(space)
        if var >= 480:
            if astcount == 6:
                var = 0
            elif astcount < 6:
                var = 0
                global x, y
                x = int(random(9))
                y = int(random(9))
                astnumlist.append(x)
                astnumlist.append(y)
                astcount += 1
                astcoordy.append(1400)
                z = int(random(5))
                asteroids.append("ast")
                if z == 0:
                    imageMode (CENTER)
                    image(asteroid, 1400, 100, 300,300)
                    astcoordx.append(100)
                if z == 1:
                    imageMode (CENTER)
                    image(asteroid, 1400, 200, 300,300)
                    astcoordx.append(200)
                if z == 2:
                    imageMode (CENTER)
                    image(asteroid, 1400, 300, 300, 300)
                    astcoordx.append(300)
                if z == 3:
                    imageMode (CENTER)
                    image(asteroid,1400,400,300,300)
                    astcoordx.append(400)
                if z == 4:
                    imageMode (CENTER)
                    image(asteroid,1400,500,300,300)
                    astcoordx.append(500)
        if len(asteroids) > 0:
            for a in range(len(asteroids)):
                astcoordy[a] = astcoordy[a] - speed
                image(asteroid, astcoordy[a], astcoordx[a], 300,300)
                fill(255)
                text ("+", astcoordy[a], astcoordx[a])
                text (str(astnumlist[a*2]), astcoordy[a] - 50, astcoordx[a])
                text (str(astnumlist[a*2+1]), astcoordy[a] + 50, astcoordx[a])
            if ((astcoordy[0] <= 200 and astcoordx[0] == 100) or (astcoordy[0] <= 210 and astcoordx[0] == 200) or (astcoordy[0] <= 220 and astcoordx[0] == 300) or (astcoordy[0] <= 217 and astcoordx[0] == 400) or (astcoordy[0] <= 211 and astcoordx[0] == 500)):
                menu = 5
                read.write("\n"+str(score))
        global x, y
        x = x
        y = y
        string = [x,"+",y]
        textFont(f,50)
        fill(0,255,0)
        text (numstring, width/2, 50)
        if m <= 1 and m >= 0.5:
            if big <= 200:
                stroke (255, 30, 30)
                strokeWeight (10)
                line(220,height/2, astcoordy[0], astcoordx[0])
                image(boom, astcoordy[0], astcoordx[0], big, big)
                fill(255,0,0)
                big += 10
                m -= 0.1
            n+=0.1
        elif m <= 2 and m >= 1.5:
            if big <= 200:
                stroke (255, 30, 30)
                strokeWeight (10)
                line(220,height/2, astcoordy[1], astcoordx[1])
                image(boom, astcoordy[1], astcoordx[1], big, big)
                fill(255,0,0)
                big += 10
                m -= 0.1
                n += 0.1
        elif m <= 3 and m >= 2.5:
            if big <= 200:
                stroke (255, 30, 30)
                strokeWeight (10)
                line(220,height/2, astcoordy[2], astcoordx[2])
                image(boom, astcoordy[2], astcoordx[2], big, big)
                fill(255,0,0)
                big += 10
                m -= 0.1
                n += 0.1
        elif m <= 4 and m >= 3.5:
            if big <= 200:
                stroke (255, 30, 30)
                strokeWeight (10)
                line(220,height/2, astcoordy[3], astcoordx[3])
                image(boom, astcoordy[3], astcoordx[3], big, big)
                fill(255,0,0)
                big += 10
                m -= 0.1       
                n += 0.1
        elif m <= 5 and m >= 4.5:
            if big <= 200:
                stroke (255, 30, 30)
                strokeWeight (10)
                line(220,height/2, astcoordy[4], astcoordx[4])
                image(boom, astcoordy[4], astcoordx[4], big, big)
                fill(255,0,0)
                big += 10
                m -= 0.1
                n += 0.1                
        if n >= 1.6:
            del astnumlist[0 and 1]
            del asteroids[0]
            del astcoordx[0]
            del astcoordy[0]
            score += 100
            astcount -= 1
            del numlist [:-1]
            numstring = ""
            n = 0
        if n >= 2.6:
            del astnumlist[2 and 3]
            del asteroids[1]
            del numlist [:-1]
            score += 100
            numstring = ""
            astcount -= 1
            del astcoordx[1]
            del astcoordy[1]
            n = 0
        if n >= 3.6:
            del astnumlist[4 and 5]
            del asteroids[2]
            del astcoordx[2]
            del astcoordy[2]
            del numlist [:-1]
            score += 100
            astcount -= 1
            numstring = ""
            n = 0
        if n >= 4.6:
            del astnumlist[6 and 7]
            del asteroids[3]
            del astcoordx[3]
            del astcoordy[3]
            astcount -= 1
            del numlist [:-1]
            numstring = ""
            score += 100
            n = 0
        if n >= 5.6:
            del astnumlist[8 and 9]
            del asteroids[4]
            del astcoordx[4]
            del astcoordy[4]
            del numlist [:-1]
            astcount -= 1
            numstring = "" 
            score += 100
            n = 0
        textAlign(LEFT)
        text(int(score),0,50)
        textAlign(CENTER)
        if speed > 7:
            speed += 0.001
        else:
            speed = speed
        if speed < 3:
            var += 1
        elif speed < 3 and speed > 5:
            var += 1.5
        elif speed > 7:
            var += 2
        else:
            var += 1.2
    elif menu == 2:
        clear()
        background(tut)
    elif menu == 3:
        textAlign(LEFT)
        text
        clear()
        background(hi)
        textFont (f, 50)
        listlines = sorted(listlines, reverse = True)
        text ("Your Last Score: "+str(score), width/2-300, height/2-50)        
        text ("1: "+str(listlines[0]), width/2-300, height/2+50)
        text ("2: "+listlines[1], width/2-300, height/2+150)
        text ("3: "+listlines[2], width/2-300, height/2+250)
    elif menu == 5:
        clear()
        background(gg)
        
        
def mouseClicked():
    global menu, score, numlist, numstring, numint, screen, var4, big, menuimg, space, asteroids, asteroid, astnumlist, speed, score, astcount, x, y,astcoordx,astcoordy, ff, boom, m, n, hiscores
    if menu == 0:
        if mouseX >= 111 and mouseX <= 459 and mouseY >= 225 and mouseY <= 345:
            print (mouseX, mouseY) 
            menu = 2
        elif mouseX >= 812 and mouseX <= 1160 and mouseY >= 225 and mouseY<= 345:
            menu = 1
            asteroids = []
            numlist = []
            numstring = ""
            numint = 0
            screen = 0
            var4 = 0
            astnumlist = []
            speed = 2
            astcoordx = []
            astcoordy = []
            score = 0
            astcount = 0
            x = 0
            y = 0
            m = 0
            big = 0
            n = 0
            print("0")
        elif mouseX >= 111 and mouseX <= 459 and mouseY >= 508 and mouseY<= 628:
            menu = 3
        elif mouseX >= 812 and mouseX <= 1160 and mouseY >= 508 and mouseY<= 628:
            exit()
    if menu == 2:
        if mouseX >= 957 and mouseY >= 607 and mouseX <= 1280 and mouseY <= 720:
            menu = 0
    if menu == 3:
        if mouseX >= 957 and mouseY >= 607 and mouseX <= 1280 and mouseY <= 720:
            menu = 0
    if menu == 5:
        if mouseX >= 1060 and mouseY >= 654 and mouseX <= 1280 and mouseY <= 720:
            menu = 0
