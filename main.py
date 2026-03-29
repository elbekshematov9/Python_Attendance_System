import csv

def load_names(file_path):
    names = set()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # avoid empty lines
                names.add(row[0].strip().lower())
    return names


def mark_attendance(students_file, attendance_file, output_file):
    students = load_names(students_file)
    attendance = load_names(attendance_file)

    with open(students_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row:
                name = row[0].strip().lower()
                status = "+" if name in attendance else "-"
                writer.writerow([row[0], status])


if __name__ == "__main__":
    students_file = "students.csv"
    attendance_file = "attendance.csv"
    output_file = "result.csv"

    mark_attendance(students_file, attendance_file, output_file)

    print("✅ Attendance processing completed! Check result.csv")
