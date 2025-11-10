from flask import Flask, jsonify
from config import Config, Config_Arrivals, Config_Positions
from models import db, Arrivals
from background import startArrivalBackgroundThread

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.before_request
def init():
    #Create tables and start background thread
    db.create_all()
    startArrivalBackgroundThread(app, Config_Arrivals.API_URL, Config_Arrivals.API_KEY, Config_Arrivals.STATION_DIVESEY)

@app.route('/Arrivals')
def get_arrivals():
    latest = Arrivals.query.order_by(Arrivals.timestamp.desc()).first()

    if not latest:
        return jsonify({"status": "no data yet"}), 200
    return jsonify(latest.data)

if __name__ == "__main__":
    app.run(debug = True, use_reloader = False)