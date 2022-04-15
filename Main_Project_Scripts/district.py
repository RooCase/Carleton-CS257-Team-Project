class District:
    def __init__(self, name, enrollment, school_list):
        self.name = name
        self.enrollment = enrollment
        self.school_list = school_list

    def get_district_data(self):
        info = f'District name: {self.name}\nEnrollment for this district: {self.enrollment}\nList of schools:\n'
        
        for school in self.school_list:
            info += f'  {school.name}\n'
            
        return info

