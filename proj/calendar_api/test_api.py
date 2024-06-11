import requests
import uuid

BASE_URL = "http://127.0.0.1:8000/v1"
TOKEN = "8ecadf46-9364-4e3a-b79d-182d6a259a75"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def test_create_schedule():
    url = f"{BASE_URL}/schedules"
    schedule_data = {
        "id": str(uuid.uuid4()),
        "time": "2024-03-20T08:00:00",
        "locationId": "loc_456",
        "person_name": "John Doe"
    }
    response = requests.post(url, json=schedule_data, headers=headers)
    print("Create Schedule:", response.status_code, response.json())
    assert response.status_code == 201, "Failed to create schedule"
    return response.json()

def test_get_schedule(schedule_id):
    url = f"{BASE_URL}/schedule/{str(schedule_id)}"
    response = requests.get(url, headers=headers)
    print("Get Schedule:", response.status_code, response.json())
    assert response.status_code == 200, "Failed to get schedule"

def test_update_schedule(schedule_id):
    url = f"{BASE_URL}/schedule/{str(schedule_id)}"
    updated_data = {
        "time": "2024-03-21T09:00:00",
        "locationId": "loc_789",
        "person_name": "Jane Doe"  # Updating the person's name
    }
    response = requests.put(url, json=updated_data, headers=headers)
    print("Update Schedule:", response.status_code, response.json())
    assert response.status_code == 200, "Failed to update schedule"

def test_delete_schedule(schedule_id):
    url = f"{BASE_URL}/schedule/{str(schedule_id)}"
    response = requests.delete(url, headers=headers)
    print("Delete Schedule:", response.status_code)
    assert response.status_code == 204, "Failed to delete schedule"
    
def test_get_schedules_by_person_name(person_name):
    url = f"{BASE_URL}/schedules/{person_name}"
    response = requests.get(url, headers=headers)
    print("Get Schedules by Person Name:", response.status_code, response.json())
    assert response.status_code == 200, "Failed to get schedules by person name"
    return response.json()

if __name__ == "__main__":
    # Run our tests
    created_schedule = test_create_schedule()  # Create and get the created schedule's details
    if "id" in created_schedule:  # Using 'id' for further operations
        test_get_schedule(created_schedule["id"])  # Test retrieval of the schedule
        test_update_schedule(created_schedule["id"])  # Test updating the schedule
        test_get_schedules_by_person_name("Jane Doe")
        test_delete_schedule(created_schedule["id"])  # Test deleting the schedule
    else:
        print("Schedule creation failed, subsequent tests skipped.")
