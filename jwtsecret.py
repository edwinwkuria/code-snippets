import jwt

found_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQxMjYwMzIwMDAsImlhdCI6MTY4MTY4ODk3MX0.9CACKOa5eluGdPeOL1z-mLv5l14qzgpS2N4eSbhis-M"
i = 10000000
while i >= 0:
    encoded_jwt = jwt.encode({"exp": 4126032000,"iat": 1681688971}, str(i) , algorithm="HS256")
    if encoded_jwt == found_token:
        print(i)
    i -= 1
print(jwt.decode(encoded_jwt, i, algorithms=["HS256"]))