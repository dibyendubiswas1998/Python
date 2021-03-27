
import logging

# Example-01:------------------------------------------------------------
logging.basicConfig(filename="newfile1.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')


logging.info("This is information")
logging.error("This is error")
logging.critical("This is critical")


# Example-02:-------------------------------------------------------------
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down to earth")


# Example-03:--------------------------------------------------------

logging.basicConfig(filename='test1.log', format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

def sum(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

num1, num2 = 10, 2
add_result = sum(num1, num2)
logging.debug(f"add: {num1} + {num2} = {add_result}")

subtraction_result = sum(num1, num2)
logging.debug(f"Subtraction: {num1} - {num2} = {subtraction_result}")

multiplication_result = sum(num1, num2)
logging.debug(f"Multiplication: {num1} * {num2} = {multiplication_result}")

division_result = sum(num1, num2)
logging.debug(f"Division: {num1} / {num2} = {division_result}")



# Example-04:-------------------------------------------------------------
logging.basicConfig(filename='info.log', format='%(asctime)s %(message)s', filemode='w', level=logging.INFO)


class Employee:
    def __init__(self, efname, elname, esal):
        self.efname = efname
        self.elname = elname
        self.esal = esal
    
    def eDetail(self):
        logging.info("Employee Name: {} {}, Salary: {}".format(self.efname, self.elname, self.esal))
    
    def eSalary(self):
        return "Employee Salary: {}".format(self.esal)

emp1 = Employee("Dbyendu", "Biswas", 60000)
emp2 = Employee("Arko", "Sen", 45000)

emp1.eDetail()
emp2.eDetail()


# print(emp1.eDetail())
# print(emp2.eDetail())