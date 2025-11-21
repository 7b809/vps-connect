from flask import Flask, render_template, request
import paramiko
import os

# When running on Vercel, set template_folder one level up
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def run_command():
    server_ip = request.form.get("server_ip", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    command = request.form.get("command", "").strip()

    # Basic input validation
    if not server_ip or not username or not command:
        return render_template("result.html", error="server_ip, username and command are required", output="")

    # SECURITY WARNING:
    # This endpoint will attempt to SSH to the provided host using supplied credentials and run the command.
    # Deploying this publicly is dangerous. Restrict access, use HTTPS, authentication, and prefer SSH keys.
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password, timeout=10)

        stdin, stdout, stderr = ssh.exec_command(command, timeout=20)
        out = stdout.read().decode(errors="replace")
        err = stderr.read().decode(errors="replace")
        ssh.close()

        return render_template("result.html", output=out, error=err)
    except Exception as e:
        return render_template("result.html", error=str(e), output="")

# Health check for Vercel
@app.route("/api/health", methods=["GET"])
def health():
    return "OK", 200
