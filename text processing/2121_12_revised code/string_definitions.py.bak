import sys
import re

class BadEmployeeFormat(Exception):
    """Badly formatted employee name"""

def get_employee():
    """
    Retrieve user information.

    This method simply prompts the user for 
    an employee's name and his current job 
    title. 
    """
    employee = raw_input('Employee Name: ')
    role = raw_input("Employee's Role: ")
    if not re.match(r'^.+\s.+', employee):
        raise BadEmployeeFormat('Full Name Required '
            'for records database.' )
    return {'name': employee, 'role': role }
            
if __name__ == '__main__':
    employees = []
    print 'Enter your employees, EOF to Exit...'
    while True:
        try:
            employees.append(get_employee()) 
        except EOFError:
            print
            print "Employee Dump"
            for number, employee in enumerate(employees):
                print 'Emp #%d: %s, %s' % (number+1, 
                    employee['name'], employee['role'])
            print u'\N{Copyright Sign}2010, SuperCompany, Inc.'
            sys.exit(0)
        except BadEmployeeFormat, e:
            print >>sys.stderr, 'Error: ' + str(e)


