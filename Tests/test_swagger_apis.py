import pytest
import random
from Helpers.SwaggerHelper import SwaggerHelper

@pytest.fixture(scope="class")
def swagger_helper():
    """
    Initialize SwaggerHelper as a shared fixture for all test methods in the class.
    """
    return SwaggerHelper()


@pytest.fixture(scope="class")
def test_data():
    """
    Setup test data and return it as a dictionary. Using 'class' scope to persist data across methods in a class.
    """
    random_int = random.randint(100, 1000)
    random_int_2 = random.randint(100, 1000)
    data = {
        "pet_id": None,
        "category_id": random_int,
        "category_name": f"Cat_Name_{random_int}",
        "name": f"petName_{random_int}",
        "photo_urls": ["https://example.com/photo1.jpg", "https://example.com/photo2.jpg"],
        "tag_id": random_int,
        "tag_name": f"tagName_{random_int}",
        "status": "available",
        "expected_status_code": 200,
        "updated_name": f"petName_{random_int_2}",
        "updated_status": "NotAvailable"

    }
    return data


@pytest.mark.usefixtures("swagger_helper", "test_data")
class TestPet:
    @pytest.mark.order1
    def test_create_pet(self, swagger_helper, test_data):
        print("start test")
        """
        Test creating a pet and storing the response's pet ID in test_data.
        """
        create_response = swagger_helper.create_new_pet(
            category_id=test_data['category_id'],
            category_name=test_data['category_name'],
            name=test_data['name'],
            photo_urls=test_data['photo_urls'],
            tag_id=test_data['tag_id'],
            tag_name=test_data['tag_name'],
            status=test_data['status']
        )
        create_data = create_response.json()
        test_data['pet_id'] = create_data['id']
        print("create")
        print(create_response.json())

        assert create_data['category']['id'] == test_data['category_id'], "Mismatch on category ID"
        assert create_data['category']['name'] == test_data['category_name'], "Mismatch on category NAME"
        assert create_data['name'] == test_data['name'], "Mismatch on Pet Name"
        assert create_data['photoUrls'] == test_data['photo_urls'], "Mismatch on PHOTOS URL"
        assert create_data['tags'][0]['id'] == test_data['tag_id'], "Mismatch on tag ID"
        assert create_data['tags'][0]['name'] == test_data['tag_name'], "Mismatch on tag name"
        assert create_data['status'] == test_data['status'], "Mismatch on status"
        assert create_response.status_code == test_data['expected_status_code'], "Mismatch on status Code"

    @pytest.mark.order2
    def test_update_pet(self, swagger_helper, test_data):
        print("start test")
        """
        Test update a pet using the ID created in `test_create_pet`.
        pet_id, name, status
        """

        update_response = swagger_helper.update_pet_with_post(
            pet_id=test_data['pet_id'],
            name=test_data['updated_name'],
            status=test_data['updated_status'],
        )
        update_pet_data = update_response.json()
        print("update test")
        print(update_pet_data)

        assert update_response.status_code == test_data['expected_status_code'], "Mismatch on status Code"


    @pytest.mark.order3
    def test_get_pet_by_id(self, swagger_helper, test_data):
        print("start test")
        """
        Test get a pet using the ID created in `test_create_pet`.
        pet_id, name, status
        """
        get_response = swagger_helper.get_pet_by_id(
            pet_id=test_data['pet_id']
        )
        get_data = get_response.json()
        print("get")
        print(get_response.json())


        assert get_data['id'] == test_data['pet_id'], "Mismatch on Pet Id On Get Method"
        assert get_data['category']['id'] == test_data['category_id'], "Mismatch on category ID"
        assert get_data['category']['name'] == test_data['category_name'], "Mismatch on category NAME"
        assert get_data['name'] == test_data['updated_name'], "Mismatch on updating Pet Name"
        assert get_data['photoUrls'] == test_data['photo_urls'], "Mismatch on PHOTOS URL"
        assert get_data['tags'][0]['id'] == test_data['tag_id'], "Mismatch on tag ID"
        assert get_data['tags'][0]['name'] == test_data['tag_name'], "Mismatch on tag name"
        assert get_data['status'] == test_data['updated_status'], "Mismatch on UPDATING status"
        assert get_response.status_code == test_data['expected_status_code'], "Mismatch on status Code"


    @pytest.mark.order4
    def test_delete_pet(self, swagger_helper, test_data):
        """
        Test deleting the pet and ensuring it can no longer be retrieved.
        """
        delete_response = swagger_helper.delete_pet(test_data['pet_id'])
        assert delete_response.status_code == 200

        # Verify deletion
        verify_response = swagger_helper.get_pet_by_id(test_data['pet_id'], expected_status_code=404)
        assert verify_response.status_code == 404
