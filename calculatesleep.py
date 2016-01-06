import time
from datetime import datetime
import urllib.request

happening = ""
def findDifference(year, month, day, hour, minute):
    date = datetime(year=year,month=month,day=day, hour=hour, minute=minute)
    now = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute)
    diff = date-now

    return diff

def getWakeuptimeFromGoogleCalendar():
    global happening

    #gets file and puts every line in the file into a list

    ##################put your link in here##################
    site = urllib.request.urlopen("https://calendar.google.com/calendar/ical/marius.kohmann%40gmail.com/public/basic.ics")

    
    html = site.read()
    html = html.decode()
    html = html.replace("\r", "")
    htmllist = html.split("\n")


    #making a 2d list with every event in the calendar, including only the necessary info
    events = []
    for i in range(0, len(htmllist)):
        if "BEGIN:VEVENT" in htmllist[i]:

            j = 0
            info = []
            while True:
                if "END:VEVENT" in htmllist[i+j]:
                    break

                if "DTSTART" in htmllist[i+j] or "DTEND" in htmllist[i+j] or "RRULE" in htmllist[i+j] or "DESCRIPTION" in htmllist[i+j] or "SUMMARY" in htmllist[i+j]:

                    info.append(htmllist[i+j])
                    #print("legger til", htmllist[i+j])
                j += 1

            #print(info)
            events.append(info)


            i += i+j

        #cheap fix
        if i > len(htmllist)-10:
            break

    #get todays date and find first event
    #hvis finn alle som gjelder for datoen idag og se på klokkeslett, velg det tidligste
    #de som gjelder nå er de som er frem i tid, altså totalt antall sekunder er større enn totalt antall nå

    possible = []
    for i in range(0, len(events)):
        #finner forskjell mellom dagens dato og når eventen ble starta, skal være med i listen om datoen ikke har vært enda
        try:
            time = events[i][0]
            time = time[time.find(":")+1:]


            year = int(time[0:4])
            month = int(time[4:6])
            day = int(time[6:8])
            hour = int(time[9:11])
            minute = int(time[11:13])

            #print(time, year, month, day, hour, minute)

            diff = findDifference(year, month, day, hour, minute)

            if diff.total_seconds() > 0 or "RRULE:" in events[i][2]:
                possible.append(events[i])

        except:
            continue

    #sorterer ut de hvor UNTIL/RRULE har gått ut
    possible2 = []
    for i in range(0, len(possible)):
        #sjekke om RRULE events er utgått
        time2 = possible[i][2]
        if "UNTIL=" in time2:

            time2 = time2[time2.find("UNTIL=")+6:]


            year2 = int(time2[0:4])
            month2 = int(time2[4:6])
            day2 = int(time2[6:8])
            hour2 = int(time2[9:11])
            minute2 = int(time2[11:13])

            #print(time2, year2, month2, day2, hour2, minute2)
            diff2 = findDifference(year2, month2, day2, hour2, minute2)
            #print(time2, diff2)

            if diff2.total_seconds() > 0:
                possible2.append(possible[i])

        else:
            possible2.append(possible[i])

    print(possible2)

    weekdays = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    currentDay = datetime.now().weekday()
    tomorrowDay = currentDay+1
    tomorrowDay = weekdays[tomorrowDay]


    #find all occurences on a day and then choose the earliest one
    #finner enten datoen i RRULE eller at startdatoen er samme dag.
    possibletimes = []
    for i in range(0, len(possible2)):

        happening = ""
        ptime = possible2[i][0]
        ptime = ptime[ptime.find(":")+1:]
        dato = datetime(year=int(ptime[0:4]), month=int(ptime[4:6]), day=int(ptime[6:8]))
        dato = dato.weekday()
        dato = weekdays[dato]


        if tomorrowDay in possible2[i][2] or tomorrowDay in dato:
            possibletime = possible2[i][1]
            possibletime = possibletime[possibletime.find(":")+1:]
            hour = int(possibletime[9:11])

            minute = int(possibletime[11:13])


            possibletimes.append([hour, minute])

            if tomorrowDay in possible2[i][2]:
                happening = possible2[i][4]
            if tomorrowDay in dato:
                happening = possible2[i][3]

    print(possibletimes)

    possibletimes.sort()
    if len(possibletimes) == 0:
        print("ingenting")
        return 0

    return possibletimes[0]


def prntime(ms):
    s=ms/1000
    m,s=divmod(s,60)
    h,m=divmod(m,60)
    d,h=divmod(h,24)

    return int(d),int(h),int(m),int(s)

def addzero(time):
    newtime = []
    for i in range(0, len(time)):

        if len(str(time[i])) == 1:
            newtime.append("0" + str(time[i]))
        else:
            newtime.append(str(time[i]))

    return newtime


def returnHappening():
    return happening


def calculateBedTime(wakeuphour, wakeupminute):
    #print(wakeuphour, wakeupminute)
    #replace currenthour currentminute with wakeuptime


    currentHourMilli = wakeuphour*3600000
    currentMinuteMilli = wakeupminute*60000
    currentTotalMilli = currentHourMilli+currentMinuteMilli
    currentTotalMilli = currentTotalMilli - 270*60000


    d, h, m, s = prntime(currentTotalMilli)
    res1 = addzero([h,m])

    d2, h2, m2, s2 = prntime(currentTotalMilli-90*60000)
    res2 = addzero([h2,m2])

    d3, h3, m3, s3 = prntime(currentTotalMilli-(90*60000)*2)
    res3 = addzero([h3, m3])

    d4, h4, m4, s4 = prntime(currentTotalMilli-(90*60000)*3)
    res4 = addzero([h4, m4])

    return res1, res2, res3, res4
