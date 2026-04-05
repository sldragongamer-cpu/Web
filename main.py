from Website import create_app
from vercel_python_wsgi import handler

# Create the Flask app
app = create_app()

# Expose the handler for Vercel
handler = handler(app)

# Optional: local dev mode
if __name__ == '__main__':
    app.run(debug=True)
