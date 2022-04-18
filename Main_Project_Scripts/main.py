"""
Non-CLI functions written by Roo Case.

This is the main python file, that has the highest amount of abstraction. The code for our command-line-interface is
here, as well as the helper functions that are a part of that.
"""

import district
from Main_Project_Scripts import csvManipulation
from Main_Project_Scripts.csvManipulation import findIndividualGroups, findLines, createSchool, createDistrict


def importSchools():
    """
    Default helper script for setting up a list of schools.
    :return: a list of schools
    """
    listOfSchools = []
    parsedCSV = findIndividualGroups(findLines("/Users/roocase/Documents/CS257/team-project-team-a/Data/Minnesota_Schools_Modified.csv"))
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
    parsedCSV = findIndividualGroups(findLines("/Users/roocase/Documents/CS257/team-project-team-a/Data/Minnesota_Districts_LearningModelData_Modified.csv"))

    for group in parsedCSV:
        district = (createDistrict(group, schools))
        if district != None:
            listOfDistricts.append(district)
    return listOfDistricts

def list_districts(districtList):
    output = ''
    for district in districtList:
        output += f'{district.name}\n'
    return output

def setup():
    schools = importSchools()
    districts = importDistricts(schools)

    return schools, districts

if __name__ == '__main__':
    schools, districts = setup()

