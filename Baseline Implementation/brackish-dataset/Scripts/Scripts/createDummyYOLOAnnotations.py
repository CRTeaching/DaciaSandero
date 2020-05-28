import os
import argparse


def createImageList(args):
    rootdir = args["inputFolder"]
    for root, _, files in os.walk(rootdir):

        for filename in files:
            filename_parts = os.path.splitext(filename)
            if filename_parts[-1] == ".png":
                txt_file = filename_parts[0]+".txt"  
                if txt_file not in files:
                    with open(os.path.join(root, filename_parts[0]+".txt"), "w"):
                        pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
            description = "Creates empty YOLO detection files for frames with no detections in it")
    ap.add_argument("-inputFolder", "--inputFolder", type=str,
                    help="Path to the main folder holding all images")
    
    args = vars(ap.parse_args())
    
    createImageList(args)