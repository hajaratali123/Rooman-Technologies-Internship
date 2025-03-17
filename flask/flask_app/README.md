# Flask Application

A basic Flask web application with SQLAlchemy integration.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix or MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the application:
```bash
python app.py
```
3. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
flask_app/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── static/            # Static files (CSS, JS, images)
│   └── css/
│       └── style.css
├── templates/         # HTML templates
│   └── home.html
└── README.md         # Project documentation
``` 