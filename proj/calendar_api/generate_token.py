# Generate a token
import uuid

def generate_token():
    return str(uuid.uuid4())

TOKEN = generate_token()
print(TOKEN)
