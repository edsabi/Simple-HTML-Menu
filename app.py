from flask import Flask, send_file

app = Flask(__name__)

# Replace 'your_html_file_path.html' with the path to your HTML file
html_file_path = 'templates/menu_with_qr_placeholder.html'

@app.route('/')
def serve_menu():
    return send_file(html_file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50050)
