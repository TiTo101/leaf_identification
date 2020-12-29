# training
I trained a neural network based on the inception_resnet_v2 model to classify leafs from 3 different trees:
- beech
- maple
- oak

## how to add images to the training data:
You can download the training data [here](https://drive.google.com/drive/folders/1g1v5hEC2sA0fSIZKqlN1ru5EqnEvrccy?usp=sharing)

To add training pictures yourself, use the following lines of code:
```python
python capture.py data/<name_of_tree>
```
and take pictures with your webcam. If you don't have a or don't want to use your webcam, you can use your samrtphone with [EpocCam](https://www.elgato.com/de/epoccam#)

## open to dos:
- My goal was to have the highest accuracy with reasonable training time. I'd like to train a second model based on the mobilenet_v3 model in the future to make quicker predictions.
- I have not yet applied all possible preprocessing functions to make the model more robust