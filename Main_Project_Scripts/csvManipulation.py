import csv
from Main_Project_Scripts.district import District
from Main_Project_Scripts.school import School


def findLines(file):
    # Creates a list of lists, where each sublist is a line in the original CSV file
    lines = []
    with open(file, 'r') as data:
        CSVReader = csv.reader(data)
        for row in CSVReader:
            lines.append(row)
    return lines[1:]


def findIndividualGroups(lines):
    # TODO: SO MUCH TESTING ON THIS. SO MUCH TESTING.
    dataset = []
    firstReaderIndex = 0
    secondReaderIndex = 1

    if(lines[0] == "Yes" or lines[0] == "No"):
        nameLocation = 1
    else:
        nameLocation = 0

    while firstReaderIndex < len(lines):
        while secondReaderIndex < len(lines) and \
                (lines[firstReaderIndex][nameLocation] == lines[secondReaderIndex][nameLocation]):
            secondReaderIndex += 1
        dataset.append(lines[firstReaderIndex:secondReaderIndex])
        firstReaderIndex = secondReaderIndex
        secondReaderIndex += 1

    return dataset


def createSchool(lines):
    # TODO: Test this function
    # Creates a school from a set of lines
    charter = isCharter(lines[0])
    grades = removeNAGradesAndCombineAllGrades(lines, 10)

    initSchool = School(charter, lines[0][3], lines[0][1], lines[0][4], fillGrades(grades))
    return initSchool


def createDistrict(lines):
    if lines[0][1] != "Charter agency":
        grades = removeNAGradesAndCombineAllGrades(lines, 11)
        initDistrict = District(lines[0][0], lines[0][2], [], fillGrades(grades))
        return initDistrict
    else:
        return None

def listSchoolsInDistrict():
    return None

def isCharter(line):
    if "Yes" in line[0]:
        return "charter"
    else:
        return "not charter"


def removeNAGradesAndCombineAllGrades(lines, lowerBoundInclusive):
    # Creates a list of grades, which each index takes the form "Grade: Value"
    # TODO: Test this function
    returnLines = []
    for line in lines:
        if(len(line) > 12):
            grades = (line[lowerBoundInclusive] + ";" + line[lowerBoundInclusive+1] + ";" + line[lowerBoundInclusive+2]).split(";")
            i = 0
            while i < len(grades):
                if "NA" in grades[i]:
                    grades.remove(grades[i])
                else:
                    i += 1
            returnLines.append(grades)

    return returnLines


def fillGrades(lines):
    gradeDictionary = {
        "K": [],
        "Gr1": [],
        "Gr2": [],
        "Gr3": [],
        "Gr4": [],
        "Gr5": [],
        "Gr6": [],
        "Gr7": [],
        "Gr8": [],
        "Gr9": [],
        "Gr10": [],
        "Gr11": [],
        "Gr12": [],
    }

    for line in lines:
        for cell in line:
            splits = cell.strip(" ").split(":")
            gradeDictionary[splits[0]].append(splits[1])
    return gradeDictionary
