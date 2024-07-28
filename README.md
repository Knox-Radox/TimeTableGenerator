# TimeTableGenerator

## Project Overview

The Python Time Table Generator is a web-based application designed using Django, a high-level Python web framework. The main objective of this project is to facilitate the generation of timetables for school classes while ensuring no clashes in periods for different classes or teachers. Additionally, the system supports dynamic management of subjects, teachers, classes, and sections, allowing users to update and configure these elements as needed.

## Deployment

**Step-1** : pip install -r requirements.txt.
**Step-2** : pip install mysqlclient(included in folder ONLY FOR PYTHON 3.11).
**Step-3** : configure mysql creds in settings.py to view locally in mysql.
**Step-4** : python manage.py runserver.

## Key Features

1. **Timetable Generation**:
   - **Conflict-Free Scheduling**: The core feature of the application is to generate conflict-free timetables. The algorithm ensures that no two classes or teachers have overlapping periods.
   - **Automatic Optimization**: The system employs optimization techniques to create balanced timetables that distribute periods evenly across the available time slots.

2. **Dynamic Management**:
   - **Subject Management**: Users can add, update, and remove subjects as required. Each subject can be associated with specific classes and teachers.
   - **Teacher Management**: Teachers can be added, updated, or removed from the system. The scheduling algorithm takes into account teacher availability and prevents double-booking.
   - **Class and Section Management**: New classes and sections can be added, and existing ones can be modified. Each class can have multiple sections, and the timetable generator considers these sections while creating schedules.

3. **User Interface**:
   - **Admin Dashboard**: Provides an interface for administrators to manage subjects, teachers, classes, and sections.
   - **Timetable View**: Users can view the generated timetable in a user-friendly format, typically using a calendar view or table format.

4. **Conflict Detection and Resolution**:
   - **Real-Time Conflict Checking**: The application performs real-time checks to detect conflicts during timetable generation and suggests possible resolutions.
   - **Feedback Mechanism**: Users can provide feedback or manually adjust the timetable if conflicts are detected after initial generation.

## Technical Architecture

1. **Django Framework**:
   - **Model Layer**: Utilizes Django’s ORM to define models for Subjects, Teachers, Classes, Sections, and Timetable Entries. These models handle database interactions and data integrity.
   - **View Layer**: Implements views for managing and displaying subjects, teachers, classes, and timetables. The views handle user requests and responses, including rendering HTML templates and processing form submissions.
   - **Controller Layer**: Django’s URL routing system directs requests to the appropriate views. Middleware handles user authentication and authorization.

2. **Database**:
   - **Database Management**: Uses Django’s built-in support for storing Tables in MySQL. The database schema is designed to efficiently store and retrieve data related to subjects, teachers, classes, sections, and timetables.
   - **Data Integrity**: Ensures referential integrity between related tables (e.g., ensuring that timetable entries are linked to existing subjects, teachers, and classes).

3. **Algorithm Design**:
   - **Scheduling Algorithm**: Implements a constraint satisfaction problem (CSP) approach or similar optimization techniques to generate conflict-free timetables. The algorithm considers teacher availability, classroom availability, and subject requirements.
   - **Heuristic Methods**: May incorporate heuristic or metaheuristic methods (e.g., genetic algorithms, simulated annealing) to improve the quality of the timetable and optimize scheduling.

4. **Front-End Technologies**:
   - **HTML**: For creating interactive and responsive user interfaces. Libraries such as Bootstrap may be used for styling, while JavaScript frameworks (e.g., jQuery) can enhance user interactions.

5. **Deployment**:
   - **Hosting**: The application can be deployed on various platforms such as Heroku, AWS, or a dedicated server. Docker containers can be used for consistent deployment environments.
   - **Continuous Integration/Deployment**: Utilizes CI/CD pipelines to automate testing, building, and deployment processes, ensuring that new features and fixes are efficiently delivered.

## Conclusion

The Python Time Table Generator project, built with Django, offers a comprehensive solution for creating and managing school timetables. By leveraging Django's robust features and implementing advanced scheduling algorithms, the project aims to streamline the scheduling process, reduce conflicts, and provide flexibility in managing school resources.
