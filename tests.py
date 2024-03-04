import unittest
from passenger import Passenger
from plane import Plane
from RepositoryOperations import Repository
from airport import Airport

class TestPassenger(unittest.TestCase):


    def setUp(self):
        self.__passenger1 = Passenger("John", "Doe", 1234567890)
        self.__passenger2 = Passenger("Alice", "Johnson", 987654321)
        self.__passenger3 = Passenger("Bob", "Smith", 555555555)

    def test_getters_passenger(self):
        self.assertEqual(self.__passenger1.get_first_name(), "John")
        self.assertEqual(self.__passenger1.get_last_name(), "Doe")
        self.assertEqual(self.__passenger1.get_passport_number(), 1234567890)

        self.assertEqual(self.__passenger2.get_first_name(), "Alice")
        self.assertEqual(self.__passenger2.get_last_name(), "Johnson")
        self.assertEqual(self.__passenger2.get_passport_number(), 987654321)

        self.assertEqual(self.__passenger3.get_first_name(), "Bob")
        self.assertEqual(self.__passenger3.get_last_name(), "Smith")
        self.assertEqual(self.__passenger3.get_passport_number(), 555555555)

    def test_setters_passenger(self):
        '''
        Desc: tests for setters
        '''
        self.__passenger1.set_first_name("Carmen")
        self.__passenger1.set_last_name("Lovinescu")
        self.__passenger1.set_passport_number(5081224019623)
        self.assertEqual(self.__passenger1.get_first_name(), "Carmen")
        self.assertEqual(self.__passenger1.get_last_name(), "Lovinescu")
        self.assertEqual(self.__passenger1.get_passport_number(), 5081224019623)

        self.__passenger2.set_first_name("George")
        self.__passenger2.set_last_name("Calinescu")
        self.__passenger2.set_passport_number(1950905018068)
        self.assertEqual(self.__passenger2.get_first_name(), "George")
        self.assertEqual(self.__passenger2.get_last_name(), "Calinescu")
        self.assertEqual(self.__passenger2.get_passport_number(), 1950905018068)

        self.__passenger3.set_first_name("Vlad")
        self.__passenger3.set_last_name("Petrescu")
        self.__passenger3.set_passport_number(2951120120201)
        self.assertEqual(self.__passenger3.get_first_name(), "Vlad")
        self.assertEqual(self.__passenger3.get_last_name(), "Petrescu")
        self.assertEqual(self.__passenger3.get_passport_number(), 2951120120201)

class TestPlane(unittest.TestCase):

    def setUp(self):
        passenger_repo_1 = Repository()
        passenger_repo_1.add_value(Passenger("John", "Doe", 1234567890))
        passenger_repo_1.add_value(Passenger("Alice", "Johnson", 987654321))

        passenger_repo_2 = Repository()
        passenger_repo_2.add_value(Passenger("Bob", "Smith", 555555555))
        passenger_repo_2.add_value(Passenger("Eva", "Williams", 111111111))

        passenger_repo_3 = Repository()
        passenger_repo_3.add_value(Passenger("Mike", "Miller", 999999999))

        self.__plane1 = Plane(1, "Wizz Air", 120, "Munich", passenger_repo_1)
        self.__plane2 = Plane(2, "TAROM", 150, "Paris", passenger_repo_2)
        self.__plane3 = Plane(3, "United Airlines", 180, "Chicago", passenger_repo_3)

    def test_getters(self):
        # Test for Plane 1
        self.assertEqual(self.__plane1.get_plane_number(), 1)
        self.assertEqual(self.__plane1.get_airline(), "Wizz Air")
        self.assertEqual(self.__plane1.get_number_of_seats(), 120)
        self.assertEqual(self.__plane1.get_destination(), "Munich")

        # Test for Plane 2
        self.assertEqual(self.__plane2.get_plane_number(), 2)
        self.assertEqual(self.__plane2.get_airline(), "TAROM")
        self.assertEqual(self.__plane2.get_number_of_seats(), 150)
        self.assertEqual(self.__plane2.get_destination(), "Paris")

        # Test for Plane 3
        self.assertEqual(self.__plane3.get_plane_number(), 3)
        self.assertEqual(self.__plane3.get_airline(), "United Airlines")
        self.assertEqual(self.__plane3.get_number_of_seats(), 180)
        self.assertEqual(self.__plane3.get_destination(), "Chicago")

    def test_setters(self):
        # Test for Plane 1
        self.__plane1.set_plane_number(10)
        self.__plane1.set_airline("Ryanair")
        self.__plane1.set_number_of_seats(200)
        self.__plane1.set_destination("Berlin")

        self.assertEqual(self.__plane1.get_plane_number(), 10)
        self.assertEqual(self.__plane1.get_airline(), "Ryanair")
        self.assertEqual(self.__plane1.get_number_of_seats(), 200)
        self.assertEqual(self.__plane1.get_destination(), "Berlin")

        # Test for Plane 2
        self.__plane2.set_plane_number(20)
        self.__plane2.set_airline("Lufthansa")
        self.__plane2.set_number_of_seats(250)
        self.__plane2.set_destination("Amsterdam")

        self.assertEqual(self.__plane2.get_plane_number(), 20)
        self.assertEqual(self.__plane2.get_airline(), "Lufthansa")
        self.assertEqual(self.__plane2.get_number_of_seats(), 250)
        self.assertEqual(self.__plane2.get_destination(), "Amsterdam")

        # Test for Plane 3
        self.__plane3.set_plane_number(30)
        self.__plane3.set_airline("Delta Airlines")
        self.__plane3.set_number_of_seats(300)
        self.__plane3.set_destination("New York")

        self.assertEqual(self.__plane3.get_plane_number(), 30)
        self.assertEqual(self.__plane3.get_airline(), "Delta Airlines")
        self.assertEqual(self.__plane3.get_number_of_seats(), 300)
        self.assertEqual(self.__plane3.get_destination(), "New York")

    def test_set_list_of_passengers(self):
        # Test for Plane 1
        new_passenger_repo_1 = Repository()
        new_passenger_repo_1.add_value(Passenger("David", "Clark", 777777777))
        new_passenger_repo_1.add_value(Passenger("Sophia", "Martinez", 888888888))

        self.__plane1.set_list_of_passengers(new_passenger_repo_1)

        passengers_1 = self.__plane1.get_list_of_passengers()
        self.assertEqual(len(passengers_1), 2)
        self.assertEqual(passengers_1[0].get_first_name(), "David")
        self.assertEqual(passengers_1[1].get_first_name(), "Sophia")

        # Test for Plane 2
        new_passenger_repo_2 = Repository()
        new_passenger_repo_2.add_value(Passenger("Michael", "Taylor", 666666666))
        new_passenger_repo_2.add_value(Passenger("Emma", "Johnson", 444444444))

        self.__plane2.set_list_of_passengers(new_passenger_repo_2)

        passengers_2 = self.__plane2.get_list_of_passengers()
        self.assertEqual(len(passengers_2), 2)
        self.assertEqual(passengers_2[0].get_first_name(), "Michael")
        self.assertEqual(passengers_2[1].get_first_name(), "Emma")

        # Test for Plane 3
        new_passenger_repo_3 = Repository()
        new_passenger_repo_3.add_value(Passenger("Christopher", "Lee", 333333333))

        self.__plane3.set_list_of_passengers(new_passenger_repo_3)

        passengers_3 = self.__plane3.get_list_of_passengers()
        self.assertEqual(len(passengers_3), 1)
        self.assertEqual(passengers_3[0].get_first_name(), "Christopher")

    def test_add_a_passenger_at_index(self):
        new_passenger = Passenger("Eva", "Williams", 111111111)
        self.__plane1.add_a_passenger_at_index(1, new_passenger)

        passengers = self.__plane1.get_list_of_passengers()
        self.assertEqual(len(passengers), 3)
        self.assertEqual(passengers[1].get_first_name(), "Eva")
        self.assertEqual(passengers[1].get_last_name(), "Williams")
        self.assertEqual(passengers[1].get_passport_number(), 111111111)

    def test_get_a_passenger_at_index(self):
        passenger = self.__plane1.get_a_passenger_at_index(0)
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")
        self.assertEqual(passenger.get_passport_number(), 1234567890)

    def test_delete_passenger_at_index(self):
        deleted_passenger = self.__plane1.delete_passenger_at_index(1)

        passengers1 = self.__plane1.get_list_of_passengers()
        self.assertEqual(len(passengers1), 1)

        deleted_passenger2 = self.__plane2.delete_passenger_at_index(1)
        passengers2 = self.__plane2.get_list_of_passengers()
        self.assertEqual(len(passengers2),1)

        deleted_passenger3 = self.__plane3.delete_passenger_at_index(0)
        passengers3 = self.__plane3.get_list_of_passengers()
        self.assertEqual(len(passengers3), 0)


    def test_sort_passengers_by_last_name(self):
        sorted_passengers = self.__plane1.sort_passengers_by_last_name()
        self.assertEqual(sorted_passengers[0].get_last_name(), "Doe")
        self.assertEqual(sorted_passengers[1].get_last_name(), "Johnson")
        self.assertEqual(sorted_passengers[1].get_first_name(), "Alice")

    def test_get_number_of_passengers_with_first_name_starting_with_a_substr(self):
        count = self.__plane1.get_number_of_passengers_with_first_name_starting_with_a_substr("A")
        self.assertEqual(count, 1)
        self.assertEqual(self.__plane1.get_number_of_passengers_with_first_name_starting_with_a_substr("J"), 1)
        self.assertEqual(self.__plane1.get_number_of_passengers_with_first_name_starting_with_a_substr("X"), 0)

    def test_starts_with_same_3_letters(self):
        self.assertFalse(self.__plane1.starts_with_same_3_letters())
        self.__plane1.add_a_passenger_at_index(1, Passenger("Sam", "Johnson", 987654321))
        self.assertTrue(self.__plane1.starts_with_same_3_letters())
        self.__plane1.delete_passenger_at_index(1)
        self.assertFalse(self.__plane1.starts_with_same_3_letters())

    def test_first_last_contain_string(self):
        result = self.__plane1.first_last_contain_string("Jo")
        self.assertEqual(result.get_length(), 2)
        self.assertEqual(result.get_all_values()[0].get_first_name(), "John")
        self.assertEqual(result.get_all_values()[0].get_last_name(), "Doe")
        self.assertEqual(result.get_all_values()[1].get_last_name(), "Johnson")

    def test_identify_passenger_with_given_name(self):
        self.assertTrue(self.__plane1.identify_passenger_with_given_name("Doe"))
        self.assertFalse(self.__plane1.identify_passenger_with_given_name("Smith"))
        self.assertTrue(self.__plane1.identify_passenger_with_given_name("Doe"))

class TestRepository(unittest.TestCase):

    def setUp(self):
        # Create a repository with some initial values
        self.repo = Repository()
        self.repo.add_value(1)
        self.repo.add_value(2)
        self.repo.add_value(3)

    def test_add_value(self):
        self.repo.add_value(4)
        self.assertEqual(self.repo.get_all_values(), [1, 2, 3, 4])
        self.assertEqual(self.repo.get_length(), 4)
        self.assertEqual(self.repo.get_value_at_index(3), 4)

    def test_add_value_at_index(self):
        self.repo.add_value_at_index(1, 10)
        self.assertEqual(self.repo.get_all_values(), [1, 10, 2, 3])
        self.assertEqual(self.repo.get_length(), 4)
        self.assertEqual(self.repo.get_value_at_index(1), 10)

    def test_get_value_at_index(self):
        value = self.repo.get_value_at_index(1)
        self.assertEqual(value, 2)
        self.assertEqual(self.repo.get_length(), 3)
        self.assertEqual(self.repo.get_all_values(), [1, 2, 3])

    def test_update_value_at_index(self):
        self.repo.update_value_at_index(1, 20)
        self.assertEqual(self.repo.get_all_values(), [1, 20, 3])
        self.assertEqual(self.repo.get_value_at_index(1), 20)
        self.assertEqual(self.repo.get_length(), 3)

    def test_delete_value_at_index(self):
        self.repo.delete_value_at_index(1)
        self.assertEqual(self.repo.get_all_values(), [1, 3])
        self.assertEqual(self.repo.get_length(), 2)
        self.assertEqual(self.repo.get_value_at_index(1), 3)

    def test_sort_repo(self):
        sorted_repo = self.repo.sort_repo(lambda x: x)
        self.assertEqual(sorted_repo, [1, 2, 3])
        self.assertEqual(self.repo.get_all_values(), [1, 2, 3])
        self.assertEqual(self.repo.get_length(), 3)

class TestAirport(unittest.TestCase):

    def setUp(self):
        passenger_repo_1 = Repository()
        passenger_repo_1.add_value(Passenger("John", "Doe", 1234567890))
        passenger_repo_1.add_value(Passenger("Alice", "Johnson", 987654321))

        passenger_repo_2 = Repository()
        passenger_repo_2.add_value(Passenger("Bob", "Smith", 555555555))
        passenger_repo_2.add_value(Passenger("Eva", "Williams", 111111111))

        passenger_repo_3 = Repository()
        passenger_repo_3.add_value(Passenger("Mike", "Miller", 999999999))

        self.airport = Airport()
        self.plane1 = Plane(1, "Airline1", 100, "Destination1", passenger_repo_1)
        self.plane2 = Plane(2, "Airline2", 150, "Destination1", passenger_repo_2)
        self.plane3 = Plane(3, "Airline3", 120, "Destination3", passenger_repo_3)

    def test_add_plane(self):
        self.airport.add_plane(self.plane1)
        planes = self.airport.get_planes()
        self.assertEqual(planes, [self.plane1])
        self.assertEqual(len(planes), 1)
        self.assertIn(self.plane1, planes)

    def test_add_plane_at_index(self):
        self.airport.add_plane(self.plane1)
        self.airport.add_plane_at_index(0, self.plane2)
        planes = self.airport.get_planes()
        self.assertEqual(planes, [self.plane2, self.plane1])
        self.assertEqual(len(planes), 2)
        self.assertIn(self.plane1, planes)
        self.assertIn(self.plane2, planes)

    def test_update_plane_at_index(self):
        self.airport.add_plane(self.plane1)
        passenger_repo_4 = Repository()
        passenger_repo_4.add_value(Passenger("Marian", "Ionescu", 123456))
        passenger_repo_4.add_value(Passenger("Mircea", "Radu", 234567))
        passenger_repo_4.add_value(Passenger("Andrei", "Popescu", 345678))
        new_plane = Plane(1, "UpdatedAirline", 120, "UpdatedDestination", passenger_repo_4)
        self.airport.update_plane_at_index(0, new_plane)
        planes = self.airport.get_planes()
        self.assertEqual(planes, [new_plane])
        self.assertEqual(len(planes), 1)
        self.assertIn(new_plane, planes)

    def test_delete_plane_at_index(self):
        self.airport.add_plane(self.plane1)
        self.airport.delete_plane_at_index(0)
        planes = self.airport.get_planes()
        self.assertEqual(planes, [])
        self.assertEqual(len(planes), 0)

    def test_sort_planes_by_number_of_passengers(self):
        self.airport.add_plane(self.plane1)
        self.airport.add_plane(self.plane2)
        self.airport.add_plane(self.plane3)
        sorted_planes = self.airport.sort_planes_by_number_of_passengers()
        self.assertEqual(sorted_planes, [self.plane1, self.plane3, self.plane2])
        self.assertEqual(len(sorted_planes), 3)
        self.assertIn(self.plane1, sorted_planes)

    def test_sort_planes_by_passengers_substring(self):
        self.airport.add_plane(self.plane1)
        self.airport.add_plane(self.plane2)
        self.airport.add_plane(self.plane3)

        sorted_planes = self.airport.sort_planes_by_passengers_substring("J")
        self.assertEqual(sorted_planes, [self.plane2, self.plane3, self.plane1])
        self.assertEqual(len(sorted_planes), 3)
        self.assertIn(self.plane1, sorted_planes)

    def test_sort_planes_by_nr_passengers_destination(self):
        self.airport.add_plane(self.plane1)
        self.airport.add_plane(self.plane2)
        self.airport.add_plane(self.plane3)

        sorted_planes = self.airport.sort_planes_by_nr_passengers_destination()
        self.assertEqual(sorted_planes, [self.plane1, self.plane3, self.plane2])
        self.assertEqual(len(sorted_planes), 3)
        self.assertIn(self.plane1, sorted_planes)

    def test_check_different_last_names(self):
        passenger1 = Passenger("John", "Doe", 1234567890)
        passenger2 = Passenger("Alice", "Johnson", 987654321)
        passenger3 = Passenger("Bob", "Smith", 555555555)

        passengers = [passenger1, passenger2]

        result = self.airport.check_different_last_names(passengers, passenger3)
        self.assertTrue(result)

    def test_groups_of_k_different_last_name(self):
        self.airport.add_plane(self.plane1)

        self.passenger1 = Passenger("John", "Doe", 1234567890)
        self.passenger2 = Passenger("Alice", "Johnson", 987654321)


        groups = self.airport.groups_of_k_different_last_name(2, 1)
        self.assertEqual(groups, [[self.passenger1, self.passenger2]])
        self.assertEqual(len(groups), 1)
        self.assertIn([self.passenger1, self.passenger2], groups)

    def test_check_same_destination_different_airline(self):
        list_of_passenger1 = Repository()
        list_of_passenger2 = Repository()
        plane1 = Plane(1, "Airline1", 100, "Destination1", list_of_passenger1)
        plane2 = Plane(2, "Airline2", 150, "Destination2", list_of_passenger2)

        result = self.airport.check_same_destination_different_airline([plane1], plane2)
        self.assertFalse(result)

    def test_group_of_k_planes_same_destination_different_airline(self):
        self.airport.add_plane(self.plane1)
        self.airport.add_plane(self.plane2)

        groups = self.airport.group_of_k_planes_same_destination_different_airline(2)
        self.assertEqual(groups, [[self.plane1, self.plane2]])
        self.assertEqual(len(groups), 1)
        self.assertIn([self.plane1, self.plane2], groups)



if __name__ == '__main__':
    unittest.main()
