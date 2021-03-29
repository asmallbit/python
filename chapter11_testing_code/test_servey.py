import unittest
from survey import AnonymousSurney

class TestSurvey(unittest.TestCase):
    def setUp(self):
        question = "What's your favrite thing?"
        self.responses = ['Women', 'Money', 'Reputation', 'Healthy body']
        self.survey = AnonymousSurney(question)

    def test_single_case(self):
        self.survey.save_reponds(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_three_cases(self):
        for response in self.responses:
            self.survey.save_reponds(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

unittest.main()