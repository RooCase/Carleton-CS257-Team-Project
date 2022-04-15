# file for parsing the rows from the dataset as School objects and doing operations with them
# class for School objects
from Main_Project_Scripts import weekly_mode_tracker


class School(weekly_mode_tracker.WeeklyModeTracker):
    def __init__(self, charter, district, name, size, grades):
        self.charter = charter
        self.district = district
        self.name = name
        self.size = size
        self.grades = grades


    # returns a district of a specific school
    def get_district(self):
        return self.district

    # creates a list of available grades in the school/
    def get_available_grades(self):
        # instance variable for available grades
        available = []
        for i in self.grades:
            if self.grades[i]:
                available.append(i)
        return available

    # printing out the information about the school
    def get_school_info(self):
        # showing possible grades
        grds = ", ".join([str(x) for x in self.get_available_grades()])
        # printing out the school information
        if self.charter == "Charter":
            info = f"""
            School name: {self.name}
            This is a {self.charter} school with a student body of {self.size} students.
            Those grades are available: {grds} 
            """
        else:
            info = f"""
            School name: {self.name}
            This is a {self.charter} school with a student body of {self.size} students.
            It is located in {self.district}.
            Those grades are available: {grds} 
            """
        return info
