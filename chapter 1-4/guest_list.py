#creating a lost of guests to invite to the dinner 
guests = ['kofi', 'josh' , 'king', 'ray']
print (f"hello {guests[0]}, you have been invited to the dinner of the century ")
print (f"hello {guests[1]}, you have been invited to the dinner of the century ")
print (f"hello {guests[2]}, you have been invited to the dinner of the century ")
print (f"hello {guests[3]}, you have been invited to the dinner of the century ")

#Kofi will not be able to make it to the dinner so his name needs to be exwmpted form the list and replaced
unlist =  guests.pop(0)
print (f"\n\nunfortunately, {unlist.title()} would not be able to make it to the dinner")

guests.insert(0, 'roger')

#print new messages to the attendees
print (f"\nhello {guests[0].title()}, you have been invited to the dinner of the century ")
print (f"hello {guests[1].title()}, you have been invited to the dinner of the century ")
print (f"hello {guests[2].title()}, you have been invited to the dinner of the century ")
print (f"hello {guests[3].title()}, you have been invited to the dinner of the century ")

print ("\nhello everyone, i have found a bigger a table")

#found a bigger table so i can invite more guests to the dinner. inserting at the beginning, the middle and the end of the list
guests.insert(0,'jeremy')
guests.insert(3,'kyle')
guests.append('jessie')

#printing a new message for the new attendees
print (f"\nhello {guests[0].title()}, you have an invite to the bigger table")
print (f"hello {guests[1].title()}, you have an invite to the bigger table")
print (f"hello {guests[2].title()}, you have an invite to the bigger table")
print (f"hello {guests[3].title()}, you have an invite to the bigger table")
print (f"hello {guests[4].title()}, you have an invite to the bigger table")
print (f"hello {guests[5].title()}, you have an invite to the bigger table")
print (f"hello {guests[6].title()}, you have an invite to the bigger table")

#unfortunately i can only nvite 2 people now due to unfortunate circumstances
#popping the uninvited guests into a new list(uninvited) and printing a message to tell them they are no longer invited

uninvited = [guests.pop(6), guests.pop(5),guests.pop(4),guests.pop(3),guests.pop(2)]
print(f"\nSorry {uninvited[0].title()}, unfortunately you cannot come to the dinner anymore")
print(f"Sorry {uninvited[1].title()}, unfortunately you cannot come to the dinner anymore")
print(f"Sorry {uninvited[2].title()}, unfortunately you cannot come to the dinner anymore")
print(f"Sorry {uninvited[3].title()}, unfortunately you cannot come to the dinner anymore")
print(f"Sorry {uninvited[4].title()}, unfortunately you cannot come to the dinner anymore")


#message to 2 invitees left 
print (f"\nhello {guests[0].title()}, you are still invited to the dinner")
print (f"hello {guests[1].title()}, you are still invited to the dinner")

#remove remaining guests
del guests[0]
del guests[0]
print (guests)