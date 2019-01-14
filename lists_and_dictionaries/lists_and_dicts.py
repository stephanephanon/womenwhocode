# Women Who Code Python Lab
# Python Lists and Dictonaries

# -----------------------------------------------------------------------
# Let's make a list
# -----------------------------------------------------------------------
# this is the syntax for creating a new list called "days_of_the_week"
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# 1. what is in the list?
print("1. -----Days of the Week-----")
print(days_of_the_week)

# 1b. what is the index of Monday?
# hint... python starts counting at 0
# 0

# 1c. what is the index of Friday?
# hint... python starts counting at 0
# 4

# 2. what is the item stored at days_of_the_week[2]? Print it out.
print("2. -----Item stored at days_of_week[2]-----")

# 2b. IndexError. What is the item stored at days_of_the_week[10]? 
# comment this one out when you are done. :)
print("2b. -----Item stored at days_of_week[10]-----")

# ---------------------------------------------------------------
# oops... we forgot the weekend! 
# 3. Let's add Saturday.
print("3. -----Added Saturday-----")

# 4. now add Sunday
print("4. -----Added Sunday-----")

# 5. what is the length of the list?
print("5. -----Length of list-----")

# ---------------------------------------------------------------
# Let's slice the list
# the slicing goes up to (but does not include) the last number
# eg, [0: 3] will give you (0, 1, 2)
# eg, [1: 5] will give you (1, 2, 3, 4)
# think: last_index - first_index = number of items

# get just the week days slice
print("6. -----Week days-----")

# and what about just the weekend slice?
print("7. -----Weekend days-----")

# ---------------------------------------------------------------
# let's get rid of Wednesday!
print("8. -----Removed that pesky Wednesday-----")

# well, maybe we should put it back. 
print("9. -----Just kidding, it's back-----")


print("---------------------------------------------------------------")
# ----------------------------------------------------------------------
# Let's make a dictionary
# ----------------------------------------------------------------------
# this is the syntax for creating a new dictionary called "contacts"
contacts = {
	"stephanie": "703-555-6789",
	"heather": "813-555-8989",
	"gina": "321-555-1234"
}

# 1. what is in the dictionary?
print("1. -----Contacts Dictionary-----")

# 2. how many items are in the dictionary?
print("2. -----Number of contacts-----")

# 3. what are the keys of the dictionary?
print("3. -----Contacts Keys-----")

# 4. What are the values?
print("4. -----Contacts Values-----")

# 5. Let's add a new friend named 'sri'
print("5. -----Added a new item-----")

# 6. Let's update Gina's phone number. She moved to DC.
print("6. -----Updated a value")

# 7. Let's remove stephanie. i know my own number
print("7. -----Removed myself-----")

print("---------------------------------------------------------------")
# ----------------------------------------------------------------------
# Let's make a nested dictionary
# ----------------------------------------------------------------------
# 1. let's make a new contact list that can handle phone and email
# Notice that gina does NOT have an email key. keys are not required fields.
updated_contacts = {
	"stephanie": {
		"phone": "703-555-6789",
		"email": "steph@email.com"
		},
	"heather": {
		"phone": "321-555-1234",
		"email": "heather@gmail.com"
	},
	"gina": {
		"phone": "202-555-2917"
	}

}

print("1. -----Nested dictionary example-----")

# 2. get stephanie's email
print("2. -----Stephanie's nested email-----")

# 3. update heather's phone number. She moved to DC, too.
print("3. -----Heather's new phone-----")

# 4. add sri's dictionary to this new phone book. 
# "sri" is the key, and the value is her dictionary of key/value pairs
# her number is 703-555-9999
# her email is "sri@sri.com"
# her twitter is @sri
print("4. -----Sri's new contact-----")

# 5. oops, remove sri's twitter. she doesn't want it in the contacts
# get sri's dictionary, then pop the twitter key
print("5. -----Sri's new contact-----")

# 6. KeyError. Try to get gina's email using bracket syntax. 
# this one with raise an exception because gina doesn't have an email key
# comment this one out when you are done. :)
print("6. -----Gina's email-----")

# 6b. Get gina's email with a default of "No email". Print it out.


