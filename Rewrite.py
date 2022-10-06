# Student
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'student name {self.name} \n'

# Enroll and unenroll students in a course
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.student_grades = {}
        self.enrolled_students = set()

    def __str__(self):
        return f'\ncourse name {self.course_name} \nstudent and grades {self.student_grades}\n' + \
                f'enrolled students {self.enrolled_students} \n'

    def enroll_student(self, student_name):
        self.enrolled_students.add(student_name)
        
    def drop_course(self, student_name):
        if student_name in self.enrolled_students:
            self.enrolled_students.remove(student_name)
        else:
            print("student doesn't exist in this course.")

    def submit_grade_for_student(self, student_name, grade):
        if student_name not in self.enrolled_students:
            print(f"student {student_name} is not enrolled.")
            return
        self.student_grades[student_name] = grade

# System management
class Manager:
    def __init__(self):
        self.courses = []
        self.students = []
        # 0: normal user
        # 1: admin user

##################### Admin or Student set up ####################################################

    def __str__(self):
        out_str = "manager: \n"
        out_str += "courses: "
        for course in self.courses:
            out_str += str(course)

        out_str += "\nstudents: \n"
        for student in self.students:
            out_str += str(student)
        return out_str

    def change_user(self):
        print("-" * 47)
        print("What is your user type?")
        print("0: Normal user.")
        print("1: Admin user.")
        new_user_type = input("Enter your user type number: ")
        self.user_type = int(new_user_type)
        return  self.user_type

    def ask_admin_user_input(self):
        print("-" * 47)
        print("Welcome to Student and Course Management System")
        print("-" * 47)
        print("Press 0. Change User Type")
        print("Press 1. Add a New Course")
        print("Press 2. Modify the Course")
        print("Press 3. Delete the Course")
        print("Press 4. Add a New Student")
        print("Press 5. Modify the Student")
        print("Press 6. Delete the Student")
        print("Press 7. Enrol Student in a Course")
        print("Press 8. Unenroll Student in a Course")
        print("Press 9. Submit Grades for Student")
        print("Press 10. Quit")
        return  input("Please, enter the number: ")

    def ask_normal_user_input(self):
        print("-" * 47)
        print("Welcome to Student and Course Management System")
        print("-" * 47)
        print("Press 0. Change User Type")
        print("Press 4. Add a New Student")
        print("Press 5. Modify the Student")
        print("Press 6. Delete the Student")
        print("Press 7. Enrol Student in a Course")
        print("Press 8. Unenroll Student in a Course")
        print("Press 9. Submit Grades for Student")
        print("Press 10. Quit")
        return  input("Please, enter the number: ")

###################### Course, Adding, Modifying, Deleting ##########################

    # Adding course
    def create_course(self):
        new_course_name = input("Enter course name: ")
        return Course(new_course_name)

    def add_course(self, new_course):
        self.courses.append(new_course)

    # Search course to find position
    def search_course(self, course_name_to_search):
        for i in range(len(self.courses)):
            if self.courses[i].course_name == course_name_to_search:
                return i

        print(f"course {course_name_to_search} do not exist in system.")
        return None

    def modify_course(self):
        course_name_to_modify = input("Which course is that you want to modify course? Enter the course name: ")
        new_course_name = input("Enter the new course name: ")
        course_to_modify_index = self.search_course(course_name_to_modify)
        self.courses[course_to_modify_index].course_name = new_course_name

    def delete_course(self):
        course_name_to_delete = input("Enter the delete course name: ")
        del_course_index = self.search_course(course_name_to_delete)
        del self.courses[del_course_index]

###################### Student, Adding, Modifying, Deleting ##########################

    def add_student(self):
        new_student_name = input("Enter a new student name: ")
        new_student = Student(new_student_name)
        self.students.append(new_student)

    def search_student(self, find_student_name):
        for i in range(len(self.students)):
            if self.students[i].name == find_student_name:
                return i
        print("Enter student not exist in system.")
        return None

    def modify_student(self):
        student_name_to_change = input("Enter the student name to modify: ")
        new_student_name = input("Enter the new name: ")

        exist_student_index = self.search_student(student_name_to_change)
        if exist_student_index != None:
            self.students[exist_student_index].name = new_student_name

    def delete_student(self):
        student_name_to_delete = input("Enter the student name to delete: ")

        del_student_index = self.search_student(student_name_to_delete)
        del self.students[del_student_index]

    def submit_grade(self):
        student_name = input("Enter the student name: ")
        student_course = input("Enter the course name: ")
        get_course_index = self.search_course(student_course)
        if get_course_index is None:
            print("Invalid course name!")
            return None
        student_grade = input("Enter the student grade: ")
        self.courses[get_course_index].submit_grade_for_student(student_name, student_grade)

    def enroll_course_for_student(self):
        student_name = input("Enter the student name: ")
        if self.search_student(student_name) is None:
            print("Invalid student name.")
            return
        student_course = input("Enter the course name: ")
        if self.search_course(student_course) is None:
            print("Invalid course name.")
            return 
        get_course_index = self.search_course(student_course)
        self.courses[get_course_index].enroll_student(student_name)

    def drop_course_for_student(self):
        student_name = input("Enter the student name: ")
        if self.search_student(student_name) is None:
            print("Invalid student name")
            return
        student_course = input("Enter the course name: ")
        get_course_index = self.search_course(student_course)
        self.courses[get_course_index].drop_course(student_name)

if __name__ == "__main__":
    manager = Manager()
    user_type = 0
    while True:

        if user_type == 0:
            user_input = manager.ask_normal_user_input()
        elif user_type == 1:
            user_input = manager.ask_admin_user_input()
        else:
            print("Unknown User type.")
        user_input = int(user_input)
        if user_input == 0:
            user_type = manager.change_user()
            continue
        # For normal user menu:
        if user_type == 0:
            if user_input == 4:
                manager.add_student()
            elif user_input == 5:
                manager.modify_student()
            elif user_input == 6:
                del_student = manager.delete_student()
            elif user_input == 7:
                enroll_course = manager.enroll_course_for_student()
            elif user_input == 8:
                uneroll_course = manager.drop_course_for_student()
            elif user_input == 9 :
                submit_grade = manager.submit_grade()
            elif user_input == 10:
                print("Welcome to use Student and Course Management System again.")
                break
            else:
                print("Enter error, only the number above, please try it again.")
        # For admin user menu:
        elif user_type == 1:
            if user_input == 1:
                new_course = manager.create_course()
                manager.add_course(new_course)
            elif user_input == 2:
                manager.modify_course()
            elif user_input == 3:
                manager.delete_course()
            elif user_input == 4:
                manager.add_student()
            elif user_input == 5:
                new_modify_student = manager.modify_student()
            elif user_input == 6:
                del_student = manager.delete_student()
            elif user_input == 7:
                enroll_course = manager.enroll_course_for_student()
            elif user_input == 8:
                uneroll_course = manager.drop_course_for_student()
            elif user_input == 9 :
                submit_grade = manager.submit_grade()
            elif user_input == 10:
                print("Welcome to use Student and Course Management System again")
                break
            else:
                print("Enter error, only the number above, please try it again.")
        print("-" * 47)
        print(str(manager))




