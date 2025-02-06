import unittest
from app import app

class TestLinkedInAgent(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_start_route(self):
        response = self.app.get('/start')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AI Agent started', response.data)

    def test_log_route(self):
        response = self.app.get('/log')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log data:', response.data)

if __name__ == '__main__':
    unittest.main()
