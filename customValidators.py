from enum import Enum
from Validator import Validator


class Position(Enum):
    BE_DEVELOPER = "Backend Developer"
    FE_DEVELOPER = "Frontend Developer"
    DEVOPS = "DevOps"

    def __str__(self):
        return self.value

    def __lt__(self, other):
        return self.value < other.value


class CustomValidator:
    @staticmethod
    def integer(error_message):
        def decorator(func):
            def wrapper(value):
                try:
                    return func(int(value))
                except:
                    raise ValueError(error_message)

            return wrapper

        return decorator

    @staticmethod
    def validate_positive_integer(error_message):
        def decorator(func):
            def wrapper(value):
                try:
                    return func(int(value))
                except ValueError:
                    raise ValueError(error_message)
            return wrapper
        return decorator

    @staticmethod
    def validateID(error_message):
        def decorator(func):
            def wrapper(value):
                if not Validator.validate_ID(value):
                    raise ValueError(error_message)
                return func(value)
            return wrapper
        return decorator

    @staticmethod
    def validateName(error_message):
        def decorator(func):
            def wrapper(value):
                if not Validator.validate_name(value):
                    raise ValueError(error_message)
                return func(value)
            return wrapper
        return decorator

    @staticmethod
    def validateEmail(error_message):
        def decorator(func):
            def wrapper(value):
                if not Validator.validate_email(value):
                    raise ValueError(error_message)
                return func(value)
            return wrapper
        return decorator

    @staticmethod
    def validatePhoneNumber(error_message):
        def decorator(func):
            def wrapper(value):
                if not Validator.validate_phone_number(value):
                    raise ValueError(error_message)
                return func(value)
            return wrapper
        return decorator

    @staticmethod
    def validateAvailability(error_message):
        def decorator(func):
            def wrapper(value):
                if not Validator.validate_availability(value):
                    raise ValueError(error_message)
                return func(value)
            return wrapper
        return decorator

    @staticmethod
    def validateSalary(error_message):
        def decorator(func):
            def wrapper(value):
                if not Validator.validate_salary(value):
                    raise ValueError(error_message)
                return func(value)
            return wrapper
        return decorator

    @staticmethod
    def validatePosition(error_message):
        def decorator(func):
            def wrapper(value):
                try:
                    user_position = Position[value]
                    return value
                except Exception as exc:
                    raise ValueError(error_message)
            return wrapper
        return decorator

    @staticmethod
    def validate_position(position):
        try:
            user_position = Position[position]
            return True
        except Exception as exc:
            return False
