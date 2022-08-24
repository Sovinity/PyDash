# ╘(̾●̮̮̃̾•̃̾)╛
import os
import queue as q
import threading as th
import random as r
import time as t

#clears the screen
def clear():
    os.system("clear")


scores_txt = open("scores.txt", "w")
scores_txt = open("scores.txt", "r")
if scores_txt.readline() == "":
    scores_txt = open("scores.txt", "w")
    scores_txt.write("0")
scores_txt = open("scores.txt", "r")
score = scores_txt.readline()
display = []
playerPos = 4
gridView = False
spikeHit = False
jump = False
emptyChunk = [" "," "," "," "," ","▮"]

#creates UI
def interface(queue):
    clear()
    print("PPP    Y   Y   DDD     AAA     SSS    H   H")
    print("P  P    Y Y    D  D   A   A   S       H   H")
    print("PPP      Y     D  D   AAAAA    SSS    HHHHH")
    print("P        Y     D  D   A   A       S   H   H")
    print("P        Y     DDD    A   A    SSS    H   H")
    print("▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮")
    print("               High score: "+score)
    #generates the bg randomly idk it's cool don't question it
    #this generates the starry background stuff
    for i in range(4):
        output = []
        for i in range(43):
            num = r.randint(1,14)
            output.append(num)
        actually_outputs = ""
        for i in output:
            if i == 7:
                actually_outputs += "."
            else:
                actually_outputs += " "
        print(actually_outputs)
    output = []
    #this generates the random spikes
    for i in range(43):
        num = r.randint(1,14)
        output.append(num)
    actually_outputs = ""
    for i in output:
        if i == 7:
            actually_outputs += "∆"
        else:
            actually_outputs += " "
    print(actually_outputs)
    output = ""
    #this generates the ground
    for i in range(43):
        output += "▮"
    print(output)

    #this is the actual menu choice
    print("         START                EXIT")
    choice = input("")
    #start : 9-14 spaces
    #exit : 30-33 spaces
    if len(choice) >= 9 and len(choice) <= 14:
    # Starts the game VVVVVVV
        startGame(queue)
    elif len(choice) >= 30 and len(choice) <= 33:
        exit
    else:
        interface(queue)
# ╘(̾●̮̮̃̾•̃̾)╛

#generates chunks of the map
def genChunk():
    global gridView
    val = r.randint(1,10)
    if gridView == True:
        if val == 1:
            chunk = ["-","-","-","-","∆","▮"]
    else:
        chunk = ["-","-","-","-","-","▮"]
    if gridView == False:
        if val == 1:
            chunk = [" "," "," "," ","∆","▮"]
        else:
            chunk = [" "," "," "," "," ","▮"]
    return chunk
# ╘(̾●̮̮̃̾•̃̾)╛
#generates chunks of blocks
#⬜

def printChunks():
    global display
    global playerPos
    global score
    print("▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ Score: "+str(score)+" ▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮")
    for a in range(len(display[0])):
        for b in range(len(display)):
            if b == 3 and a == playerPos:
                print("P"+f"", end="")
            else:
                print(display[b][a]+f"", end="")
        print("")

def gameEnd(queue):
    global score
    runThread.join()
    clear()
    print("▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ Score: "+str(score)+" ▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮")
    for i in range(4):
        output = []
        for i in range(43):
            num = r.randint(1,14)
            output.append(num)
        actually_outputs = ""
        for i in output:
            if i == 7:
                actually_outputs += "."
            else:
                actually_outputs += " "
        print(actually_outputs)
    output = []
    if score < 100:
        something_idk_funni = "You suck!"
    else:
        something_idk_funni = "Try again!"
    print("▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ " + something_idk_funni + " ▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮")

#lets the player jump
def jumpp(queue):
    while True:
        temp = input("")
        if temp == "":
            action = "jump"
            queue.put(action) 

def runn(queue):
    global spikeHit
    global score
    global display
    global playerPos
    start = inputThread.start()
    jacksoniscool = 0
    while spikeHit == False:
        score = int(score)
        score += 1
        clear()
        display.append(genChunk())
        display.pop(0)
        printChunks()
        t.sleep(0.2)
        action = queue.empty()
        if  action == False and jacksoniscool == 0:
            playerPos = 3
            jacksoniscool += 1
        elif action == False and (jacksoniscool == 1 or jacksoniscool == 2 or jacksoniscool == 3):
            playerPos = 2
            jacksoniscool += 1
        elif action == False and jacksoniscool == 4:
            playerPos = 3
            jacksoniscool += 1
        elif action == False and jacksoniscool == 5:
            playerPos = 4
            jacksoniscool = 0
            action = queue.get()
        elif action == True:
            jacksoniscool = 0
        else:
            jacksoniscool = 0
            action = queue.get()
        if display[2][4] == "∆" and playerPos == 4:
            spikeHit = True

# ╘(̾●̮̮̃̾•̃̾)╛
#starts the game
def startGame(queue):
    global emptyChunk
    for x in range(50):
        display.append(emptyChunk)
    printChunks()
    runn(queue)
    calvin_bunker = open("scores.txt", "w")
    calvin_bunker.write(str(score))
    
# ╘(̾●̮̮̃̾•̃̾)╛
#- - - - - -end of PyDash Class - - - - - -

queue = q.Queue()
inputThread = th.Thread(target=jumpp, args = (queue, ))
runThread = th.Thread(target=interface, args = (queue, ))
endThread = th.Thread(target=gameEnd, args=(queue, ))
run = runThread.start()
while spikeHit == False:
    pass
end = endThread.start()