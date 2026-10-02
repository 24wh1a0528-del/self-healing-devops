"""
Self-Healing DevOps Platform - Flask Application
Phase 1: Basic Flask app with health check endpoint
"""

from flask import Flask, jsonify

# Create the Flask application instance
app = Flask(__name__)

# Application metadata
APP_NAME = "Self-Healing DevOps Platform"
APP_VERSION = "1.0.0"


@app.route("/")
def home():
    """Home page - displays application name and version."""
    return f"""
    <html>
        <head>
            <title>{APP_NAME}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f4f8;
                }}
                .card {{
                    background: white;
                    padding: 40px 60px;
                    border-radius: 12px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h1 {{ color: #2d3748; }}
                .version {{
                    color: #718096;
                    font-size: 1.1rem;
                    margin-top: 8px;
                }}
                .status {{
                    margin-top: 20px;
                    padding: 8px 16px;
                    background-color: #c6f6d5;
                    color: #276749;
                    border-radius: 6px;
                    display: inline-block;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>{APP_NAME}</h1>
                <p class="version">Version: {APP_VERSION}</p>
                <span class="status">&#10003; Running</span>
            </div>
        </body>
    </html>
    """


@app.route("/health")
def health():
    """Health check endpoint - used by Docker and Kubernetes to verify the app is alive."""
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    # Run the app on all network interfaces (0.0.0.0) so Docker can reach it
    app.run(host="0.0.0.0", port=5000, debug=False)
