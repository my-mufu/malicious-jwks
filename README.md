Malicious JWKS Hosting for JWT jku Injection

This project hosts a malicious JSON Web Key Set (JWKS) at a public endpoint, intended for security testing of JWT `jku` header injection vulnerabilities.

Files:

- `.well-known/jwks.json`: The malicious JWKS file served at the public endpoint.

Deployment:

Host the `.well-known/jwks.json` file on a static site hosting service (e.g., GitHub Pages, Netlify) to make it accessible via HTTPS.

Disclaimer

This project is intended for educational and authorized security testing purposes only. Unauthorized use is prohibited.
