# Dependencies Setup
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
measurement = Base.classes.measurement

station = Base.classes.station

# Flask Setup
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/startdate <br/>"
        f"/api/v1.0/startdate/enddate <br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    """Return last 12 months of precipitation"""
    
    precip_data = Session.query(measurement.date, measurement.prcp) .\
     filter (measurement.date >= query_date).all()

    session.close()

    # Convert list of tuples into normal list
    precip = list(np.ravel(precip_data))

    return jsonify(precip)

app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    """Return list of stations"""
    
    total_stations = Session.query(station.station).all()

    session.close()

    # Convert list of tuples into normal list
    station_list = list(np.ravel(total_stations))

    return jsonify(station_list)

app.route("/api/v1.0/tobs")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    """Return temperature observations for the most active station for last 12 months"""
    
    most_active_temp_data = Session.query(measurement.date, measurement.tobs) .\
    filter (measurement.station == 'USC00519281').\
    filter (measurement.date >= query_date).all()

    session.close()

    # Convert list of tuples into normal list
    active_station = list(np.ravel(most_active_temp_data))

    return jsonify(active_station)

app.route("/api/v1.0/<start>")
def summary_after_start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return summary statistics after start date"""
    
    summary_after_start = session.query(func.min(measurement.tobs),
                                     func.max(measurement.tobs),
                                     func.avg(measurement.tobs)).\
                                        filter((measurement.date) >= start).all()

    # Convert list of tuples into normal list 
    summary_start = list(np.ravel(summary_after_start))
    return jsonify(summary_after_start)

app.route("/api/v1.0/<start>/<end>")
def summary_between_start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return summary statistics betweeen start and end dates"""
    
    summary_start_end = session.query(func.min(measurement.tobs),
                                     func.max(measurement.tobs),
                                     func.avg(measurement.tobs)).\
                                        filter((measurement.date) >= start).\
                                        filter((measurement.date) <= end).all()
    
    # Convert list of tuples into normal list
    summary_between_dates = list(np.ravel(summary_start_end))
    return jsonify(summary_between_dates)

if __name__ == '__main__':
    app.run(debug=True)