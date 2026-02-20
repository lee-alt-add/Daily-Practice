import redis

# Connecting to redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Add users and their points
r.zadd("leaderboard", {"Alice": 100, "Bob": 250, "Charlie": 175})

top_users = r.zrevrange("leaderboard", 0, 1, True)
print("🏆 Top Users:")
for user, score in top_users:
    print(user.decode(), ":", int(score))

rank = r.zrevrank("leaderboard", "Alice")
print("Alice's Rank:", rank + 1)