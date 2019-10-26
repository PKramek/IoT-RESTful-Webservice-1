from app.main.util.constants import Constants

response_message_codes = {
    Constants.RESPONSE_MESSAGE_OK: 200,
    Constants.RESPONSE_MESSAGE_CREATED: 201,
    Constants.RESPONSE_MESSAGE_ERROR: 500,
    Constants.RESPONSE_MESSAGE_LOGGER_LEVEL_OFF: 500,
    Constants.RESPONSE_MESSAGE_BAD_REQUEST: 400,
    Constants.RESPONSE_MESSAGE_CONFLICTING_DATA: 409,
    Constants.RESPONSE_MESSAGE_BAD_MIMETYPE: 400,
    Constants.RESPONSE_MESSAGE_PRODUCT_KEY_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_DEVICE_KEY_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_USER_GROUP_NAME_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_USER_GROUP_NOT_DEFINED: 400,
    Constants.RESPONSE_MESSAGE_USER_DOES_NOT_HAVE_PRIVILEGES: 403,
    Constants.RESPONSE_MESSAGE_INVALID_CREDENTIALS: 401,
    Constants.RESPONSE_MESSAGE_USER_NOT_DEFINED: 400,
    Constants.RESPONSE_MESSAGE_USER_ALREADY_EXISTS: 409,
    Constants.RESPONSE_MESSAGE_ADMIN_NOT_DEFINED: 400,
    Constants.RESPONSE_MESSAGE_SIGNATURE_EXPIRED: 400,
    Constants.RESPONSE_MESSAGE_INVALID_TOKEN: 400,
    Constants.RESPONSE_MESSAGE_UPDATED_SENSORS_AND_DEVICES: 201,
    Constants.RESPONSE_MESSAGE_WRONG_DATA: 400,
    Constants.RESPONSE_MESSAGE_PARTIALLY_WRONG_DATA: 400,
    Constants.RESPONSE_MESSAGE_SENSOR_TYPE_NAME_NOT_DEFINED: 400,
    Constants.RESPONSE_MESSAGE_SENSOR_TYPE_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_SENSOR_TYPES_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_SENSOR_NAME_ALREADY_DEFINED: 500,
    Constants.RESPONSE_MESSAGE_SENSORS_READINGS_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_SENSORS_READINGS_NOT_LIST: 400,
    Constants.RESPONSE_MESSAGE_DEVICE_STATES_NOT_FOUND: 400,
    Constants.RESPONSE_MESSAGE_DEVICE_STATES_NOT_LIST: 400,
    Constants.RESPONSE_MESSAGE_DEVICE_KEYS_NOT_LIST: 400,
    Constants.RESPONSE_MESSAGE_EXECUTIVE_TYPE_NAME_NOT_DEFINED: 400,
    Constants.RESPONSE_MESSAGE_UNCONFIGURED_DEVICE_NOT_FOUND: 400
}
