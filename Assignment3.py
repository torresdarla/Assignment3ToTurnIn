# Programmed by Darla Torres
# July 18, 2017

# This program takes a set of temperatures from the NASA website, and analyzes temperature anomalies
data = open('temps.txt', 'r')

# This function reads the temps from the temps.txt file and returns them in a list

def readTemps(file):
    temps=[]
    for line in file:
        temps.append(float(line))
    return temps

file = readTemps(data)


# This function calculates the average of a range of numbers as specified by start (inclusive) and stop (inclusive)

def calculateAve(start, stop, file):
    numbers = []
    for index in range(len(file)):
        if index >= start and index <= stop:
            numbers.append(file[index])
    avg = sum(numbers)/len(numbers)
    return avg

# This function counts all values that have a positive deviation in the range as specified by start (inclusive) and stop (inclusive)       

def count(start, stop, file):
    numbers = []
    for index in range(len(file)):
        if index >= start and index <= stop and file[index]>0:
            numbers = numbers + [file[index]]
    length= len(numbers)
    return length

#Main Function
#Data downloaded from http://climate.nasa.gov/
#Data represents the deviation in global surface
#Temperature relative to 1952-1980 average temperatures
def main():
    average = calculateAve(0,80,file)
    dev= count(0,80,file)
    average1= calculateAve(81,115,file)
    dev1= count(81,115,file)
    print "During the first 81 years, the average deviation from the temperature anomaly is %s" %(average) 
    print "Dyring the first 81 years, %s had a positive temperature anomoly" %dev
    print "During the last 35 years, the average deviation from the temperature anomaly is %s" %(average1) 
    print "Dyring the last 35 years, %s had a positive temperature anomoly" %dev1
  

  
main()

