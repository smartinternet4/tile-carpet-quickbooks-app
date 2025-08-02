import os
from flask import Flask, request, jsonify, redirect
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Tile and Carpet Solutions - QuickBooks Integration</h1>
    <p>QuickBooks OAuth callback handler is running.</p>
    <p>Status: Ready for authorization callbacks</p>
    """

@app.route("/callback")
def oauth_callback():
    """Handle QuickBooks OAuth callback"""
    
    # Get authorization code and realm ID from callback
    auth_code = request.args.get('code')
    realm_id = request.args.get('realmId')
    state = request.args.get('state')
    error = request.args.get('error')
    
    if error:
        return f"""
        <h1>Authorization Error</h1>
        <p>Error: {error}</p>
        <p>Description: {request.args.get('error_description', 'Unknown error')}</p>
        <a href="/">Back to Home</a>
        """
    
    if not auth_code or not realm_id:
        return """
        <h1>Missing Authorization Data</h1>
        <p>Authorization code or company ID is missing.</p>
        <a href="/">Back to Home</a>
        """
    
    return f"""
    <h1>QuickBooks Authorization Successful!</h1>
    <div style="background: #f0f0f0; padding: 20px; margin: 20px; border-radius: 5px;">
        <h3>Authorization Details:</h3>
        <p><strong>Authorization Code:</strong> {auth_code}</p>
        <p><strong>Company ID (Realm ID):</strong> {realm_id}</p>
        <p><strong>State:</strong> {state}</p>
    </div>
    
    <h3>Next Steps:</h3>
    <ol>
        <li><strong>Copy the Authorization Code above</strong></li>
        <li><strong>Go back to Lutra</strong></li>
        <li><strong>Provide the code to exchange for tokens</strong></li>
    </ol>
    
    <div style="background: #e8f5e8; padding: 15px; margin: 20px; border-radius: 5px;">
        <h4>Copy this information to Lutra:</h4>
        <p><code>Authorization Code: {auth_code}</code></p>
        <p><code>Company ID: {realm_id}</code></p>
    </div>
    """

@app.route("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "quickbooks-oauth-handler"}

@app.route("/test")
def test_endpoint():
    """Test endpoint to verify app is working"""
    return {
        "message": "Railway app is working!",
        "callback_url": "/callback",
        "ready_for_oauth": True
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
