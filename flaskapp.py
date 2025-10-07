from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <!doctype html>
<html lang="en" class="bg-gray-900 text-gray-300 font-sans max-w-4xl mx-auto my-12 p-8 rounded-xl shadow-lg shadow-black/70">
<head>
  <meta charset="utf-8"/>
  <title>Deploy Flask Starter Kit on Azure VM</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-gray-300 selection:bg-blue-700 selection:text-gray-100">

  <header class="mb-8 text-center">
    <h1 class="text-4xl font-extrabold tracking-wide text-gray-100 drop-shadow-lg mb-1 border-b-4 border-blue-800 pb-2">Deploying the Flask Starter Kit on Azure VM</h1>
    <p class="text-blue-400 text-lg italic tracking-wide">There are many routes to get to Dublin. I took this route!</p>
  </header>

  <main class="flex flex-col md:flex-row gap-8 mb-12">

    <section class="flex-1 bg-gray-800 rounded-lg p-6 shadow-inner shadow-black/50 flex flex-col">
      <h2 class="text-xl font-semibold mb-4 border-b border-gray-700 pb-2 drop-shadow-sm">Azure VM Setup</h2>
      <ol class="list-decimal list-inside space-y-3 text-gray-400 text-base">
        <li>Sign in to the 
          <a href="https://portal.azure.com" target="_blank" class="text-blue-400 hover:text-blue-600 underline transition">Azure Portal</a> and start a new VM.</li>
        <li>Select Ubuntu or another Linux distribution.</li>
        <li>Create/assign a <b class="text-blue-400">Static</b> Public IP for consistent access.</li>
        <li>Add an inbound rule in Network Security Group for TCP port <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">5003</code>.</li>
      </ol>
    </section>

    <section class="flex-1 bg-gray-800 rounded-lg p-6 shadow-inner shadow-black/50 flex flex-col">
      <h2 class="text-xl font-semibold mb-4 border-b border-gray-700 pb-2 drop-shadow-sm">Deploy Flask Kit</h2>
      <ol class="list-decimal list-inside space-y-3 text-gray-400 text-base">
        <li><b>SSH</b> into VM: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">ssh user@public-ip</code></li>
        <li>Update system: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">sudo apt update -y</code></li>
        <li>Install Python venv: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">sudo apt install python3.12-venv -y</code></li>
        <li>Create/activate venv: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">python3 -m venv venv</code>, <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">source venv/bin/activate</code></li>
        <li>Clone repo:<br><code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">git clone https://github.com/hantswilliams/HHA-504-2025-FlaskStarter.git</code><br><code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">cd HHA-504-2025-FlaskStarter</code></li>
        <li>Install dependencies: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">pip3 install -r requirements.txt</code></li>
        <li>Run app: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">python3 app.py</code></li>
        <li>Access: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">http://&lt;Public-IP&gt;:5003</code></li>
      </ol>
    </section>

    <section class="flex-1 bg-gray-800 rounded-lg p-6 shadow-inner shadow-black/50 flex flex-col">
      <h2 class="text-xl font-semibold mb-4 border-b border-gray-700 pb-2 drop-shadow-sm">Management &amp; Security</h2>
      <ol class="list-decimal list-inside space-y-3 text-gray-400 text-base">
        <li>Deactivate Python env: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">deactivate</code></li>
        <li>Close SSH: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">exit</code>, verify: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">ps aux | grep ssh</code></li>
        <li>Remove unneeded files: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">rm -rf /path/to/files</code></li>
        <li>Clean SSH/private data:</li>
        <ul>
          <li><code class="bg-gray-700 px-1 rounded text-blue-400 font-mono text-sm">ls -al ~/.ssh/</code>, <code class="bg-gray-700 px-1 rounded text-blue-400 font-mono text-sm">rm -rf ~/.ssh/*</code>, <code class="bg-gray-700 px-1 rounded text-blue-400 font-mono text-sm">ssh-add -D</code></li>
        </ul>
          <li>Clear history: <code class="bg-gray-700 px-1 rounded text-blue-400 font-mono text-sm">history -c</code> (bash), <code class="bg-gray-700 px-1 rounded text-blue-400 font-mono text-sm">&gt; ~/.zsh_history</code> (zsh)</li>
        <li>Review logs: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">log show --predicate 'eventMessage contains "sshd"' --info</code></li>
        <li>Close terminal: <code class="bg-gray-700 px-1.5 rounded text-blue-400 font-mono text-sm">Ctrl+D</code></li>
      </ol>
    </section>

  </main>

  <section class="border-l-4 border-blue-700 pl-6 mb-12 text-gray-400 space-y-4 text-lg leading-relaxed">
    <h2 class="text-gray-200 text-2xl font-semibold drop-shadow">VM Management in Healthcare Informatics</h2>
    <p>
      In today’s US healthcare environment, setting up and managing virtual machines isn’t just a technical task—it’s about giving care teams the tools to handle sensitive data and keep up with ever-changing IT policies and regulations. The process can feel daunting, especially as organizations strive for interoperability across countless systems, with federal incentives pushing for better data exchange and privacy.
    </p>
    <p>
      Deploying apps in the cloud, like a Python Flask demo, highlights both the promise and realities of modern IT. While remote access, easy scaling, and automation are game changers, cost pressures and gaps in digital resources remain real hurdles—particularly for safety net providers and clinics serving marginalized populations. The right VM strategy can make it easier to stay compliant, keep expenses predictable, and tailor solutions for different communities.
    </p>
    <p>
      Navigating these issues means not just meeting technical standards, but also recognizing where IT can foster equity and where it may unintentionally widen the divide. That’s why a thoughtful approach to VM management can go a long way—helping teams deliver care more efficiently, protect patient information, and adapt quickly to new policy or technology shifts.
    </p>
  </section>

  <footer class="border-t border-gray-700 pt-4 text-center italic text-gray-500 text-sm max-w-4xl mx-auto">
    <small>This code was generated using a LLM, refined and tested through hands-on steps with Flask deployment.</small>
  </footer>
  <p class="text-center text-gray-600 text-xs mt-2 mb-8">Created by: Briggs Prashar</p>

  <p class="text-center text-gray-700 font-semibold uppercase tracking-widest mb-6 select-none">HHA 504</p>

</body>
</html>
    """

if __name__ == "__main__":
    # Run on all interfaces (so it's accessible via public IP), port 5003
    app.run(host="0.0.0.0", port=5003)