"""
CLI and its helper functions written by Batmend.
Non-CLI functions written by Roo Case.

This is the main python file, that has the highest amount of abstraction. The code for our command-line-interface is
here, as well as the helper functions that are a part of that.
"""

import sys
import Main_Project_Scripts.district
import Main_Project_Scripts.school
from Main_Project_Scripts.csvManipulation import findIndividualGroups, findLines, createSchool, createDistrict

def importSchools():
    """
    Default helper script for setting up a list of schools.
    :return: a list of schools
    """
    listOfSchools = []
    parsedCSV = findIndividualGroups(findLines("Data/Minnesota_Schools_Modified.csv"))
    for group in parsedCSV:
        listOfSchools.append(createSchool(group))
    return listOfSchools


def importDistricts(schools):
    """
    Default helper script for setting up a list of districts.
    :param: a list of all schools
    :return: a list of districts
    """
    listOfDistricts = []
    parsedCSV = findIndividualGroups(findLines("Data/Minnesota_Districts_LearningModelData_Modified.csv"))

    for group in parsedCSV:
        
        district = (createDistrict(group, schools))
        if district != None:
            listOfDistricts.append(district)
    return listOfDistricts

def list_objects(objectList):
    """
    A helper function that concatenates and returns the member objects' names.
    :param: a list of objects.
    :return: concatenated string consisting of member objects' names.
    """
    output = ''
    for object in objectList:
        output += f'{object.name}\n'
    return output

def find_object_by_name(listOfObjects, objectName):
    """
    A helper function that returns a member object with matching name.
    :param: a list of objects and a namestring.
    :return" an object whose name matches the namestring.
    """
    for object in listOfObjects:
        if object.name == objectName:
            return object

def setup():
    """
    A quick helper function that sets up the data in the proper manner.
    :return: schools: list of all schools in the Schools dataset.
             districts: a list of all districts in the Districts dataset.
    """
    schools = importSchools()
    districts = importDistricts(schools)
    
    return schools, districts

def find_school_info_by_name(schools, schoolName):
    """
    A helper function that returns school data with a given name.
    :param: List of school objects and a name of a school
    :return: Info of a school as a string
    """
    resultSchool = find_object_by_name(schools, schoolName)
    if resultSchool == None:
        return "School Not Found"
    else:
        return resultSchool.get_school_info()

def find_district_info_by_name(districts, districtName):
    """
    A helper function that returns district data with a given name.
    :param: List of district objects and a name of a district
    :return: Info of a district as a string
    """
    resultDistrict = find_object_by_name(districts, districtName)
    if resultDistrict == None:
        return "district Not Found"
    else:
        return resultDistrict.get_district_data()

def get_weekly_data(schools, schoolName):
    """
    A helper function that returns a school's weekly data.
    :param: List of school objects and a name of a school
    :return: Weekly data of a school
    """
    resultSchool = find_object_by_name(schools, schoolName)
    return resultSchool.get_covid_data().transpose()

if __name__ == '__main__':
    schools, districts = setup()
    argumentList = sys.argv[1:]
    
    terminalOutput = ""
    
    if argumentList[0] == "-s":
        terminalOutput = find_school_info_by_name(schools, argumentList[1])

    if argumentList[0] == "-d":
        terminalOutput = find_district_info_by_name(districts, argumentList[1])

    if argumentList[0] == "--list-districts":
        terminalOutput = list_objects(districts)
    
    if argumentList[0] == "--list-schools":
       terminalOutput = list_objects(schools)

    if argumentList[0] == "--weekly-data":
        terminalOutput = get_weekly_data(schools, argumentList[1])

    print(terminalOutput)