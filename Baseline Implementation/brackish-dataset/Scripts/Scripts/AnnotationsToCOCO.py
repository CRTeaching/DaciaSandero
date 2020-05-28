import cv2
import json
import numpy as np
import os
import pandas as pd
import argparse

def importCategories(name_file):
    # Import category names list
    categoryLabels = dict()
    categoryNumbers = dict()

    with open(name_file) as f:
        lineNumber = 1

        for line in f:
            entries = line.replace('\n', '')

            if len(entries) > 1:
                number = lineNumber
                label = entries

                categoryLabels[int(number)] = label
                categoryNumbers[label] = int(number)

            lineNumber += 1

    return (categoryLabels, categoryNumbers)


def imageToDictEntry(imagePath, imageId, shortPath):
    imageFile = cv2.imread(imagePath)

    image = dict()

    if imageFile is not None:
        height, width, _ = imageFile.shape

        # Image dictionary
        image = dict()
        image['id'] = imageId
        image['width'] = width
        image['height'] = height
        image['file_name'] = shortPath
        image['license'] = 0
    else:
        print("Could not read: " + imagePath)

    return image

def annotationToDictEntry(df_entry, annotationId, imageToIDDict, categoryToNumberDict):
    annotation = dict()

    annotation["iscrowd"] = 0
    annotation["id"] = annotationId
    annotation["image_id"]= imageToIDDict[df_entry["Filename"]]
    annotation["category_id"] = categoryToNumberDict[df_entry["Annotation tag"]]
    tl_x = df_entry["Upper left corner X"]
    tl_y = df_entry["Upper left corner Y"]
    br_x = df_entry["Lower right corner X"]
    br_y = df_entry["Lower right corner Y"]
    width = br_x-tl_x
    height = br_y-tl_y
    annotation["bbox"] = [tl_x, tl_y, width, height]
    annotation["area"] = width*height

    return annotation

def createCategoryList(categoryLabels):
    categories = []

    for catId, name in categoryLabels.items():
        catEntry = dict()
        catEntry['supercategory'] = 'None'
        catEntry['id'] = catId
        catEntry['name'] = name

        categories.append(catEntry)

    return categories


def AAUToCOCO(args):
    # Import category names list
    datasetName = args["datasetName"]
    imagelistPath = args["imageList"]
    annotationPath = args["annotationCSV"]
    categoryfilePath = args["categories"]
    categoryLabels, categoryNumbers = importCategories(categoryfilePath)
    categoryList = createCategoryList(categoryLabels)
    


    with open(imagelistPath, 'r') as f:
        imagelist = f.readlines()
    imagelist = [x.rstrip() for x in imagelist]

    annotations_df = pd.read_csv(annotationPath, sep=";")

    images = []
    annotations = []
    idToImageLookupTable = dict()
    imageToIdLookupTable = dict()
    imageIdCounter = 0
    annotationIdCounter = 0


    for filename in imagelist:
        #print(filename)
        if os.path.splitext(filename)[-1] == ".png":
            basename = os.path.basename(filename)
            imageIdCounter += 1 
            image = imageToDictEntry(filename, 
                                    imageIdCounter, 
                                    basename)

            idToImageLookupTable[imageIdCounter] = basename
            imageToIdLookupTable[basename] = imageIdCounter

            images.append(image)


    for index, row in annotations_df.iterrows():
        annotationIdCounter += 1
        annotation = annotationToDictEntry(row, annotationIdCounter, imageToIdLookupTable, categoryNumbers)
        annotations.append(annotation)



    dataset_info = {'Description': datasetName,
                    "url": "",
                    "version": "0.0.1",
                    "year": 2019,
                    "Contributor": "Visual Analysis of People lab, AAU",
                    "date_created": "12-04-2019"}


    gtDict = dict(info = dataset_info, 
                licenses = ['MIT'],
                images = images, 
                annotations = annotations,
                categories = categoryList)

    with open(datasetName +'_groundtruth.json', 'w') as outfile:
        json.dump(gtDict, outfile)

    lookupDict = dict(idToImageLookupTable = idToImageLookupTable,
                    imageToIdLookupTable = imageToIdLookupTable,
                    categoryNametoId = categoryNumbers,
                    categoeryIdtoName = categoryLabels)

    with open(datasetName+'_helper_dirs.json', 'w') as outfile:
        json.dump(lookupDict, outfile)


    
if __name__ == "__main__":
    ap = argparse.ArgumentParser(
            description = "Converts the ground truth annotations from AAU Bounding Box annotation format to MS COCO format")
    ap.add_argument("-imageList", "--imageList", type=str,
                    help="Path to imagelist text file")
    ap.add_argument("-annotationCSV", "--annotationCSV", type=str,
                    help="Path to csv file with AAU Bounding Box annotations")
    ap.add_argument("-categories", "--categories", type=str,
                    help="Path to file with categories")
    ap.add_argument("-datasetName", "--datasetName", type=str,
                    help="The dataset name")
    args = vars(ap.parse_args())
    
    AAUToCOCO(args)