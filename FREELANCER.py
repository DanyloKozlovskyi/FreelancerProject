from enum import Enum

import customValidators
from Validator import validate_input, validateInputInClass
from Validator import Validator
from Validator import validateDataProperty
from customValidators import CustomValidator, Position


class Freelancer:
    fieldnames = {
        "ID": None,
        "name": None,
        "email": None,
        "phone_number": None,
        "availability": None,
        "salary": None,
        "position": None
    }

    @staticmethod
    def validateFreelancer(*args):
        field_value = list(zip(Freelancer.fieldnames_validators.items(), args))
        errors = []
        for tup in field_value:
            try:
                tup[0][1](tup[1])
            except ValueError as exc:
                errors.append(f'{exc}')
        return errors

    # 111
    def __str__(self):
        all_properties = [str(value) if attr != "fieldnames" else "" for attr, value in vars(self).items()]
        del all_properties[-1]
        return ', '.join(all_properties)

        # return f"{self.ID} {self.name} {self.email} {self.phone_number} " \
        #        f"{self.availability} {self.salary} {self.position.value}"

    def get_fieldname(self, name):
        # may throw
        return self.fieldnames[name]

    #clear
    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.ID < other.ID

    @staticmethod
    def get_freelancer(ID=None, name=None, email=None, phone_number=None, availability=None, salary=None, position=None):
        if ID is None:
            ID = Validator.get_ID('enter ID of freelancer must contain only 8 digits: ')
        if name is None:
            name = Validator.get_name('enter name of freelancer must be capitalized: ')
        if email is None:
            email = Validator.get_email('enter email of freelancer: ')
        if phone_number is None:
            phone_number = Validator.get_phone_number('enter phone number of freelancer may start with +38 or not: ')
        if availability is None:
            availability = Validator.get_availability('enter availability(hours per week) of freelancer: ')
        if salary is None:
            salary = Validator.get_salary('enter salary of freelancer: ')
        if position is None:
            position = Freelancer.get_position('enter position of freelancer(DEVOPS, BE_DEVELOPER, FE_DEVELOPER): ')
        return Freelancer(ID, name, email, phone_number, availability, salary, position)

    # 333
    @staticmethod
    def string_to_freelancer(string_data):
        data = string_data.split()
        return Freelancer(*data)

    def partial_overlapping_equal(self, parameter):
        res = False
        for field in self.fieldnames.values():
            res = res or str(field).count(parameter)
        return res

    @property
    def ID(self):
        return self._ID

    @staticmethod
    @CustomValidator.validateID('ID: should be 8 digits')
    def validateID(_id):
        return _id

    @ID.setter
    def ID(self, ID):
        ID = Freelancer.validateID(ID)
        self._ID = ID

    @property
    def name(self):
        return self._name

    @staticmethod
    @CustomValidator.validateName('name: should be capitalized string with letters only')
    def validateName(value):
        return value

    @name.setter
    def name(self, name):
        name = Freelancer.validateName(name)
        self._name = name

    @property
    def email(self):
        return self._email

    @staticmethod
    @CustomValidator.validateEmail('email: should be valid email')
    def validateEmail(value):
        return value

    @email.setter
    def email(self, email):
        email = Freelancer.validateEmail(email)
        self._email = email

    @property
    def phone_number(self):
        return self._phone_number

    @staticmethod
    @CustomValidator.validatePhoneNumber('phone number: should be valid phone number')
    def validatePhoneNumber(value):
        return value

    @phone_number.setter
    def phone_number(self, phone_number):
        phone_number = Freelancer.validatePhoneNumber(phone_number)
        self._phone_number = phone_number


    @property
    def availability(self):
        return self._availability

    @staticmethod
    @CustomValidator.validateAvailability('availability: should be float in range 0 to 72')
    def validateAvailability(value):
        return value

    @availability.setter
    def availability(self, availability):
        availability = Freelancer.validateAvailability(availability)
        self._availability = float(availability)

    @property
    def salary(self):
        return self._salary

    @staticmethod
    @CustomValidator.validateSalary('salary: should be positive float')
    def validateSalary(value):
        return value

    @salary.setter
    def salary(self, salary):
        salary = Freelancer.validateSalary(salary)
        self._salary = float(salary)

    @property
    def position(self):
        return self._position

    @staticmethod
    @CustomValidator.validatePosition('position: should be enum value')
    def validatePosition(value):
        return value

    @position.setter
    def position(self, position):
        position = Freelancer.validatePosition(position)
        self._position = Position[position]

    @validateInputInClass('enter parameter: ', Validator.validate_file_name)
    def write_in_file(self, file_path):
        try:
            with open(file_path, 'w') as f:
                f.write(str(self))
                return True
        except Exception as exc:
            print(f'file {file_path} not found')
        return False

    @staticmethod
    def validate_parameter(parameter, parameters=fieldnames.keys()):
        if parameter in parameters:
            return True
        return False

    @staticmethod
    @validate_input('Enter your parameter: ', validate_parameter)
    def get_parameter(parameter_string):
        return parameter_string

    @staticmethod
    def get_position(caption):
        position_string = Validator.get_data_to_attribute(caption, CustomValidator.validate_position)
        return position_string

    fieldnames_validators = {
        "ID": validateID,
        "name": validateName,
        "email": validateEmail,
        "phone_number": validatePhoneNumber,
        "availability": validateAvailability,
        "salary": validateSalary,
        "position": validatePosition
    }

    def __init__(self, ID, name, email, phone_number, availability, salary, position):
        self.ID = ID
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.availability = availability
        self.salary = salary
        self.position = position

        self.fieldnames = {
            "ID": self.ID,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "availability": self.availability,
            "salary": self.salary,
            "position": self.position
        }


