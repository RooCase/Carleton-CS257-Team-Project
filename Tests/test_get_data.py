import unittest
from Main_Project_Scripts import csvManipulation


class MyTestCase(unittest.TestCase):

    def test_dummy(self):
        school_data_dummy = [['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '8/30/20', '9/4/20', 'Closed', '', '', 'K: No Data Available; Gr1: No Data Available; Gr2: No Data Available; Gr3: No Data Available; Gr4: No Data Available; Gr5: No Data Available', 'Gr6: No Data Available; Gr7: No Data Available; Gr8: No Data Available', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '9/5/20', '9/11/20', 'Virtual', 'Virtual', 'Virtual', 'K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance', 'Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['Yes', 'Academia Cesar Chavez Charter School', 'Regular school', 'Academia Cesar Chavez Charter Schools', '518', '9/12/20', '9/19/20', 'Virtual', 'Virtual', 'Virtual', 'K: AllDistance; Gr1: AllDistance; Gr2: AllDistance; Gr3: AllDistance; Gr4: AllDistance; Gr5: AllDistance', 'Gr6: AllDistance; Gr7: AllDistance; Gr8: AllDistance', 'Gr9: NA; Gr10: NA; Gr11: NA; Gr12: NA', '', '', '55'], ['        ']]

        self.assertEqual(school_data_dummy, csvManipulation.findLines("example.csv"))  # add assertion here

if __name__ == '__main__':
    unittest.main()
