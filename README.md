# -bitbucket
#image blur detection
# i am putting it in the public format
# here features are image size  and number of pixel it occupies and shape
#the project consist four parts 
#1 classsification-KNN classifier
#2 traing
#3 testing and validation
#4 find accuracy
#here we use train and test the data in dataset
#first convert the data folder into .jar file
#install openCV and then create file name as detect_blur.py
#import packages tensorflow,sklearn,keras and imulits and gensim
#classification is run as $python ml6-img_classifier.py
#execuete code as python detect_blur.py
# it can be trained by tensorflow 
#for that one we have to download tensorflow package
#then train run script as
#$ python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/flower_photos
  # now for find the accuracy 
  #$ python  detect_blur.py
