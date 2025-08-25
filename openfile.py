def file_read_write():
    try:
        # Ask user for input filename
        input_file = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Define output filename
        output_file = "modified_" + input_file

        # Write modified content to new file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File processed successfully. Modified version saved as '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the program
file_read_write()
