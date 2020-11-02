import csv
from collections import Counter


def Find_Mean(Data):
    SumOfWeights = sum(Data)
    noOfWeights = len(Data)
    Mean = SumOfWeights / noOfWeights
    print("Mean (Average) is -> ", Mean, 'pounds')


def Find_Median(Data):
    Data.sort()
    noOfWeights = len(Data)
    if(noOfWeights % 2 == 0):
        observation1 = float(Data[noOfWeights//2])
        observation2 = float(Data[noOfWeights//2 + 1])
        Median = (observation1 + observation2)/2
        print('Median is -> ', Median, 'pounds')
    else:
        observation3 = float(Data[noOfWeights//2])
        print('Median is -> ', observation3, 'pounds')


def Find_Mode(Data):
    mode = Counter(Data)
    r = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0,
    }
    for weight, number in mode.items():
        if 75 < float(weight) < 85:
            r["75-85"] += number
        elif 85 < float(weight) < 95:
            r["85-95"] += number
        elif 95 < float(weight) < 105:
            r["95-105"] += number
        elif 105 < float(weight) < 115:
            r["105-115"] += number
        elif 115 < float(weight) < 125:
            r["115-125"] += number
        elif 125 < float(weight) < 135:
            r["125-135"] += number
        elif 135 < float(weight) < 145:
            r["135-145"] += number
        elif 145 < float(weight) < 155:
            r["145-155"] += number
        elif 155 < float(weight) < 165:
            r["155-165"] += number
        elif 165 < float(weight) < 175:
            r["165-175"] += number

    modeRange, modeNumber = 0, 0
    for Range, Number in r.items():
        if Number > modeNumber:
            modeRange, modeNumber = [
                int(Range.split("-")[0]), int(Range.split("-")[1])], Number

    Mode = float((modeRange[0] + modeRange[1]) / 2)
    print("Median is -> ", Mode, 'pounds')


with open("C:/Users/Teju Sraav/Desktop/Sravan/WhitehatJr Python/Projects/Mean,Median and Mode/SOCR-HeightWeight.csv", newline='') as f:
    readedData = csv.reader(f)
    fileData = list(readedData)
    fileData.pop(0)
    Weight_Data = []
    for i in range(len(fileData)):
        Data = fileData[i][2]
        Weight_Data.append(float(Data))

    Find_Mean(Weight_Data)
    Find_Median(Weight_Data)
    Find_Mode(Weight_Data)
