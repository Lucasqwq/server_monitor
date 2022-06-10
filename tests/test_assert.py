import requests
def assert_test():
    r = requests.get("http://127.0.0.1:5001?a= &b=1")
    assert r.status_code==200
    
assert_test()
