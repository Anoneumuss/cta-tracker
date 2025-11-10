import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://service_user:secretpassword@localhost:5432/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POLL_INTERVAL = 30
    API_URL = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    API_KEY = "00d1931d506b433e93218b2d5ea57bd4"
    ROUTE_RED = "red"
    ROUTE_BROWN = "brown"
    ROUTE_BLUE = "blue"
    ROUTE_PURPLE = "purple"
    STATION_DIVESEY = 40530

class Config_Arrivals:
    API_URL = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    API_KEY = "00d1931d506b433e93218b2d5ea57bd4"
    ROUTE_RED = "red"
    ROUTE_BROWN = "brown"
    ROUTE_BLUE = "blue"
    ROUTE_PURPLE = "purple"
    STATION_DIVESEY = 40530

class Config_Positions: 
    API_URL = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx"
    API_KEY = "00d1931d506b433e93218b2d5ea57bd4"
    ROUTE_RED = "red"
    ROUTE_BROWN = "brown"
    ROUTE_BLUE = "blue"
    ROUTE_PURPLE = "purple"
    STATION_DIVESEY = 40530
