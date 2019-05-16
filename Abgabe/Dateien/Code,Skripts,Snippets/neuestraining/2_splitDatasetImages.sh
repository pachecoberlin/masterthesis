echo "
cd ../train/labels
for file in *; do mv ../../images/${file/txt/jpg} ../images/ ; done
cd ../images
find `pwd` -name \*.jpg | sort -R > ../../train.txt
cd ../../test/labels
for file in *; do mv ../../images/${file/txt/jpg} ../images/ ; done
cd ../images
find `pwd` -name \*.jpg | sort -R > ../../test.txt
"