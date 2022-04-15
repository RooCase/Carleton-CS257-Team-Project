import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "Main_Project_Scripts"))
import weekly_mode_tracker

class TestWeeklyModeTracker(unittest.TestCase):
    
    def test_weekly_mode_tracker(self):
        dummy_weekly_mode_tracker = weekly_mode_tracker.WeeklyModeTracker()
        dummy_weekly_mode_tracker.add_week(['AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance', 'AllDistance10', 'AllDistance', 'AllDistance'])
        assert(dummy_weekly_mode_tracker.get_weeks_for_grade(10), ['AllDistance'])

if __name__ == '__main__':
    unittest.main()



