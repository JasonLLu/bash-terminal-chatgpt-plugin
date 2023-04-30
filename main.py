import json
import subprocess

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/bash")
async def execute_bash():
    request_data = await quart.request.get_json(force=True)
    command = request_data.get("command")
    if not command:
        return quart.Response(response='Command not provided', status=400)
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return quart.Response(response=result, status=200)
    except subprocess.CalledProcessError as e:
        return quart.Response(response=e.output, status=400)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
