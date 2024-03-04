from RepositoryOperations import Repository
from passenger import Passenger

class Plane:
    def __init__(self, plane_number, airline, number_of_seats, destination, list_of_passengers):
        """
        D: Constructor method for creating Plane object
        Parameters:
        -plane_number: -int
        -airline: -str
        -company: -str
        -number_of_seats: -int
        -destination: -str
        -list_of_passengers: -repository
        """

        if isinstance(plane_number, int):
            self.__plane_number = plane_number
        else:
            raise ValueError("The plane number have to be an integer")

        if isinstance(airline, str):
            self.__airline = airline
        else:
            raise ValueError("The plane airline have to be a string")


        if isinstance(number_of_seats, int):
            self.__number_of_seats = number_of_seats
        else:
            raise ValueError("The number of seats of the plane have to be an integer")

        if isinstance(destination, str):
            self.__destination = destination
        else:
            raise ValueError("The destination have to be a string")

        if isinstance(list_of_passengers, Repository):
            self.__list_of_passengers = list_of_passengers
        else:
            raise ValueError("The list of passengers have to be a repository")

    def get_plane_number(self):
        """
        D:Returns the number of the plane
        """
        return self.__plane_number

    def get_airline(self):
        """
        D:Returns the airline of the plane
        """
        return self.__airline


    def get_number_of_seats(self):
        """
        D:Returns the number of seats of the plane
        """
        return self.__number_of_seats

    def get_destination(self):
        """
        D:Returns the destination of the plane
        """
        return self.__destination

    def get_list_of_passengers(self):
        """
        D:Returns the list of passengers of the plane
        """
        return self.__list_of_passengers.get_all_values()

    def get_list_of_passengers2(self):
        """
        D:Returns the list of passengers of the plane
        """
        return self.__list_of_passengers

    def set_plane_number(self, plane_number):
        """
        D: Set the plane number
        Parameter:
        -plane number: int
        """

        self.__plane_number = plane_number

    def set_airline(self, airline):
        """
        D: Set the airline of the plane
        Parameter:
        - airline: str
        """

        self.__airline = airline


    def set_number_of_seats(self, number_of_seats):
        """
        D: Set the number of seats of the plane
        Parameter:
        - number_of_seats: int
        """

        self.__number_of_seats = number_of_seats

    def set_destination(self, destination):
        """
        D: Set the destination of the plane
        Parameter:
        - destination: str

        """

        self.__destination = destination

    def set_list_of_passengers(self, list_of_passengers):
        """
        D: Set the list of the passengers of the plane
        Parameter:
        - list_of_passengers: repository
        """

        self.__list_of_passengers = list_of_passengers

    def add_a_passenger(self, passenger: object):
        """
        D: Adds a passenger in the plane
        Parameter:
        -passenger: object
        """
        self.__list_of_passengers.add_value(passenger)

    def add_a_passenger_at_index(self, index, passenger:object):
        """
        D: Adds a passenger in the plane at a given index
        Parameters:
        -passenger: object
        -index: int
        """

        if isinstance(index, int) and 0 <= index < self.__list_of_passengers.get_length():
            self.__list_of_passengers.add_value_at_index(index, passenger)
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")




    def get_a_passenger_at_index(self, index):
        """
        D: gets a passenger in the plane at a given index
        Parameter:
        -index: int
        """

        if isinstance(index, int) and 0 <= index < self.__list_of_passengers.get_length():
            return self.__list_of_passengers.get_value_at_index(index)
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")

    def delete_passenger_at_index(self, index):
        """
        D: gets a passenger in the plane at a given index
        Parameter:
        -index: int
        """

        if isinstance(index, int) and 0 <= index < self.__list_of_passengers.get_length():
            return self.__list_of_passengers.delete_value_at_index(index)
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")

    def sort_passengers_by_last_name(self):
        """
        D: returns the list of passengers sorted by last name of passengers
        """

        return self.__list_of_passengers.sort_repo(lambda x:x.get_last_name())

    def get_number_of_passengers_with_first_name_starting_with_a_substr(self, substring):
        """
        D: Return the number of passengers with the first name starting with a given substring
        Parameter:
        -subsring -str
        """
        k=0
        for passenger in self.__list_of_passengers.get_all_values():
            if passenger.get_first_name().startswith(substring):
                k += 1

        return k

    def starts_with_same_3_letters(self):
        """
        D: Identify if there exists passengers with passport numbers starting with same 3 digits
        """
        k = 0
        for passenger1 in self.__list_of_passengers.get_all_values():
            for passenger2 in self.__list_of_passengers.get_all_values():
                if str(passenger1.get_passport_number())[:3] == str(passenger2.get_passport_number())[:3]:
                    k += 1

        if k > self.__list_of_passengers.get_length():
            return True
        else:
            return False

    def first_last_contain_string(self, string):
        """
        D: Identify the passengers for which the first name or the last name contain a given string
        Paramete:
        -string: str
        """
        result = Repository()
        for passenger in self.__list_of_passengers.get_all_values():
            if string in passenger.get_first_name() or string in passenger.get_last_name():
                result.add_value(passenger)

        return result

    def identify_passenger_with_given_name(self, name):
        """
        D: Identify if there exists a passenger with a given name
        Parameter:
        - name: str
        """

        ok = 0
        for passenger in self.__list_of_passengers.get_all_values():
            if passenger.get_last_name() == name:
                ok = 1

        if ok == 1:
            return True
        else:
            return False


    def __str__(self):
        """
        D: return the string representation of a plane
        """

        ans = "Plane with number " + str(self.__plane_number) + ", airline " + str(self.__airline) + ", number of seats " + str(self.__number_of_seats) + ", destination " + str(self.__destination) + " and the passengers:\n"
        for passenger in self.__list_of_passengers.get_all_values():
            ans += str(passenger) + "\n"
        return ans
