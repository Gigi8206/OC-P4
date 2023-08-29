
from datetime import datetime

class Input:
    """Help class for input function."""

    @classmethod
    def for_string(cls, message):
        """Check if the value of an input is a string."""
        value = input(message)
        while not value.isalpha():
            print("Incorrect value, it has to be a word !")
            value = input(message)
        return value

    @classmethod
    def for_integer(cls, message):
        """Check if the value of an input is an integer."""
        value = input(message)
        while not value.isdigit() or "." in value:
            print("Incorrect value, it has to be a positive number !")
            value = input(message)
        return int(value)

    @classmethod
    def for_score(cls, message):
        """
        Check the value of the score is correct.
        Enter the scores for each round:
        1 point for the winner,
        0.5 point if draw,
        0 point for the loser.
        """
        score = -1
        scores = [0, 0.5, 1]
        error = (
            "Incorrect score, it has to be 1 point for the winner, "
            "0.5 point if draw, 0 point for the loser!"
        )
        while score not in scores:
            try:
                score = input(message)
                score = float(score) if "." not in score else float(score)
            except (ValueError, TypeError):
                print(error)
        return score

    @classmethod
    def birthday(cls, message):
        birthday = input(message)
        try:
            birthday_converted = datetime.strptime(birthday, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return birthday_converted

    @classmethod
    def for_identifier (cls, message):
        """ check if the identifier format is correct """
        value = input(message)
        if len(value) != 7:
            print("length error it has to be equal to 7")
        elif value[:2].isdigit() or value[2:7].isalpha():
            print("Incorrect identifier please respect the format! ")
        else:
            return value

