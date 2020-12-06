from flask import Flask,render_template
posts=[
    {
        'author': 'Abhishek Soy',
        'title': 'Track Shipment',
    }
]


app = Flask(__name__)


@app.route('/')
def track_shipment():
    return render_template('track_shipment.html',posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
