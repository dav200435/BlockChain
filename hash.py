import hashlib

class Hash:
    @staticmethod
    def convHash(data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        hash_result = sha256_hash.hexdigest()
        return hash_result
