import logging, beautifullogger
import sys

logger = logging.getLogger(__name__)

def setup_nice_logging():
    beautifullogger.setup(logmode="w")
    logging.getLogger("toolbox.ressource_manager").setLevel(logging.WARNING)
    logging.getLogger("toolbox.signal_analysis_toolbox").setLevel(logging.WARNING)

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        logger.info("Keyboard interupt")
        sys.exit()
        return
    else:
        sys.__excepthook__(exc_type, exc_value, exc_traceback)


sys.excepthook = handle_exception

# from dlc_api.api import load_video, ask_user_for_positions, label_frames, mk_video, PosePredictionModel

# def myfunc():
#     model = PosePredictionModel()
#     frames= load_video("myvideo.mp4")
#     training_frames = [f for i,f in enumerate(frames) if i % 10 ==0]
#     bodyparts_positions = ask_user_for_positions(training_frames)
#     model.train(training_frames, bodyparts_positions)
#     new_video = load_video("new_video.mp4")
#     res = model.predict(new_video)
#     nf = label_frames(new_video, res)
#     mk_video(nf, "labeled_video.mp4")


#############IMPORTANT CODE STARTS HERE########################
from dlc_api.api_simpl import ask_user_for_positions, label_frames, PosePredictionModel

def myfunc_simpl():
    model = PosePredictionModel()
    bodyparts_positions = ask_user_for_positions(["myvideo.mp4"])
    model.train(["myvideo.mp4"], bodyparts_positions)
    res = model.predict(["new_video.mp4"])
    nf = label_frames(["new_video.mp4"], res)

def run():
    setup_nice_logging()
    logger.info("Running start")
    myfunc_simpl()
    logger.info("Running end")