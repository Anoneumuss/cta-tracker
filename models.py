from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def mapPayloadToModel(apiPayload:dict, modelClass):
    """
    Safely maps the api payload to the model for an arbirtrary number of returned keys and values. 

    Args:
        apiPayload (dict): the returned dict from the api
        modelClass (_type_): _description_

    Returns:
        _type_: _description_
    """
    columns = {c.name for c in modelClass.__table__.columns}
    filtered = {k: v for k, v in apiPayload.items() if k in columns}
    return modelClass(**filtered)

class Arrivals(db.Model):
    __tablename__ = "arrivals"

    #PK Id:
    id = db.Column(db.Integer, primary_key = True)
    
    #Insertion timestamp:
    timestamp = db.Column(db.DateTime, server_default = db.func.now())

    #Station Id: GTFS parent station ID which this prediction is for (five digits in4xxxx range) (matches “mapid” specified by requestor in query)
    staId = db.Column(db.Integer)

    #Stop Id: GTFS unique stop ID within station which this prediction is for (five digits in 3xxxx range)
    stpId = db.Column(db.Integer)

    #Station Name: Textual proper name of parent station
    staNm = db.Column(db.String)

    #Stop Description: Textual description of platform for which this prediction applies
    stpDe = db.Column(db.String)

    #Run Number: Run number of train being predicted for
    rn = db.Column(db.Integer)

    #Route: Textual, abbreviated route name of train being predicted for (matches GTFS routes)
    rt = db.Column(db.String)

    #Destination Stop: GTFS unique stop ID where this train is expected to ultimately end its service run (experimental and supplemental only—see note below)
    destSt = db.Column(db.Integer)

    #Destination Number: Friendly destination description (see note below)
    destNm = db.Column(db.String)

    #Numeric train route direction code (see appendices)
    trDr = db.Column(db.Integer)

    #Date-time format stamp for when the prediction was generated: yyyyMMdd HH:mm:ss (24-hour format, time local to Chicago)
    prdt = db.Column(db.DateTime)

    #Date-time format stamp for when a train is expected to arrive/depart yyyyMMdd HH:mm:ss (24-hour format, time local to Chicago)
    arrT = db.Column(db.DateTime)

    #ndicates that Train Tracker is now declaring “Approaching” or “Due” on site for this train
    isApp = db.Column(db.Boolean)

    #Boolean flag to indicate whether this is a live prediction or based on schedule in lieu of live data
    isSch = db.Column(db.Boolean)

    #Boolean flag to indicate whether a potential fault has been detected (see note below)
    isFlt = db.Column(db.Boolean)

    #Boolean flag to indicate whether a train is considered “delayed” in Train Tracker
    isDly = db.Column(db.Boolean)

    #Latitude position of the train in decimal degrees
    lat = db.Column(db.Float)

    #Longitude position of the train in decimal degrees
    lon = db.Column(db.Float)

    #Heading, expressed in standard bearing degrees (0 = North, 90 = East, 180 = South, and 270 = West; range is 0 to 359, progressing clockwise)
    heading = db.Column(db.Integer)

    #The __init__ needs to be finished
  #  def __init__ (self, )
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
