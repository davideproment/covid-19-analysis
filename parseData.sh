#!/usr/local/bin/python3
#!/usr/bin/git

# to be run after 2pm BST
python3 ./parseData.py
git add .
git commit -m 'data parsed'
git push
