import json

from app.main.util.auth_utils import Auth
from app.main.util.constants import Constants


def test_get_executive_device_info_should_return_device_info_when_valid_request(
        client,
        insert_device_group,
        insert_executive_device,
        insert_user,
        get_user_group_default_values,
        create_user_group,
        insert_executive_type,
        insert_formula):
    content_type = 'application/json'

    device_group = insert_device_group()
    user = insert_user()

    user_group_values = get_user_group_default_values()
    user_group_values['users'] = [user]

    user_group = create_user_group(user_group_values)
    executive_type = insert_executive_type()
    formula = insert_formula()
    executive_device = insert_executive_device()

    response = client.get(
        '/api/hubs/' + device_group.product_key + '/executive-devices/' + executive_device.device_key,
        content_type=content_type,
        headers={
            'Authorization': 'Bearer ' + Auth.encode_auth_token(user.id)
        }
    )

    assert response is not None
    assert response.status_code == 200
    assert response.content_type == content_type

    response_data = json.loads(response.data.decode())
    assert response_data is not None

    assert response_data['name'] == executive_device.name
    assert response_data['state'] == executive_device.state
    assert response_data['isUpdated'] == executive_device.is_updated
    assert response_data['isActive'] == executive_device.is_active
    assert response_data['isAssigned'] == executive_device.is_assigned
    assert response_data['isFormulaUsed'] == executive_device.is_formula_used
    assert response_data['isPositiveState'] == executive_device.positive_state
    assert response_data['isNegativeState'] == executive_device.negative_state
    assert response_data['deviceKey'] == executive_device.device_key
    assert response_data['deviceTypeName'] == executive_type.name
    assert response_data['deviceUserGroup'] == user_group.name
    assert response_data['formulaName'] == formula.name


def test_get_executive_device_info_should_return_user_does_not_have_privileges_error_when_not_known_user_id(
        client,
        insert_device_group,
        insert_executive_device,
        insert_user,
        get_user_group_default_values,
        create_user_group,
        insert_executive_type,
        insert_formula):
    content_type = 'application/json'

    device_group = insert_device_group()
    user = insert_user()

    user_group_values = get_user_group_default_values()
    user_group_values['users'] = [user]

    create_user_group(user_group_values)
    insert_executive_type()
    insert_formula()
    executive_device = insert_executive_device()

    response = client.get(
        '/api/hubs/' + device_group.product_key + '/executive-devices/' + executive_device.device_key,
        content_type=content_type,
        headers={
            'Authorization': 'Bearer ' + Auth.encode_auth_token(user.id + 1)
        }
    )

    assert response is not None
    assert response.status_code == 400
    assert response.content_type == content_type

    response_data = json.loads(response.data.decode())
    assert response_data['errorMessage'] == Constants.RESPONSE_MESSAGE_USER_DOES_NOT_HAVE_PRIVILEGES


def test_get_executive_device_info_should_return_device_key_not_found_when_device_key_was_not_found(
        client,
        insert_device_group,
        insert_executive_device,
        insert_user,
        get_user_group_default_values,
        create_user_group,
        insert_executive_type,
        insert_formula):
    content_type = 'application/json'

    device_group = insert_device_group()
    user = insert_user()

    user_group_values = get_user_group_default_values()
    user_group_values['users'] = [user]

    create_user_group(user_group_values)
    insert_executive_type()
    insert_formula()

    response = client.get(
        '/api/hubs/' + device_group.product_key + '/executive-devices/' + '1',
        content_type=content_type,
        headers={
            'Authorization': 'Bearer ' + Auth.encode_auth_token(user.id + 1)
        }
    )

    assert response is not None
    assert response.status_code == 400
    assert response.content_type == content_type

    response_data = json.loads(response.data.decode())
    assert response_data['errorMessage'] == Constants.RESPONSE_MESSAGE_DEVICE_KEY_NOT_FOUND


def test_get_executive_device_info_should_return_device_key_not_found_when_product_key_was_not_found(
        client,
        insert_executive_device,
        insert_user,
        get_user_group_default_values,
        create_user_group,
        insert_executive_type,
        insert_formula):
    content_type = 'application/json'

    executive_device = insert_executive_device()
    user = insert_user()

    user_group_values = get_user_group_default_values()
    user_group_values['users'] = [user]

    create_user_group(user_group_values)
    insert_executive_type()
    insert_formula()

    response = client.get(
        '/api/hubs/' + 'test' + '/executive-devices/' + executive_device.device_key,
        content_type=content_type,
        headers={
            'Authorization': 'Bearer ' + Auth.encode_auth_token(user.id + 1)
        }
    )

    assert response is not None
    assert response.status_code == 400
    assert response.content_type == content_type

    response_data = json.loads(response.data.decode())
    assert response_data['errorMessage'] == Constants.RESPONSE_MESSAGE_PRODUCT_KEY_NOT_FOUND


def test_get_executive_device_info_should_return_user_does_not_have_privileges_error_when_user_not_is_same_user_group(
        client,
        insert_device_group,
        insert_executive_device,
        insert_user,
        create_user_group,
        insert_executive_type,
        insert_formula):
    content_type = 'application/json'

    device_group = insert_device_group()
    create_user_group()
    insert_executive_type()
    insert_formula()
    executive_device = insert_executive_device()
    user = insert_user()

    response = client.get(
        '/api/hubs/' + device_group.product_key + '/executive-devices/' + executive_device.device_key,
        content_type=content_type,
        headers={
            'Authorization': 'Bearer ' + Auth.encode_auth_token(user.id + 1)
        }
    )

    assert response is not None
    assert response.status_code == 400
    assert response.content_type == content_type

    response_data = json.loads(response.data.decode())
    assert response_data['errorMessage'] == Constants.RESPONSE_MESSAGE_USER_DOES_NOT_HAVE_PRIVILEGES


def test_get_executive_device_info_should_return_device_key_not_found_error_when_device_is_in_another_device_group(
        client,
        insert_device_group,
        insert_executive_device,
        insert_user,
        create_user_group,
        insert_executive_type,
        insert_formula,
        get_device_group_default_values):
    content_type = 'application/json'

    insert_device_group()

    second_device_group_data = get_device_group_default_values()
    second_device_group_data['id'] += 2
    second_device_group_data['product_key'] += "2"
    second_device_group = insert_device_group(second_device_group_data)

    create_user_group()
    insert_executive_type()
    insert_formula()
    executive_device = insert_executive_device()
    user = insert_user()

    response = client.get(
        '/api/hubs/' + second_device_group.product_key + '/executive-devices/' + executive_device.device_key,
        content_type=content_type,
        headers={
            'Authorization': 'Bearer ' + Auth.encode_auth_token(user.id + 1)
        }
    )

    assert response is not None
    assert response.status_code == 400
    assert response.content_type == content_type

    response_data = json.loads(response.data.decode())
    assert response_data['errorMessage'] == Constants.RESPONSE_MESSAGE_DEVICE_KEY_NOT_FOUND
