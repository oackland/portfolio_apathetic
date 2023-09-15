from flask import Flask, request, jsonify, render_template
import requests
from . import api


PACKAGES = [
    "prettier",
    "react-router-dom",
    "axios",
    "classnames",
    "formik",
    "bootstrap",
]

BASE_URL = "https://portfolio.apathetic.app"


@api.route("/install-packages", methods=["POST"])
def install_packages():
    requested_packages = request.json
    if not set(requested_packages).issubset(set(PACKAGES)):
        return jsonify({"error": "Invalid package requested"}), 400

    # Placeholder for the package installation logic.
    # For now, just a mock response.
    return jsonify({"message": "Packages installed successfully"})


@api.route("/available", methods=["GET"])
def available_packages():
    # Common data for curl command
    data = '["prettier", "axios"]'
    headers = '-H "Content-Type: application/json"'

    curl_command = (
        f"curl -X POST {headers} -d \\'{data}\\' {BASE_URL}/api/install-packages"
    )

    # Raw HTTP request:
    http = f"""POST /api/install-packages HTTP/1.1
Host: {BASE_URL}
Content-Type: application/json
Content-Length: {len(data)}

{data}
"""

    # Postman instructions:
    postman = f"""1. Set request type to POST.
2. Enter URL: {BASE_URL}/api/install-packages
3. Go to Headers:
   - Key: Content-Type | Value: application/json
4. Go to Body, select 'raw' and 'JSON (application/json)':
   - Enter: {data}
5. Hit Send.
"""

    # Windows PowerShell:
    powershell = f'curl -Method Post -Headers @{{ "Content-Type" = "application/json" }} -Body \'{data}\' -Uri {BASE_URL}/api/install-packages'

    # OpenAPI (simplified snippet):
    openapi = f"""{{
  "paths": {{
    "/api/install-packages": {{
      "post": {{
        "summary": "Install packages",
        "consumes": ["application/json"],
        "parameters": [
          {{
            "in": "body",
            "name": "packages",
            "description": "List of packages to install",
            "required": true,
            "schema": {{
              "type": "array",
              "items": {{ "type": "string" }}
            }}
          }}
        ],
        "responses": {{
          "200": {{
            "description": "Packages installed successfully"
          }}
        }}
      }}
    }}
  }}
}}
"""

    response = {
        "curl": curl_command,
        "http": http,
        "postman": postman,
        "powershell": powershell,
        "openapi": openapi,
        "package": PACKAGES,
    }

    return jsonify(response)


@api.route('/git')
def gitpage():
    return render_template('project_github.html')