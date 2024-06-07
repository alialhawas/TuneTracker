import redis

from src.config import redis_params



redis_pool = redis.ConnectionPool(**redis_params)

def get_redis_connection():
    """Get a Redis connection from the pool."""
    return redis.Redis(connection_pool=redis_pool)

def add_token(token_key, token_value, expiration=None):

    conn = get_redis_connection()
    conn.set(token_key, token_value, ex=expiration)

def get_token(token_key):

    conn = get_redis_connection()
    return conn.get(token_key)


add_token('access_token', 'your_token_value_here', expiration=1800) # 30 minutes (1800 seconds)

token = get_token('access_token')
if token:
    print(f"Retrieved token: {token.decode('utf-8')}")
else:
    print("Token not found")
