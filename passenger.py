class Passenger:
    def __init__(self, first_name, last_name, passport_number):
        """
        D: Constructor method for creating Passenger object
        Parameters:
            -first_name: str
            -last_name: str
            -passport_number: int
        """
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            raise ValueError("First name have to be a string")

        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            raise ValueError("Last name have to be a string")

        if isinstance(passport_number, int):
            self.__passport_number = passport_number
        else:
            raise ValueError("Passport number have to be an integer")

    def get_first_name(self):
        """
        D: Returns the first_name of the passenger
        """
        return self.__first_name

    def get_last_name(self):
        """
        D: Returns the last_name of the passenger
        """

        return self.__last_name

    def get_passport_number(self):
        """
        D: Returns the passport number of the passenger
        """

        return self.__passport_number

    def set_first_name(self, first_name):
        """
        D: Set the first name of the passenger
        Parameter:
        - first_name- str
        """

        self.__first_name = first_name

    def set_last_name(self, last_name):
        """
        D: Set the last name of the passenger
        Parameter:
        - last_name- str
        """

        self.__last_name = last_name

    def set_passport_number(self, passport_number):
        """
        D: Set the passport number of the passenger
        Parameter:
        - passport_number- int
        """

        self.__passport_number = passport_number

    def __str__(self):
        """
        D: returns the string representation of a passenger
        """
        return f"Passenger {self.__first_name} {self.__last_name} with passport number {self.__passport_number}"

    def __eq__(self, other):
        """
        D: verify if 2 passengers are the same
        """
        return self.__first_name == other.__first_name and self.__last_name == other.__last_name and self.__passport_number == other.__passport_number