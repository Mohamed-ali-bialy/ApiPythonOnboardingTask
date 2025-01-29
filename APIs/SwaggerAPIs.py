import inspect
from ApiBase.ApiBase import ApiBase

#Swagger calling class api
class SwaggerAPIs:
    #base URL for swagger  api
    api_base = ApiBase(base_url="https://petstore.swagger.io/v2")

    #method for calling get pet by id
    @classmethod
    def call_get_pet_api(cls, pet_id, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        #call needed request
        response = cls.api_base.get(f"/pet/{str(pet_id)}")
        #assert on status code and return response
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    #method for calling get pet by status
    @classmethod
    def call_get_pet_by_stats_api(cls, status, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # call needed request
        response = cls.api_base.get(f"/pet/findByStatus?status={status}")
        # assert on status code and return response
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    #method for creating pet
    @classmethod
    def call_create_pet_api(cls, category_id, category_name, name, photo_urls, tag_id, tag_name, status,
                            expected_status_code):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Validate the photo_urls parameter is a list
        assert isinstance(photo_urls, list), "photo_urls must be a list"

        #building request body for create api
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

        # call needed request
        response = cls.api_base.post("/pet", data=request_body)
        # assert on status code and return response
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    #method for updating pet with PUT method
    @classmethod
    def call_update_pet_with_put_api(cls, pet_id, category_id, category_name, name, photo_urls, tag_id, tag_name,
                                     status,
                                     expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Validate the photo_urls parameter
        assert isinstance(photo_urls, list), "photo_urls must be a list"

        # building request body for update api
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
        # call needed request
        response = cls.api_base.put("/pet", data=request_body)
        # assert on status code and return response
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    #Method for updating pet with Post method
    @classmethod
    def call_update_pet_with_post_api(cls, pet_id, name, status, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # building request body for update api
        request_body = {
            "name": name,
            "status": status
        }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        # call needed request
        response = cls.api_base.post(f"/pet/{pet_id}", data=request_body, headers=headers)
        # assert on status code and return response
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    # method for deleting pet
    @classmethod
    def call_delete_pet_api(cls, pet_id, expected_status_code):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        #creating special headers for deleting method as needed in docs
        headers = {
            "accept": "application/json",
            "api_key": "special-key"  # Replace with the actual API key if required
        }

        #creating needed endpoint
        end_point = f"/pet/{pet_id}"
        # call needed request
        response = cls.api_base.delete(end_point, headers=headers)
        # assert on status code and return response
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response
