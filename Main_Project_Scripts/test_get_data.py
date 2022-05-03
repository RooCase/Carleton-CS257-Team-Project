import unittest
import example

class MyTestCase(unittest.TestCase):

    def test_dummy(self):
        school_data_dummy = "Yes,Academia Cesar Chavez Charter School,Regular school,Academia Cesar Chavez Charter " \
                            "Schools,518,10/3/20,10/9/20,Virtual,Virtual,Virtual,K: AllDistance; Gr1: AllDistance; " \
                            "Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance,Gr6: AllDistance; " \
                            "Gr7: AllDistance; Gr8: AllDistance,Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA,,,55 "
        school_data_actual = example.getSchoolData("Academia Cesar Chavez Charter School")
        self.assertEqual(school_data_actual, school_data_dummy)  # add assertion here

if __name__ == '__main__':
    unittest.main()
