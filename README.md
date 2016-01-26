# ML_Project

Implementation of a content based image classifier using the bag of visual words model in Python.

/* THIS WORK IS SIMILAR TO SHACKENBERG'S Minimal-Bag-of-Visual-Words-Image-Classifier 

The script learn.py will generate a visual vocabulary and train a classifier using a user provided set of already classified images.
After the learning phase classify.py will use the generated vocabulary and the trained classifier to predict the class for any image 
given to the script by the user.

The learning consists of:

1)Extracting local features of all the dataset images
2)Generating a codebook of visual words with clustering of the features
3)Aggregating the histograms of the visual words for each of the traning images
4)Feeding the histograms to the classifier to train a model

The classification consists of:

1)Extracting local features of the to be classified image
2)Aggregating the histograms of the visual words for the image using the prior generated codebook
3)Feeding the histogram to the classifier to predict a class for the image

This code relies on:

1)SIFT features for local features
2)k-means for generation of the words via clustering
3)SVM as classifier using the LIBSVM library

Example use:

You train the classifier for a specific dataset with:
python learn.py -d path_to_folders_with_images

To classify images use:
python classify.py -c path_to_folders_with_images/codebook.file -m path_to_folders_with_images/trainingdata.svm.model images_you_want_to_classify

References:

Libsvm:
Chih-Chung Chang and Chih-Jen Lin, LIBSVM : a library for support vector machines. ACM Transactions on Intelligent Systems and Technology, 2:27:1--27:27, 2011. Software available at http://www.csie.ntu.edu.tw/~cjlin/libsvm
SIFT:
David G. Lowe, "Distinctive image features from scale-invariant keypoints," International Journal of Computer Vision, 60, 2 (2004), pp. 91-110.
sift.py:
Taken from http://www.janeriksolem.net/2009/02/sift-python-implementation.html
libsvm.py:
Addapted from easy.py contained in the LIBSVM packet by Chih-Chung Chang and Chih-Jen Lin.
