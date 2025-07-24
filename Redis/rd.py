import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True) ###decode_responses=True를 설정하면 redis에서 가져온 데이터가 자동으로 decode되어 utf-8로 변환됨


print(r.ttl('message')) ###남은 시간 출력
r.hset('userprofile:1', mapping={
    'name': 'John',
    'age': 30,
    'city': 'New York'
})

print(r.hgetall('userprofile:1')) ###userprofile:1의 모든 필드와 값을 가져옴