from flask import Flask, request
from sendMessage import sendMessage

app = Flask(__name__)

@app.route('/transmission-request', methods=['POST'])
def generate_tg_message():
    token = request.args.get('token')
    chatid = request.args.get('chatid')
    offer_data = request.get_json()
    offer = '''<b>Имя:</b> {}
<b>Телефон:</b> {}
<b>Проблема:</b> {}
<b>Адрес:</b> {}
    '''.format(offer_data["name"], offer_data["number"], offer_data["problem"], offer_data["addres"])
    sendMessage(token,chatid, offer)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, port=5000)