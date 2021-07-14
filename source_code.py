import csv
import os
import shutil

f_append=open('Storage_Unit.csv','a')
f_read=open('Storage_Unit.csv','r')
os.chdir('/home/xonynix/Desktop/Python Projects/Phone Book/edited csv file')
f_edit=open('Storage_Unit.csv','w+')
os.chdir('/home/xonynix/Desktop/Python Projects/Phone Book')
csv_writer=csv.writer(f_append, delimiter=",")
csv_editer=csv.writer(f_edit,delimiter=',')
csv_reader=csv.reader(f_read)
csv_value=list(csv_reader)
csv_editer_reader = csv.reader(f_edit)
csv_editer_value = list(csv_editer_reader)
source = r'/home/xonynix/Desktop/Python Projects/Phone Book/edited csv file/Storage_Unit.csv'
phone_number=[]
people = []
for i in range(len(csv_value)):
    phone_number.append(csv_value[i-1][1])
    people.append(csv_value[i-1][0])



class ph_book:
    def write():
        name_input = input('Write owners name: ').lower()
        phone_number_input = input('Phone Number: ').lower()
        if phone_number_input in phone_number:
            print("Phone NUmber Already Exists in Directory")
        elif phone_number_input not in phone_number:
            csv_writer.writerow([name_input, phone_number_input])


    def find():
        name_input_find=input("Whose number to find? ").lower()
        if name_input_find in people:
            index_to_find=people.index(name_input_find)
            print(csv_value[index_to_find-1][1])
        elif name_input_find not in people:
            print("Number Not Found")


    def edit():
        input_edit_type=input("What to Edit? ").lower()
        if input_edit_type =="name":
            mode="name"
        elif input_edit_type =="phone" or "phone number":
            mode="phone"
        if mode == "name":
            phonenumber_name=input("Which phone number's nme to Change? ").lower()
            if phonenumber_name in phone_number:
                new_name = input("What will be the new Owners Name? ").lower()
                phone_number_index=phone_number.index(phonenumber_name)
                csv_value[phone_number_index-1][0] = new_name.capitalize()
                print("Name Changed Successfully")
            elif phonenumber_name not in phone_number:
                print("Phone Number Not Found")
        elif mode=="phone":
            number_owner = input("Whose number to change? ").lower()
            if number_owner in people:
                new_phone_number=input("What will new phone number be? ")
                owner_index=people.index(number_owner)
                csv_value[owner_index-1][1] = new_phone_number
                print("Phone Number Edited Successfully")
            elif number_owner not in people:
                print("Person's Details not in Directory")
        for i in csv_value:
            csv_editer.writerow(i)
        f_edit.close()
        shutil.copy(source,os.getcwd())
        
    def delete():
        data_to_delete = input('Whose data to delete? ')
        if data_to_delete not in people:
            print("Person's details doesn't exist. ")
        elif data_to_delete in people:
            index_to_delete = people.index(data_to_delete) - 1
        del csv_value[index_to_delete]
        for i in csv_value:
            csv_editer.writerow(i)
        f_edit.close()
        shutil.copy(source,os.getcwd())

print('''Commands:
Write - To write new Entries
Find - To find Data
Edit - To edit data
Delete - To delete Data''')

command = input("What to do? ").lower()

if command == 'write':
    ph_book.write()
elif command == 'find':
    ph_book.find()
elif command == 'edit':
    ph_book.edit()
elif command == 'delete':
    ph_book.delete()

f_edit.close()
f_read.close()
f_append.close()