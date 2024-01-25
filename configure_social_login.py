import requests
import json

# This is just a template for future reference 
# The variables should be modified with actual configuration data

# Define Configuration Data
erpnext_api_url = 'http://your-erpnext-instance/api/resource/Social Login Key'
erpnext_api_key = 'your-erpnext-api-key'

keycloak_client_id = 'your-keycloak-client-id'
keycloak_client_secret = 'your-keycloak-client-secret'
keycloak_auth_url = 'https://your-keycloak-instance/auth/realms/your-realm/protocol/openid-connect/auth'
keycloak_token_url = 'https://your-keycloak-instance/auth/realms/your-realm/protocol/openid-connect/token'
keycloak_redirect_url = 'http://your-erpnext-instance/login'

# Prepare ERPNext API Data

social_login_data = {
    "doctype": "Social Login Key",
    "provider_name": "Keycloak",
    "client_id": keycloak_client_id,
    "client_secret": keycloak_client_secret,
    "auth_url": keycloak_auth_url,
    "token_url": keycloak_token_url,
    "redirect_url": keycloak_redirect_url
}

# Make API Call to ERPNext:

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + erpnext_api_key
}

response = requests.post(erpnext_api_url, data=json.dumps(social_login_data), headers=headers)

if response.status_code == 200:
    print("Social login configuration added successfully.")
else:
    print("Error: Unable to add social login configuration.")
