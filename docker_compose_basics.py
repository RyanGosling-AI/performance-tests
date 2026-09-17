from redis import Redis

cache = Redis("redis", port=6379)
cache.incr("times", amount=1)
print(cache.get("times"))
