import requests
import sys


def fetch_employee_data(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct URLs to fetch employee data and task
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Send GET requests to retrieve data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check if the requests were successful (status code 200)
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data. Please check the employee ID or try again later.")
        return None, None  # Return None if data retrieval fails

    # Extract JSON data from responses
    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data  # Return retrieved user and todos data

def display_employee_progress(user_data, todos_data):
    # Check if data is available
    if user_data is not None and todos_data is not None:
        if 'name' in user_data:
            employee_name = user_data['name']
            total_tasks = len(todos_data)
            completed_tasks = sum(1 for task in todos_data if task['completed'])

            # Display the employee's TODO list progress
            print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
            print(f"\t{employee_name}: name of the employee")
            print(f"\t{completed_tasks}: number of completed tasks")
            print(f"\t{total_tasks}: total number of tasks")

if __name__ == "__main__":
    # Check if the correct number of arguments (employee ID) is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])  # Get employee ID from command line argument
    user_info, tasks_info = fetch_employee_data(employee_id)  # Fetch user and tasks data
    display_employee_progress(user_info, tasks_info)  # Display employee's progress

