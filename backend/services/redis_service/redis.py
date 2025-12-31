import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

redis_client.set("hello", "world")
print(redis_client.get("hello"))  # world