# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:18:12 2022

@author: Home
"""

from flask import Flask, jsonify, request, render_template
import torch
from PIL import Image
from torchvision import transforms
from torch.autograd import Variable

print('loading the model.....')

model_conv = torch.load('covid_resnet18_epoch30.pt')
model_conv.eval()
imsize= 224
class_names = ['covid','non-covid']
loader = transforms.Compose([transforms.Resize(imsize), 
                             transforms.CenterCrop(224), 
                             transforms.ToTensor(),
                             transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

def image_loader(image_name):
    """load image, returns cuda tensor"""
    image = Image.open(image_name).convert("RGB")
    image = loader(image).float()
    image = Variable(image, requires_grad=True)
    image = image.unsqueeze(0)  #this is for VGG, may not be needed for ResNet
    return image
sm = torch.nn.Softmax()

def predict_result(image):
    
    model_output= model_conv(image)
    cur_pred = model_output.max(1, keepdim=True)[1]# Returns the maximum value of all elements in the input tensor 
                                                     #If keepdim is True, the output tensors are of the same size as input
    return "Covid predicted label:", ( class_names[int(cur_pred.data.numpy())])
    
          
app = Flask(__name__)

@app.route('/predict', methods=["POST"])

def infer_image():
   
       if "album" not in request.files:
           return "Bad Request", 400
       file=request.files["album"]
       if not file:
          return
       
       cur_img= image_loader(file)
       prediction=predict_result(cur_img)
    
       return jsonify(prediction)
         
   
@app.route('/', methods=['GET'])
def website():
      return render_template('website.html', name="Homa")
        
if __name__ == '__main__':
    app.run()
    
    
    
