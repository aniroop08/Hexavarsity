class Enrollment:
    def __init__(self,enrollment_id,student_id,course_id,enrollment_date):
        self.__enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def Get_enrollment_id(self):
        return self.__enrollment_id

    def Get_student_id(self):
        return self.__student_id

    def Get_course_id(self):
        return self.__course_id

    def Get_enrollment_date(self):
        return self.__enrollment_date

    def Set_enrollment_id(self, enrollment_id):
        self.__enrollment_id = enrollment_id

    def Set_student_id(self, student_id):
        self.__student_id = student_id

    def Set_course_id(self, course_id):
        self.__course_id = course_id

    def Set_enrollment_date(self, enrollment_date):
        self.__enrollment_date = enrollment_date