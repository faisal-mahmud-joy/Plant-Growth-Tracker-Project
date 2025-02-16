import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store plant data
FILE_NAME = "plant_growth_data.txt"

# Ensure the CSV file exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Plant Name", "Height (cm)", "Notes"])
    df.to_csv(FILE_NAME, index=False)


# Function to add new plant growth data
def add_plant_data():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            pd.to_datetime(date)  # Validate date format
            break
        except ValueError:
            print("Invalid date format! Please enter in YYYY-MM-DD format.")

    plant_name = input("Enter plant name: ")

    while True:
        height = input("Enter plant height (cm): ")
        if height.replace(".", "", 1).isdigit():
            height = float(height)
            break
        print("Please enter a valid numeric height.")

    notes = input("Enter notes (optional): ")

    # Append data to TEXT file
    df = pd.read_txt(FILE_NAME)
    new_entry = pd.DataFrame([[date, plant_name, height, notes]], columns=df.columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("\nData added successfully.\n")


# Function to display stored plant data
def view_data():
    df = pd.read_txt(FILE_NAME)
    if df.empty:
        print("\nNo data available.\n")
    else:
        print("\nPlant Growth Data:\n")
        print(df.to_string(index=False))


# Function to visualize growth trends
def plot_growth():
    df = pd.read_txt(FILE_NAME)

    if df.empty:
        print("\nNo data available to plot.\n")
        return

    plant_name = input("Enter plant name to visualize growth: ")

    # Filter data for the selected plant
    df_plant = df[df["Plant Name"].str.lower() == plant_name.lower()]

    if df_plant.empty:
        print("\nNo data found for this plant.\n")
        return

    # Convert Date and Height columns to correct data types
    df_plant["Date"] = pd.to_datetime(df_plant["Date"])
    df_plant["Height (cm)"] = pd.to_numeric(df_plant["Height (cm)"])

    # Sort data by date
    df_plant = df_plant.sort_values(by="Date")

    # Plot the growth trend
    plt.figure(figsize=(8, 5))
    plt.plot(df_plant["Date"], df_plant["Height (cm)"], marker="o", linestyle="-", color="g", label=plant_name)

    plt.xlabel("Date")
    plt.ylabel("Height (cm)")
    plt.title(f"Growth Trend of {plant_name.capitalize()}")
    plt.legend()
    plt.grid()

    plt.xticks(rotation=45)
    plt.show()


# Main menu loop
while True:
    print("\nPlant Growth Tracker")
    print("1. Add Plant Data")
    print("2. View Data")
    print("3. Visualize Growth")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_plant_data()
    elif choice == "2":
        view_data()
    elif choice == "3":
        plot_growth()
    elif choice == "4":
        print("\nExiting... Thank you.\n")
        break
    else:
        print("\nInvalid choice! Please enter a number from 1 to 4.\n")