import requests

from app import configuration


def call_room_driver(endpoint):
    port = configuration.config.ROOM_DRIVER_PORT
    host = configuration.config.ROOM_DRIVER_HOST
    url = f'http://{host}:{port}/api/{endpoint}'

    # Perform the GET request
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the content of the response
        data = response.text  # if the response is JSON formatted
    else:
        print(f"Request failed with status code: {response.status_code}")

    # Optionally, to view the entire response content as text
    return response.text


def call_room_driver_command(endpoint, command):
    port = configuration.config.ROOM_DRIVER_PORT
    host = configuration.config.ROOM_DRIVER_HOST
    url = f'http://{host}:{port}/api/{endpoint}'

    # Perform the POST request
    response = requests.post(url, json=command)  # or use 'data=payload' for form-encoded data

    # Check if the request was successful
    if response.status_code == 200 or response.status_code == 201:
        # Parse the response, assuming it comes back as JSON
        data = response.content
    else:
        print(f"Request failed with status code: {response.status_code}")

    # To view the raw text response
    print(response.text)
