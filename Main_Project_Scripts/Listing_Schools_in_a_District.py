#Rowen Hinrichs
from Main_Project_Scripts.district import *
from Main_Project_Scripts.school import *

#Dummy schools
school1 = School("sus", 'a')
school2 = School("sus", 'b')
school3 = School("amogus", 'c')
school4 = School("balls", 'd')
school5 = School("amogus", 'e')
school6 = School("balls", 'f')
school7 = School("balls", 'g')
school8 = School("amogus", 'h')
school9 = School("amogus", 'i')
school0 = School("balls", 'j')

#Dummy districts
sus = District("sus", [])
amogus = District("amogus", [])
balls = District("balls", [])


#Listing Schools in a District
#Schools have districts, districts do not have schools
#given a district, list all the schools
#given a school, list all the other schools in its district
#district objects will have an empty school list in them, that I then populate
# this is basically the function code and a test put together. I'll make sure to seperate it later.


schoolsList = [school1, school2, school3, school4, school5, school6, school7, school8, school9, school0]

districtList = [sus, amogus, balls]

#given list of districts and list of schools
#School objects contain district
#district object does NOT contain schools
#output an array of schools that are in each district.
#have district object contain list of schools

#Lists schools in a district, given a list of all schools and a district
def listSchools(schoolsList, District):
    listOfSchoolsInDistrict = []
    for school in schoolsList:
        if school.district == District.name:
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


print(f"The schools in {amogus.name} are {listSchools(schoolsList, amogus)}.")
print (listOtherSchools(schoolsList, school7))

