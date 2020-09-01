
# So this is a fish class
class Fish:
    # The __init__ function tells what information the user should give
    def __init__(self, name, type_, origin, rate_in_percentage):
        self.name = name.lower()
        self.type_ = type_.lower()
        self.origin = origin.lower()
        self.rate_in_percentage = rate_in_percentage

    def data_output(self):

        # This code looks like a gun btw.
        # Returns the name, type, and the rate in %

        print('Name: {}, Type: {}, Origin: {}, Rate in %: {} \n'.format(
            self.name, self.type_, self.origin, self.rate_in_percentage
        ))

    # Validates the data
    def data_validator(self):

        # Validates the string data
        def str_data_validator():

            # All the parameters stored in a list so that we can iterate in its
            temp_parameter_list = [self.name, self.type_, self.origin]

            # iteration loop on the list
            for parameter in temp_parameter_list:
                # If the type of the parameter is string
                if type(parameter) is str:
                    # Print that its valiated
                    print('\'{}\', \n validating... done'.format(parameter))

                else:
                    # Otherwise, print this message.
                    print('Incorrect argument value.')

        def number_data_validator():
            # Validates the data thats in numeric form

            # Same case but for integer
            if type(self.rate_in_percentage) is int:
                pass

            # Just print a message if it doesn't works
            # In detail, print a error message if the rate in % is not an
            # integer value.
            else:
                print('Incorrect values for the rate in %.')

        # Call both the validation functions
        str_data_validator()
        number_data_validator()

    # Logs the output of the object or the data stored in the object
    def log_output(self):
        # Open the file called log.txt with append permissions
        file = open('log.txt', 'a')
        # Print that this operation is currently running
        print('\n writing data..')

        # Write the information
        file.writelines(
            'Name -> {}, Type -> {}, Origin -> {}, Rate (%) -> {} \n'.format(
                self.name, self.type_, self.origin, self.rate_in_percentage)
        )
        # Close the file
        file.close()

    # Erase/flush the contents of the log file
    def flush(self):
        file_temp = open('log.txt', 'w')

        blank = ''
        file_temp.write(blank)
