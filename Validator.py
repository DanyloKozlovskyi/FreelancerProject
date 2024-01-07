import re


def validateInputInClass(caption, validation_function):
    def decorator(func):
        def wrapper(self, name='', *args, **kwargs):
            while True:
                if validation_function(name):
                    return func(self, name)
                name = input(caption)

                print(f'Try again, {caption}')

        return wrapper
    return decorator


def validateDataProperty(validation_function):
    def decorator(func):
        def wrapper(self, name, *args, **kwargs):

            if validation_function(name):
                func(self, name)

            else:
                raise Exception(f'incorrect data in {func.name}')

        return wrapper
    return decorator


def validate_input(caption, validation_function):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                data_string = input(caption)
                if validation_function(data_string):
                    return func(data_string)
                else:
                    print(f'Try again, {caption}')

        return wrapper

    return decorator


class Validator:
    @staticmethod
    def get_data_to_attribute(caption, function_to_validate):
        check_data = True
        while check_data:
            data_string = input(caption)
            if not function_to_validate(data_string):
                print(f'try again, {caption}')
                check_data = False

            if not check_data:
                check_data = True
            else:
                check_data = False
        return data_string

    @staticmethod
    def validate_ID(ID):
        if all(Validator.validate_natural_number(digit) for digit in str(ID)):
            # my ID should all have 8 digits
            return len(ID) == 8
        return False

    @staticmethod
    def get_ID(caption):
        ID_string = Validator.get_data_to_attribute(caption, Validator.validate_ID)
        return ID_string

    @staticmethod
    def validate_name(name):
        if Validator.validate_string_with_letters_only(name):
            return Validator.validate_capitalized(name)
        return False

    @staticmethod
    def get_name(caption):
        name_string = Validator.get_data_to_attribute(caption, Validator.validate_name)
        return name_string

    @staticmethod
    def validate_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        if re.match(email_pattern, email):
            return True
        else:
            return False

    @staticmethod
    def get_email(caption):
        email_string = Validator.get_data_to_attribute(caption, Validator.validate_email)
        return email_string

    @staticmethod
    def validate_phone_number(phone_number):
        pattern = r'^(\+?380\d{9}|380\d{9})$'
        if re.match(pattern, phone_number):
            return True
        else:
            return False

    @staticmethod
    def get_phone_number(caption):
        phone_number_string = Validator.get_data_to_attribute(caption, Validator.validate_phone_number)
        return phone_number_string

    @staticmethod
    def validate_availability(availability):
        if Validator.validate_float(availability):
            return Validator.validate_boundaries(float(availability), 0, 72)
        return False

    @staticmethod
    def get_availability(caption):
        availability_string = Validator.get_data_to_attribute(caption, Validator.validate_availability)
        return float(availability_string)

    @staticmethod
    def validate_salary(salary):
        if Validator.validate_float(salary):
            return Validator.validate_boundaries(float(salary), 0, 100000)
        return False

    @staticmethod
    def get_salary(caption):
        salary_string = Validator.get_data_to_attribute(caption, Validator.validate_salary)
        return float(salary_string)





    @staticmethod
    def validate_float(some_string):
        try:
            float(some_string)
            return True
        except Exception as exc:
            return False

    @staticmethod
    def validate_int(some_string):
        if Validator.validate_float(some_string):
            try:
                int(some_string)
                return True
            except Exception as exc:
                return False
        return False

    @staticmethod
    def validate_natural_number(some_string):
        if Validator.validate_int(some_string):
            return int(some_string) >= 0
        return False

    @staticmethod
    def get_float(caption):
        number_string = Validator.get_data_to_attribute(caption, Validator.validate_float)
        return float(number_string)

    @staticmethod
    def get_int(caption):
        number_string = Validator.get_data_to_attribute(caption, Validator.validate_int)
        return int(number_string)

    @staticmethod
    def get_natural_number(caption):
        number_string = Validator.get_data_to_attribute(caption, Validator.validate_natural_number)
        return int(number_string)

    @staticmethod
    def validate_string_with_letters_only(string_data):
        return all(letter.isalpha() for letter in string_data)

    @staticmethod
    def validate_capitalized(string_data):
        return string_data == string_data.capitalize()

    @staticmethod
    def validate_boundaries(number, lower_bound, upper_bound):
        return lower_bound <= number <= upper_bound

    @staticmethod
    def validate_file_name(file_name):
        try:
            with open(file_name, 'r') as file:
                return True
        except Exception as exc:
            return False

    @staticmethod
    def get_file_name(caption):
        file_name_string = Validator.get_data_to_attribute(caption, Validator.validate_file_name)
        return file_name_string
