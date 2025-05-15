# fake_jwks_server.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/.well-known/jwks.json")
def jwks():
    return jsonify({
        "keys": [
            {
                "kty": "RSA",
                "use": "sig",
                "alg": "RS256",
                "kid": "1337",
                "n": "REPLACE_WITH_BASE64URL_MODULUS",
                "e": "AQAB"
            }
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=("cert.pem", "key.pem"))
