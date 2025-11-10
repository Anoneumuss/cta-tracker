import threading
import requests
import ctaHandlers
import time
from models import db, Arrivals

def startArrivalBackgroundThread(app, url: str, api_key: str, map_id: int, route: str | None = None):
    def run():
        with app.app_context():
            while True:
                try:
                    params = {
                        "key":api_key,
                        "outputType": "JSON",
                        "mapid": map_id,
                        "rt": route
                    }

                    response = requests.get(url, params=params)
                    response.raise_for_status()
                    responseJson = response.json()

                    #Need to unpack the data in a meaningful way:
                    records = ctaHandlers.unpackArrivalResponse(responseJson)

                    #Write to the database:
                    for record in records:
                        row = Arrivals(data = record)
                        db.session.add(record)
                    db.session.commit

                    print('Data updated at ',  time.strftime("%X"))
                
                except Exception as e:
                    print('Exception', e)
                    db.session.rollback()
                
                time.sleep(app.config['POLL_INTERVAL'])
    
    thread = threading.Thread(target = run, daemon = True)
    thread.start()