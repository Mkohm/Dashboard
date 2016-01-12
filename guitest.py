import tkinter as Tk
import calculatesleep
import broscience
import calculateIfBedNow

bedtime = ""
happening = ""
results = []


def findTimeBeforeMidnightElseFindTimeToday():
    return time

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
        res1, res2, res3, res4 = calculatesleep.calculateBedTime(time[0], time[1], prepareminutes=60)
        bedtime = "Du må legge deg: " + res4[0] + "." + res4[1] + ", " + res3[0] + "." + res3[1] + ", " + res2[0] + "." + res2[1] + " eller " + res1[0] + "." + res1[1] + " - " + time[2].replace("SUMMARY:", "") + " klokken " + str(time[0]) + ":" + str(time[1]) + "."



def createGui():

    root = Tk.Tk()


    sleep = Tk.Label(root, bg="#EC663C",font="Arial 20 bold", fg="white", height="5", text=bedtime, width="100")
    sleep.grid(row=0)

    temperature = Tk.Label(root, bg="#EC663C",font="Arial 25 bold", fg="white", height="5", text="21 grader")
    temperature.grid(row=1)

    quoteText = Tk.Label(root, bg="#EC663C",font="Arial 25 bold", fg="white", height="5",text=quote)
    quoteText.grid(row=2)

    root.mainloop()


#Trenger bare å gjøres 1 gang om dagen, før klokken 12
time = calculatesleep.getWakeuptimeFromGoogleCalendar()
findHappening()
soveLengeEllerLeggeseg()

#get random quote
broscience.importQuoteList()
quote = broscience.getRandomQuote()


#time if bed now(list with 1 to 7 cycles), update every minute,
results = calculateIfBedNow.calculateTime()


createGui()





