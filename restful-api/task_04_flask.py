import unittest
import requests

class TestFlaskAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://127.0.0.1:5000'

    def test_home_route(self):
        response = requests.get(f'{self.url}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_data_route_no_users(self):
        response = requests.get(f'{self.url}/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_user(self):
        user_data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = requests.post(f'{self.url}/add_user', json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "User added", "user": user_data})

    def test_data_route_after_adding_user(self):
        expected_users = ["john"]
        response = requests.get(f'{self.url}/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_users)

    def test_get_user(self):
        username = "john"
        user_data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = requests.get(f'{self.url}/users/{username}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), user_data)

    def test_get_nonexistent_user(self):
        username = "doesnotexist"
        response = requests.get(f'{self.url}/users/{username}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "User not found"})

    def test_status_route(self):
        response = requests.get(f'{self.url}/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_add_user_without_username(self):
        user_data = {
            "name": "Alice",
            "age": 25,
            "city": "San Francisco"
        }
        response = requests.post(f'{self.url}/add_user', json=user_data)
        self.assertEqual(response.status_code, 400)

    def test_add_duplicate_user(self):
        user_data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = requests.post(f'{self.url}/add_user', json=user_data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
