import pyodbc


class DBConnUtil:
    @staticmethod
    def get_connection(connection_string):
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-7MH0675Q\SQLEXPRESS01;'
                      'Database=carconnect;'
                      'Trusted_Connection=yes;')

            return connection
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            return None