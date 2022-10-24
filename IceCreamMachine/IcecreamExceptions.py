class OutOfStockException(Exception):
    """Raised when something is out of stock"""
    def __init__(self, name,*args: object) -> None:
        super().__init__(*args)
        self.name = name

    def __str__(self):
        return f'{self.name} seems to be out of stock at the moment, Please proceed with other choices'

class NeedsCleaningException(Exception):
    """Raised when the icecream machine needs cleaning"""

    def __str__(self):
        return 'Icecream Machine needs cleaning, Please wait before you proceed.'

class InvalidChoiceException(Exception):
    """Raised when an invalid choice is picked"""
    def __init__(self, choice,*args: object) -> None:
        super().__init__(*args)
        self.choice = choice

    def __str__(self):
        return f'"{self.choice}" is an Invalid Choice. Please choose a valid one from given options.'

class ExceededRemainingChoicesException(Exception):
    """Raised when there are too many scoops of icecream"""
    def __init__(self, type,*args: object) -> None:
        super().__init__(*args)
        self.type = type

    def __str__(self):
        return f'You have exceeded the number of {self.type}s, proceeding to next step.'

class InvalidPaymentException(Exception):
    """Raised when an invalid payment amount is given"""
    def __init__(self, value,*args: object) -> None:
        super().__init__(*args)
        self.givenInput = value

    def __str__(self):
        return f'{self.givenInput} does not match with the amount to be paid. Please provide the right value'