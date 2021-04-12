import requests

res = requests.post("http://localhost:9809/api/v1/execute/python", json={
    "code": open("./manual_tests/test_execute.py").read()
})

print(res.json())