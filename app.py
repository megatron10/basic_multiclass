from fastcore.all import *
from fastai.vision.all import *
import gradio as gr

learn = load_learner('./test.pkl')
categories = ('anime', 'phineas and ferb', 'tom & jerry')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

demo = gr.Interface(
    fn=classify_image,
    inputs=["image"],
    outputs=["label"],
    examples=["./perry.jpg","./aot.jpg","./t&j.jpg","./phineas_and_ferb.jpg"]
)

demo.launch()