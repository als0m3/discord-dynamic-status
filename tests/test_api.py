import unittest
from unittest.mock import patch
from services import apiCalls

class ApiTests(unittest.TestCase):
    @patch.object(apiCalls.requests, "request")
    def test_missing_token_never_sends_request(self, request):
        with patch.object(apiCalls, "USER_TOKEN", None):
            with self.assertRaises(RuntimeError):
                apiCalls.setStatus("hello", "online")
        request.assert_not_called()

    @patch.object(apiCalls.requests, "request")
    def test_request_is_bounded_and_checks_http_errors(self, request):
        with patch.object(apiCalls, "USER_TOKEN", "test-token"):
            apiCalls.setStatus("hello", "online")
        self.assertEqual(request.call_args.kwargs["timeout"], 15)
        request.return_value.raise_for_status.assert_called_once()
