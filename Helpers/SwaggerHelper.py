import inspect
from APIs.SwaggerAPIs import SwaggerAPIs


# this class is for calling swagger methods and returning response
class SwaggerHelper:
    # create pet method
    def create_new_pet(self, category_id, category_name, name, photo_urls, tag_id, tag_name, status,
                       expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Call the needed API
        response = SwaggerAPIs.call_create_pet_api(category_id, category_name, name, photo_urls, tag_id, tag_name,
                                                   status,
                                                   expected_status_code)
        return response

    #get pet by id
    def get_pet_by_id(self, pet_id, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Call the needed API
        response = SwaggerAPIs.call_get_pet_api(pet_id, expected_status_code)
        return response

    # get pets by status
    def get_pets_by_status(self, status, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Call the needed API
        response = SwaggerAPIs.call_get_pet_by_stats_api(status, expected_status_code)
        return response

    # update pet with PUT
    def update_pet_with_put(self, pet_id, category_id, category_name, name, photo_urls, tag_id, tag_name, status,
                            expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Call the needed API
        response = SwaggerAPIs.call_update_pet_with_put_api(pet_id, category_id, category_name, name, photo_urls,
                                                            tag_id,
                                                            tag_name, status, expected_status_code)
        return response

    # update pet with POST
    def update_pet_with_post(self, pet_id, name, status, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Call the needed API
        response = SwaggerAPIs.call_update_pet_with_post_api(pet_id, name, status, expected_status_code)
        return response

    #delete pet
    def delete_pet(self, pet_id, expected_status_code=200):
        # Get the name of the current function
        function_name = inspect.currentframe().f_code.co_name
        print(f"Calling {function_name}...")

        # Call the needed API
        response = SwaggerAPIs.call_delete_pet_api(pet_id, expected_status_code)
        return response
