from torchvision  import models
import torch
from torchvision import transforms
from PIL import Image
import cv2, numpy


class LiNet:
    def __init__(self, netname='AlexNet'):
        if netname.lower() == 'alexnet':
            self.net = models.alexnet(pretrained=True)
            self.size = 256
        elif netname.lower() == 'googlenet':
            self.net = models.googlenet(pretrained=True)
            self.size = 244
        else:
            self.net = None
            

        self.transform = transforms.Compose([          #[1]
            transforms.Resize(self.size),              #[2]
            transforms.CenterCrop(224),                #[3]
            transforms.ToTensor(),                     #[4]
            transforms.Normalize(                      #[5]
            mean=[0.485, 0.456, 0.406],                #[6]
            std=[0.229, 0.224, 0.225]                  #[7]
        )])


    def classify(self, imagefile="dog.jpg"):
        if type(imagefile) == numpy.ndarray: # if its a webcam image
            imgRGB = cv2.cvtColor(imagefile,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(imgRGB)

        else:   # if its a file name
            img = Image.open(imagefile)

        img_t = self.transform(img)
        batch_t = torch.unsqueeze(img_t, 0)
        self.net.eval()
        out = self.net(batch_t)

        with open('imagenet_classes.txt') as f:
            labels = [line.strip() for line in f.readlines()]

        # find labels index with the correspond highest value
        _, index = torch.max(out, 1)

        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
        print(labels[index[0]], percentage[index[0]].item())
        return (labels[index[0]],percentage[index[0]].item())

    