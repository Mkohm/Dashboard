from tkinter import *
import calculatesleep
import broscience

bedtime = ""
happening = ""

def findHappening():
    global happening
    #happening kan være "" tom streng
    happening = calculatesleep.returnHappening()
    happening = happening.replace("SUMMARY:", "")
def soveLengeEllerLeggeseg():
    global bedtime
    if time == 0:
        bedtime = "Du kan sove lenge."
    else:
        res1, res2, res3, res4 = calculatesleep.calculateBedTime(time[0], time[1])
        bedtime = "Du må legge deg: " + res1[0] + "." + res1[1] + ", " + res2[0] + "." + res2[1] + ", " + res3[0] + "." + res3[1] + " eller " + res4[0] + "." + res4[1] + " - " + happening + "."
def createGui():
    root = Tk()

    sleepFrame = Frame(root)
    quoteFrame = Frame(root)
    temperatureFrame = Frame(root)

    quoteFrame.pack(side=BOTTOM, expand=True, fill='both')
    sleepFrame.pack(side=LEFT, fill=BOTH)
    temperatureFrame.pack(side=LEFT, fill=BOTH)



    sleep = Text(sleepFrame, bg="#EC663C",font="Arial 25 bold", fg="white", height="20")
    sleep.insert(END, bedtime)
    sleep.pack()

    temperature = Text(temperatureFrame, bg="#EC663C",font="Arial 25 bold", fg="white", height="20")
    #get temperature
    temperature.insert(END, "21℃tndhaentdaeonuthdaonetuhd")
    temperature.pack()


    quoteText = Text(quoteFrame, bg="#47BBB3",font="Arial 25 bold", fg="white", height="5")
    quoteText.insert(END,quote)
    quoteText.pack()





    root.mainloop()


#Trenger bare å gjøres 1 gang om dagen, før klokken 12
time = calculatesleep.getWakeuptimeFromGoogleCalendar()
findHappening()
soveLengeEllerLeggeseg()

#get random quote
broscience.importQuoteList()
quote = broscience.getRandomQuote()


createGui()

print(quote)



