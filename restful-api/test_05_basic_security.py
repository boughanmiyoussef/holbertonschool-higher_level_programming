import unittest
import json
from task_05_basic_security import app, users
from flask_jwt_extended import create_access_token

class TestAPISecurity(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_basic_protected_no_auth(self):
        response = self.app.get('/basic-protected')
        self.assertEqual(response.status_code, 401)

    def test_basic_protected_with_auth(self):
        response = self.app.get('/basic-protected', headers={
            'Authorization': 'Basic ' + base64.b64encode(b'user1:password').decode('utf-8')
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Basic Auth: Access Granted"})

    def test_login(self):
        response = self.app.post('/login', json={"username": "user1", "password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)

    def test_jwt_protected_no_token(self):
        response = self.app.get('/jwt-protected')
        self.assertEqual(response.status_code, 401)

    def test_jwt_protected_with_token(self):
        access_token = create_access_token(identity={'username': 'user1', 'role': 'user'})
        response = self.app.get('/jwt-protected', headers={
            'Authorization': 'Bearer ' + access_token
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "JWT Auth: Access Granted"})

    def test_admin_only_with_user_token(self):
        access_token = create_access_token(identity={'username': 'user1', 'role': 'user'})
        response = self.app.get('/admin-only', headers={
            'Authorization': 'Bearer ' + access_token
        })
        self.assertEqual(response.status_code, 403)

    def test_admin_only_with_admin_token(self):
        access_token = create_access_token(identity={'username': 'admin1', 'role': 'admin'})
        response = self.app.get('/admin-only', headers={
            'Authorization': 'Bearer ' + access_token
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Admin Access: Granted"})

if __name__ == "__main__":
    unittest.main()
