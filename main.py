from passenger import Passenger
from plane import Plane
from airport import Airport
from RepositoryOperations import Repository

def display_menu():
    """
    D: displays the menu
    """
    print("Menu: ")
    print("1. Add a plane ")
    print("2. Add a plane at index")
    print("3. Get all planes ")
    print("4. Get a plane at index")
    print("5. Update a plane at index")
    print("6. Delete a plane at index")
    print("7. Add a passenger to a plane")
    print("8. Add a passenger to a plane at a given index")
    print("9. Get all passengers from a plane")
    print("10. Get a passenger at index from a plane")
    print("11. Delete a passenger")
    print("12. Sort the passengers in a plane by last name")
    print("13. Sort planes according to the number of passengers")
    print("14. Sort planes according to the number of passengers with the first name starting with a given substring")
    print("15.Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination")
    print("16.Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the same 3 letters")
    print("17. Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contain a string given as parameter")
    print("18. Identify plane/planes where there is a passenger with given name")
    print("19. Form groups of 𝒌 passengers from the same plane but with different last names ")
    print("20. Form  groups  of 𝒌 planes  with  the  same  destination  but  belonging  to  different airline companies")
    print("21. Exit the program")

def main():
    """
    D:Executes the asked operations
    """

    plane_repo = Airport()

    plane1 = Repository()
    plane1.add_value(Passenger("Marian", "Ionescu", 123456))
    plane1.add_value(Passenger("Mircea", "Radu", 234567))
    plane1.add_value(Passenger("Andrei", "Popescu", 345678))
    plane_repo.add_plane(Plane(1, "Wizz Air", 120, "Munich", plane1))


    plane2 = Repository()
    plane2.add_value(Passenger("Ana", "Popescu ", 456789))
    plane2.add_value(Passenger("Andrei", "Dinescu", 456890))
    plane2.add_value(Passenger("Bogdan", "Stan", 678901))
    plane_repo.add_plane(Plane(2, "TAROM", 160, "Paris", plane2))

    plane3 = Repository()
    plane3.add_value(Passenger("Ionut", "Radu", 789012))
    plane3.add_value(Passenger("Adrian", "Stoicu", 890123))
    plane3.add_value(Passenger("Roxana", "Mihai", 901234))
    plane3.add_value(Passenger("Razvan", "Ionescu", 112233))
    plane_repo.add_plane(Plane(3, "United Airlines", 200, "Chicago", plane3))

    plane4 = Repository()
    plane4.add_value(Passenger("Elena", "Marinescu", 445566))
    plane4.add_value(Passenger("Catalin", "Popa", 556677))
    plane_repo.add_plane(Plane(4, "Lufthansa", 150, "Munich", plane4))

    plane5 = Repository()
    plane5.add_value(Passenger("Maria", "Ivanov", 667788))
    plane5.add_value(Passenger("Victor", "Petrov", 778899))
    plane_repo.add_plane(Plane(5, "Wizz Air", 220, "London", plane5))

    plane6 = Repository()
    plane6.add_value(Passenger("Diana", "Gheorghe", 889900))
    plane6.add_value(Passenger("Stefan", "Muresan", 990011))
    plane6.add_value(Passenger("Alexandra", "Antonescu", 112233))
    plane_repo.add_plane(Plane(6, "Delta Airlines", 170, "New York", plane6))

    plane7 = Repository()
    plane7.add_value(Passenger("George", "Constantin", 334455))
    plane7.add_value(Passenger("Ana-Maria", "Iacob", 445566))
    plane7.add_value(Passenger("Cristian", "Dumitru", 556677))
    plane_repo.add_plane(Plane(7, "Lufthansa", 190, "Munich", plane7))

    plane8 = Repository()
    plane8.add_value(Passenger("Larisa", "Ilie", 667788))
    plane8.add_value(Passenger("Ion", "Barbu", 778899))
    plane_repo.add_plane(Plane(8, "Emirates", 210, "Dubai", plane8))

    plane9 = Repository()
    plane9.add_value(Passenger("Mihai", "Olaru", 889900))
    plane9.add_value(Passenger("Andreea", "Florescu", 990011))
    plane9.add_value(Passenger("Eduard", "Georgescu", 112233))
    plane_repo.add_plane(Plane(9, "Delta Airlines", 160, "Singapore", plane9))

    plane10 = Repository()
    plane10.add_value(Passenger("Oana", "Preda", 334455))
    plane10.add_value(Passenger("Vlad", "Stancu", 445566))
    plane10.add_value(Passenger("Alina", "Iancu", 556677))
    plane10.add_value(Passenger("Dorin", "Stancu", 667788))
    plane_repo.add_plane(Plane(10, "United Airlines", 200, "Paris", plane10))

    while True:
        display_menu()
        try:
            x = int(input("Choose an option:"))
            if x == 1:
                #add a plane
                try:
                    number = int(input("Plane number: "))
                    airline = input("Airline company: ")
                    number_of_seats = int(input("Number of seats: "))
                    destination = input("Destination: ")
                    list_of_passenger = Repository()
                    plane_repo.add_plane(Plane(number, airline, number_of_seats, destination, list_of_passenger))
                    print("Plane added successfully")
                except ValueError:
                    print("Wrong input data")

            elif x == 2:
                #add a plane at index
                try:
                    index = int(input("Index: "))
                    number = int(input("Plane number: "))
                    airline = input("Airline company: ")
                    number_of_seats = int(input("Number of seats: "))
                    destination = input("Destination: ")
                    list_of_passenger = Repository()
                    plane_repo.add_plane_at_index(index, Plane(number, airline, number_of_seats, destination, list_of_passenger))
                    print("Plane added successfully")
                except (ValueError, IndexError):
                    print("Wrong input data")

            elif x == 3:
                #Get all planes
                for plane in plane_repo.get_planes():
                    print(plane)

            elif x == 4:
                #Get a plane at index
                try:
                    index = int(input("Index: "))
                    print(plane_repo.get_plane_at_index(index))
                except IndexError:
                    print("Wrong input data")

            elif x == 5:
                #update a plane at index
                try:
                    index = int(input("Index: "))
                    number = int(input("Plane new number: "))
                    airline = input("New airline company: ")
                    number_of_seats = int(input("New number of seats: "))
                    destination = input("New destination: ")
                    list_of_passenger = Repository()
                    plane_repo.update_plane_at_index(index, Plane(number, airline, number_of_seats, destination, list_of_passenger))
                    print("Plane updated succesfully")
                except (ValueError, IndexError):
                    print("Wrong input data")

            elif x == 6:
                #delete a plane at index
                try:
                    index = int(input("Index: "))
                    plane_repo.delete_plane_at_index(index)
                    print("Plane deleted succesfully")
                except IndexError:
                    print("Wrong input data")

            elif x == 7:
                #insert a passenger to a plane
                try:
                    number = int(input("Plane number: " ))
                    first_name = input("First name of the new passenger: ")
                    last_name = input("Last name of the new passenger: ")
                    passport_number = int(input("Passport number of the new passenger: "))
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            plane.add_a_passenger(Passenger(first_name, last_name, passport_number))
                    print("Passenger added successfully")
                except ValueError:
                    print("Wrong input data")

            elif x == 8:
                #add a passenger to a plane at a given index
                try:
                    number = int(input("Plane number: "))
                    index = int(input("Index: "))
                    first_name = input("First name of the new passenger: ")
                    last_name = input("Last name of the new passenger: ")
                    passport_number = int(input("Passport number of the new passenger: "))
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            plane.add_a_passenger_at_index(index, Passenger(first_name, last_name, passport_number))
                    print("Passenger added successfully")
                except (ValueError, IndexError):
                    print("Wrong input data")

            elif x == 9:
                #get all passengers from a plane
                try:
                    number = int(input("Plane number: "))
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            for passenger in plane.get_list_of_passengers():
                                print(passenger)
                except ValueError:
                    print("Wrong input data")

            elif x == 10:
                #get a passenger at index from a plane
                try:
                    number = int(input("Plane number: "))
                    index = int(input("Index: "))
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            print(plane.get_a_passenger_at_index(index))
                except (ValueError, IndexError):
                    print("Wrong input data")

            elif x == 11:
                #delete a passenger
                try:
                    number = int(input("Plane number: "))
                    index = int(input("Index: "))
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            plane.delete_passenger_at_index(index)
                    print("Passenger deleted successfully")
                except (ValueError, IndexError):
                    print("Wrong input data")

            elif x == 12:
                #Sort passengers in a plane
                try:
                    number = int(input("Plane number: "))
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            answear = plane.sort_passengers_by_last_name()

                    for passenger in answear:
                        print(passenger)
                except ValueError:
                    print("Wrong input data")


            elif x == 13:
                #Sort planes by number of passengers
                sorted_repo = plane_repo.sort_planes_by_number_of_passengers()
                for plane in sorted_repo:
                    print(plane)

            elif x == 14:
                #Sort planes according to the number of passengers with the first name starting with a given substring
                substring = input("Substring: ")
                sorted_repo = plane_repo.sort_planes_by_passengers_substring(substring)
                for plane in sorted_repo:
                    print(plane)

            elif x == 15:
                #Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
                sorted_repo = plane_repo.sort_planes_by_nr_passengers_destination()
                for plane in sorted_repo:
                    print(plane)

            elif x == 16:
                #Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the same 3 letters
                for plane in plane_repo.get_planes():
                    if plane.starts_with_same_3_letters():
                        print(plane)

            elif x == 17:
                #Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contain a string given as parameter
                try:
                    number = int(input("Plane number: "))
                    string = input("String: ")
                    for plane in plane_repo.get_planes():
                        if plane.get_plane_number() == number:
                            result = plane.first_last_contain_string(string)

                    for passenger in result.get_all_values():
                        print(passenger)

                except ValueError:
                    print("Wrong input data")

            elif x == 18:
                #Identify plane/planes where there is a passenger with given name
                name = input("Name: ")
                for plane in plane_repo.get_planes():
                    if plane.identify_passenger_with_given_name(name):
                        print(plane)

            elif x == 19:
                #Form groups of 𝒌 passengers from the same plane but with different last names
                try:
                    k = int(input("k: "))
                    number = int(input("Plane number: "))
                    answer = plane_repo.groups_of_k_different_last_name(k, number)
                    for item1 in answer:
                        for item2 in item1:
                            print(item2)
                        print()
                    print()
                except ValueError:
                    print("Wrong k")

            elif x == 20:
                #Form  groups  of 𝒌planes  with  the  same  destination  but  belonging  to  different airline companies
                try:
                    k = int(input("k: "))
                    answer = plane_repo.group_of_k_planes_same_destination_different_airline(k)
                    for item1 in answer:
                        for item2 in item1:
                            print(item2)
                        print(";")
                    print()
                except ValueError:
                    print("Wrong k")

            elif x == 21:
                break
            else:
                raise ValueError("Wrong operation")

        except ValueError:
            print("non-existent option")

if __name__ == "__main__":
    main()