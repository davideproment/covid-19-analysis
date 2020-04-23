#!/usr/local/bin/python3
#!/usr/bin/git

# to be run after 5.30pm BST
python3 ./updateFigure.py
python3 ./updateREADME.py
git add .
git commit -m 'analysis updated'
git push
