monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")

print(f"Monday class:", monday_class)

print(f"Wednesday class:", wednesday_class)

print(f"Attended both classes:", monday_class & wednesday_class)

print(f"Attended either class:", monday_class | wednesday_class)

print(f"Only Monday:", monday_class - wednesday_class)

print(f"Only one class (not both):", monday_class ^ wednesday_class)

all_classes = monday_class | wednesday_class
print(f"Is Monday subset of all students?", monday_class <= all_classes)