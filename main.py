from flask import Flask, request

app = Flask(__name__)

@app.route('/transmission-request', methods=['POST'])
def generate_tg_message():
    offer_data = request.get_json()
    offer = f'Имя: {offer_data["name"]}\nТелефон: {offer_data["number"]}\nПроблема: {offer_data["problem"]}'
    return offer

if __name__ == "__main__":
    app.run(debug=True, port=5000)