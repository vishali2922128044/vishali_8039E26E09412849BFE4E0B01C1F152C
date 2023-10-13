class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sorted the list of students in decreasing order of cgpa
  sorted_students = sorted(student_list,                        
                          key=lambda student: student.cgpa,
                          reverse=True)
  return sorted_students


#Example usage
students = [
    student("Hari", "A123", 7.8),
    student("srikanth", "A124", 8.9),
    student("mahidhar", "A126", 9.9),
]

sorted_students = sort_students(students)

# print the sorted list of students
for student in sorted_students:
  print("name: {}, roll number: {}, cgpa: {}".format(student.name,
student.roll_number,
                                                student.cgpa))              
        






