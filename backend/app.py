from flask import Flask, request, jsonify, render_template, redirect
import hashlib

app = Flask(__name__)

# Simulating a database with a dictionary for now
url_database = {}

# Homepage route (rendering the frontend)
@app.route('/')
def index():
    return render_template('index.html')

# URL shortening route
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('longUrl')
    
    # Create a hash of the long URL
    short_url = hashlib.md5(long_url.encode()).hexdigest()[:6]
    
    # Store the mapping in the dictionary
    url_database[short_url] = long_url
    
    return jsonify({'short_url': short_url})

# Redirect to long URL when short URL is visited
@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
