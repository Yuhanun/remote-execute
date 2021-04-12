import io
import traceback
import subprocess
import contextlib

from flask import Flask, request

app = Flask(__name__)


@app.route("/api/v1/execute/batch", methods=["POST"])
def execute_batch():
    json_data = request.json
    if json_data is None:
        return {
            "error": "We expect json with a `code` argument"
        }

    if 'code' not in json_data:
        return {
            "error": "`code` was not present as JSON argument"
        }

    code = json_data['code']
    res = None
    try:
        res = subprocess.check_output(code, shell=True)
    except Exception as e:
        return {
            "error": str(e)
        }
    return {
        "output": res.decode()
    }


@app.route("/api/v1/execute/python", methods=["POST"])
def execute_python():
    json_data = request.json
    if json_data is None:
        return {
            "error": "We expect json with a `code` argument"
        }

    if 'code' not in json_data:
        return {
            "error": "`code` was not present as JSON argument"
        }

    code = json_data['code']
    print(code)
    stdout = io.StringIO()
    ret = None
    try:
        with contextlib.redirect_stdout(stdout):
            ret = exec(code)
    except Exception as e:
        value = stdout.getvalue()
        return {
            "output": value,
            "exception": traceback.format_exc(),
            "return": ret,
        }
    else:
        value = stdout.getvalue()
        return {
            "output": value,
            "return": ret
        }


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9809)
