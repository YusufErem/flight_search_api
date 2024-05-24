<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Flight Search API</h1>
    <h2>Overview</h2>
    <p>This is a backend API for a flight search application, developed using Django REST framework.</p>
    <h2>Features</h2>
    <ul>
        <li>Data Modeling: Relational database structure for storing flight and airport information.</li>
        <li>CRUD Operations: Create, Read, Update, Delete operations for managing flights and airports.</li>
        <li>Search API: Endpoints for searching flights based on specific criteria.</li>
        <li class="not-done">Authentication: User authentication for secure access. (Not Done)</li>
        <li class="not-done">Scheduled Jobs: Daily tasks to fetch flight information from a mock third-party API. (Not Done)</li>
        <li class="not-done">API Documentation: Detailed API documentation using Swagger. (Not Done)</li>
        <li>Version Control: Project managed using Git and hosted on GitHub.</li>
    </ul>
    <h2>Installation</h2>
    <h3>Clone the repository:</h3>
    <pre><code>git clone https://github.com/yourusername/flight-search-api.git
cd flight-search-api</code></pre>
    <h3>Create a virtual environment and install dependencies:</h3>
    <pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt</code></pre>
    <h3>Install additional dependencies:</h3>
    <pre><code>sudo apt-get install libpq-dev python3-dev</code></pre>
    <h3>Configure PostgreSQL database:</h3>
    <pre><code>sudo -u postgres psql
CREATE DATABASE flightsearch;
CREATE USER flightsearchuser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE flightsearch TO flightsearchuser;
</code></pre>
    <h3>Set up environment variables for database configuration in your <code>.env</code> file:</h3>
    <pre><code>DATABASE_NAME=flightsearch
DATABASE_USER=flightsearchuser
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432</code></pre>
    <h3>Run database migrations:</h3>
    <pre><code>python manage.py migrate</code></pre>
    <h3>Start the development server:</h3>
    <pre><code>python manage.py runserver</code></pre>
</body>
</html>
