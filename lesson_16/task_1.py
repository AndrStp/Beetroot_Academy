# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, 
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

# Email validations:
# https://help.xmatters.com/ondemand/trial/valid_email_format.htm 
# https://en.wikipedia.org/wiki/Email_address 


class EmailValidator:
    def __init__(self, email) -> None:
        if EmailValidator.validate(email):
            self.email = email
        else:
            raise ValueError('E-mail name is not valid!')

    @staticmethod
    def validate(email):
        if '@' not in email:
            return False
        elif email.startswith('@') or email.endswith('@'):
            return False
        elif email.count('@') > 1:
            return False
        elif email.startswith('.') or email.endswith('.'):
            return False
        
        at_index = email.index('@')
        prefix = email[:at_index]
        domain = email[at_index+1:]

        if '.' not in domain:
            return False

        
