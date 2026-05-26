import unittest
import requests


class TestHelloSpencerAPI(unittest.TestCase):

    BASE_URL = "http://localhost:5556"

    def test_hello_endpoint_status(self):
        """Test if the live API returns HTTP 200"""
        response = requests.get(f"{self.BASE_URL}/api/hello")
        self.assertEqual(response.status_code, 200)

    def test_hello_endpoint_response(self):
        """Test if the live API returns correct JSON"""
        response = requests.get(f"{self.BASE_URL}/api/hello")
        data = response.json()
        self.assertEqual(data['message'], 'Hello Spencer')
        self.assertEqual(data['status'], 'success')

# test
if __name__ == '__main__':
    unittest.main()