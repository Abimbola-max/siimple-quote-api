import unittest
from datetime import datetime
from src.models.quote import Quote
from src.service.quoteservice import QuoteService

class TestQuoteService(unittest.TestCase):

    def setUp(self):
        self.service = QuoteService()

    def test_add_quote_success(self):
        description = "I love python."
        date_quoted = datetime.utcnow().isoformat()
        quote = self.service.add_quote(description, date_quoted)
        self.assertIsInstance(quote, Quote)
        self.assertEqual(quote.description, description)
        self.assertEqual(quote.date_quoted, date_quoted)
        self.assertEqual(len(self.service.list_of_quotes), 1)

    def test_add_quote_empty_description_raises_an_exception(self):
        with self.assertRaises(ValueError) as context:
            self.service.add_quote("   ", "2025-06-24T00:00:00Z")
        self.assertEqual(str(context.exception), "The field must not be empty")

    def test_get_all_quotes_empty_when_nothing_is_added(self):
        quotes = self.service.get_all_quotes()
        self.assertIsInstance(quotes, list)
        self.assertEqual(len(quotes), 0)

    def test_get_all_quotes_returns_the_actual_number_of_quotes_after_adding(self):
        self.service.add_quote("i love java", "2025-06-24T00:00:00Z")
        self.service.add_quote("i love python", "2025-06-25T00:00:00Z")
        quotes = self.service.get_all_quotes()
        self.assertEqual(len(quotes), 2)
        self.assertEqual(quotes[0].description, "i love java")
        self.assertEqual(quotes[1].description, "i love python")

    def test_add_quote_strips_description(self):
        description = "   Trimmed quote   "
        date_quoted = "2025-06-24T00:00:00Z"
        quote = self.service.add_quote(description, date_quoted)
        self.assertEqual(quote.description, description)

if __name__ == "__main__":
    unittest.main()
