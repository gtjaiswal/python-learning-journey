class DataValidator:

    @staticmethod
    def is_valid_email(email:str):
        return '@' in email and '.' in email

    @staticmethod
    def is_positive(number:int):
        return number>0
