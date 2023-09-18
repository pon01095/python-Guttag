# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:45:17 2021

@author: LeeHoonGi
"""
from ch_10_MIT_person import *

class Grades(object):
    def __init__(self):
        """Creat empty grade book"""
        self.students = []
        self.grades = {}
        self.is_sorted = True
        
    def add_student(self, student):
        """
        Parameters
        ----------
        student : type Student
        add student to the grade book
        """
        if student in self.students:
            raise ValueError('Duplicat student')
        self.students.append(student)
        self.grades[student.get_id_num()] = []
        self.is_sorted = False
            
    def add_grade(self, student, grade):
        """
        Parameters
        ----------
        student : type Student
        grade : float
        Returns
        add grade to the list of grades for student
        """
        try:
            self.grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')
            
    def get_grades(self, student):
        """
        Parameters
        ----------
        student : TYPE Student
        Returns
        -------
        a list of grades for student.

        """
        try:
            return self.grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')
            
    def get_students(self):
        """
        Returns
        -------
        A sorted list of the students in the grade book.

        """
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        return self.students[:]
    
def grade_report(course):
    """Assumes course is of type GRades"""
    report = ''
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
    return report    
        
            
    
    
if __name__ == "__main__": 
    ug1 = UG('Jane Doe', 2021)
    ug2 = UG('Pierce Addison', 2041)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')
    six_hundred = Grades()
    six_hundred.add_student(ug1)
    six_hundred.add_student(ug2)
    six_hundred.add_student(g1)
    six_hundred.add_student(g2)
    for s in six_hundred.get_students():
        six_hundred.add_grade(s, 75)
    six_hundred.add_grade(g1, 25)
    six_hundred.add_grade(g2, 100)
    six_hundred.add_student(ug3)
    print(grade_report(six_hundred))