import unittest
from src.calc import add, divide
from src.employee import getEmployeeData
from unittest.mock import patch


# While mocking, we used the path src.employee --> It has imported requests package and we used get on it.
# The function recieves the second parameter as mocked object. Here it's request_patch_get (It can be any name).
@patch("src.employee.requests.get")
class TestEmployee(unittest.TestCase):
    def test_employee_api(self, request_patch_get):

        # Mock return values
        request_patch_get.return_value.ok = True
        request_patch_get.return_value.text = "Success"

        result = getEmployeeData(2)

        # Check assert_called_with
        request_patch_get.assert_called_with(
            "https://jsonplaceholder.typicode.com/todos/2"
        )
        self.assertEqual(result, "Success")

        request_patch_get.return_value.ok = False
        result = getEmployeeData(2)
        self.assertEqual(result, "Bad response")
