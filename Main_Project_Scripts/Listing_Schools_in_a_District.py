import school
import district

#Dummy schools
school1 = school("sus", 'a')
school2 = school("sus", 'b')
school3 = school("amogus", 'c')
school4 = school("balls", 'd')
school5 = school("amogus", 'e')
school6 = school("balls", 'f')
school7 = school("balls", 'g')
school8 = school("amogus", 'h')
school9 = school("amogus", 'i')
school0 = school("balls", 'j')
#Rowen Hinrichs
#Listing Schools in a District
#Schools have districts, districts do not have schools
#given a district, list all the schools
#given a school, list all the other schools in its district
#district objects will have an empty school list in them, that I then populate
# this is basically the function code and a test put together. I'll make sure to seperate it later.


#classes for testing
# class schools:
#     def __init__(self, district, name):
#         self.name = name
#         self.district = district

# class district:
#     def __init__(self, name, schools):
#         self.name = name
#         self.schools = schools

# #Dummy districts
sus = district("sus", [])
amogus = district("amogus", [])
balls = district("balls", [])





schoolsList = [school1, school2, school3, school4, school5, school6, school7, school8, school9, school0]

districtList = [sus, amogus, balls]

#given list of districts and list of schools
#School objects contain district
#district object does NOT contain schools
#output an array of schools that are in each district.
#have district object contain list of schools

#itterate through list ofschool
#looks at district
#find district in list/dictionary of districts

#Lists schools in a district, given a list of all schools and a district
#I don't think it needs to return anything, because it's only editing an object that already exists.
def listSchools(schoolsList, District):
    schoolNameList = []
    for school in schoolsList:
        if school.district == District.name:
            District.schools.append(school.name)
    print(f"The schools in {District.name} are {District.schools}.")


listSchools(schoolsList, amogus)

