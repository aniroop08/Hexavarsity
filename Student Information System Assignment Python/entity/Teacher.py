class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.courses_assigned = []

    def Get_teacher_id(self):
        return self.__teacher_id

    def Get_first_name(self):
        return self.__first_name

    def Get_last_name(self):
        return self.__last_name

    def Get_email(self):
        return self.__email

    def Set_teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    def Set_first_name(self, first_name):
        self.__first_name = first_name

    def Set_last_name(self, last_name):
        self.__last_name = last_name

    def Set_email(self, email):
        self.__email = email