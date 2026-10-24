# Grazioso Salvare Rescue Dashboard

**Created by:** Shatoria Giles  
**Course:** CS-340 Client/Server Development

## About the Project

This project is a dashboard that helps Grazioso Salvare find dogs for search-and-rescue training. It uses information from the Austin Animal Center database.

The dashboard lets users choose different rescue types and see dogs that match the requirements.

## Tools Used

- Python: Used to write the application.
- MongoDB: Stores the animal shelter information.
- PyMongo: Connects Python to MongoDB.
- Dash: Creates the interactive dashboard.
- Pandas: Organizes the data.
- Plotly: Creates the charts and map.

## How the Dashboard Works

The dashboard has four filtering choices: Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking, and Reset.

When a user selects a filter, the dashboard searches MongoDB and updates the animal table, breed chart, and location map.

The table also includes pagination and sorting to make the data easier to use.

## How to Run the Project

1. Set up MongoDB and import the animal shelter data.
2. Create the `aacuser` database account.
3. Install the required Python libraries.
4. Set the MongoDB connection credentials in the application.
5. Open `ProjectTwoDashboard.ipynb` in Jupyter.
6. Run the notebook cells.
7. Open the dashboard link.

## Screenshots

### Starting Dashboard
Insert starting dashboard screenshot here.

### Water Rescue
Insert Water Rescue screenshot here.

### Mountain or Wilderness Rescue
Insert Mountain Rescue screenshot here.

### Disaster or Individual Tracking
Insert Disaster screenshot here.

### Reset
Insert Reset screenshot here.

## Challenges and Solutions

Describe any problems you encountered while connecting the database, creating the filters, or displaying the charts. Explain how you fixed them.

## Conclusion

This project demonstrates how Python, MongoDB, and Dash can work together to build a database-driven web application. The dashboard provides an easy way to search and visualize animal shelter information.