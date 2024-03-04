from RepositoryOperations import Repository
from plane import Plane

class Airport:
    def __init__(self):
        """
        D: constructor method for an Airport object
        """
        self.__Airport = Repository()

    def get_planes(self):
        """
        D: returns all planes from an Airport
        """
        return self.__Airport.get_all_values()

    def get_plane_at_index(self, index):
        """
        D: returns a plane at a given index
        Parameter:
        -index: int
        """
        try:
            return self.__Airport.get_value_at_index(index)
        except IndexError:
            print("The index has to be an integer between 0 and the length of the repository")
    def add_plane(self, plane: object):
        """
        D: adds a plane at the Airport repository
        Parameter:
        -plane: object
        """
        if isinstance(plane, Plane):
            self.__Airport.add_value(plane)
        else:
            raise ValueError("Plane has to be a plane object")

    def add_plane_at_index(self, index, plane: object):
        """
        D: adds a plane at a given index in Airport repository
        Parameters:
            -index: int
            -plane: object
        """
        try:
            if isinstance(plane, Plane):
                self.__Airport.add_value_at_index(index, plane)
            else:
                raise ValueError("Plane has to be a plane object")
        except IndexError:
            print("The index has to be an integer between 0 and the length of the repository")

    def update_plane_at_index(self, index, new_plane:object):
        """
        D: Updates a plane at a given index in Airport repository
        Parameters:
             -index: int
             -new_plane: object
        """
        try:
            if isinstance(new_plane, Plane):
                self.__Airport.update_value_at_index(index, new_plane)
            else:
                raise ValueError("New Plane have to be a plane object")
        except IndexError:
            print("The index has to be an integer between 0 and the length of the repository")

    def delete_plane_at_index(self, index):
        """
        D: Deletes a plane at a given index
        Parameter:
        -index: int

        """
        try:
            self.__Airport.delete_value_at_index(index)
        except IndexError:
            print("The index has to be an integer between 0 and the length of the repository")

    def sort_planes_by_number_of_passengers(self):
        """
        D:Sort the planes by the number of passengers
        Return: Airport repository sorted
        """
        return self.__Airport.sort_repo(lambda x:x.get_number_of_seats())

    def sort_planes_by_passengers_substring(self, substring):
        """
        D:Sort the planes by number of passengers for which first name starts with a given substring
        Parameter:
        -substring: str
        """
        return  self.__Airport.sort_repo(lambda x: x.get_number_of_passengers_with_first_name_starting_with_a_substr(substring))

    def sort_planes_by_nr_passengers_destination(self):
        """
        D:Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
        Return: Airport repository sorted
        """

        return self.__Airport.sort_repo(lambda x:(str(x.get_number_of_seats()) + x.get_destination()))

    def check_different_last_names(self, list_of_pasengers, new_passenger):
        """
        D: check if the last name of a passenger don't appear in list_of_passengers or if he already is in the list
        Parameters:
            -list_of_passengers: list
            -new_passenger: object

        """
        for passenger in list_of_pasengers:
            if passenger.get_last_name() == new_passenger.get_last_name() or passenger == new_passenger:
                return False

        return True
    def groups_of_k_different_last_name(self, k, number):
        """
        D:Forms group of k passengers from the same plane, having different last name

        """
        answer = []
        for plane in self.__Airport.get_all_values():
            if plane.get_plane_number() == number:
                values = []
                for passenger in plane.get_list_of_passengers2().get_all_values():
                    values.append(passenger)
                solution = self.__Airport.get_k_groups_with_property(values, k, self.check_different_last_names)
                if solution != []:
                    answer.extend(solution)

        return answer

    def check_same_destination_different_airline(self, planes, new_plane):
        """
        D:check if the new_plane destination is the same with planes destination, if it has different airline company
        and if it is already in the list
        Parameters:
            -planes: list
            -new_plane: object
        """
        for plane in planes:
            if plane.get_destination() != new_plane.get_destination() or plane.get_airline() == new_plane.get_airline() or plane == new_plane:
                return False

        return True

    def group_of_k_planes_same_destination_different_airline(self, k):
        """
        D:Forms  groups  of 𝒌 planes  with  the  same  destination  but  belonging  to  different airline companies

        """
        answer = []
        values = []
        for plane in self.__Airport.get_all_values():
            values.append(plane)

        solution = self.__Airport.get_k_groups_with_property(values, k, self.check_same_destination_different_airline)
        if solution != []:
            answer.extend(solution)

        return answer
