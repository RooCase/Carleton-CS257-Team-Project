class WeeklyModeTracker:

    def add_week(self, mode_list):
        for ind, mode in enumerate(mode_list, start=1):
            self.learning_modes_for_grades[ind].append(mode)

    def get_weeks_for_grade(self, grade):
        return self.learning_modes_for_grades[grade]

    # creates a list of available grades in the school/district
    def get_available_grades(self):
        # instance variable for available grades
        available = []
        for i in self.grades:
            if self.grades[i]:
                available.append(i)
        return available

    def __init__(self, name, size, grades):
        self.name = name
        self.size = size
        self.learning_modes_for_grades = grades
