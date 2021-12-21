# Machine-Learning-Projects

For an advanced Machine Learning course I completed 4 machine learning projects ranging from implementing simple supervised machine learning solutions such as KNNs to complicated CNN models such as SqueezeNet and AlexNet. The code for all 4 projects can be found in this repo. Each project has a `Report.pdf` file which outlines the content of each project in great detail. Below is a higher level decription of each of the 4 projects.

## 1. KNNs and Decision Trees
In this project we implemented a custom cross validation method in addition to applying two machine learning classifcation models, KNNs and Decision Trees. The two datasets used for this project were the [Adult](https://archive.ics.uci.edu/ml/datasets/Adult) and [Clothing Fit](https://www.kaggle.com/rmisra/clothing-fit-dataset-for-size-recommendation) datasets. Both models were evaluated on both datasets using using our custom cross validation method to provide us with an F1 score as a measure of model accuracy. 

## 2. Gradient Descent and NLP
This project explored different gradient descent algorithms and compares their convergence speed on a logistic regression model. The classification task was to determine whether or not a person has diabetes given 8 features of medical information. Mini batch stochastic gradient descent and momentum was analyzed to see how these variations affect convergence speed and accuracy. The second part of this project analyzed different text pre-processing techniques and how they can improve the accuracy of alogistic regression model classifying sentences into 2 classes; human generated and computer generated.

## 3. CNN for MNIST dataset with 2 handwritten digits per image
Here we perfomed multi-label image classification using a neural network. The primary task consisted of correctly identifying the digit and letter from the English
language present on each input image. This objective was achieved by experimenting with different layers of various size, tuning many hyper-parameters, and observing the effects of various deep learning techniques to achieve a satisfactory model. After much tweaking via trial and error, we were able to achieve a test accuracy of 86.933% on our dataset by using several hidden layers and various data augmentation techniques.

## 4. SqueezeNet and other well-established CNNs
In this project, we compared the SqueezeNet architecture with a number of popular architectures, as well as our own modified SqueezeNet, on the CIFAR10 and the Fashion-MNIST datasets. We compared the models based on accuracy giving importance to model size since this is integral for better deployment of AI in everyday life. Our results found that SqueezeNet was able to perform similarly to other much larger CNN architectures such as AlexNet with 78 times less parameters. Our customized CNN ‘ISS’ was able to emulate this with minor modifications showcasing a systematic approach to building CNN architectures.
