# Interface_Master
This project is made to andarrange the various interfaces (Student management, Vehicle Management, Hospital management, etc.). 

# Interface_Master
I have created this project for my College work. In this project, you have to choose the interface (Student, Vehicle, Hospital, etc.) Management System. Used Python and SQL for interface and database.

To run mysql,Download: https://dev.mysql.com/downloads/file/?id=518835

Step to Open File:
1. Open interface.py
Here you have to choose which interface you want.
And enter password 1234
click on INTERFACE

2.Next file will open auto.

----------------------------------------------------------------------------------------------

## Understand project

# 1.Interface.py
Certainly! Here's a simplified explanation of the code:

# Login Interface with Interface Selection

This is a Python script that creates a graphical user interface (GUI) for a login system with interface selection. Users can log in with their credentials and choose different interfaces based on their role.

## Prerequisites
- Python 3.x
- Tkinter
- Pygame
- PIL (Python Imaging Library)

## Getting Started
1. Clone the repository or download the code files.
2. Install the required dependencies mentioned in the prerequisites.
3. Run the `login_interface.py` script.

## How It Works
1. The script imports necessary modules such as `tkinter` for GUI, `messagebox` for displaying messages, `ttk` for styling widgets, `PIL` for image processing, and `subprocess` for opening other scripts.
2. It plays a sound at the beginning using the Pygame library.
3. The `Interface()` function is defined, which is called when the user clicks the "Interface" button.
4. The script creates a Tkinter window and sets its properties, including size and background.
5. It loads and displays a background image in the window.
6. A login frame is created within the window to hold the login elements.
7. The logo image and other images are loaded and displayed within the login frame.
8. Labels and entry fields are created for the username and password.
9. A combobox (dropdown menu) is configured for interface selection.
10. The `Interface()` function checks the entered credentials and performs actions accordingly:
    - If the fields are empty, it displays an error message.
    - If the entered credentials match 'Vehicle' and '1234', it displays a welcome message for the "Vehicle Management" interface.
    - If the entered credentials match 'Student' and '1234', it displays a welcome message for the "Student Management" interface and opens the 'StudentManagementI.py' script.
    - If the entered credentials match 'Hospital' and '1234', it displays a welcome message for the "Hospital Management" interface and opens the 'HospitalManagementI.py' script.
    - If the entered credentials do not match any of the above, it displays an error message.
11. The script creates a button labeled "Interface" that triggers the `Interface()` function when clicked.
12. A list of interface options is defined for the combobox.
13. The window enters the main event loop, allowing the GUI to be displayed and interacted with.

## Customization
- Replace the provided image files ('bg.jpg', 'InterfaceIcon.png', 'ini.png', 'password.png') with your own images for customization.
- Modify the interface options in the `Options` list to match your system's available interfaces.
- Customize the login logic in the `Interface()` function to match your authentication requirements.

Feel free to explore and modify the code according to your needs!

## License
This project is licensed under the [MIT License](LICENSE).


-----------------------------------------------
-----------------------------------------------

## Student Management System

This is a simple student management system application built using Python and Tkinter. The application allows you to perform various operations such as adding, searching, updating, and deleting student records. It also provides functionality to export the data to a CSV file.

### Requirements

- Python 3.x
- Tkinter library
- ttkthemes library
- pygame library
- pymysql library
- pandas library

### Installation

1. Clone the repository or download the source code files.
2. Install the required libraries by running the following command:
   ```
   pip install ttkthemes pygame pymysql pandas
   ```
3. Run the application by executing the following command:
   ```
   python test_student.py
   ```

### Features

- Connect to a MySQL database to store and retrieve student records.
- Add new student records by providing the required information.
- Search for student records using various criteria such as ID, name, email, etc.
- Update existing student records with new information.
- Delete student records from the database.
- Show all the student records in a tabular format.
- Export the student data to a CSV file.

### Usage

1. Launch the application by running the `test_student.py` script.
2. Click on the "Connect database" button to establish a connection to the MySQL database. Enter the hostname, username, and password for the database.
3. Once the database connection is established, you can perform the following operations:
   - Add Student: Click on the "Add Student" button to open a new window and enter the details of the student. Click the "Add" button to add the student to the database.
   - Search Student: Click on the "Search Student" button to open a new window and enter the search criteria. Click the "Search" button to find matching student records.
   - Delete Student: Select a student record from the displayed table and click the "Delete Student" button to delete the selected student from the database.
   - Update Student: Select a student record from the displayed table and click the "Update Student" button to open a new window with the selected student's details. Update the information and click the "Update" button to save the changes.
   - Show Student: Click on the "Show Student" button to display all the student records in a tabular format.
   - Export data: Click on the "Export data" button to save the student data to a CSV file. Choose the destination directory and enter the file name.
   - Exit: Click on the "Exit" button to close the application.

### Credits

- The application uses the Tkinter library for creating the GUI.
- The ttkthemes library is used to apply custom themes to the GUI.
- The pygame library is used to play a welcome sound when the application starts.
- The pymysql library is used to connect to the MySQL database.
- The pandas library is used for exporting the data to a CSV file.

### License

This project is licensed under the [MIT License](LICENSE).
