import random
from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/temperature")
def get_temperature_by_location():
    location = request.args.get("location", "")
    return jsonify(build_temperature(location=location))

@app.get("/temperature/<sensor_id>")
def get_temperature_by_sensor_id(sensor_id):
    return jsonify(build_temperature(sensor_id=sensor_id))

ROOM_BY_SENSOR_ID = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen"
}

SENSOR_ID_BY_ROOM = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3"
}


def build_temperature(location = "", sensor_id = ""):
    if not location:
        location = ROOM_BY_SENSOR_ID.get(sensor_id, "Unknown")

    if not sensor_id:
        sensor_id = SENSOR_ID_BY_ROOM.get(location, "0")

    return {
        "value": round(random.uniform(0, 40), 1),
        "unit": "celsius",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "location": location,
        "status": "online",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Temperature sensor in {location}"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)