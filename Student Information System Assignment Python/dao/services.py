from abc import ABC, abstractmethod
from typing import List
from entity.Student import Student
from entity.Course import Course
from entity.Enrollment import Enrollment
from entity.Teacher import Teacher
from entity.Payment import Payment


class StudentDAO(ABC):
    @abstractmethod
    def Add_student(self):
        pass

    @abstractmethod
    def Update_student(self):
        pass

    @abstractmethod
    def Get_student(self):
        pass

    @abstractmethod
    def Delete_student(self):
        pass

    @abstractmethod
    def Get_all_students(self) -> List[Student]:
        pass


class CourseDAO(ABC):
    @abstractmethod
    def Add_course(self):
        pass

    @abstractmethod
    def Update_course(self):
        pass

    @abstractmethod
    def Get_course(self):
        pass

    @abstractmethod
    def Delete_course(self):
        pass

    @abstractmethod
    def Get_all_courses(self) -> List[Course]:
        pass


class EnrollmentDAO(ABC):
    @abstractmethod
    def Add_enrollment(self):
        pass

    @abstractmethod
    def Update_enrollment(self):
        pass

    @abstractmethod
    def Get_enrollment(self):
        pass

    @abstractmethod
    def Delete_enrollment(self):
        pass

    @abstractmethod
    def Get_all_enrollments(self) -> List[Enrollment]:
        pass


class TeacherDAO(ABC):
    @abstractmethod
    def Add_teacher(self):
        pass

    @abstractmethod
    def Update_teacher(self):
        pass

    @abstractmethod
    def Get_teacher(self):
        pass

    @abstractmethod
    def Delete_teacher(self):
        pass

    @abstractmethod
    def Get_all_teachers(self) -> List[Teacher]:
        pass


class PaymentDAO(ABC):
    @abstractmethod
    def Add_payment(self):
        pass

    @abstractmethod
    def Update_payment(self):
        pass

    @abstractmethod
    def Get_payment(self):
        pass

    @abstractmethod
    def Delete_payment(self):
        pass

    @abstractmethod
    def Get_all_payments(self) -> List[Payment]:
        pass
