new_member=input("Add a new member: ")

file=open("files/members.txt","r")
existing_member=file.readlines()
file.close()

existing_member.append(new_member+"\n")

file=open("files/members.txt","w")
existing_member=file.writelines(existing_member)
file.close()