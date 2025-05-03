with open("hw_debug_dump.bin", "rb") as file:
    data = file.read(1024)  # Read the first 1KB of the file
    print(data[:100])       # Print the first 100 bytes