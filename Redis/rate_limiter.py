import redis


r = redis.Redis(host="localhost", port=6379, db=0)

def is_allowed(user_id):
    key = f"login:{user_id}"
    count = r.incr(key)

    if count == 1:
        r.expire(key, 60)

    return True if count < 5 else False