import  cv2
import pandas as pd


data = pd.read_csv("data/output_0.csv")
sz = len(data['image'])

for i in range(0, sz-1):
    img = cv2.imread(data['image'][i])
    print(data['servo'][i], data['motor'][i])

    img = cv2.resize(img, (640,320), interpolation = cv2.INTER_AREA)

    steer = data['servo'][i]
    start_point = (150, 300) 
    end_point = (int(steer*1000), 200)
    color = (0, 255, 0) 
    thickness = 9
    img = cv2.line(img, start_point, end_point, color, thickness)
    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (150, 300) 
    fontScale = 1
    color = (255, 0, 0)   
    thickness = 2
    motor = str(data['motor'][i])
    
    img = cv2.putText(img, motor, org, font,  fontScale, color, thickness, cv2.LINE_AA) 


    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
