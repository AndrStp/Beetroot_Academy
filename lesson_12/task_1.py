# School

# Make a class structure in python representing people at school. Make a base class called Person, a class called Student, 
# and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes, 
# and keep in mind which are common and which are not. For example, the name should be a Person attribute, 
# while salary should only be available to the teacher. 


class Person:

    students = 0
    teachers = 0

    def __init__(self, name: str, age: int, foreign: bool, department: str, role: str) -> None:
        self.name = name
        self.age = age
        self.foreign = foreign
        self.department = department
        self.role = role
    
    def __str__(self):
        return f'{self.role} : {self.name} - {self.department} department'

    def display_info(self) -> None:
        print(f'My name is {self.name} and I\'m a {self.role} from the {self.department} department')
    
    def __del__(self) -> None:
        pass
    

class Student(Person):
    
    def __init__(self, name: str, age: int, foreign: bool, department: str, role: str, degree: str, admission_year: int, course_year: int, gpa: float) -> None:
        super().__init__(name, age, foreign, department, role)
        Person.students += 1
        self.degree = degree
        self.admission_year = admission_year
        self.course_year = course_year
        self.gpa = gpa
    
    def update_gpa(self, marks: list) -> None:
        """Calculates and updates the gpa of the student"""
        gpa = sum(marks) / len(marks)
        self.gpa = round(gpa, 2)
    
    def transfer_to_next_year(self) -> None:
        """Move the student to the next year"""
        if self.degree == 'bachelor':
            if self.course_year > 4:
                print("Cannot transfer. It's the students final year")
            else:
                self.course_year += 1
        else:
            if self.course_year > 1:
                print("Cannot transfer. It's the students final year")
            else:
                self.course_year += 1

    def move_department(self, department: str) -> None:
        """Move the student to the given department provided his/her GPA is high enough"""
        if self.gpa >= 4.5:
            self.department = department
            print(f'Approved! You are in the {self.department} department!')
        else:
            print('Your GPA is too low. Consider another department')
    
    def display_graduation_year(self) -> None:
        """Displays the students projected graduation year"""
        if self.degree == 'bachelor':
            print(f'Your are to graduate in {self.admission_year + 4}')
        else:
            print(f'Your are to graduate in {self.admission_year + 1}')

    def display_info(self) -> None:
        """Display basic info about the student"""
        super().display_info()
        print(f'I\'m {self.course_year} year student who wants to obtain {self.degree} degree and my GPA is {self.gpa}!')

    def expell(self) -> None:
        """Expell the student and decrease the number of students"""
        super().__del__()
        Person.students -= 1
        print(f'The {self} has been expelled')


class Teacher(Person):

    def __init__(self, name: str, age: int, foreign: bool, department: str, role: str, degree: str, license_terms: int, salary: int) -> None:
        super().__init__(name, age, foreign, department, role)
        Person.teachers += 1
        self.degree = degree
        self.salary = salary
        self.license_terms = license_terms

    
    def display_info(self) -> None:
        """Display basic info about the teacher"""
        super().display_info()
        print(f'I have a {self.degree} degree and {self.license_terms} license_terms and my salary is {self.salary}')
    
    def change_salary(self, change: str, amount: int) -> None:
        """Either 'increase' or 'decrease' the teacher's salary by the given amount"""
        if change == 'increase':
            self.salary += amount
        else:
            self.salary -= amount
        
    def dismiss(self) -> None:
        """Dismiss the teacher and decrease the number of staff"""
        super().__del__()
        Person.teachers -= 1
        print(f'The {self} has been dismissed')




student_1 = Student('Anna', 20, False, 'ComputerScience', 'student', 'bachelor', 2020, 2, 4.9)
student_2 = Student('Bob', 23, False, 'ComputerScience', 'student', 'master', 2021, 1, 4.2)
student_3 = Student('Caroline', 19, False, 'Physics', 'student', 'bachelor', 2019, 3, 4.4)
student_4 = Student('Diego', 21, True, 'Mathematics', 'student', 'bachelor', 2020, 2, 4.6)
student_5 = Student('Ethan', 21, False, 'Mathematics', 'student', 'bachelor', 2018, 4, 3.9)

teacher_1 = Teacher('Andrew', 45, False, 'ComputerScience', 'teacher', 'PhD', 5, 40000)
teacher_2 = Teacher('Billie', 35, False, 'Physics', 'teacher', 'PhD', 8, 60000)
teacher_3 = Teacher('Cimon', 55, False, 'Mathematics', 'teacher', 'PhD', 6, 45000)

print(Person.students) # -> 5
student_5.display_info() # -> My name is Ethan and I'm a student from the Mathematics department\nI'm 4 year student who wants to obtain bachelor degree and my GPA is 3.9!
student_5.display_graduation_year() # -> Your are to graduate in 2022
student_5.move_department('ComputerScience') # -> Your GPA is too low. Consider another department
student_5.expell() # -> The student : Ethan - Mathematics department has been expelled
print(Person.students) # -> 4

print(Person.teachers) # -> 3
teacher_1.display_info() # -> My name is Andrew and I'm a teacher from the ComputerScience department\nI have a PhD degree and 5 license_terms and my salary is 40000
teacher_1.change_salary('increase', 5000)
print(teacher_1.salary) # -> 45000
teacher_1.dismiss() # The teacher : Andrew - ComputerScience department has been dismissed
print(Person.teachers) # -> 2