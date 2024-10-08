# backend/app.py
from flask import Flask, request, jsonify
import yaml
import random
import string

app = Flask(__name__)

# Load configuration from config.yaml
with open("../config/config.yaml") as config_file:
    config = yaml.safe_load(config_file)

url_mapping = {}

def generate_short_url(length=6):
    """Generate a random short URL key."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Shorten a given URL."""
    data = request.json
    long_url = data.get('longUrl')
    
    if not long_url:
        return jsonify({"error": "No URL provided."}), 400
    
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return jsonify({"shortUrl": f"{config['base_url']}/{short_url}"}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    """Redirect to the original URL."""
    long_url = url_mapping.get(short_url)
    
    if long_url:
        return jsonify({"longUrl": long_url}), 302
    return jsonify({"error": "URL not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config['port'])
