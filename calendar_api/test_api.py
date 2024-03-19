import requests

BASE_URL = "http://127.0.0.1:8000/v1"

def test_create_schedule():
    url = f"{BASE_URL}/schedules"
    schedule_data = {
        "id": "1",
        "guardId": "guard_123",
        "time": "2024-03-20T08:00:00",
        "locationId": "loc_456"
    }
    response = requests.post(url, json=schedule_data)
    print("Create Schedule:", response.status_code, response.json())
    return response.json()  # Returning the created schedule for further tests

def test_get_schedule(schedule_id):
    url = f"{BASE_URL}/schedule/{schedule_id}"
    response = requests.get(url)
    print("Get Schedule:", response.status_code, response.json())

def test_update_schedule(schedule_id):
    url = f"{BASE_URL}/schedule/{schedule_id}"
    updated_data = {
        "id": schedule_id,
        "guardId": "guard_123_updated",
        "time": "2024-03-21T09:00:00",
        "locationId": "loc_789"
    }
    response = requests.put(url, json=updated_data)
    print("Update Schedule:", response.status_code, response.json())

def test_delete_schedule(schedule_id):
    url = f"{BASE_URL}/schedule/{schedule_id}"
    response = requests.delete(url)
    print("Delete Schedule:", response.status_code)

if __name__ == "__main__":
    # Run our tests
    created_schedule = test_create_schedule()  # Create and get the created schedule's details
    test_get_schedule(created_schedule["id"])  # Test retrieval of the schedule
    test_update_schedule(created_schedule["id"])  # Test updating the schedule
    test_delete_schedule(created_schedule["id"])  # Test deleting the schedule
