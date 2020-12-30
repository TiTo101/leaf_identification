import logging
import os
import cv2
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras.applications import inception_resnet_v2
from utils import key_action, init_cam


def predict_frame(frame, model, classes):
    '''
    helper function to make predictions which kind of leaf a picture shows
    '''
    # convert from bgr to rgb
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_preprocessed = inception_resnet_v2.preprocess_input(frame_rgb)
    img_preprocessed = img_preprocessed.reshape((1, 224, 224, 3))
    predictions = data_model.predict(img_preprocessed)
    result_dict = dict(zip(classes, predictions.tolist()[0]))
    print(result_dict)
    print(max(result_dict, key=result_dict.get))
    return result_dict


saved_model_path = '../models/maple_oak_beech_basemodel_trained.h5'
data_model = keras.models.load_model(saved_model_path)
classes = ['maple', 'oak', 'beech']
predicted_class = "none"
proba_of_class = 0
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.7
color = (0, 0, 0)
thickness = 2
org = (50, 50)

if __name__ == "__main__":

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

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
            cv2.rectangle(frame, (0 + 48, 0 + 8),
                          (224 + 48, 224 + 8), (0, 0, 0), 2)

            if key == 'space':
                # write the image without overlay
                # extract the [224x224] rectangle out of it
                image = frame[0 + 8: 224 + 8, 0 + 48: 224 + 48, :]
                result_dict = predict_frame(image, data_model, classes)
                predicted_class = max(result_dict, key=result_dict.get)
                proba_of_class = np.round(max(result_dict.values()), 3)

            # displaying results to screen
            cv2.putText(
                frame,
                f'{predicted_class} with probability {proba_of_class}',
                org,
                font,
                fontScale,
                color,
                thickness)

            # disable toolbar
            cv2.namedWindow('frame', flags=cv2.WINDOW_GUI_NORMAL)

            # display the resulting frame
            cv2.imshow('frame', frame)

    finally:
        # when everything done, release the capture
        logging.info('quit webcam')
        webcam.release()
        cv2.destroyAllWindows()
