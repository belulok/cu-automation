import requests

# Constants
API_TOKEN = 'pk_44498223_U0V6G4V0O72TYB8W4N3DCR9BBESTN8ZE'
BASE_URL = 'https://api.clickup.com/api/v2'
TASK1_ID = '#862kgpdh4'
TASK2_ID = '#862kgpm18'

headers = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json'
}

def get_task_status(task_id):
    response = requests.get(f"{BASE_URL}/task/{task_id}", headers=headers)
    if response.status_code == 200:
        return response.json().get('status', {}).get('status')
    else:
        print(f"Error getting status for task {task_id}. Status code: {response.status_code}")
        return None

def update_task(task_id, data):
    response = requests.put(f"{BASE_URL}/task/{task_id}", headers=headers, json=data)
    if response.status_code == 200:
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Error updating task {task_id}. Status code: {response.status_code}")

def main():
    # Check if Task 1 is done
    if get_task_status(TASK1_ID) == "handover":
        # Update Task 2 status to active and set other attributes
        data = {
            "status": "available",
            "description": "New Description",
            "due_date": "New Due Date Timestamp"
            # ... Add more attributes as needed
        }
        update_task(TASK2_ID, data)
        
        # Create subtask for Task 2 and set its attributes (This is a placeholder as the exact endpoint might differ)
        # ... Add code here

if __name__ == "__main__":
    main()
