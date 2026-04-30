from apiflask import Schema
from apiflask.fields import String, Integer

class Status0utSchema(Schema):
    status = String()
    message = String()
    service = String()
    items_count = Integer()