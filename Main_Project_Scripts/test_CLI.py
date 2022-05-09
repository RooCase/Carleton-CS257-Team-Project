"""
Tests by Batmend
"""
import unittest

import district, school
import main

dummy_grade_data = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [],
                    '7': [], '8': [], '9': [], '10': [],'11': [], '12': [
                        'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson']}

dummy_school = school.School("charter", "", "Dummy Name", "1234", dummy_grade_data)
dummy_district = district.District("DummyDistrict", 69, [dummy_school], dummy_grade_data)

 
class TestCLI(unittest.TestCase):
    def test_find_school_info_by_name(self):
        """
        Tests if the find_school_info_by_name is returning a correct string.
        :return: nothing
        """
        info = f"""
School name: Dummy Name.
This is a charter school with a student body of 1234 students.
These grades are available: 12
"""
        self.assertEqual(info, main.find_school_info_by_name([dummy_school], "Dummy Name"))
        
    def test_find_district_info_by_name(self):
        """
        Tests if the find_district_info_by_name is returning a correct string.
        :return: nothing
        """
        info = f"""District name: DummyDistrict
Enrollment for this district: 69
List of schools:
  Dummy Name
"""
        self.assertEqual(info, main.find_district_info_by_name([dummy_district], "DummyDistrict"))

    def test_list_objects(self):
        """
        Tests if the list_objects is returning a correct string.
        :return: nothing
        """
        info = f"""DummyDistrict
"""
        self.assertEqual(info, main.list_objects([dummy_district]))
        print(main.list_objects([dummy_district]))
    
    def test_get_weekly_data(self):
        """
        Tests if the get_weekly_data is returning a correct string.
        :return: nothing
        """
        info = f"""           Grade 12
Week 1  AllDistance
Week 2  AllDistance
Week 3  AllDistance
Week 4  AllDistance
Week 5  AllInPerson"""
        self.assertEqual(info, str(main.get_weekly_data([dummy_school], "Dummy Name")))
    #     pass



if __name__ == '__main__':
    unittest.main()



