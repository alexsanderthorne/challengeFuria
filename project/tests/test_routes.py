import unittest
from app.routes import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Adjust based on actual content

    # Add more tests for other routes as needed

if __name__ == '__main__':
    unittest.main()