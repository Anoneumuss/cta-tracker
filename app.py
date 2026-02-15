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
    arrivals = Arrivals.query.all()

    if not arrivals:
        return jsonify({"status": "no data yet"}), 200

    # Serialize rows
    data = [a.to_dict() for a in arrivals]

    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug = True, use_reloader = True)