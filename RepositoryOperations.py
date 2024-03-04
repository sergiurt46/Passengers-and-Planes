class Repository:

    def __init__(self):
        """
        D: constructs a repository
        """

        self.__repo = []

    def add_value(self, value: object):
        """
        D: inserts a value at the end of the repository
        Parameter:
        -value: object
        """

        self.__repo.append(value)

    def add_value_at_index(self, index, value: object):
        """
        D: inserts a value at a given index
        Parameters:
            -index: int
            -value: object
        """
        if isinstance(index, int) and 0 <= index < len(self.__repo):
            self.__repo.insert(index, value)
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")

    def get_all_values(self):
        """
        D: gets all the values from the repository
        """
        return self.__repo[:]

    def get_value_at_index(self, index):
        """
        D: gets a value at a given index
        Parameter:
        - index: int
        """
        if isinstance(index, int) and 0 <= index < len(self.__repo):
            return self.__repo[index]
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")

    def update_value_at_index(self, index, new_value:object):
        """
        D:update a value at a given index
        Parameters:
            -index: int
            -new_value: object
        """
        if isinstance(index, int) and 0 <= index < len(self.__repo):
            self.__repo[index] = new_value
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")

    def delete_value_at_index(self, index):
        """
        D: delete a value at a given index
        Parameter:
        -index: int
        """
        if isinstance(index, int) and 0 <= index < len(self.__repo):
            del self.__repo[index]
        else:
            raise IndexError("The index has to be an integer between 0 and the length of the repository")

    def get_length(self):
        """
        D: returns the length of the repository
        """
        return len(self.__repo)

    def sort_repo(self, key_function):
        """
        D:Sorts a repo by key_function
        """
        return sorted(self.__repo, key = key_function)

    def get_k_groups_with_property(self, values, k, key_function, index=0, curr_sol=[]):
        '''
        Desc: gets groups of k elements having the property key_function
        In: values - list
            k - int
            key_function - function
        '''

        if len(curr_sol) == k:
            return [curr_sol[:]]

        list_of_groups = []
        for i in range(index, len(values)):
            x = values[i]
            if not key_function(curr_sol, x):
                continue
            curr_sol.append(x)
            new_groups = self.get_k_groups_with_property(values, k, key_function, i + 1, curr_sol)
            list_of_groups.extend(new_groups)
            curr_sol.pop()

        return list_of_groups