class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []
        self.payments = []

    def Get_student_id(self):
        return self.__student_id

    def Get_first_name(self):
        return self.__first_name

    def Get_last_name(self):
        return self.__last_name

    def Get_date_of_birth(self):
        return self.__date_of_birth

    def Get_email(self):
        return self.__email

    def Get_phone_number(self):
        return self.__phone_number

    def Set_student_id(self, student_id):
        self.__student_id = student_id

    def Set_first_name(self, first_name):
        self.__first_name = first_name

    def Set_last_name(self, last_name):
        self.__last_name = last_name

    def Set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def Set_email(self, email):
        self.__email = email

    def Set_phone_number(self, phone_number):
        self.__phone_number = phone_number
