# AS LIKE OTHER LANGUAGES COLLECTIONS ARE ALSO SUPPORTED IN THE PYTHON ]
# LANGUAGE AS LIST, DICT, TUPLES, RANGE, SET  ALL WITH THEIR EXTENDED TYPES


# LIST DEMOSTRATION
# works just like an resizeable array
# can contain mixed type of data 
array = ["MUhammad", 507, True]

array[2] # can be accessed like this

## METHODS
array.append(23) # to add elements later in the array
array.insert(0, "20-ARID-507") # to add element at specific index of the array
array.reverse() # this method reverses the array elements order
array.remove(507) # to remove a specific item or every occurence of the item
array.pop() # remove item that is entered or added or placed at last in the array or list

### to use sort method all elements of the list should be of the same type
# array.sort(reverse=True) # to sort in descending order or leave this parameter for ascending order
array.clear() # to empty the list




# TUPLES DEMONSTRATION
# tuples are type of data structure
# in which items or elements are ordered in place
# and once entered then a tuple can be changed, added, modified, removed
# can have duplicate values
# can also have mixed type of data
columns = ("studentRollNo", "studentName", "studentName", "studentClass")
columns = tuple(("studentRollNo", "studentName", "studentName", "studentClass"))

## methods
columns[1] # elements can be accessed like this

columns.count("studentRollNo") #will return the number of occurence of this string item in tuple
columns.index("studentName", 2, columns.__len__()-1) # will return the first occurence index of the value from the provided range of tuple indexes
columns.__sizeof__() # should returns size 

# can also be converted to a list to modify its data can be converted back to tuple then
columns_list = list(columns)
columns_list.insert(1, "studentName")
columns = tuple(columns_list)


# DICT (DICTIONARY) DEMOSTRATION
# dictionary is a type of mapped data structure
# with key-value pair where each unique key in the dictionary have
# a value associated with it or mapped to it
# must have unique keys that can be associated with the some multiple occurred values in the map
# works just like js objects or hashmaps or maps
students_data = {
    "studentName" : "Muhammad Bin Zulfiqar",
    "studentRollNo" : 507,
    "studentClass" : "BSCS-6A"
}

# methods
## used to access the element
students_data.get("studentName") # will return the name of the student
students_data.update(students_data) # used to update the current map with new key-value pairs
students_data.items() # returns ItemsView object representing all the values in the dict
# example accessing items on 1 index as like this all vkeys can be accessed on index 0
stu = students_data.items()
for x in stu:
    print(x[1])

students_data.keys() # use index 0 as used above 1 in place of it traverse all keys in the dict
students_data.pop("studentName", 10) # provide default argument incase the key is missing. actually it will pop out that particular key and will return its corresponding value
students_data.clear() # to clear all the key-values pairs sets from the dict


# SET DEMONSTRATION 
# a set is a type of data structure
# in which data is stored in the form of values that are unique in nature 
# with respect to their data types
# A items can be added or removed but cannot be changed
# all items should be unique
# also unordered and unchangeable

student_roll_no = {507, 528, 537, 557, "20-ARID-507", "20-ARID-537"}
student_roll_no = set((507, 528, 537, 557, "20-ARID-507", "20-ARID-537"))

# methods
student_roll_no.update({208,  "20-ARID-567", "20-ARID-537"}) # takes union of both objects
student_roll_no.add(507) # if the element is already present then there will be no effect
student_roll_no.discard(537) # remove an element if present and do nothing if not
# student_roll_no.remove(507) # don't use this method to remove element as it throws error if the element is not present in the set
student_roll_no.union({65765757, 507}) # will take the union of both set and will return the merged set with unique elements from both
student_roll_no.difference({208,  "20-ARID-567", "20-ARID-537"}) # will return the set with elements that are not present in the argument set
student_roll_no.intersection({507, 528}) # will return the set with elements that are common in both sets
student_roll_no.pop() # to pop or remove the last added element from the set
student_roll_no.symmetric_difference({507, 528}) # will return the set having the values that are not present in either of the sets with respect to each other. in simple taking a difference with respect to each other
student_roll_no.clear() # clears all elements from the set
## SHALLOW COPY means the change in the copy will not be reflected in the original set
copied_student_roll_no_set = student_roll_no.copy() # return a shallow copy or reference copy of the original mutable set items






