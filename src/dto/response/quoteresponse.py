from marshmallow import Schema, fields


class QuoteResponse(Schema):
    message = fields.Str()
    date = fields.DateTime()