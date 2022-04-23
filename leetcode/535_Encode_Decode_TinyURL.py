# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

class Codec:

    def __init__(self):
        self.url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url[longUrl] = longUrl
        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url[shortUrl]



from hashlib import md5
class Codec:

    def __init__(self):
        self.url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_key = md5(longUrl.encode()).hexdigest()
        self.url[hash_key] = longUrl
        return hash_key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url[shortUrl]

from random import choice
class Codec:

    def __init__(self):
        self.secret = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.urls = {}

    def getKey(self) -> str:
        return ''.join(choice(self.secret) for i in range(6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.getKey()
        while key in self.urls:
            key = self.getKey()

        self.urls[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]