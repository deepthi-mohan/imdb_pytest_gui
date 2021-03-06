from pathlib import Path

"""This class contains general function """


class General():

    # Get directory path
    def get_directory_path(self):
        application_path = Path().absolute()
        print(application_path)
        return application_path

    # Strip delimiter from string value
    # params: string value, delimiter to be stripped
    def strip_string_value(self, value, delimiter):
        stripped_string = value.strip(delimiter)
        print(stripped_string)
        return stripped_string

    # Verify a string value present in list
    # params: list, expected text value
    def verify_list_values(self, value_list, expected_text):
        if expected_text in value_list:
            assert True
        else:
            assert False

    # Compare and verify two lists
    # params: actual list, expected list
    def verify_list(self, actual_list, expected_list):
        if actual_list == expected_list:
            assert True
        else:
            assert False

    # Sort list in  order
    # params: actual list, boolean order details
    def sort_list(self, actual_list, reverse):
        sorted_list = actual_list[:]
        sorted_list.sort(reverse=reverse)
        return sorted_list

    # Compare and verify two lists
    # params: actual list, expected list
    def verify_values(self, actual_value, expected_value):
        if actual_value == expected_value:
            assert True
        else:
            assert False

    # def sort_list_in_decending_order1(self, actual_list):
    #     test_list1 = actual_list[:]
    #     test_list1.sort(reverse=True)
    #     sorted_list = sorted(actual_list)
    #     print("actual list is")
    #     print(actual_list)
    #     print("sorted list is" )
    #     print(sorted_list)
    #     print("test_list1 list is")
    #     print(test_list1)
    #     if test_list1 == actual_list:
    #         assert True
    #     else:
    #         assert False

