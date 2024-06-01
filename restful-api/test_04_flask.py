import unittest
import requests

class TestFlaskAPI(unittest.TestCase):

    base_url = "http://127.0.0.1:5000"

    def test_home_route(self):
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Welcome to the Flask API!")

    def test_get_data_no_users(self):
        # Clear users for this test
        requests.post(f"{self.base_url}/clear_users")
        response = requests.get(f"{self.base_url}/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_add_user(self):
        user = {"username": "alice", "name": "Alice", "age": 25, "city": "Seattle"}
        response = requests.post(f"{self.base_url}/add_user", json=user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["user"], user)

    def test_get_data_after_adding_user(self):
        user = {"username": "bob", "name": "Bob", "age": 32, "city": "Chicago"}
        requests.post(f"{self.base_url}/add_user", json=user)
        response = requests.get(f"{self.base_url}/data")
        self.assertEqual(response.status_code, 200)
        self.assertIn("bob", response.json())

    def test_get_user(self):
        # Ensure the user "john" is added before testing
        user = {"username": "john", "name": "John", "age": 30, "city": "New York"}
        requests.post(f"{self.base_url}/add_user", json=user)
        response = requests.get(f"{self.base_url}/users/john")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "john")

    def test_get_user_not_found(self):
        response = requests.get(f"{self.base_url}/users/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_status_route(self):
        response = requests.get(f"{self.base_url}/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_add_user_without_username(self):
        user = {"name": "Charlie", "age": 29, "city": "Denver"}
        response = requests.post(f"{self.base_url}/add_user", json=user)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Username is required")

    def test_add_duplicate_user(self):
        user = {"username": "john", "name": "John", "age": 30, "city": "New York"}
        requests.post(f"{self.base_url}/add_user", json=user)
        response = requests.post(f"{self.base_url}/add_user", json=user)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()["error"], "User already exists")

if __name__ == "__main__":
    unittest.main()
