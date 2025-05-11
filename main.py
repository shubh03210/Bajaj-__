
import requests

def generate_webhook():
    init_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

    registration_data = {
        "name": "Shubham Kushwaha",
        "regNo": "0827AL221127",
        "email": "shubhamkushwaha220788@acropolis.in"
    }

    webhook_response = requests.post(init_url, json=registration_data)

    if webhook_response.status_code == 200:
        response_info = webhook_response.json()
        url_result = response_info.get('webhook')
        token_result = response_info.get('accessToken') 

        if url_result and token_result:
            print("Generated Webhook URL:", url_result)
            print("Generated Auth Token:", token_result)
        else:
            print("Error: Missing webhook URL or token in response.")
        return url_result, token_result
    else:
        print(f"Error: Status code {webhook_response.status_code}")
        print("Response message:", webhook_response.text)
        return None, None

url_from_api, token_from_api = generate_webhook()
