import requests

res = requests.post("http://localhost:9809/api/v1/execute/batch", json={
    "code": "echo \"test\""
})

print(res.json())