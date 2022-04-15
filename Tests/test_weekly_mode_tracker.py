import os
import sys
import unittest

from Main_Project_Scripts.weekly_mode_tracker import WeeklyModeTracker
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "Main_Project_Scripts"))

class TestWeeklyModeTracker(unittest.TestCase):
    
    def test_weekly_mode_tracker(self):
        dummy_weekly_mode_tracker = WeeklyModeTracker()
        dummy_weekly_mode_tracker.add_week(['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance10', 'AllDistance', 'AllDistance'])
        assert(dummy_weekly_mode_tracker.get_weeks_for_grade(10), ['AllDistance'])
    def test_availible_grades(self):
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

        dummy_school = WeeklyModeTracker("Charter", "Dummy District", "Dummy Name", "1234", dummy_grade_data)
        assert(dummy_school, ["6", "7", "8", "9", "10", "11", "12"])
if __name__ == '__main__':
    unittest.main()



