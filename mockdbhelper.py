MOCK_USERS = [{"email": "test@example.com", "salt": "pLlgTRYlE11EGGhuofj/ZJqU/CQ=",
              "hashed": "4a2ae72127911c2842b1b1f4835c0a6567b18f7f4e1d62bdb7f84953d4f068476d1048fcf0758a9243db7e2c29c69e"
                        "47788572b3e1ffd3a10dcf3bdb6303aaff"}]


class MockDBHelper:
    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email": email, "salt": salt, "hashed": hashed})
