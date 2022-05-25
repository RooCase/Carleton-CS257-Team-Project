"""
Initializing the School object and creating all the basic getters and setters for it.
Written by Artem Yushko.
"""
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

    # creates a list of available grades in the school
    def get_available_grades(self):
        # instance variable for available grades
        available = []
        for i in self.grades:
            if self.grades[i]:
                available.append(i)
        return available

    # the same function, but as a list
    def get_list_available_grades(self):
        # instance variable for available grades
        available = []
        for i in self.grades:
            if self.grades[i]:
                available.append("Grade " + str(i))
        return available

    # printing out the information about the school
    def get_school_info(self):
        # showing possible grades
        grds = ", ".join([str(x) for x in self.get_available_grades()])
        # printing out the school information
        if self.charter == "charter":
            info = f"""
School name: {self.name}.\nThis is a {self.charter} school with a student body of {self.size} students.\nThese grades 
are available: {grds} 
"""
        else:
            info = f"""
School name: {self.name}\nThis is a {self.charter} school with a student body of {self.size} students.\nIt is located 
in {self.district}.\nThese grades are available: {grds} 
"""
        return info

    # getting weekly covid data from the school
    def get_covid_data(self):
        # setting the row and column names
        row_names = self.get_list_available_grades()
        col_names = self.get_school_year()
        # creating the matrix as a file
        matrix = []
        # adding grades to the matrix
        for grade in self.grades:
            if self.grades[grade]:
                i = 0
                row = []
                while i < len(self.grades[grade]):
                    number = grade.split("r")[1]
                    row.append(f"Week {i} Grade {number}: " + str(self.grades[grade][i]))
                    i += 1
                matrix.append(row)
        return matrix

    # getting the length of the school year
    def get_school_year(self):
        school_year_len = []
        # iterating through the grade list to get the length of the school year
        for grade in self.grades:
            if self.grades[grade]:
                i = 0
                # counting weeks and adding them as strings
                while i < len(self.grades[grade]):
                    school_year_len.append("Week " + str(i+1))
                    i += 1
                return school_year_len
