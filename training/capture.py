import sys
import logging
import os
import cv2
from utils import write_image, key_action, init_cam


if __name__ == "__main__":
    # folder to write images to
    out_folder = sys.argv[1]
    os.environ['KMP_DUPLICATE_LIB_OK']='True'
    logging.getLogger().setLevel(logging.INFO)
    webcam = init_cam(640, 480)
    key = None

    try:
        # q key not pressed 
        while key != 'q':
            # Capture frame-by-frame
            ret, frame = webcam.read()
            
            # get key event
            key = key_action()

            # draw a [224x224] rectangle into the middle of the frame
            cv2.rectangle(frame,(0+48,0+8),(224+48,224+8),(0,0,0),2)     

            if key == 'space':
                # write the image without overlay
                # extract the [224x224] rectangle out of it
                image = frame[0+8: 224+8, 0+48: 224+48, :]
                write_image(out_folder, image) 
                
            # disable ugly toolbar
            cv2.namedWindow('frame', flags=cv2.WINDOW_GUI_NORMAL)              
            
            # display the resulting frame
            cv2.imshow('frame', frame)            
      
    finally:
        # when everything done, release the capture
        logging.info('quit webcam')
        webcam.release()
        cv2.destroyAllWindows()
        