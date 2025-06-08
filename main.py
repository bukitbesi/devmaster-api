from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "devmaster_2025_ismal_secure_4x"

def is_authorized(req):
    auth = request.headers.get("Authorization", "")
    return auth == f"Bearer {API_KEY}"

@app.route("/devmaster/format", methods=["POST"])
def format_code():
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401
    code = request.json.get("code", "")
    formatted = code.replace("{", "{\n  ").replace("}", "\n}").replace(";", ";\n")
    return jsonify({"formattedCode": formatted.strip()})

@app.route("/devmaster/explain", methods=["POST"])
def explain_code():
    if not is_authorized(request):
        return jsonify({"error": "Unauthorized"}), 401
    code = request.json.get("code", "")
    return jsonify({
        "explanation": f"This is a simulated explanation of your code:\n{code[:60]}..."
    })

@app.route("/", methods=["GET"])
def home():
    return "✅ DevMaster API is live. Use Authorization: Bearer {your_key}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
