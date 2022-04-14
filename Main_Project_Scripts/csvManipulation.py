import csv

from Main_Project_Scripts.school import School


def findLines(file):
    # Creates a list of lists, where each sublist is a line in the original CSV file
    lines = []
    with open(file, 'r') as data:
        CSVReader = csv.reader(data)
        for row in CSVReader:
            lines.append(row)
    return lines[1:]


def createSchool(lines):
    # TODO: Test this function
    #Creates a school from a set of lines
    if lines[0][0] == "Yes":
        charter = True
    else:
        charter = False
    grades = removeNAGradesAndCombineAllGrades(lines)

    initSchool = School(charter, lines[0][3], lines[0][1], lines[0][4], fillGrades(grades))
    return initSchool

def removeNAGradesAndCombineAllGrades(lines):
    #Creates a list of grades, which eacb index takes the form "Grade: Value"
    #TODO: Test this function

    for line in lines:
        grades = [line[11].split(";"), line[12].split(";"), line[13].split(";")]
        for individualGrade in grades:
            if "NA" in individualGrade:
                grades.remove(individualGrade)

    return grades

def fillGrades(lines):
    #TODO: finish this.
    gradeDictionary = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
    }
    return gradeDictionary
