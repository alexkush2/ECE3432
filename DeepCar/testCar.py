import  cv2
import pandas as pd
from time import sleep


data = pd.read_csv("data/output_0.csv")
sz = len(data['image'])

for i in range(0, sz-1):
    img = cv2.imread(data['image'][i])
    print(data['servo'][i], data['motor'][i])

    # resize
    img = cv2.resize(img, (640,320), interpolation = cv2.INTER_AREA)

    # add line
    steer = data['servo'][i]
    start_point = (150, 300) 
    end_point = (int(steer*1000), 200)
    color = (0, 255, 0) 
    thickness = 9
    img = cv2.line(img, start_point, end_point, color, thickness)
    
    # add text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (150, 300) 
    fontScale = 1
    color = (255, 0, 0)   
    thickness = 2
    motor = str(data['motor'][i])
    
    img = cv2.putText(img, motor, org, font,  fontScale, color, thickness, cv2.LINE_AA) 

    # show image
    cv2.imshow('image',img)
    cv2.waitKey(50)

cv2.destroyAllWindows()
