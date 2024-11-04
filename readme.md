# Placement Application

This Python application allows users to analyze their chances of getting selected for a placement drive based on their academic percentage. It provides an interactive command-line interface where users can enter their details, and based on their percentage, the application provides feedback on their likelihood of placement.

## Class Details

### `Placement` Class
The `Placement` class is the core of this application. It allows users to input their details such as name, branch, city, percentage, and college. Based on the provided percentage, the `Analysis` method evaluates the chances of placement and displays a summary of the user's details along with their placement status.

### Attributes
- `name` (str): The user's name.
- `branch` (str): The branch of study (e.g., Computer Science, Electrical).
- `city` (str): The city of the user's residence.
- `percentage` (float): The user's academic percentage.
- `college` (str): The name of the user's college.

### Methods
- `__init__(self, name, branch, city, percentage, college)`: Initializes a new user profile with the given attributes.
- `Analysis(self)`: Evaluates and displays the placement chance based on the percentage (requires 90% or above for likely placement).

## Usage

1. Run the script.
2. Enter the requested details (name, branch, city, percentage, college).
3. The program will store each user's details and calculate their placement likelihood based on their percentage.
4. Repeat the process as needed to add more users.
5. When finished, type "no" when prompted to stop adding data. All user details will be displayed with their placement analysis.

## Example

```plaintext
please enter your name: John Doe
please enter your branch: Computer Science
please enter your city: New York
please enter your percentage: 92
please enter your college name: NYU
your data has been added successfully
do you want to add more data [Yes|NO]: no

All the placement data
########################################
Hi, John Doe Congrats you have the capability to be selected in the placement drive based on the provided data.
Your good name is: John Doe
Your branch: Computer Science
Your city: New York
Your percentage: 92
Your college: NYU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ```


This project is licensed under the MIT License.

