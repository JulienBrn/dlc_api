from __future__ import annotations

import deeplabcut as dlc
import pathlib
import os
import tensorflow as tf
import logging, beautifullogger
from typing import List, Sequence, Dict, Union, Tuple
beautifullogger.setup()
import pandas as pd
import numpy as np


class PosePredictionModel:
    def __init__(self, cache_folder="./cache", initialize: str =None):
        if initialize is None:
            print("Initializing from default dlc model")
        else:
            print("Initializing from modelzoo {}".format(initialize))

    def train(self, frames: Sequence[np.ndarray], expected: pd.DataFrame) -> None : 
        print("train called")

    def predict(self, frames: Sequence[np.ndarray]) -> pd.DataFrame: 
        print("predict called")
        return pd.DataFrame([], columns=["video", "frame_number", "bodypart1.x", "bodypart1.y", "bodypart2.x", "bodypart2.y"])

    def save(self, path: str): 
        print("save called")

    @staticmethod
    def load(path: str, cache_folder="./cache") -> PosePredictionModel:
        res = PosePredictionModel()
        #load
        return res




def evaluate(frames: Sequence[np.ndarray], predicted: pd.DataFrame, expected: pd.DataFrame) -> float:
    print("evaluate called")
    return np.nan

def label_frames(frames: Sequence[np.ndarray], labels: pd.DataFrame) -> Sequence[np.ndarray]: #Add coloring options, legends, point size, likelyhood as colors, ... later
    print("label frames called")
    return []

def mk_video(frames: Sequence[np.ndarray], name: str) -> None:
    print("making video {} from frames".format(name))

def load_video(name: str) -> Sequence[np.ndarray]: 
    print("load video called for {}".format(name))
    return []

def ask_user_for_positions(training_frames:Sequence[np.ndarray]) -> pd.DataFrame:
    print("ask_user_for_positions called")
    return pd.DataFrame([], columns=["bodypart1.x", "bodypart1.y", "bodypart2.x", "bodypart2.y"])

