from util.dbconn import DBConnection
from dao.services import *
from exception.exceptions import (
    DuplicateEnrollmentException,
    CourseNotFoundException,
    StudentNotFoundException,
    TeacherNotFoundException,
    PaymentValidationException,
    InvalidStudentDataException,
    InvalidCourseDataException,
    InvalidEnrollmentDataException,
    InvalidTeacherDataException,
    InsufficientFundsException
)
from entity.Course import Course
from entity.Enrollment import Enrollment
from entity.Teacher import Teacher
from entity.Payment import Payment
from entity.Student import Student


class StudentServiceImpl(StudentDAO, DBConnection):

    def Add_student(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        if not first_name or not last_name or not date_of_birth or not email or not phone_number:
            raise InvalidStudentDataException("All fields are required.")
        
        with self.conn:
            self.conn.execute(
                "INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number) VALUES (?, ?, ?, ?, ?)",
                (first_name, last_name, date_of_birth, email, phone_number))
        print("Student added successfully!")

    def Update_student(self):
        student_id = input("Enter the student ID to update: ")
        first_name = input("Enter updated first name: ")
        last_name = input("Enter updated last name: ")
        date_of_birth = input("Enter updated date of birth (YYYY-MM-DD): ")
        email = input("Enter updated email: ")
        phone_number = input("Enter updated phone number: ")
        
        with self.conn:
            self.conn.execute(
                "UPDATE students SET first_name=?, last_name=?, date_of_birth=?, email=?, phone_number=? WHERE student_id=?",
                (first_name, last_name, date_of_birth, email, phone_number, student_id))
        print("Student updated successfully!")

    def Get_student(self):
        try:
            student_id = int(input("Enter student_id: "))
            print("Searching for student with ID:", student_id)

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
            row = cursor.fetchone()

            if row:
                student = Student(*row)
                print("Student found:", student)
                return student
            else:
                raise StudentNotFoundException(f"No student found with ID: {student_id}")

        except StudentNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error retrieving student:", e)
        finally:
            cursor.close()

    def Delete_student(self):
        student_id = int(input("Enter student_id: "))
        
        with self.conn:
            self.conn.execute("DELETE FROM students WHERE student_id= ?", (student_id,))
        print("Student deleted successfully!")

    def Get_all_students(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM students")
            students = [Student(*row) for row in cursor.fetchall()]
            cursor.close()

            if students:
                print("All students:")
                for student in students:
                    print(f"Student ID: {student.student_id}")
                    print(f"First Name: {student.first_name}")
                    print(f"Last Name: {student.last_name}")
                    print(f"Date of Birth: {student.date_of_birth}")
                    print(f"Email: {student.email}")
                    print(f"Phone Number: {student.phone_number}")
                    print()
            else:
                print("No students found.")
        except Exception as e:
            print("Error retrieving students:", str(e))


class CourseServiceImpl(CourseDAO, DBConnection):

    def Add_course(self):
        course_id = int(input("Enter course_id: "))
        course_name = input("Enter course name: ")
        teacher_id = int(input("Enter teacher_id: "))
        credits = int(input("Enter credits: "))
        if not course_name or credits <= 0:
            raise InvalidCourseDataException("Course name is required and credits should be a positive number.")
        
        with self.conn:
            self.conn.execute("INSERT INTO courses (course_id, course_name, teacher_id, credits) VALUES (?, ?, ?, ?)",
                              (course_id, course_name, teacher_id, credits))
        print("Course added successfully!")

    def Update_course(self):
        course_id = int(input("Enter course_id: "))
        course_name = input("Enter updated course name: ")
        teacher_id = int(input("Enter updated teacher_id: "))
        credits = int(input("Enter updated credits: "))
        
        with self.conn:
            self.conn.execute("UPDATE courses SET course_name=?, teacher_id=?, credits=? WHERE course_id=?",
                              (course_name, teacher_id, credits, course_id))
        print("Course updated successfully!")

    def Get_course(self):
        try:
            course_id = int(input("Enter course_id: "))
            print("Searching for course with ID:", course_id)

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,))
            row = cursor.fetchone()
            cursor.close()

            if row:
                course = Course(*row)
                print(f"Course ID: {course.course_id}")
                print(f"Course Name: {course.course_name}")
                print(f"Credits: {course.credits}")
                print(f"Teacher ID: {course.teacher_id}")
            else:
                raise CourseNotFoundException(f"No course found with ID: {course_id}")

        except CourseNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error retrieving course:", e)

    def Delete_course(self):
        course_id = int(input("Enter course_id: "))
        
        with self.conn:
            self.conn.execute("DELETE FROM courses WHERE course_id= ?", (course_id,))
        print("Course deleted successfully!")

    def Get_all_courses(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM courses")
            courses = [Course(*row) for row in cursor.fetchall()]
            cursor.close()

            if courses:
                print("All courses:")
                for course in courses:
                    print(f"Course ID: {course.course_id}")
                    print(f"Course Name: {course.course_name}")
                    print(f"Credits: {course.credits}")
                    print(f"Teacher ID: {course.teacher_id}")
                    print()
            else:
                print("No courses found.")
        except Exception as e:
            print("Error retrieving courses:", str(e))

from typing import List

class EnrollmentServiceImpl(EnrollmentDAO, DBConnection):
    def Add_enrollment(self):
        try:
            # Input values for enrollment
            student_id = int(input("Enter student_id: "))
            course_id = int(input("Enter course_id: "))
            enrollment_date = input("Enter enrollment date: ")

            if not enrollment_date:
                raise InvalidEnrollmentDataException("Enrollment date is required.")

            # Create a cursor from the connection
            cursor = self.conn.cursor()

            # Check if the student is already enrolled in the course
            cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
            existing = cursor.fetchone()

            if existing:
                raise DuplicateEnrollmentException("Student is already enrolled in the course.")

            # Insert new enrollment if no existing record is found
            cursor.execute(
                "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
                (student_id, course_id, enrollment_date)
            )

            # Commit the transaction
            self.conn.commit()

            # Close the cursor
            cursor.close()

            print("Enrollment added successfully!")

        except InvalidEnrollmentDataException as e:
            print(f"Error: {e}")
        except DuplicateEnrollmentException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def Update_enrollment(self):
        student_id = int(input("Enter student_id: "))
        course_id = int(input("Enter course_id: "))
        enrollment_date = input("Enter enrollment date: ")
        enrollment_id = int(input("Enter enrollment id: "))

        self.conn.execute("UPDATE Enrollments SET student_id = ?, course_id = ?, enrollment_date = ? WHERE enrollment_id = ?",
                          (student_id, course_id, enrollment_date, enrollment_id))
        self.conn.commit()
        print("Enrollment updated successfully!")

    def Get_enrollment(self):
        course_id = int(input("Enter Course ID: "))  
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Enrollments WHERE course_id = ?", (course_id,))
        rows = cursor.fetchall()  # Fetch all results
        cursor.close()

        if rows:
            for row in rows:
                enrollment_id, student_id, course_id, enrollment_date = row
                print(f"Enrollment ID: {enrollment_id}")
                print(f"Student ID: {student_id}")
                print(f"Course ID: {course_id}")
                print(f"Enrollment Date: {enrollment_date}")
                print()  # Add a new line for better readability
        else:
            print("No enrollments found for Course ID:", course_id)

    def Delete_enrollment(self):
        enrollment_id = int(input("Enter enrollment id: "))
        self.conn.execute("DELETE FROM Enrollments WHERE enrollment_id = ?", (enrollment_id,))
        self.conn.commit()
        print("Enrollment deleted successfully!")

    def Get_all_enrollments(self) -> List[Enrollment]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Enrollments")
        enrollments = [Enrollment(*row) for row in cursor.fetchall()]
        cursor.close()

        if enrollments:
            for enrollment in enrollments:
                print(f"Enrollment ID: {enrollment.Get_enrollment_id()}")
                print(f"Student ID: {enrollment.student_id}")
                print(f"Course ID: {enrollment.course_id}")
                print(f"Enrollment Date: {enrollment.enrollment_date}")
        else:
            print("No enrollments found.")
        return enrollments


class TeacherServiceImpl(TeacherDAO, DBConnection):

    def Add_teacher(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")

        if not first_name or not last_name or not email:
            raise InvalidTeacherDataException("First name, last name, and email are required.")

        self.conn.execute("INSERT INTO teacher (first_name, last_name, email) VALUES (?, ?, ?)",
                          (first_name, last_name, email))
        self.conn.commit()
        print("Teacher added successfully!")

    def Update_teacher(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        teacher_id = int(input("Enter teacher id: "))

        self.conn.execute("UPDATE teacher SET first_name = ?, last_name = ?, email = ? WHERE teacher_id = ?",
                          (first_name, last_name, email, teacher_id))
        self.conn.commit()
        print("Teacher updated successfully!")

    def Get_teacher(self):
        teacher_id = int(input("Enter teacher id: "))
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM teacher WHERE teacher_id = ?", (teacher_id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            teacher_id, first_name, last_name, email = row
            print(f"Teacher ID: {teacher_id}")
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Email: {email}")
        else:
            print("No teacher found with ID:", teacher_id)

    def Delete_teacher(self):
        teacher_id = int(input("Enter teacher id: "))
        self.conn.execute("DELETE FROM teacher WHERE teacher_id = ?", (teacher_id,))
        self.conn.commit()
        print("Teacher deleted successfully!")

    def Get_all_teachers(self) -> List[Teacher]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM teacher")
        teachers = [Teacher(*row) for row in cursor.fetchall()]
        cursor.close()

        if teachers:
            for teacher in teachers:
                print(f"Teacher ID: {teacher.teacher_id}")
                print(f"First Name: {teacher.first_name}")
                print(f"Last Name: {teacher.last_name}")
                print(f"Email: {teacher.email}")
        else:
            print("No teachers found.")
        return teachers


class PaymentServiceImpl(PaymentDAO, DBConnection):

    def Add_payment(self):
        payment_id = int(input("Enter payment id: "))
        student_id = int(input("Enter student id: "))
        amount = int(input("Enter amount: "))
        payment_date = input("Enter payment_date: ")

        if amount <= 0:
            raise PaymentValidationException("Amount must be positive.")
        if student_id <= 0:
            raise PaymentValidationException("Student ID must be positive.")

        self.conn.execute("INSERT INTO payments (payment_id, student_id, amount, payment_date) VALUES (?, ?, ?, ?)",
                          (payment_id, student_id, amount, payment_date))
        self.conn.commit()
        print("Payment added successfully!")

    def Update_payment(self):
        student_id = int(input("Enter student_id: "))
        amount = int(input("Enter amount: "))
        payment_date = input("Enter date: ")
        payment_id = int(input("Enter payment ID: "))

        self.conn.execute("UPDATE payments SET student_id = ?, amount = ?, payment_date = ? WHERE payment_id = ?",
                          (student_id, amount, payment_date, payment_id))
        self.conn.commit()
        print("Payment updated successfully!")

    def Get_payment(self):
        payment_id = int(input("Enter payment ID: "))
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM payments WHERE payment_id = ?", (payment_id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            payment_id, student_id, amount, payment_date = row
            print(f"Payment ID: {payment_id}")
            print(f"Student ID: {student_id}")
            print(f"Amount: {amount}")
            print(f"Payment Date: {payment_date}")
        else:
            print("No payment found with ID:", payment_id)

    def Delete_payment(self):
        payment_id = int(input("Enter payment id: "))
        self.conn.execute("DELETE FROM payments WHERE payment_id = ?", (payment_id,))
        self.conn.commit()
        print("Payment deleted successfully!")

    def Get_all_payments(self) -> List[Payment]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM payments")
        payments = [Payment(*row) for row in cursor.fetchall()]
        cursor.close()

        if payments:
            for payment in payments:
                print(f"Payment ID: {payment.Get_payment_id()}")
                print(f"Student ID: {payment.Get_student_id()}")
                print(f"Amount: {payment.Get_amount()}")
                print(f"Payment Date: {payment.Get_payment_date()}")
        else:
            print("No payments found.")
        return payments
