import base64

message = "aGkgYnJv"
#message=base64.b64encode(message.encode("ascii")).decode("ascii")
print(base64.b64decode(message).decode("ascii"))