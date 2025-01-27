from Helpers.SwaggerHelper import SwaggerHelper
import random
import json


class TestSwaggerAPI:
    swagger_helper = SwaggerHelper()
    random_int = random.randint(100, 1000)
    print("random number " + str(random_int))

    # testing data
    pet_id = None
    category_id = random_int
    category_name = "Cat_Name_" + str(random_int)
    name = "petName_" + str(random_int)
    photo_urls = ["https://example.com/photo1.jpg", "https://example.com/photo2.jpg"]
    tag_id = random_int
    tag_name = "tagName_" + str(random_int)
    status = "available"
    expected_status_code = 200

    #updating data
    updated_name = "updatedPetName_" + str(random.randint(100, 1000))
    updated_status = "NotAvailable"

    def test_create_new_pet(self):
        create_response = self.swagger_helper.create_new_pet(
            category_id=self.category_id,
            category_name=self.category_name,
            name=self.name,
            photo_urls=self.photo_urls,
            tag_id=self.tag_id,
            tag_name=self.tag_name,
            status=self.status,
            expected_status_code=self.expected_status_code
        )

        create_data = create_response.json()
        self.pet_id = create_data['id']
        print("create_data: " + json.dumps(create_data))

        assert create_response.status_code == self.expected_status_code
        assert create_data['category']['id'] == self.category_id
        assert create_data['category']['name'] == self.category_name
        assert create_data['name'] == self.name
        assert create_data['photoUrls'] == self.photo_urls
        assert create_data['tags'][0]['id'] == self.tag_id
        assert create_data['tags'][0]['name'] == self.tag_name
        assert create_data['status'] == self.status

    def test_get_pet_by_id(self):
        get_pet_response = self.swagger_helper.get_pet_by_id(self.pet_id)
        get_pet_data = get_pet_response.json()

        assert get_pet_response.status_code == self.expected_status_code
        assert get_pet_data['category']['id'] == self.category_id
        assert get_pet_data['category']['name'] == self.category_name
        assert get_pet_data['name'] == self.name
        assert get_pet_data['photoUrls'] == self.photo_urls
        assert get_pet_data['tags'][0]['id'] == self.tag_id
        assert get_pet_data['tags'][0]['name'] == self.tag_name
        assert get_pet_data['status'] == self.status

    def test_update_pet_with_post(self):

        update_response = self.swagger_helper.update_pet_with_post(
            pet_id=self.pet_id,
            name= self.updated_name ,
            status=self.updated_status,
            expected_status_code=self.expected_status_code
        )

        update_data = update_response.json()

        assert update_response.status_code == self.expected_status_code
        assert update_data['id'] == self.pet_id
        assert update_data['name'] == self.updated_name
        assert update_data['status'] == self.updated_status

    def test_delete_pet(self):
        delete_response = self.swagger_helper.delete_pet(
            pet_id=9223372036854775807,
            expected_status_code=self.expected_status_code
        )

        assert delete_response.status_code == self.expected_status_code

        # Verify that the pet is no longer available
        get_pet_response = self.swagger_helper.get_pet_by_id(self.pet_id,404)
        print("create_data: " + json.dumps(get_pet_response.json()))
        assert get_pet_response.status_code == 404

    """
    def test_get_pets_by_status(self):
        available_pets_response = self.swagger_helper.get_pets_by_status(
            status="available",
            expected_status_code=self.expected_status_code
        )

        available_pets_data = available_pets_response.json()

        assert available_pets_response.status_code == self.expected_status_code
        for pet in available_pets_data:
            assert pet['status'] == "available"

        sold_pets_response = self.swagger_helper.get_pets_by_status(
            status="sold",
            expected_status_code=self.expected_status_code
        )

        sold_pets_data = sold_pets_response.json()

        assert sold_pets_response.status_code == self.expected_status_code
        for pet in sold_pets_data:
            assert pet['status'] == "sold"
    """