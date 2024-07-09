import subprocess

print("git add commit and push")
add = input("do you want to add everything? (Y/n) : ").strip().lower()
if add == "n":
	files = input("enter files to add (separated by space): ")
	subprocess.run(["git", "add"] + files.split())
else:
	subprocess.run(["git", "add", "."])
commit = input("enter commit message: ")
subprocess.run(["git", "commit", "-m", commit])
push = input("do u want to push your code? (Y/n) : ").strip().lower()
if push != "n":
	subprocess.run(["git","push","-u","origin"])
print("all done.")
