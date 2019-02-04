rm cyclists/* -r
mkdir cyclists/train
mkdir cyclists/train/images
mkdir cyclists/train/labels
mkdir cyclists/test
mkdir cyclists/test/images
mkdir cyclists/test/labels
cp selfmade/* cyclists/ -r
cd cyclists/labels
shuf -zen10000 * | xargs -0 mv -t ../test/labels
mv * ../train/labels
