from sys import argv
script, user_name, adjective = argv
prompt = '>? '
prompt1 = " ?<3? "

print(f"Hi {user_name}, I'm the {script} script software.")
print(f"I'd like to ask you a {adjective} questions: ")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input (prompt)

print ("What kinde of a pet do you have?")
pet = input(prompt1)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not shure where that is.
And you have a {computer}. Nice.
Ok than, your {pet} from now is a debuging pet! :D
""")
