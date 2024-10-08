 Project Overview

TinyURLz is a simple yet powerful URL shortening service that converts long URLs into short, shareable links. Whether you're looking to reduce the length of URLs for social media, emails, or other digital platforms, TinyURLz makes it easy to generate compact URLs while maintaining functionality.

Key Features

Shorten long URLs into concise, easy-to-share links.
Track click statistics for each shortened URL.
URL expiry for managing the lifespan of links.
User-friendly interface for quick URL generation.

Technologies Used

Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Database: MongoDB (for storing original and shortened URLs)
Cache: Redis (optional for speeding up the lookup of shortened URLs)
Other Technologies:
Bootstrap for styling
Docker for containerization

Project Architecture

User Interface: Users submit a long URL to be shortened.

Backend: The Flask application processes the request, checks if the URL has already been shortened, and if not, generates a unique short URL.

Database: MongoDB stores the long URLs and their corresponding shortened versions.

Cache (optional): Redis stores frequently accessed URLs to speed up the redirection process.
