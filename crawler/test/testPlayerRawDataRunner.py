import unittest
from runners.runPlayerRawData import run_player_raw_data, handle_arguments
from utils.testUtils.requestsTestUtils import mock_requests_get

class TestPlayerRawDataRunner(unittest.TestCase):

    def test_should_fail_if_no_arguments(self):
        with self.assertRaises(TypeError):
            handle_arguments([])
    


if __name__ == '__main__':
    unittest.main()