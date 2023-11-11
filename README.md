[![Version](https://img.shields.io/badge/Version-0.0.0-blue)](https://83hn4m.streamlit.app)
[![Status](https://img.shields.io/badge/Status-cold_start-yellow)](https://83hn4m.streamlit.app)
[![Revision](https://img.shields.io/badge/Last_Edit-Nov_2023-green)](https://83hn4m.streamlit.app)

# Toolbox
I keep my tools here, feel free to use.

## Streamlit process
Just clone the repo in your system, open a terminal in the folder:
```
streamlit run Toolbox.py
```
That's it!

## Github process

### 1- New Repo:
```
git init
git add .
git status
git commit -m “first commit”
git branch -M main
git remote add origin [https://repo.git]
git push -u origin main
```

### 2- Update Repo:
```
git status
git add .
git status
git commit -m "Vx.x.x - comment”
git push -u origin main
```

### 3- Restore to commit:
```
git reset --hard <commit-sha1-id>
git push origin HEAD --force
```
