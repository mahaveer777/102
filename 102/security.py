from os import access
from tracemalloc import Snapshot, start
import cv2
import dropbox
import random
import time
starttime=time.time()
def snapshot():
    # initializing cv2
    # 0 stands for camera
    vco=cv2.VideoCapture(0)
    result=True
    while(result):
        # read the frames while the camera is on
        ret,frame=vco.read()
        imagename="newpic"+str(random.randint(0,100))+".jpg"
        # cv2.imwrite method isused to save an image to any storage device 
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
    return imagename    
   # turns off the camera
    vco.release()
         #closes all the window that might be open during the process
    cv2.destroyAllWindows()
def uploadfiles(imagename):
    accestoken="N8kMVNwIOlUAAAAAAAAAAXjmvMXZCM8xQuI37zS2wWV4asCiVgkMiZJ7N3GKxzkL"
    filefrom=imagename
    fileto="/securedimages/"+imagename
    dbx=dropbox.Dropbox(accestoken)
    with open(filefrom,"rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")
def main():
    while(True):
        if(time.time()-starttime>=5*60):
            imagename=snapshot()    
            uploadfiles(imagename)
main()    
