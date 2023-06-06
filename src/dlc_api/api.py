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
    def __init__(self, cache_folder="./cache", initialize=None):pass
    def train(self, frames: Sequence[np.ndarray], expected: pd.DataFrame) -> None : pass #row: frame, columns: (bodyparts, coordinate)
    def predict(self, frames: Sequence[np.ndarray]) -> pd.DataFrame: pass #row: frame, columns: (bodyparts, coordinate)
    def save(self, path: str): pass 
    def copy(self): pass

basic_dlc_model: PosePredictionModel = None


def evaluate(frames: Sequence[np.ndarray], predicted: pd.DataFrame, expected: pd.DataFrame) -> float:pass
def label_frames(frames: Sequence[np.ndarray], labels: pd.DataFrame) -> Sequence[np.ndarray]: pass #Add coloring options, legends, point size, likelyhood as colors, ... later
def mk_video(frames: Sequence[np.ndarray], name: str) -> None: pass
def load_video(name: str) -> Sequence[np.ndarray]: pass
def ask_user_for_positions(training_frames:Sequence[np.ndarray]) -> pd.DataFrame: pass


