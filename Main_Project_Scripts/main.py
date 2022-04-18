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


def importDistricts():
    """
    Default helper script for setting up a list of districts.
    :return: a list of districts
    """
    listOfDistricts = []
    parsedCSV = findIndividualGroups(findLines("/Users/roocase/Documents/CS257/team-project-team-a/Data/Minnesota_Districts_LearningModelData_Modified.csv"))

    for group in parsedCSV:
        listOfDistricts.append(createDistrict(group))
    return listOfDistricts

def list_districts(districtList):
    ans = ''
    for district in districtList:
        ans += f'{district.name}\n'
    return ans

if __name__ == '__main__':
    schools = importSchools()
    districts = importDistricts()

    for school in schools:
        print(school.get_school_info())
    for district in districts:
        print(district.get_district_data())
