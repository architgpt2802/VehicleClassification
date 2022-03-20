# some code to extract frames from a video and store them in a particular directory
import cv2
import os
def Extract_Frames(path = "/media/dc/DC/Traffic/Day.avi", extr_img_dir="/content/drive/MyDrive/TRAFFIC/Extr_imgs"):
    count = 0
    vidcap = cv2.VideoCapture(path)
    success, image = vidcap.read()
    success = True
    frameSize = (image.shape[1], image.shape[0])
    print(frameSize)
    out = cv2.VideoWriter('/home/dc/Desktop/1234.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize) ## Output video Path 
    while success and count <30 :
        try:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*333))#1000))
            success,image = vidcap.read()
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Here the image will have only one channel
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            print (f'Read a new frame + {(image.shape[1], image.shape[0])}' + str(count) + ' :', success,)
            out.write(image)
            # cv2.imwrite( os.path.join(extr_img_dir , "frame%d.jpg" % count), image)          # save frame as JPEG file
            count = count + 1
            #cv2_imshow(image)
        except Exception as e:
            print("Some error occured here : " + e)
            #break
    out.release()
            
Extract_Frames()