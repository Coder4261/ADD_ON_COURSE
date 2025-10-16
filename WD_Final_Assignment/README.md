# add_on_course_assignment

This repository is a copy of the WD_Final_Assignment workspace on the user's machine. It contains two small Flask projects:

- `BMI_Calculator/` — Flask app to calculate BMI
- `ToDo_List/` — Flask ToDo list app

How to push these files to GitHub

1. Install Git for Windows: https://git-scm.com/download/win
2. (Optional) Install GitHub CLI: https://cli.github.com/
3. In PowerShell run:

```powershell
cd 'C:\Users\sanja\Desktop\WD_Final_Assignment'
git init
git add .
git commit -m "Initial commit of WD_Final_Assignment"
# Create remote with gh (optional):
# gh repo create add_on_course_assignment --public --source=. --remote=origin --push
# OR create repo on github.com and then:
# git remote add origin https://github.com/<your-username>/add_on_course_assignment.git
# git push -u origin main
```

If you want, I can continue and attempt to create the remote for you once you confirm Git/gh are installed and you're comfortable providing any needed details for remote creation.