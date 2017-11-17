import hashlib

def hash_function(guess):
    hash_object = hashlib.sha1(guess.encode('utf-8'))
    return hash_object.hexdigest()

def crack_hash(hash_to_crack):
    # Try to hash everything in our guess list
    for guess in ['trovador', 'trovad0r', 'Trovador', 'Trovad0r']:
        new_hash = hash_function(guess)
        # if the hashes match, we found it
        if new_hash == hash_to_crack:
            return guess
    # If none of them match, give up
    return None

if __name__ == '__main__':
    hash = 'dac56971fb41a0d8db599c6da220e7a0da933178'
    print('HASH: {0} -> VALOR: {1}'.format(hash, crack_hash(hash)))