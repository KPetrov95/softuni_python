from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            value = 'Your name must contain letters only!'
        self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class ExactLengthValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            value = 'Your passcode must be exactly 6 digits!'
        self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not (value.isdigit() and len(value) == 6):
            raise ValidationError(self.message)