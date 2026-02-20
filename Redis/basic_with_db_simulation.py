import redis
import json

# 1. Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def get_user(user_id: int):
    key = f"user:{user_id}"
    cached = r.get(key)

    if (cached):
        # Getting data from memory
        print("✅ From Cache")
        return json.loads(cached)
    else:
        # Simulating db retrieval
        print("🔄 Getting data from 'database'")
        data = {"id": user_id, "name": "Lindo", "points": 100}

        # Store for 60 seconds
        r.set(key, json.dumps(data), ex=60)
        return data
      
