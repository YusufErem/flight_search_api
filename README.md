<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Flight Search API</h1>
    <h3>A powerful backend API for a flight search application, built with Django REST framework.</h3>
    <h2>📖 Overview</h2>
    <p>The <strong>Flight Search API</strong> is designed to manage and query flight data efficiently. Using Django REST framework, it supports CRUD operations for flights and airports, offers secure authentication, and includes scheduled tasks and Swagger documentation for ease of use.</p>
    <h2>🚀 Features</h2>
    <ul>
        <li><strong>Data Modeling</strong>: Structured database for flights and airports.</li>
        <li><strong>CRUD Operations</strong>: Full Create, Read, Update, and Delete functionalities.</li>
        <li><strong>Search API</strong>: Search flights with custom criteria.</li>
        <li><strong>Authentication</strong>: Secure access to endpoints.</li>
        <li><strong>Scheduled Jobs</strong>: Fetches data daily from a third-party mock API using Redis.</li>
        <li><strong>API Documentation</strong>: Easily accessible via Swagger.</li>
        <li><strong>Version Control</strong>: Managed with Git and hosted on GitHub.</li>
    </ul>
    <h2>🛠️ Installation Guide</h2>
    <h3>1. Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/flight-search-api.git
cd flight-search-api</code></pre>
    <h3>2. Set Up a Virtual Environment and Install Dependencies</h3>
    <p><strong>Linux/MacOS</strong>:</p>
    <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
    <p><strong>Windows</strong>:</p>
    <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
    <p>Then, install the required dependencies:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h3>3. Configure PostgreSQL Database</h3>
    <p>Set up a PostgreSQL database with the following steps:</p>
    <ol>
        <li><strong>Access PostgreSQL</strong>:
            <ul>
                <li><strong>Linux</strong>: <pre><code>sudo -u postgres psql</code></pre></li>
                <li><strong>Windows</strong>: Open the PostgreSQL Command Line Client.</li>
            </ul>
        </li>
        <li><strong>Create the Database and User</strong>:
            <pre><code>CREATE DATABASE flightsearch;
CREATE USER yourusername WITH PASSWORD 'yourpassword';
ALTER ROLE yourusername SET client_encoding TO 'utf8';
ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
ALTER ROLE yourusername SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE flightsearch TO yourusername;</code></pre>
        </li>
        <li><strong>Exit</strong> PostgreSQL with <code>\q</code> on Linux or by closing the Command Line Client on Windows.</li>
    </ol>
    <h3>4. Configure Database Settings in Django</h3>
    <p>Instead of using a <code>.env</code> file, configure your database directly in Django’s <code>settings.py</code> file. Locate the <code>DATABASES</code> section and modify it as follows:</p>
    <pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flightsearch',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}</code></pre>
    <h3>5. Run Database Migrations</h3>
    <p>Apply migrations to set up the database structure:</p>
    <pre><code>python manage.py migrate</code></pre>
    <h3>6. Start the Development Server</h3>
    <p>Start the Django development server:</p>
    <pre><code>python manage.py runserver</code></pre>
    <h3>7. (Optional) Redis Setup for Scheduled Jobs</h3>
    <p>For scheduled tasks, Redis should be set up and running:</p>
    <ul>
        <li><strong>Linux</strong>: Install Redis with: <pre><code>sudo apt-get install redis-server</code></pre></li>
        <li><strong>Windows</strong>: Download and install Redis from <a href="https://github.com/tporadowski/redis/releases">Redis for Windows</a>.</li>
    </ul>
    <p>After installing, start the Redis server to enable scheduled tasks.</p>
    <h2>📄 API Documentation</h2>
    <p>API documentation is accessible via Swagger. Once the server is running, go to <code>/swagger/</code> in your browser for detailed documentation on each endpoint.</p>
    <h2>🤝 Contributing</h2>
    <p>Contributions are welcome!</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch: <code>git checkout -b feature/your-feature-name</code>.</li>
        <li>Commit your changes: <code>git commit -m 'Add some feature'</code>.</li>
        <li>Push to the branch: <code>git push origin feature/your-feature-name</code>.</li>
        <li>Submit a pull request.</li>
    </ol>
    <p>Happy Coding! 🚀</p>
</body>
</html>
