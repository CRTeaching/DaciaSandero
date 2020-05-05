import os
import subprocess
import argparse


def extractFrames(args):
    main_dir = args["inputFolder"]

    for filename in os.listdir(main_dir):
        if os.path.isdir(os.path.join(main_dir, filename)):
            continue
        
        videoFile = os.path.join(os.path.abspath(main_dir), filename)
        
        fileFolder = os.path.join(os.path.abspath(main_dir), filename[:-4])
        if not os.path.exists(fileFolder):
            os.makedirs(fileFolder)           

        fileprefix = os.path.join(fileFolder, filename[:-4])

        cmd_command = ["ffmpeg", "-i", videoFile, "-vf", "scale=960:540", "-sws_flags", "bicubic", "{}-%04d.png".format(fileprefix), "-hide_banner"]
        subprocess.call(cmd_command)
        
        dirContent = os.listdir(fileFolder)
        for fi in dirContent:
            with open("{}".format(os.path.join(fileFolder, "inputList.txt")), "a") as f:
                f.write("{}\n".format(fi))





if __name__ == "__main__":
    ap = argparse.ArgumentParser(
            description = "Takes a set of videos and extracts each ones frames to separate folders")
    ap.add_argument("-inputFolder", "--inputFolder", type=str, required = True,
                    help="Path to the main folder holding all videos")
    
    args = vars(ap.parse_args())
    
    extractFrames(args)