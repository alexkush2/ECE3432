import torchvision.datasets as datasets
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torchvision.utils import make_grid

from flowerNet import FlowerClassifierCNNModel
from torch.optim import Adam
import torch.nn as nn
from torch.utils.data import random_split
from PIL import Image
import torch
from torch.autograd import Variable

from utility import show_transformed_image


class FlowerModel:
    def __init__(self):
        self.cuda = False
        self.cnn_model = FlowerClassifierCNNModel()
        if (self.cuda):
            self.cnn_model.cuda()
        self.optimizer = Adam(self.cnn_model.parameters())
        if  (self.cuda):
            self.loss_fn=nn.CrossEntropyLoss().cuda()
        else:
            self.loss_fn = nn.CrossEntropyLoss()


    def train(self, epoches=10):

        train_size = int(0.8 * len(self.total_dataset))
        test_size = len(self.total_dataset) - train_size
        train_dataset, test_dataset = random_split(self.total_dataset, [train_size, test_size])

        train_dataset_loader = DataLoader(dataset = train_dataset, batch_size = 100)


        for epoch in range(epoches):
            self.cnn_model.train()
            # for i, (images, labels) in enumerate(train_dataset_loader):
            #     self.optimizer.zero_grad()
            #     outputs = self.cnn_model(images)
            #     loss = self.loss_fn(outputs, labels)
            #     if i % 5 == 4:  # print every 5 mini-batches                    
            #         print('[%d, %5d] loss: %.6f' % (epoch + 1, i + 1, loss / (i + 1)))  
            #     loss.backward()
            #     self.optimizer.step()
            for i, (images, labels) in enumerate(train_dataset_loader):

                if (self.cuda):
                    images, labels = Variable(images.cuda(non_blocking=True)), Variable(labels.cuda(non_blocking=True))
                else:
                    images, labels = Variable(images), Variable(labels)

                self.optimizer.zero_grad()
                if self.cuda:
                    outputs = self.cnn_model(images).cuda(non_blocking=True)
                else:
                    outputs = self.cnn_model(images)
                outputs = outputs.squeeze()
                loss = self.loss_fn(outputs, labels)
                loss.backward()
                self.optimizer.step()
                #running_loss += loss.item()

    def pre_processing(self, datadir='./data/'):
        self.transformations = transforms.Compose([
            transforms.RandomResizedCrop(64),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        self.total_dataset = datasets.ImageFolder(datadir, transform=self.transformations)
        self.dataset_loader = DataLoader(dataset=self.total_dataset, batch_size=100)
        items = iter(self.dataset_loader)
        image, label = items.next()
        show_transformed_image(make_grid(image))

    def predict(self,fileName="./data/dandelion/13920113_f03e867ea7_m.jpg"):
        test_image = Image.open(fileName)
        test_image_tensor = self.transformations(test_image).float()
        if (self.cuda):
            test_image_tensor = Variable(test_image_tensor.cuda(non_blocking=True))
            output = self.cnn_model(test_image_tensor).cuda(non_blocking=True)
        else:
            test_image_tensor = test_image_tensor.unsqueeze_(0)
            output = self.cnn_model(test_image_tensor)
        class_index = output.data.numpy().argmax()
        return class_index

    # def saveModel(self, PATH="CNN_Model.pth"):
    #     torch.save(self.cnn_model, PATH)

    # def loadModel(self, PATH="CNN_Model.pth"):
    #     self.cnn_model=torch.load(PATH)
    #     self.cnn_model.eval()

    ### save model
    def saveModel(self, mfile='model.pth'):
        print('Saving Model ')
        torch.save(self.cnn_model.state_dict(),mfile)

    #### Load model from file system
    def loadModel(self, mfile='model.pth'):
        self.cnn_model.load_state_dict(torch.load(mfile,map_location=lambda storage, loc: storage))
