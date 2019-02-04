rm test.tmp
rm train.tmp
rm train.list
rm test.list
cat benchmark/valid.txt >> test.tmp
cat benchmark/test.txt >> test.tmp
cat benchmark/train.txt >> train.tmp
cat cyclists/test.txt >> test.tmp
cat cyclists/train.txt >> train.tmp
cat train.tmp | sort -R > train.list
cat test.tmp | sort -R > test.list
