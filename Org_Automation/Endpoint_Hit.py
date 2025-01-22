import requests

def hit_endpoint(url):
    try:
        # Send GET request to the API
        data = requests.get(url)

        # Check if the response was successful (HTTP status code 200)
        if data.status_code == 200:
            try:
                # Try to parse the response as JSON
                json_data = data.json()
                print(json_data)  # Print the JSON response
            except ValueError as e:
                # If JSON parsing fails, print the error and response text
                print(f"Error decoding JSON: {e}")
                print(f"Raw response text: {data.text}")  # Print the raw response
        else:
            print(f"Failed to retrieve data. Status code: {data.status_code}")
            print(f"Response text: {data.text}")

    except requests.exceptions.RequestException as e:
        # Catch any request errors (like network issues)
        print(f"Request failed: {e}")

# Example API endpoint
hit_endpoint("https://api.publicapis.org/entries")
