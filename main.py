import pandas as pd
import matplotlib.pyplot as plt

# 1. Read student data
df = pd.read_csv("students.csv")


# 2. Update student marks
update_name = input("Enter student name to update: ")
student_exists = df["Name"].str.lower().eq(update_name.lower()).any()

if student_exists:
    try:
        new_marks = int(input("Enter new marks (0-100): "))

        if 0 <= new_marks <= 100:
            df.loc[
                df["Name"].str.lower() == update_name.lower(),
                "Marks"
            ] = new_marks

            df.to_csv("students.csv", index=False)
            print("Marks updated successfully!")

        else:
            print("Invalid marks! Enter marks between 0 and 100.")

    except ValueError:
        print("Please enter marks as a whole number.")

else:
    print("Student not found! Marks not updated.")


# 3. Average, highest and lowest marks
def show_average(data):
    average = data["Marks"].mean()
    print("Average Marks:", round(average, 2))


show_average(df)
print("\nStudent Data:")
print(df)

print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())


# 4. Topper
topper = df.loc[df["Marks"].idxmax()]
print("\nTopper:", topper["Name"])
print("Topper Marks:", topper["Marks"])


# 5. Sort students by marks
print("\nStudents Sorted by Marks:")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)


# 6. Calculate grades
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


df["Grade"] = df["Marks"].apply(calculate_grade)

print("\nStudent Grades:")
print(df[["Name", "Marks", "Grade"]])


# 7. Pass or Fail
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print("\nStudent Results:")
print(df[["Name", "Marks", "Grade", "Result"]])

pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("Total Passed:", pass_count)
print("Total Failed:", fail_count)


# 8. Bar chart of marks
chart_df = df.sort_values(by="Marks", ascending=False)

bars = plt.bar(chart_df["Name"], chart_df["Marks"])
plt.bar_label(bars)

average = df["Marks"].mean()
plt.axhline(
    y=average,
    linestyle="--",
    label=f"Average: {average:.2f}"
)

plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.legend()
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()


# 9. Calculate percentage
df["Percentage"] = df["Marks"]

print("\nStudent Percentage:")
print(df[["Name", "Marks", "Percentage"]])


# 10. Students scoring 80 or above
high_scorers = df[df["Marks"] >= 80]

print("\nStudents Scoring 80 or Above:")
print(high_scorers[["Name", "Marks", "Grade"]])


# 11. Save complete results
df.to_csv("student_results.csv", index=False)
print("\nStudent results saved successfully!")


# 12. Read saved results
saved_data = pd.read_csv("student_results.csv")

print("\nData Read From CSV:")
print(saved_data)


# 13. Search for a student
search_name = input("\nEnter student name to search: ")

student = df[df["Name"].str.lower() == search_name.lower()]

if not student.empty:
    print("\nStudent Found:")
    print(student[["Name", "Marks", "Grade", "Result"]])
else:
    print("Student not found!")


# 14. Student rankings
df["Rank"] = df["Marks"].rank(
    ascending=False,
    method="dense"
).astype(int)

print("\nStudent Rankings:")
print(df[["Name", "Marks", "Rank"]].sort_values("Rank"))


# 15. Marks summary
print("\nMarks Summary:")
print(df["Marks"].describe().round(2))


# 16. Pass vs Fail pie chart
result_counts = df["Result"].value_counts()

plt.pie(
    result_counts,
    labels=result_counts.index,
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail")
plt.tight_layout()
plt.savefig("pass_fail_chart.png")
plt.show()
