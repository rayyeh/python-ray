import sys

class BadEmployeeFormat(Exception):
    """Badly formatted employee name"""
    def __init__(self, reason, name):
        Exception.__init__(self, reason)
        self.name = name

def get_employee():
    """
    Retrieve user information.

    This method simply prompts the user for 
    an employee's name and his current job 
    title. 
    """
    employee = input('Employee Name: ')
    role = input("Employee's Role: ")
    employee, role = employee.strip(), role.strip()

    # Make sure we have a full name
    if not employee.count(' '):
        raise BadEmployeeFormat('Full Name Required '
            'for records database.', employee )
    return {'name': employee, 'role': role }
            
if __name__ == '__main__':
    employees = []
    failed_entries = []
    print('Enter your employees, EOF to Exit...')
    while True:
        try:
            employees.append(get_employee()) 
        except EOFError:
            print()
            print("Employee Dump")
            for number, employee in enumerate(employees):
                print('Emp #%d: %s, %s' % (number+1, 
                    employee['name'], employee['role'].title()))

            print('The following entries failed: ' + ', '.join(failed_entries))
            print('\N{Copyright Sign}2010, SuperCompany, Inc.')
            sys.exit(0)
        except BadEmployeeFormat as e:
            failed_entries.append(e.name)
            err_msg = 'Error: ' + str(e)
            print(err_msg.center(len(err_msg)+20, '*'), file=sys.stderr)


