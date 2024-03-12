
services = {
    "http_client": None,
    "authorization": "1",
}

test1 = all(services.values())

services.update({"http_client": "test", "authorization": "test"})
test2 = all(services.values())
print("")