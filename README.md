# SSH Web Console (Flask) — Vercel-ready example

**IMPORTANT SECURITY NOTICE:** This example demonstrates how to build a Flask web UI that accepts credentials and runs SSH commands on a remote host. **Do not** deploy this publicly without strong protections:
- Add authentication (OAuth / password + sessions)
- Use HTTPS (Vercel will provide HTTPS on deployment)
- Prefer SSH keys or vaults; do not accept plaintext passwords from users
- Add input sanitization and command whitelists
- Be aware of Vercel Function timeouts and bundle size limits

## Project structure
```
ssh-web-vercel/
├─ api/index.py         # Flask app (WSGI) served by Vercel
├─ templates/
│  ├─ index.html
│  └─ result.html
├─ requirements.txt
├─ vercel.json
└─ .gitignore
```

## Local testing
1. Create a virtualenv: `python -m venv .venv`
2. Activate it and install deps: `pip install -r requirements.txt`
3. Run locally: `python -m flask --app api/index.py run --port 5000`
4. Open: http://127.0.0.1:5000/

## Deploying to Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. `vercel login` and `vercel` in project root
3. Vercel will detect `vercel.json` and deploy the Python function.
