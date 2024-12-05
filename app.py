from flask import Flask, render_template

app = Flask(__name__)

# قائمة المنتجات
products = [
    {
        'name': 'ساعة ذكية',
        'image': 'https://example.com/smartwatch.jpg',
        'price': '50 دولار',
        'link': 'https://s.click.aliexpress.com/e/_d6sj56y'  # رابط تابع صحيح
    },
    {
        'name': 'سماعات بلوتوث',
        'image': 'https://example.com/bluetooth_earphones.jpg',
        'price': '20 دولار',
        'link': 'https://s.click.aliexpress.com/e/_d8sf9u3'  # رابط تابع صحيح
    },
    {
        'name': 'كاميرا مراقبة',
        'image': 'https://example.com/security_camera.jpg',
        'price': '35 دولار',
        'link': 'https://s.click.aliexpress.com/e/_d4jgkz7'  # رابط تابع صحيح
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
