"""
title: Homework Planner
author: Chelsea Chen
date created: 06-17-2020
"""
"""
# graphics
from tkinter import *
root = Tk()
# creating alabel widget
Screen = Label(root, text = "Homework Planner")
Screen.pack()
# Button

def myClick():
    input = Entry(root)
    input.pack()
    date = Label(root, text= "What is the date you would like to set?" + input.get())
    date.pack()
    button = Button(root, text = "set")
    button.pack()

setStudy = Button(root, text = "Press to schedule studytime", padx = 20, pady = 20)
setStudy.pack()
testDate = Button(root, text = "Press to schedule due/test date", padx = 20, pady = 20, command = myClick)
testDate.pack()
Quitbutton = Button(root, text ="Exit", command = root.quit)
Quitbutton.pack()


# put on screen
root.mainloop()
# Button
"""

import time
again = True
months = (("January",1),("February",2), ("March",3), ("April",4), ("May",5), ("June",6), ("July",7), ("August",8), ("September",9), ("October",10), ("November",11), ("December",12))
studyperiod = 5
shortbreak = 5
longbreak = 5
def menu():
    global choice
    print(
"""
Welcome to the Homework Helper
1. Schedule a due date or study time
2. View scheduled due dates or study times
3. Delete a scheduled event 
4. Use timer for studying (pomodoro technique)
"""
    )
    choice = int(input("input number: "))
    if choice > 4 or choice <= 0:
        print("Please enter valid choice")
        return menu()

def cal():
    calendar = []
    for i in range(13):
        calendar.append([])
        for j in range(32):
            calendar[i].append([])
            for l in range(25):
                calendar[i][j].append([])
                for m in range(61):
                    calendar[i][j][l].append([])
    calendar[1].pop()
    calendar[1].pop()
    calendar[1].pop()
    calendar[3].pop()
    calendar[5].pop()
    calendar[8].pop()
    calendar[10].pop()
    return calendar

date = cal()

def chooseDate():
    global months
    global year
    global time
    chooseMonth = str(input("input the month (capatilize first letter of the month): "))
    if (chooseMonth == "January") or chooseMonth ==  "February" or chooseMonth == "March" or chooseMonth == "April" or chooseMonth == "May" or chooseMonth == "June"or chooseMonth == "July"or chooseMonth == "August" or chooseMonth == "Septemeber" or chooseMonth == "October" or chooseMonth == "November" or chooseMonth == "December":
        for i in range(len(months)):
            if chooseMonth == months[i][0]:
                chooseMonth = months[i][1]
                chooseMonth = int(chooseMonth)
    else:
        print("Choose Valid month")
        return chooseDate()
    chooseDay = int(input("input the day: "))
    if (chooseDay < 0 or chooseDay > len(date[11])):
        print("Please input valid day of the month")
        return chooseDate()
    chooseHour = int(input("input the hour of day: "))
    if (chooseHour > 24):
        print("Please input valid hour of day (24 hour clock)")
        return chooseDate()
    chooseMinute = int(input("input minute of the day: "))
    if (chooseMinute > 60):
        print("Please input valid value")
        return chooseDate()
    else:
        return chooseMonth, chooseDay, chooseHour, chooseMinute
def timer():
    for i in range(timeperiod):
        minutes = timeperiod // 60
        seconds = timeperiod % 60
        timers = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
        print("\r", end=timers)
        time.sleep(1)
        period = period - 1
    return timeperiod
def study():
    global study
    for i in range(study):
        time.sleep
        study = study - 1
    return study

# --- Main --- #
event = []
# --- Inputs --- #
while again == True:
    menu()
    if choice == 1:
        print("What would you like to name the date you are scheduling? ")
        event = str(input())
        month, day, hour, minute = chooseDate()
        date[month][day][hour][minute] = event
        print("date saved")
        for i in range(len(months)):
            if month == months[i][1]:
                month = months[i][0]
    elif choice == 2:
        print("""
    1. Search for test/assignment due date or scheduled study time
    2. Search for events planned based on date and time
        """)
        myinput = int(input("input number: "))
        while (myinput <= 0) or (myinput > 2):
            print("Please enter valid choice")
            myinput = int(input("input number: "))
        if myinput == 1:
            name = str(input("Name of test/assignment/study time: "))
            if name == event:
                print("test/assignment/study time: " + str(event))
                if minute > 10:
                    print("date: " + str(month) + " " + str(day) + "," + str(hour) + ":" + str(minute))
                else:
                    print("date: " + str(month) + " " + str(day) + "," + str(hour) + ":0" + str(minute))
            else:
                print("There was no event planned this day")
        if myinput == 2:
            month, day, hour, minute = chooseDate()
            if date[month][day][hour][minute] == event:
                print(event)
            else:
                print("There was no event planned this day")
    elif choice == 3:
        name = str(input("Name of test/assignment/study time: "))
        if name == event:
            print("test/assignment/study time: " + str(event))
        delete = input("Would you like to delete this event y/N?")
        if delete == "Y" or "Y":
            print(str(event) + "" + "was deleted")
            event = 0
        else:
            pass
    elif choice == 4:
        study = int(input("How long would you like to study for? (minutes): "))
        start = input("Press s/S to start the timer")
        if start == "s" or start == "S":
            while study > 0:
                for i in range(study):
                    time.sleep
                    study = study - 1
                for i in range(1,5):
                    studyperiod = 5
                    print("")
                    print("Start studying for 25 minutes!")
                    for i in range(studyperiod):
                        minutes = studyperiod//60
                        seconds = studyperiod % 60
                        timers = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
                        print("\r", end = timers)
                        time.sleep(1)
                        studyperiod = studyperiod -1
                        shortbreak = 5
                    if studyperiod == 0:
                        print("")
                        print("Start your 5 minute break! Take this time to destress")
                        for i in range(shortbreak):
                            minutes = shortbreak // 60
                            seconds = shortbreak % 60
                            timers = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
                            print("\r", end=timers)
                            time.sleep(1)
                            shortbreak = shortbreak - 1
                print("")
                print("Start your 20 minute break!")
                for i in range(longbreak):
                    minutes = longbreak// 60
                    seconds = longbreak % 60
                    timers = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
                    print("\r", end=timers)
                    time.sleep(1)
                    longbreak = longbreak - 1