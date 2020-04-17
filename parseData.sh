
# to be run after 2pm BST

python3 parseData.py > test.log
git add .
git commit -m 'data parsed'
git push
