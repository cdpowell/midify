from os import listdir
from os.path import join, isfile, splitext
import cv2
import datetime
import jsonpickle


IMGPATH = 'data/scores_coco_2019/train/scores_coco_train_2019/'
ANNPATH = 'data/scores_coco_2019/train/annotations/'


def main():

    now = datetime.datetime.now()

    coco_dict = dict()
    img_id_dict = dict()

    coco_dict["info"] = {
        "year": 2019,
        "version": "0.1",
        "description": "Music score/note dataset",
        "contributor": "Christian D. Powell",
        "url": "https://github.com/cdpowell/midify",
        "date_created": str(now),
    }

    coco_dict["licenses"] = [{
        "url": "https://github.com/cdpowell/midify",
        "id": 0,
        "name": "Apache License, Version 2.0"
    }]

    coco_dict["images"] = list()
    count = 0
    files = [f for f in listdir(IMGPATH) if isfile(join(IMGPATH, f)) and f.endswith('.png')]
    for file in files:
        img_id_dict[splitext(file)[0]] = count
        img = cv2.imread(join(IMGPATH, file), 0)
        height, width = img.shape[:2]
        coco_dict["images"].append({
            "id": count,
            "width": width,
            "height": height,
            "file_name": file,
            "license": 0,
            "flickr_url": "None",
            "coco_url": "None",
            "date_captured": str(now)
        })
        count += 1

    coco_dict["annotations"] = list()
    class_dict = dict()
    class_count = 0
    count = 0
    files = [f for f in listdir(ANNPATH) if isfile(join(ANNPATH, f)) and f.endswith('.json')]
    for file in files:
        with open(join(ANNPATH, file), 'r') as f:
            supervisely_dict = jsonpickle.decode(f.read())

        for obj in supervisely_dict["objects"]:
            x1, y1 = obj["points"]["exterior"][0]
            x2, y2 = obj["points"]["exterior"][1]
            x_side = x2 - x1
            y_side = y2 - y1

            area = x_side * y_side
            bbox = [x1, y1, x_side, y_side]

            if obj["classTitle"] not in list(class_dict.keys()):
                class_dict[obj["classTitle"]] = class_count
                cat_id = class_count
                class_count += 1
            else:
                cat_id = class_dict[obj["classTitle"]]

            coco_dict["annotations"].append({
                "id": count,
                "image_id": img_id_dict[splitext(file)[0]],
                "category_id": cat_id,
                "segmentation": None,
                "area": area,
                "bbox": bbox,  # [x, y, width, height] where x, y is origin
                "iscrowd": 0
            })
            count += 1

    coco_dict["categories"] = list()
    for class_name in list(class_dict.keys()):
        coco_dict["categories"].append({
        "id": class_dict[class_name],
        "name": class_name,
        "supercategory": "music_note"
        })

    with open(join(ANNPATH, 'coco_annotations.json'), 'w') as f:
        f.write(jsonpickle.encode(coco_dict))


if __name__ == '__main__':
    main()