from application import application
import unittest


class TestPosts(unittest.TestCase):

    # check if response is 200
    def test_response(self):
        tester = application.test_client(self)
        response = tester.get('/posts', query_string={'subreddit_name': 'python'})
        self.assertEqual(response.status_code, 200)

    # check if content type is application/json
    def test_content(self):
        tester = application.test_client(self)
        response = tester.get('/posts', query_string={'subreddit_name': 'python'})
        self.assertEqual(response.content_type, 'application/json')

    # check response body
    def test_data(self):
        tester = application.test_client(self)
        response = tester.get('/posts', query_string={'subreddit_name': 'python'})
        self.assertTrue(b'hottest' in response.data and b'newest' in response.data)


if __name__ == "__main__":
    unittest.main()
