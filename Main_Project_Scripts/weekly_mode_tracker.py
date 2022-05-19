"""
Written by unknown, refactored by Artem Yushko
"""

class WeeklyModeTracker:
    def __init__(self, name, size, grades):
        self.name = name
        self.size = size
        self.learning_modes_for_grades = grades

    def add_week(self, mode_list):
        for ind, mode in enumerate(mode_list):
            self.learning_modes_for_grades[ind-1] = mode

    def get_weeks_for_grade(self, grade):
        return self.learning_modes_for_grades[grade]


