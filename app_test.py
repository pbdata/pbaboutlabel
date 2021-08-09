"""Unit test file for app.py"""
from app import returntestscore
import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def test_f1_score(self):
        """Test f1 score"""
        score = returntestscore()
        print('f1_score is ' + str(score))
        self.assertGreater(score, 0.5)

if __name__ == "__main__":
    unittest.main()
