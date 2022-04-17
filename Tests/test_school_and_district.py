from Main_Project_Scripts.district import *
from Main_Project_Scripts.school import *
from Main_Project_Scripts.Listing_Schools_in_a_District import *

#Test schools
school1 = School("District_A", 'a')
school2 = School("District_A", 'b')
school3 = School("District_B", 'c')
school4 = School("District_C", 'd')
school5 = School("District_B", 'e')
school6 = School("District_C", 'f')
school7 = School("District_C", 'g')
school8 = School("District_B", 'h')
school9 = School("District_B", 'i')
school0 = School("District_C", 'j')

#Dummy districts
District_A = District("District_A", [])
District_B = District("District_B", [])
District_C = District("District_C", [])

schoolsList = [school1, school2, school3, school4, school5, school6, school7, school8, school9, school0]

print(f"The schools in {District_A.name} are {listSchools(schoolsList, District_A)}.")
print (listOtherSchools(schoolsList, school7))