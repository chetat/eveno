import jwt
import base64


payload ={'school': 'udacity'}
algo = 'HS256'
secret = 'learning'

encode = jwt.encode(payload, secret, algorithm=algo)

print(encode)

"""n = int(input("Enter a number "))
    result = 0
    while(n != 0):
        result = result + n % 10
        n = n/10

    print(int(result))"""