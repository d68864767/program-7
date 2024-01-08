import requests

class APIClient:
    def __init__(self, base_url: str):
        """
        Initialize the APIClient with the base URL for the API endpoints.

        :param base_url: The base URL for the API endpoints.
        """
        self.base_url = base_url

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
        Send a GET request to the specified API endpoint.

        :param endpoint: The API endpoint to send the GET request to.
        :param params: Optional parameters to include in the request.
        :return: The JSON response as a dictionary.
        """
        response = requests.get(url=f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict) -> dict:
        """
        Send a POST request to the specified API endpoint.

        :param endpoint: The API endpoint to send the POST request to.
        :param data: The data to include in the POST request.
        :return: The JSON response as a dictionary.
        """
        response = requests.post(url=f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict) -> dict:
        """
        Send a PUT request to the specified API endpoint.

        :param endpoint: The API endpoint to send the PUT request to.
        :param data: The data to include in the PUT request.
        :return: The JSON response as a dictionary.
        """
        response = requests.put(url=f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> dict:
        """
        Send a DELETE request to the specified API endpoint.

        :param endpoint: The API endpoint to send the DELETE request to.
        :return: The JSON response as a dictionary.
        """
        response = requests.delete(url=f"{self.base_url}/{endpoint}")
        response.raise_for_status()
        return response.json()
