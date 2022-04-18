#Rowen Hinrichs

#A function that lists schools in a district, given a list of all schools and a district
#:param: list of all schools and name of district
#:return: list of school objects in given district
def listSchools(schoolsList, DistrictName):
    listOfSchoolsInDistrict = []
    if schoolsList != None:
        for school in schoolsList:
            if school.district == DistrictName:
                listOfSchoolsInDistrict.append(school)
        if listOfSchoolsInDistrict == []:
            print("There are no schools in that district.")
            return
    return listOfSchoolsInDistrict
    
#A function that lists all the other schools in a particular school's district, given a school.
#:param: List of all schools and a school object
#:return: List of all school objects that share a district with param school.
def listOtherSchools(schoolList, school):
    district = school.district
    listOfOtherSchools = listSchools(schoolList, district)
    for i in listOfOtherSchools:
            if i == school:
                listOfOtherSchools.remove(i)
    return listOfOtherSchools