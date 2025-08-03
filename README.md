---
title: Basic Multiclass
emoji: 🐢
colorFrom: pink
colorTo: indigo
sdk: gradio
sdk_version: 5.39.0
app_file: app.py
pinned: false
license: apache-2.0
python_version: "3.13.3"
short_description: classify between anime, tom & jerry, phineas & ferb
---

# Fast AI Practical Deep Learning course: Lectures 1-2.
- This is an adaptation of simple bird classifier from lectures 1 and 2.

## Fast AI
- Uses functional programming style a lot. Internal: Partial and parralel are useful, parallel is useful despite GIL because we do IO heavy tasks like loading files.
- Fast AI library has lots of helpers. Nice abstractions.

## Curious
- What the heck does finetune a resnet mean? Resnet has a convolutional layer, max pool, followed by 4 residual layers with 2 conv layers each. Then a fully connected output layer nn.Linear to classes. Fine-tuning typically just trains this last layer to understand newer labels.

- Tried to see what the `error_rate` function works, it operates at batch level, gets the linear layer outputs before softmax for entire batch, along with `y_actual` for entire batch, it computes prediction using softmax/argmax and then simple 0-1 error.

## Experiment, does it understand cartoons.
- Multi classification: Phineas and Ferb, Tom and Jerry, Anime. I checked manual search on DDG, and its probably not going to be easy as it not simple close up pictures. There's lots of different characters. I wasn't able to "prompt" it to get a single character for some reason.
 
 Multi class: 'phineas and ferb','tom and jerry','anime'
  * First attempt: <7% error rate with 0.01 * L2 norm.
  * Got more data :p, coz we can.
  * Dataset had skew: 120 anime, 140 p&f, 180 t&j
  * 0 error rate without norms.
  
![dataset](./Screenshots/dataset.png "dataset")
![manualtest](./Screenshots/perry_kicks.png "perry the platypus")

## Confusion matrix and error explanations
![confusion_matrix](./Screenshots/confusion_matrix.png "Confusion matrix")
- The model works quite well for the small amount of effort put into it.

![Errors](./Screenshots/error_images.png "misses")
- The error cases indicate that model is biased by cartoon style. 3d images are more likely to be classified as Tom & Jerry, and flatter 2d like Phineas and Ferb! I see Tom & Jerry 3d images in training set, but none of P&F.
- Searching more different training set images of different styles so it doesn't overindex on style would help.
- Give it more images of: Sketch and 3d styles of each class, so it can't associate things like this. Anyway, I will move onto the next lesson!
