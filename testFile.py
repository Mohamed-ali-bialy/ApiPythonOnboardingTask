import SwaggerAPIs


get_response = SwaggerAPIs.call_get_pet_api("9223372036854764239")
print(get_response)
print(get_response.status_code)
print(get_response.json())

photo_urls = ["https://example.com/photo1.jpg", "https://example.com/photo2.jpg", "https://example.com/photo3.jpg"]

get_response = SwaggerAPIs.call_create_pet_api("1","catgName","petName",photo_urls,"0","tagName",200)
print(get_response)
print(get_response.status_code)
print(get_response.json())





get_response = SwaggerAPIs.call_get_pet_by_stats_api("available")
print(get_response)
print(get_response.status_code)
print(get_response.json())

get_response = SwaggerAPIs.call_update_pet_with_post_api("9223372036854765161","pychrmName","nooo")
print(get_response)
print(get_response.status_code)
print(get_response.json())
