Pull Project
- git clone [Repository URL]

Create a new branch 
- git branch <new-branch-name>

Return which branch you're working in:
- git status
  - Shows amount of commits 

Add changes:
- git add .

Snapshot code status at a particular time
- git commit -m "Write a message"

Make sure you verify which branch you're working in:
- git branch 

Then, push changes to repository on GitHub:
- git push

Create an empty file in Powershell:
- wsl touch [file_name.type]

Observe results of code for a commit in time
- git log
   - Copy Hash for the commit, then run:
	- git checkout <branch-name -OR- hash>
