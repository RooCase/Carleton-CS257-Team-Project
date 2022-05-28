import unittest


class TestSchoolInDistrict(unittest.TestCase):
    def test_If_School_In_District(self):
        school1 = "Pacific Ridge High School" #School object, given as input
        district1 = "Carlesbad School District" #District field
        self.assertEqual(school1, district1)

    def test_If_District_In_School(self):
        school2 = "Pacific Ridge High School" #School field
        district2 = "Carlesbad School District" #District Object, given as input
        self.assertEqual(school2, district2)

if __name__ == '__main__':
    unittest.main()