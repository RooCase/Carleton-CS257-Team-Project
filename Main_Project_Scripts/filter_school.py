"""
This file contains helper functions for filtering schools by
enrollment, charter, and grades
Created by Batmend Batsaikhan."""

from flask import request

def get_request_args():
    enrollment = "select"
    charter = "select"
    grade = "select"
    if "enrollment" in request.args:
        enrollment = request.args['enrollment']
    if "charter" in request.args:
        charter = request.args['charter']
    if "grade" in request.args:
        grade = request.args['grade']
    return enrollment, charter, grade
    
def filter_schools_by_charter(myschools, charter):
    if charter == "select":
        return myschools
    ans = []
    for school in myschools:
        if school.charter == charter:
            ans.append(school)
    return ans

def filter_schools_by_enrollment(myschools, enrollment):
    l = 0
    r = 0
    if enrollment == "select":
        return myschools
    if enrollment == "0-99":
        l = 0
        r = 99
    if enrollment == "100-999":
        l = 100
        r = 999
    if enrollment == "1000-Inf":
        l = 1000
        r = 100000

    ans = []
    for school in myschools:
        if l <= int(school.size) and int(school.size) <= r:
            ans.append(school)
    return ans

def filter_schools_by_grade(myschools, grade):
    if grade == "select":
        return myschools
    ans = []
    for school in myschools:
        if grade in school.get_available_grades():
            ans.append(school)
    return ans

def filter_schools(myschools, enrollment, charter, grade):
    print("Yooo this is " + grade)
    myschools = filter_schools_by_enrollment(myschools, enrollment)
    myschools = filter_schools_by_charter(myschools, charter)
    myschools = filter_schools_by_grade(myschools, grade)
    return myschools