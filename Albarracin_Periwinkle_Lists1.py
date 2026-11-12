


my_list = []

print("Enter 5 values:")
for i in range(5):
    value = input(f"Enter value {i + 1}: ")
    my_list.append(value)

# Display original list
print("\nOriginal List:", ", ".join(my_list))

# Input index to update
index = int(input("\nInput Index to Update: "))

# Check if index is valid
if 0 <= index < len(my_list):

    # Display selected element
    print("Selected Value:", my_list[index])

    # Input new value
    new_value = input("Input New Value: ")

    # Update list element
    my_list[index] = new_value

else:
    print("Invalid Index!")

# Input slice range
start = int(input("\nEnter Slice Range 1: "))
end = int(input("Enter Slice Range 2: "))

# Display sliced list
if 0 <= start <= end <= len(my_list):
    sliced_list = my_list[start:end]

    print("\nSliced List:", ", ".join(sliced_list))

    # Search for an item in the sliced list
    search_item = input("\nEnter Search Item: ")

    if search_item in sliced_list:
        print("Search Result (from sliced array):",
              search_item, "is found in the sliced list.")
    else:
        print("Search Result (from sliced array):",
              search_item, "is not found in the sliced list.")

else:
    print("Invalid Slice Range!")

# Display updated list
print("\nUpdated List:", ", ".join(my_list))
