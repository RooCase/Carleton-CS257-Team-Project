"""
CLI and its helper functions written by Batmend.
Non-CLI functions written by Roo Case.

This is the main python file, that has the highest amount of abstraction. The code for our command-line-interface is
here, as well as the helper functions that are a part of that.
"""

import sys

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
    values = resultSchool.get_covid_data().transpose().values.array
    weeks = [[]]
    for i in range(0,len(values[0])):
        for val in values:
            weeks[i].append(val[i])
        return ""

if __name__ == '__main__':
    schools, districts = setup()
    argumentList = sys.argv[1:]
    
    terminalOutput = ""

    if len(argumentList) > 2 or len(argumentList) < 1:
        terminalOutput = "Please input only one argument and that you have input a valid command. For more info, you can type \'python3 main.py -h\'"
    if argumentList[0] == "-h" or argumentList[0] == "--help":
        terminalOutput = """
        HELP: 
        
        CLI options:
        -s "School Name"      //finds data about entered school
        -d "District Name"    //finds data about entered district
        --list-districts      //list all districts in the database
        --list-schools        //list all schools in the database
        --weekly-data         //give school covid data by grade for schools
        
        Examples:
        python3 main.py -s "Avalon School"
        python3 main.py -d "Minneapolis Public School District"
        python3 main.py --weekly-data "Great River School"
        """

    elif argumentList[0] == "-s":
        terminalOutput = find_school_info_by_name(schools, argumentList[1])
    elif argumentList[0] == "-d":
        terminalOutput = find_district_info_by_name(districts, argumentList[1])
    elif argumentList[0] == "--list-districts":
        terminalOutput = list_objects(districts)
    elif argumentList[0] == "--list-schools":
       terminalOutput = list_objects(schools)
    elif argumentList[0] == "--weekly-data":
        terminalOutput = get_weekly_data(schools, argumentList[1])

    print(terminalOutput)
