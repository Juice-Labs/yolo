import torch

print( torch.cuda.is_available() )
print( torch.cuda.get_device_name() )
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = ['https://ultralytics.com/images/zidane.jpg']
results = model(imgs)
results.print()
