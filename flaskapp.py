from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Deploy Flask Starter Kit on Azure VM - Sophisticated Grey</title>
  <style>
    /* Sophisticated Minimalistic Grey Theme:
       Dark grey background with subtle gradients, muted text,
       elegant typography and spacious layout for professional look */

    body {
      background-color: #2f3237; /* Soft dark grey */
      color: #b0b3b8; /* Muted light grey for text */
      font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      max-width: 900px;
      margin: 60px auto;
      padding: 36px 48px;
      line-height: 1.7;
      border-radius: 10px;
      box-shadow:
        0 1px 4px rgba(0,0,0,0.3),
        inset 0 0 50px #3a3f47;
      user-select: text;
      background-image: linear-gradient(135deg, #31353b 25%, #2e3035 75%);
    }

    h1, h2, h3 {
      font-weight: 700;
      margin-top: 2.8em;
      margin-bottom: 0.6em;
      color: #a0a4b0;
      letter-spacing: 0.05em;
      user-select: text;
    }
    h1 {
      font-size: 3.2em;
      border-bottom: 3px solid #494e57;
      padding-bottom: 0.3em;
      letter-spacing: 0.1em;
      text-shadow: 0 0 4px #4b5361;
    }
    h2 {
      font-size: 1.9em;
      border-bottom: 1.3px solid #444950;
      padding-bottom: 0.2em;
      text-shadow: 0 0 2px #394048;
    }

    p {
      font-size: 1.15em;
      margin: 1.2em 0;
      color: #a8abb0;
      max-width: 720px;
      user-select: text;
      text-shadow: 0 0 1px #262a2f;
    }

    ol {
      margin-left: 1.6em;
      margin-bottom: 2em;
      font-size: 1.1em;
      color: #a8abb0;
      user-select: text;
    }
    li {
      margin: 0.6em 0;
      line-height: 1.5;
    }

    code {
      background-color: #3d4149;
      padding: 0.3em 0.6em;
      border-radius: 6px;
      font-family: 'Fira Mono', Consolas, Monaco, monospace;
      font-size: 0.95em;
      color: #7db9e8;
      user-select: text;
      box-shadow:
        inset 0 0 8px #2a2e35;
    }

    a {
      color: #7db9e8;
      text-decoration: none;
      transition: color 0.3s ease;
      user-select: text;
    }
    a:hover {
      color: #a8c9f8;
      text-decoration: underline;
    }

    hr {
      border: none;
      border-top: 1px solid #484f59;
      margin: 3.8em 0;
      user-select: none;
      box-shadow: inset 0 0 10px #2a2e34;
    }

    .narrative {
      padding-left: 1.5em;
      border-left: 4px solid #7db9e8;
      margin-top: 3.8em;
      color: #bbbfc5;
      font-style: normal;
      font-size: 1.13em;
      line-height: 1.6;
      user-select: text;
      text-shadow: 0 0 2px #2c323a;
    }
  </style>
</head>
<body>

<h1>Deploying the Flask Starter Kit on Azure VM</h1>

<h2>Step 1: Create an Azure Virtual Machine (VM)</h2>
<ol>
  <li>Sign in to the <a href="https://portal.azure.com" target="_blank" rel="noopener">Azure Portal</a> and start a new VM creation.</li>
  <li>Choose Ubuntu or preferred Linux distribution and select required resources.</li>
</ol>

<h2>Step 2: Create a Public IP Address</h2>
<ol>
  <li>During VM setup, create or specify a Public IP address.</li>
  <li>Set IP allocation as <code>Static</code> to maintain a consistent address.</li>
</ol>

<h2>Step 3: Configure Port 5003 for Flask Application</h2>
<ol>
  <li>In the VM’s Network Security Group (NSG), add an inbound rule.</li>
  <li>Allow TCP traffic on port <code>5003</code> to enable external access.</li>
</ol>

<hr />

<h2>Step 4: Deploy Flask Starter Kit from Mac Terminal</h2>
For a Windows terminal the commands and process will be different.
<ol>
  <li>
    <strong>Connect to your VM via SSH:</strong><br />
    <code>ssh user@public-ip-address</code><br />
    Confirm your location with <code>pwd</code>.
  </li>
  <li>
    <strong>Update your system packages:</strong><br />
    <code>sudo apt update -y</code> (may take a moment)
  </li>
  <li>
    <strong>Check Python version and install virtual environment support:</strong><br />
    <code>python3 --version</code><br />
    <code>sudo apt install python3.12-venv -y</code>
  </li>
  <li>
    <strong>Create and activate a virtual environment:</strong><br />
    <code>python3 -m venv venv</code><br />
    <code>source venv/bin/activate</code> (your prompt will show <code>(venv)</code>)
  </li>
  <li>
    <strong>Clone the Flask Starter Kit repository:</strong><br />
    <code>git clone "GITHUB REPO URL"</code><br />
    <code>cd (VM Folder representing the github repo) </code>
  </li>
  <li>
    <strong>Install required dependencies:</strong><br />
    <code>pip install -r requirements.txt</code>
  </li>
  <li>
    <strong>Run the Flask application:</strong><br />
    <code>python3 app.py</code>
  </li>
  <li>
    <strong>Open a browser and navigate to:</strong><br />
    <code>http://&lt;Public-IP&gt;:5003</code>
  </li>
  <li>
    <strong>When finished, deactivate and disconnect:</strong><br />
    <code>deactivate</code> to exit the Python environment<br />
    <code>exit</code> to close the SSH session.
  </li>
  <li>
    <strong>Verify active SSH connections:</strong><br />
    <code>ps aux | grep ssh</code>
  </li>
  <li>
    <strong>Optional cleanup steps:</strong><br />
    Remove unneeded files:<br />
    <code>rm -rf /path/to/files</code>
  </li>
  <li>
    <strong>Remove SSH artifacts from local machine:</strong>
    <ul>
      <li><code>ls -al ~/.ssh/</code></li>
      <li><code>rm -rf ~/.ssh/*</code></li>
      <li><code>ssh-add -D</code></li>
      <li>Clear terminal history:<br /><code>history -c</code> (bash) or<br /><code>&gt; ~/.zsh_history</code> (zsh)</li>
    </ul>
  </li>
  <li>
    <strong>Review logs and restart terminal as needed:</strong><br />
    <code>log show --predicate 'eventMessage contains "sshd"' --info</code> (Ctrl+C to stop)
  </li>
  <li>
    <strong>Close terminal session:</strong><br />
    Press <code>Ctrl+D</code> then close the terminal window.
  </li>
</ol>

<hr />

<div class="narrative">
  <h2>VM Management in Health Informatics</h2>
  <p>
    Virtual Machines provide the backbone of scalable and secure infrastructure vital to health informatics — enabling sensitive data processing, collaborative development, and rapid deployment of healthcare solutions.
  </p>
  <p>
    This exercise exemplifies the seamless integration of cloud VM provisioning, secure remote access from Apple devices, and version-controlled deployment using Python Flask applications. By mastering these workflows, health informatics professionals can ensure compliance, agility, and precision in managing healthcare IT ecosystems.
  </p>
  <p>
    Effective VM management can foster help with better decision making to accelerate innovation and dependable delivery of health services even when many extraneous variables play a deciding role.
</div>

<footer>
  <small>The original HTML code was generated using a LLM after multiple prompting and after adding my own steps listed after various iterations of the whole Flask Starter demo process. The final HTML code was edited and tweaked.</small>
</footer>

</body>
</html>
    """

if __name__ == "__main__":
    # Run on all interfaces (so it's accessible via public IP), port 5003
    app.run(host="0.0.0.0", port=5003)