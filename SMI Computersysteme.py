
file_name = "log.txt"


error_count = 0
warning_count = 0
info_count = 0


errors = []

try:

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            # Check type of log
            if line.startswith("ERROR"):
                error_count += 1
                errors.append(line)

            elif line.startswith("WARNING"):
                warning_count += 1

            elif line.startswith("INFO"):
                info_count += 1


    print("=== Log Report ===")
    print("Errors:", error_count)
    print("Warnings:", warning_count)
    print("Info:", info_count)

    print("\nCritical Issues:")
    for error in errors:
        print("-", error)

except FileNotFoundError:
    print("File not found. Please check the file name.")