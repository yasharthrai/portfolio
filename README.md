# Yasharth Rai — Portfolio (FastAPI)

A modern, full-stack Python portfolio built with **FastAPI** and **Jinja2** templating.

## Features

✨ **FastAPI Backend**
- Lightweight and fast Python web framework
- Data-driven content management
- RESTful API structure

🎨 **Dynamic Frontend**
- Fully responsive design
- Dark/light theme toggle
- Smooth scroll reveal animations
- 5-second loading animation with rotating captions
- Populated skill bars

📱 **Mobile-Optimized**
- Responsive grid layouts
- Touch-friendly navigation
- Adaptive typography

## Project Structure

```
.
├── app.py                 # FastAPI application with portfolio data
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Jinja2 template (all CSS & JS included)
└── README.md             # This file
```

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The portfolio will be available at: **`http://localhost:8000`**

## Environment Setup

### Using venv (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
```

### Using conda

```bash
conda create -n portfolio python=3.11
conda activate portfolio
pip install -r requirements.txt
python app.py
```

## API Endpoints

- **`GET /`** - Serves the portfolio homepage
- **`GET /health`** - Health check endpoint

## Customization

### Change Portfolio Content

Edit the `portfolio_data` dictionary in `app.py`:

```python
portfolio_data = {
    "name": "Your Name",
    "title": "Your Title",
    "location": "Your Location",
    # ... add more data
}
```

### Modify Styling

All CSS is embedded in `templates/index.html` within the `<style>` tag. You can:
- Adjust CSS variables (colors, spacing, fonts)
- Modify component styles
- Add new animations

### Update JavaScript

All JavaScript is in `templates/index.html` within the `<script>` tag. You can:
- Modify the theme toggle logic
- Enhance the experience switcher
- Add new interactive features

## Deployment

### Deploy to Render

```bash
# Add this to requirements.txt (already included)
# Connect your GitHub repo to Render
# Set Start Command: uvicorn app:app --host 0.0.0.0 --port 8000
```

### Deploy to Heroku

```bash
# Push to Heroku
git push heroku main
```

### Deploy to Railway

```bash
# Connect repo and Railway handles the rest
```

## Technologies

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Jinja2** - Template engine
- **HTML/CSS/JavaScript** - Frontend

## License

MIT - Free to use and modify

---

**Built with Python & FastAPI** 🚀
