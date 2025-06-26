
from src.models.quote import Quote


class QuoteService:

    def __init__(self):
        self.list_of_quotes = []

    def add_quote(self, description: str, date_quoted: str)-> Quote:
        if not description.strip():
            raise ValueError("The field must not be empty")
        new_quote = Quote(description=description,
                          date_quoted=date_quoted
        )
        self.list_of_quotes.append(new_quote)
        return new_quote

    def get_all_quotes(self)-> list[Quote]:
        return self.list_of_quotes
