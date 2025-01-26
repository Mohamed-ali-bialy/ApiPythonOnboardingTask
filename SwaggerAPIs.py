from ApiBase import ApiBase

api_base = ApiBase(base_url="https://petstore.swagger.io/v2")

def call_get_pet_api(pet_id, expected_status_code=200):
    response = api_base.get(f"/pet/{pet_id}")
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    return response

def call_get_pet_by_stats_api(status, expected_status_code=200):
    response = api_base.get(f"/pet/findByStatus?status={status}")
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    return response

def call_create_pet_api(category_id, category_name, name, photo_urls, tag_id, tag_name, status,expected_status_code=200):
    # Validate the photo_urls parameter
    assert isinstance(photo_urls, list), "photo_urls must be a list"

    request_body = {
        "id": 0,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "name": name,
        "photoUrls": photo_urls,
        "tags": [
            {
                "id": tag_id,
                "name": tag_name
            }
        ],
        "status": status
    }

    response = api_base.post("/pet", data=request_body)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    return response



def call_update_pet_with_put_api(pet_id,category_id, category_name, name, photo_urls, tag_id, tag_name, status,expected_status_code=200):
    # Validate the photo_urls parameter
    assert isinstance(photo_urls, list), "photo_urls must be a list"

    request_body = {
        "id": pet_id,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "name": name,
        "photoUrls": photo_urls,
        "tags": [
            {
                "id": tag_id,
                "name": tag_name
            }
        ],
        "status": status
    }

    response = api_base.put("/pet", data=request_body)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    return response

def call_update_pet_with_post_api(pet_id, name, status, expected_status_code=200):
    request_body = {
        "name": name,
        "status": status
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = api_base.post(f"/pet/{pet_id}", data=request_body, headers=headers)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    return response
