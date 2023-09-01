import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Gju4kbkwy3",
    "database": "python"
}

def add_task(cursor, connection):
    task = input("Enter the Task: ")  # Changed 'x' to task
    insert_query = "INSERT INTO todolist (task) VALUES (%s)"
    data = (task,)  # Put task in a tuple
    cursor.execute(insert_query, data)
    connection.commit()
    print("Task added successfully!")

def delete_task(cursor, connection):
    task = input("Enter the Task to Remove: ")
    delete_query = "DELETE FROM todolist WHERE task = %s"
    cursor.execute(delete_query, (task,))  # Use a tuple here
    connection.commit()
    print("Task deleted successfully!")

def update_task(cursor, connection):
    new = input("Enter the new Task to update: ")
    old = input("Enter Old Task to update: ")
    update_query = "UPDATE todolist SET task = %s WHERE task = %s"  # Corrected table name and columns
    cursor.execute(update_query, (new, old))
    connection.commit()
    print("Task updated successfully!")

def display_task(cursor):
    select_query = "SELECT * FROM todolist"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    

def main():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Changed int(input(...)) to input(...)

        if choice == "1":
            add_task(cursor, connection)
        elif choice == "2":
            delete_task(cursor, connection)
        elif choice == "3":
            print("******todolist********")
            display_task(cursor)
        elif choice == "4":
            update_task(cursor, connection)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()