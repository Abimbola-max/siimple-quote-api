from marshmallow import Schema, fields, validate

class QuoteRequest(Schema):
    description = fields.Str(
        required=True,
        allow_none=False,
        validate=validate.Length(min=4),
    )
    date_quoted = fields.DateTime(required=False, allow_none=True)