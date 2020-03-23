from torchvision  import models
import torch
from torchvision import transforms
from PIL import Image
import cv2, numpy


# load a net
alexnet = models.alexnet(pretrained=True)

# an image transformation 256x256
transform = transforms.Compose([            #[1]
 transforms.Resize(256),                    #[2]
 transforms.CenterCrop(224),                #[3]
 transforms.ToTensor(),                     #[4]
 transforms.Normalize(                      #[5]
 mean=[0.485, 0.456, 0.406],                #[6]
 std=[0.229, 0.224, 0.225]                  #[7]
 )])

# load an image
img = Image.open("cow.jpg")

while True:
      cv2.imshow("my pic", numpy.array(img))

      if cv2.waitKey(0) & 0xFF == ord('q'):
          break

# transform the image into a 256x256 picture with normalization 
img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)

# evaluate
alexnet.eval()
out = alexnet(batch_t)

with open('imagenet_classes.txt') as f:
 labels = [line.strip() for line in f.readlines()]


# find labels index with the correspond highest value
_, index = torch.max(out, 1)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
print(labels[index[0]], percentage[index[0]].item())



# uncomment below to show top 5 labels
#_, indices = torch.sort(out, descending=True)
#for idx in indices[0][:5]:
# print(labels[idx], percentage[idx].item())
#[print(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]
