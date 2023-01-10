# Make-an-app-for-covid-images-classifucation-using-flask


Machine Learning (ML) is a great way to do tasks that cannot be explicitly coded, for example, image classification. But when the model is already built, it will be useless when we don’t deploy it into an application.

Deployment is an essential step in the machine learning workflow. It is a step where we want to apply our ML model into an application. Afterwards, we can use the model in real life.

But how can we create the model as an application? We can build an Application Programming Interface (API). With that, we can access the model from everywhere, whether it is on the mobile application or even on the web application. In Python, there’s a library that can help us to build an API. It’s called Flask.

This respotirary will show you how to build a REST API for our machine learning model using Flask. Without further ado, let’s get started!

REST API
Before we get into the implementation, let me explain REST API. REST API stands for Representational State Transfer Application Programming Interface.

The mechanism of REST API looks like this. Let’s say you want to search cat photos on Google. The first step is to send a request to Google by giving them a query like ‘cat photos’. Then, the server will send you a response to your computer, which is the compilation of cat photos.

That’s all about the REST API! It’s the way to communicate between you as the client by requesting something to the server, and then the server will send you the response. Here is an illustration of how the REST API works.

# Create a virtual enviroment 

We need to create a virtual enviroment to save all we need to make our app in that enviroment. We also need to install all library we need in this mentioned enviroment. For example by following command, I created the virtual enviroment in myproject folder. 
(base) C:\Users\Home\myproject>virtualenv venv
Then we need to activate it. 

# load a model
You need to save the output of your model which is aready trained in a desired direction. In this case the output in the pythorch output called ##covid_resnet18_epoch30.pt. Then, you need to have your model in a same direction you have app.py. The name of my model file is model_conv.

# dataset
We also need to have our images in our desired location or upload it the http://127.0.0.1:5000/ to see the prediction.
