from marshmallow import Schema, fields
# marshmallow 라는 모듈에서 Schema와 fields를 불러옴

class ItemSchema(Schema):
# 클래스명을 ItemSchema 라고 하고 marshmallo 에서의 Schema를 상속받음

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    # 위 세 줄의 형태를 객체라고 하며,   
    # 이 객체를 나중에 직렬화하거나 역직렬화할 때   
    # 실제로 거기에 데이터에서 뭔가 잘못된 것이 있는지 체크해줌