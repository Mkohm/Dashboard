from datetime import datetime
import calculatesleep

def calculateTime():
    #regner sleep cycles fremover + pluss på 14 minutter

    nowhour = datetime.now().hour
    nowminute = datetime.now().minute

    milli = convertToMilli(nowhour, nowminute)

    #1 cycle fremover
    d, h, m, s = calculatesleep.prntime(milli + (90*60000))
    res1 = calculatesleep.addzero([h, m])

    #2 cycle fremover
    d2, h2, m2, s2 = calculatesleep.prntime(milli + (90*60000)*2)
    res2 = calculatesleep.addzero([h2, m2])

    #3 cycle fremover
    d3, h3, m3, s3 = calculatesleep.prntime(milli + (90*60000)*3)
    res3 = calculatesleep.addzero([h3, m3])

    #4 cycle fremover
    d4, h4, m4, s4 = calculatesleep.prntime(milli + (90*60000)*4)
    res4 = calculatesleep.addzero([h4, m4])

    #5 cycle fremover
    d5, h5, m5, s5 = calculatesleep.prntime(milli + (90*60000)*5)
    res5 = calculatesleep.addzero([h5, m5])

    #6 cycle fremover
    d6, h6, m6, s6 = calculatesleep.prntime(milli + (90*60000)*6)
    res6 = calculatesleep.addzero([h6, m6])

    #7 cycle fremover
    d7, h7, m7, s7 = calculatesleep.prntime(milli + (90*60000)*7)
    res7 = calculatesleep.addzero([h7, m7])

    return [res1, res2, res3, res4, res5, res6, res7]

def convertToMilli(hour, minute):
    return (hour*3600000) + (minute*60000)



print(calculateTime())