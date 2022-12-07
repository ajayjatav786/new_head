import os

###### DATASET ######

LABEL2INDEX = {"background": 0, "head": 1}
INDEX2LABEL = {0: "background", 1: "head"}

###### MODEL ######

# fmt: off
HEAD_SEGMENTATION_MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "head_segmentation.ckpt")
HEAD_SEGMENTATION_MODEL_URL = "https://drive.google.com/uc?id=1eb4HcG_2cTY17aNWa7EopulDr1Go8Gia"
# fmt: on
