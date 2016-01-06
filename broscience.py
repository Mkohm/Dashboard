import random
quotelist = []
def importQuoteList():
    global quotelist

    with open("brosciencequotes.txt", "r") as f:
        for line in f:
            quotelist.append(line.strip())

def getRandomQuote():
    return quotelist[random.randint(0, len(quotelist)-1)]

