#Rowen Hinrichs

#Lists schools in a district, given a list of all schools and a district
def listSchools(schoolsList, DistrictName):
    listOfSchoolsInDistrict = []
    for school in schoolsList:
        if school.district == DistrictName:
            listOfSchoolsInDistrict.append(school)
    return listOfSchoolsInDistrict
    
#List all the other schools in a particular school's district, given a school.
def listOtherSchools(schoolList, school):
    district = school.district
    listOfOtherSchools = listSchools(schoolList, district)
    for i in listOfOtherSchools:
            if i == school:
                listOfOtherSchools.remove(i)
    return listOfOtherSchools