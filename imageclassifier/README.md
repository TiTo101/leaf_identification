# leaf classifier
Use your webcam to classify leafs from oak, maple and beech trees.

## Usage
Run the following line of code from the terminal within this folder. 

```bash
python live_prediction.py
```
As I currently build on the inception_resnet_v2 (high accuracy, low speed), loading the application will take several minutes. Optimizing this is an open to do on my end.

After loading, a window pops up showing the webcam (or smartphone cam). There is a rectangle in the top right of that screen. Hold the leaf in that rectangle than press `space` to make a prediction.

Exit the program with `q`