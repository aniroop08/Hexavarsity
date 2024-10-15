class Payment:
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.__payment_id = payment_id
        self.__student_id = student_id
        self.__amount = amount
        self.__payment_date = payment_date

    def Get_payment_id(self):
        return self.__payment_id

    def Get_student_id(self):
        return self.__student_id

    def Get_amount(self):
        return self.__amount

    def Get_payment_date(self):
        return self.__payment_date

    def Set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def Set_student_id(self, student_id):
        self.__student_id = student_id

    def Set_amount(self, amount):
        self.__amount = amount

    def Set_payment_date(self, payment_date):
        self.__payment_date = payment_date

