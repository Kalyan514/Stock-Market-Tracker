import yfinance as yf 
from flask import request, render_template, jsonify, Flask 

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    try:
        ticker = request.get_json()['ticker']
        data = yf.Ticker(ticker).history(period='1y') 
        return jsonify({
            'currentPrice': float(data.iloc[-1].Close),
            'openPrice': float(data.iloc[-1].Open)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__': 
    app.run(debug=True)
