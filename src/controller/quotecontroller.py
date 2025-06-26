from flask import jsonify, request
from marshmallow import ValidationError
from datetime import datetime
from src.dto.request.quoterequest import QuoteRequest
from src.models.quote import Quote

class QuoteController:
    def __init__(self, quoteservice):
        self.quoteservice = quoteservice

    def add_quote(self):
        try:
            data = request.json
            schema = QuoteRequest()
            validated_data = schema.load(data)

            description = validated_data["description"]
            date_quoted = validated_data.get("date_quoted", None)

            if date_quoted is None:
                date_quoted = datetime.now().isoformat()

            self.quoteservice.add_quote(description, date_quoted)

            date_obj = datetime.fromisoformat(date_quoted)
            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M")

            return jsonify({
                "message": "You have successfully added a Quote",
                "date_quoted": formatted_date
            }), 201

        except ValidationError as e:
            return jsonify({"error": e.messages}), 400

    def get_quotes(self):
        quotes = self.quoteservice.get_all_quotes()
        quote_list = [
            {
                "description": quote.description,
                "date_quoted": quote.date_quoted
            }
            for quote in quotes
        ]
        return jsonify({"quotes": quote_list}), 200