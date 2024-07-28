from PIL import Image
import numpy as np

def update(model1,model2,mu):
    for p1,p2 in zip(model1.parameters(),model2.parameters()):
        p1 = mu*p1+(1-mu)*p2