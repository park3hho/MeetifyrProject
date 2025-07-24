from marshmallow import Schema, fields # 스키마 생성

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)