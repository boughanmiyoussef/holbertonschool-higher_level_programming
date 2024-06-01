import unittest
import json
from task_04_flask import app


class TestFlaskAPI(unittest.TestCase):
    def test_home_route(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.decode('utf-8'),
            'Welcome to the Flask API!')

    def test_data_route(self):
        client = app.test_client()
        response = client.get('/data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_status_route(self):
        client = app.test_client()
        response = client.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'OK')

    def test_get_user(self):
        client = app.test_client()
        response = client.get('/users/john')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['username'], 'john')

    def test_get_nonexistent_user(self):
        client = app.test_client()
        response = client.get('/users/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'User not found')

    def test_add_user(self):
        client = app.test_client()
        new_user_data = {
            'username': 'alice',
            'name': 'Alice',
            'age': 25,
            'city': 'San Francisco'
        }
        response = client.post('/add_user', json=new_user_data)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User added')
        self.assertEqual(data['user']['username'], 'alice')

    def test_add_user_no_username(self):
        client = app.test_client()
        new_user_data = {
            'name': 'Alice',
            'age': 25,
            'city': 'San Francisco'
        }
        response = client.post('/add_user', json=new_user_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)

    def test_add_duplicate_user(self):
        client = app.test_client()
        new_user_data = {
            'username': 'john',
            'name': 'John',
            'age': 30,
            'city': 'New York'
        }
        response = client.post('/add_user', json=new_user_data)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)


if __name__ == '__main__':
    unittest.main()
