class WeeklyModeTracker:
    learning_modes_for_grades = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []
    }

    def add_week(self, mode_list):
        for ind, mode in enumerate(mode_list, start=1):
            self.learning_modes_for_grades[ind].append(mode)

    def get_weeks_for_grade(self, grade):
        return self.learning_modes_for_grades[grade]