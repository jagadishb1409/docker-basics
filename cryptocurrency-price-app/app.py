from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Base URL for the CoinGecko API
base_url = 'https://api.coingecko.com/api/v3'

@app.route('/get_prices', methods=['POST'])
def get_prices():
    data = request.json
    cryptocurrencies = data.get('cryptocurrencies')

    if not cryptocurrencies or not isinstance(cryptocurrencies, list):
        return jsonify({'error': 'Missing or invalid cryptocurrencies parameter (should be a list)'}), 400

    payload = {
        'ids': ','.join(cryptocurrencies),
        'vs_currencies': 'usd'
    }

    response = requests.get(f"{base_url}/simple/price", params=payload)

    if response.status_code == 200:
        price_data = response.json()
        prices = {}
        for cryptocurrency in cryptocurrencies:
            price = price_data.get(cryptocurrency, {}).get('usd')
            if price is not None:
                prices[cryptocurrency] = price
        return jsonify(prices), 200
    else:
        return jsonify({'error': 'Error fetching price data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

