# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:35:16 2022

@author: Homa
"""
import torchvision
model_conv = torchvision.models.resnet18(pretrained=True)
for param in model_conv.parameters():
    param.requires_grad = False ## All new operations in the torch.set_grad_enabled(False) block won’t require gradients. 
    
