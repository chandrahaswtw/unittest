import unittest
from src.calc import add, divide
from src.employee import getEmployeeData
from unittest.mock import patch

# Assert:
# assertEqual(a, b)	--> checks a == b
# assertNotEqual(a, b) --> checks	a != b
# assertTrue(x) --> checks	bool(x) is True
# assertFalse(x) --> checks	bool(x) is False
# assertIs(a, b) --> checks	a is b
# assertIsNot(a, b) --> checks	a is not b
# assertIsNone(x) --> checks	x is None
# assertIsNotNone(x) --> checks	x is not None
# assertIn(a, b) --> checks	a in b
# assertNotIn(a, b) --> checks	a not in b
# assertIsInstance(a, b) --> checks	isinstance(a, b)
# assertNotIsInstance(a, b) --> checks	not isinstance(a, b)
# assertIsSubclass(a, b) --> checks	issubclass(a, b)
# assertNotIsSubclass(a, b) --> checks	not issubclass(a, b)


class TestCalc(unittest.TestCase):

    # Runs once before any test methods in this class.
    # Use for populating DB values etc.
    @classmethod
    def setUpClass(cls):
        pass

    # runs once after all test methods in this class.
    @classmethod
    def tearDownClass(cls):
        pass

    # Executes before each test method in this class.
    def setUp(self):
        pass

    # Executes before each test method in this class.
    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(15, add(5, 10))

    def test_divide(self):
        #  Here we are not calling the function directly but passing the arguments later
        self.assertRaises(ValueError, divide, 2, 0)

        # Same example using context manager, we can pass make the function call directly
        with self.assertRaises(ValueError):
            divide(2, 0)
