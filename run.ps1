Set-Location -Path $PSScriptRoot
git pull 
python main.py
git add . 
git commit -m "update"
git push 