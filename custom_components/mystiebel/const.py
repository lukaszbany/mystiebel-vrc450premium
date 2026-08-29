"""Constants for the Mystiebel integration."""

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass

DOMAIN = "mystiebel"
WS_URL = "wss://serviceapi.mystiebel.com/ws/v1"

# API Configuration
BASE_URL = "https://auth.mystiebel.com"
SERVICE_URL = "https://serviceapi.mystiebel.com"

# App Configuration
APP_NAME = "MyStiebelApp"
APP_VERSION_ANDROID = "Android_2.3.0"
USER_AGENT = f"{APP_NAME}/2.3.0 Dalvik/2.1.0"

# Timing Constants
WEBSOCKET_HEARTBEAT = 30  # seconds
WEBSOCKET_RECONNECT_INITIAL = 5  # seconds
WEBSOCKET_RECONNECT_MAX = 300  # 5 minutes
TOKEN_REFRESH_MARGIN = 300  # Refresh token 5 minutes before expiry
API_RATE_LIMIT_DELAY = 1  # Minimum seconds between API calls

# Message ID Range
MSG_ID_MIN = 1_000_000
MSG_ID_MAX = 9_999_999
MSG_ID_LONG_MIN = 1_000_000_000
MSG_ID_LONG_MAX = 9_999_999_999

# All registers belonging to the VRC450 ventilation controller.
# Used to (a) enable them by default and (b) group them under their own HA device.
VRC450_REGISTERS = {
    2553,  # Fan Speed / Humidity
    2554,  # Air Temperature
    2555,  # Register 2555
    2556,  # Register 2556
    2557,  # Register 2557
    2558,  # Register 2558
    2559,  # Register 2559
    2560,  # Register 2560
    2561,  # Register 2561
    2562,  # Operating Mode / Fan Speed
    2563,  # Filter Change Countdown
    2564,  # Current Fan Speed
    2565,  # Fan Speed Setpoint
}

# List of essential read-only sensors.
# These will be enabled by default. All other sensor-type entities will be disabled by default.
ESSENTIAL_SENSORS = [
    2553,  # VRC450: Fan Speed / Humidity
    2554,  # VRC450: Air Temperature
    2555,  # VRC450: Register 2555
    2556,  # VRC450: Register 2556
    2557,  # VRC450: Register 2557
    2558,  # VRC450: Register 2558
    2559,  # VRC450: Register 2559
    2560,  # VRC450: Register 2560
    2561,  # VRC450: Register 2561
    2562,  # VRC450: Operating Mode / Fan Speed
    2563,  # VRC450: Filter Change Countdown
    2564,  # VRC450: Current Fan Speed
]

# List of essential control entities (switches, numbers, selects).
# These will also be enabled by default. All other controls will be disabled.
ESSENTIAL_CONTROLS = [
    2565,  # VRC450: Fan Speed Setpoint
]

# List of individual sensors to exclude from creation,
# because they are used to build more advanced, combined sensors.
EXCLUDED_INDIVIDUAL_SENSORS = {
    # Version numbers (major, minor, patch, revision for Controller and Wi-Fi)
    65523,
    65524,
    65525,
    65535,
    65536,
    65537,
    65559,
    65560,
    # Product and Gateway ID numbers (order, production, factory, plant)
    65553,
    65554,
    65555,
    65556,
    65557,
    65558,
    65593,
    65594,
    # Runtime numbers in days and hours (are combined into a single sensor)
    2449,
    555,
    2450,
    558,
    # Weekly hygiene program time (combined into single time entity)
    2477,  # Minutes
    2483,  # Hours
}

# --- Centralized Mappings ---

UNIT_MAP = {
    "degree_celsius": "°C",
    "degree_celtius": "°C",
    "liter": "L",
    "second": "s",
    "minute": "min",
    "hour": "h",
    "day": "d",
    "watt": "W",
    "kilowatt": "kW",
    "watt_hour": "Wh",
    "kilowatt_hour": "kWh",
    "humidity": "%",
    "none": None,
    "": None,
    "None": None,
}

DEVICE_CLASS_MAP = {
    "°C": SensorDeviceClass.TEMPERATURE,
    "s": SensorDeviceClass.DURATION,
    "min": SensorDeviceClass.DURATION,
    "h": SensorDeviceClass.DURATION,
    "d": SensorDeviceClass.DURATION,
    "L": SensorDeviceClass.VOLUME,
    "W": SensorDeviceClass.POWER,
    "kW": SensorDeviceClass.POWER,
    "kWh": SensorDeviceClass.ENERGY,
    "Wh": SensorDeviceClass.ENERGY,
    "Pa": SensorDeviceClass.PRESSURE,
    "%": SensorDeviceClass.HUMIDITY,
}

STATE_CLASS_MAP = {
    "Temperature": SensorStateClass.MEASUREMENT,
    "Number": SensorStateClass.MEASUREMENT,
    "Pressure": SensorStateClass.MEASUREMENT,
    "Humidity": SensorStateClass.MEASUREMENT,
    "Second": SensorStateClass.MEASUREMENT,
    "Hour": SensorStateClass.MEASUREMENT,
    "Minute": SensorStateClass.MEASUREMENT,
    "DurationHours": SensorStateClass.MEASUREMENT,
    "DurationDays": SensorStateClass.MEASUREMENT,
    "WWK_LuminosityLevel": SensorStateClass.MEASUREMENT,
    "Power": SensorStateClass.MEASUREMENT,
    "Energy": SensorStateClass.TOTAL_INCREASING,
    "State": None,
    "NotificationCode": None,
    "SwitchingTime": None,
    "LocalTime": None,
}

DATA_TYPE_DEVICE_CLASS_MAP = {
    "LocalTime": SensorDeviceClass.TIMESTAMP,
}

NUMERIC_CONTROL_TYPES = {
    "Temperature",
    "Number",
    "Percentage",
    "Hour",
    "Minute",
    "DurationHours",
    "DurationDays",
    "WWK_LuminosityLevel",
}
