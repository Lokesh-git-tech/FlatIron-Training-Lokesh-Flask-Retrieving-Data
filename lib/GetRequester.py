import requests
import json
from flask import Flask, jsonify

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            # 1. Make the HTTP GET request using the requests library
            response = requests.get(self.url)
            
            # 2. Raise an exception for 4xx or 5xx HTTP status codes
            response.raise_for_status()
            
            # --- METHODS FOR GETTING THE RESPONSE BODY ---
            
            # Method A: Extract as parsed JSON (Returns a dict or list)
            response_body_json = response.content
            return response_body_json
        except requests.exceptions.RequestException as e:
            response_body_json['status'] = 'error'
            response_body_json['message'] = str(e)
            return response_body_json

    def load_json(self):
        response_body = json.loads(self.get_response_body())
        return response_body