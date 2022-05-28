import os
import sys
import unittest

from Main_Project_Scripts.weekly_mode_tracker import WeeklyModeTracker
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "Main_Project_Scripts"))

class TestWeeklyModeTracker(unittest.TestCase):
    
    def test_weekly_mode_tracker_names_and_size(self):
        dummy_weekly_mode_tracker = WeeklyModeTracker("Dummy", 123, None)
        self.assertEqual(dummy_weekly_mode_tracker.name, "Dummy")
        self.assertEqual(dummy_weekly_mode_tracker.size, 123)
        self.assertEqual(dummy_weekly_mode_tracker.learning_modes_for_grades, None)

    def test_availible_grades(self):
        """
        Tests that inputted grades are properly handled.
        :return: none, unit test.
        """
        dummy_grade_data = {'1': [], '2': [], '3': [], '4': [], '5': [],
                            '6': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance',
                                  'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson'],
                            '7': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance',
                                  'AllDistance', 'AllDistance', 'AllInPerson', 'Hybrid'],
                            '8': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance',
                                  'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson'],
                            '9': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'Hybrid', 'AllInPerson',
                                  'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson'],
                            '10': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson',
                                   'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson'],
                            '11': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'Hybrid',
                                   'AllInPerson', 'AllInPerson', 'AllInPerson', 'Hybrid'],
                            '12': ['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllInPerson', 'AllInPerson',
                                   'AllInPerson', 'AllInPerson', 'AllInPerson', 'AllInPerson']}

        dummy_school = WeeklyModeTracker("Dummy Name", "1234", dummy_grade_data)
        self.assertEqual(dummy_school.learning_modes_for_grades, dummy_grade_data)
if __name__ == '__main__':
    unittest.main()



