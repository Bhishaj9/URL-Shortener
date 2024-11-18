# URL Shortener

A simple, lightweight URL shortener built with Python and Flask. This web application allows users to create shortened versions of long URLs, making them easier to share and manage.

## Features

- Shorten any valid URL
- Automatic random code generation
- Persistent storage using SQLite database
- Clean and responsive web interface
- Instant redirection to original URLs

## Requirements

- Python 3.6 or higher
- Flask

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
```

3. Activate the virtual environment
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS and Linux:
```bash
source venv/bin/activate
```

4. Install required packages
```bash
pip install flask
```

## Project Structure

```
url_shortener/
    ├── app.py                 # Main application file
    ├── urls.db               # SQLite database (auto-generated)
    ├── requirements.txt      # Project dependencies
    └── templates/
        └── index.html        # HTML template
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter a URL you want to shorten and click "Shorten URL"

4. Copy and share your shortened URL

## How It Works

1. When a user submits a URL, the application generates a unique short code
2. The original URL and its short code are stored in the SQLite database
3. Users can access the original URL by visiting the shortened URL
4. The application automatically redirects to the original URL

## Database Schema

The application uses a simple SQLite database with the following schema:

```sql
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_code TEXT NOT NULL UNIQUE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Future Improvements

- [ ] Add URL validation
- [ ] Implement custom short codes
- [ ] Add visit tracking
- [ ] Create API endpoints
- [ ] Add user authentication
- [ ] Implement rate limiting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Styled with CSS
- Uses SQLite for database management

## Author

Your Name
- GitHub: Bhishaj09 - Gaurav vashistha(https://github.com/Bhishaj09)
- Email: gaurav.vashistha09@gmail.com
