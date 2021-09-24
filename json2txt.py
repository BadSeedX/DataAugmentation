import json
import os


def convert(img_size, box):

    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]
    return (x1, y1, x2, y2)


def decode_json(json_folder_path, txt_folder_path):

    json_paths = os.listdir(json_folder_path)

    for json_path in json_paths:
        json_path = json_folder_path + json_path
        data = json.load(open(json_path, 'r', encoding='utf-8'))
        for i in data['shapes']:
            img_w = data['imageWidth']
            img_h = data['imageHeight']
            if (i['shape_type'] == 'rectangle' and i['label'] == 'bird'):
                x1 = i['points'][0][0]
                y1 = i['points'][0][1]
                x2 = i['points'][1][0]
                y2 = i['points'][1][1]
                bb = (x1, y1, x2, y2)
                bbox = convert((img_w, img_h), bb)
                txt = open(txt_folder_path + "/" + json_path.split('/')[-1].split('.')[0] + ".txt", "a+")
                # 种类 x1, y1, x2, y2
                txt.write("bird" + " " + " ".join([str(b) for b in bbox]) + '\n')
                txt.close()

if __name__ == "__main__":
    json_folder_path = "E:/DataAugmentation/data/json/"
    txt_folder_path = "E:/DataAugmentation/data/txt"
    # json_name = "001.json"
    decode_json(json_folder_path, txt_folder_path)