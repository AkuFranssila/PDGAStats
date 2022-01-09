import unittest
from runners.runPlayerRawData import runPlayerRawData, handleArguments
from utils.testUtils.requestsTestUtils import mock_requests_get

class TestPlayerRawDataRunner(unittest.TestCase):

    def test_should_fail_if_no_arguments(self):
        with self.assertRaises(TypeError):
            handleArguments([])
    


if __name__ == '__main__':
    unittest.main()