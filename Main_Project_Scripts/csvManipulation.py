"""
Code written by Roo Case

This file is responsible for many of the inner-workings of the project relating to use within a dataset.
Most of the code here takes on the process of creating object instances.
"""

import csv
from district import District
from school import School
from Listing_Schools_in_a_District import listSchools


def findLines(file):
    """
    A function that gets each individual line from a source CSV file, and then returns each row in the CSV
    file as a list, in one large list.
    :param file: a csv file
    :return: a list of lists, where each "row" (internal list) represents one row of the source CSV file.
    """
    lines = []
    with open(file, 'r') as data:
        CSVReader = csv.reader(data)
        for row in CSVReader:
            lines.append(row)
    return lines[1:]


def findIndividualGroups(lines):
    """
    A function that finds individual units (districts or schools), and cordons them off for later use.
    :param lines: the list of lists as created in findLines().
    :return: a 3-dimensional list, with the inner list being each line, the next outer list being each "unit", and the
    most outer layer being a list of these units.
    """
    dataset = []
    firstReaderIndex = 0
    secondReaderIndex = 1

    if lines[0][0] == "Yes" or lines[0][0] == "No":
        #The two datasets has the data in a slightly different order.
        #Lines 39 through 44 are for determining which datatype is being delt with
        nameLocation = 1
    else:
        nameLocation = 0

    while firstReaderIndex < len(lines):
        """
        This while loop looks has two pointer nodes, 'firstReaderIndex' and 'secondReaderIndex'
        secondReaderIndex will always be at least 1 ahead of firstReaderIndex. They mark the head and tail
        of each of set of data associated with a singular unit (being a school or district)
        
        Once a block has been correctly identified, the head will go to the tail +1, and the cycle will begin anew.
        """
        while secondReaderIndex < len(lines) and \
                (lines[firstReaderIndex][nameLocation] == lines[secondReaderIndex][nameLocation]):
            secondReaderIndex += 1
        dataset.append(lines[firstReaderIndex:secondReaderIndex])
        firstReaderIndex = secondReaderIndex + 1
        secondReaderIndex += 1

    return dataset


def createSchool(lines):
    """
    Creates school object with data provided.
    :param lines: the lines representing a given school dataset.
    :return: the created school object
    """
    # TODO: Test this function
    # Creates a school from a set of lines
    charter = isCharter(lines[0])
    grades = removeNAGradesAndCombineAllGrades(lines, 10)

    initSchool = School(charter, lines[0][3], lines[0][1], lines[0][4], fillGrades(grades))
    return initSchool


def createDistrict(lines, schools):
    """
    A function that creates a district object with the data provided
    :param lines: the lines representing a school district dataset
    :param schools: a list of schools, as to be sorted through by a separate helper function.
    :return:
    """
    if lines[0][1] != "Charter agency":
        grades = removeNAGradesAndCombineAllGrades(lines, 11)
        initDistrict = District(lines[0][0], lines[0][2], listSchools(schools, lines[0][0]), fillGrades(grades))
        return initDistrict
    else:
        return None


def isCharter(line):
    """
    Checks to see if a school is a charter school
    :param line: a singular list, representing a line of a CSV file
    :return: a string that will be stored and outputted later.
    """
    if "Yes" in line[0]:
        return "charter"
    else:
        return "not charter"


def removeNAGradesAndCombineAllGrades(lines, lowerBoundInclusive):
    """
    Not all schools and districts have all grades (well, most districts do, but we're including the possibility for
    edge cases here.) This function trims down all the grades that don't exist, and combines all the lines into a
    singular list of grades.
    :param lines: the lines representing a school district dataset
    :param lowerBoundInclusive: because of differences in our dataset's formatting, this parameter represents where in the list the data in question begins.
    :return: a list of list of grades's learning modes, by week.
    """
    returnLines = []
    for line in lines:
        if (len(line) > 12):
            grades = (line[lowerBoundInclusive] + ";" + line[lowerBoundInclusive + 1] + ";" + line[
                lowerBoundInclusive + 2]).split(";")
            i = 0
            while i < len(grades):
                if "NA" in grades[i]:
                    grades.remove(grades[i])
                else:
                    i += 1
            returnLines.append(grades)

    return returnLines


def fillGrades(lines):
    """
    creates a dictionary of grades and their learning modes.
    :param lines: a list of list of grades's learning modes, by week.
    :return: dictionary of grades and their learning modes. Each index in the value for each key represents a given week.
    """
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
            try:
                gradeDictionary[splits[0]].append(splits[1])
            except(KeyError):
                continue

    return gradeDictionary
