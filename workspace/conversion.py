""" converting the dataset to csv format """
import os
import glob
import xml.etree.ElementTree as ET
import pandas as pd


def xml_to_csv(path):
    """ converting the xml dataset to csv format """
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    """ run the main function to convert the format"""
    for folder in ['train', 'test']:
        image_path = os.path.join(os.getcwd(),
                                  ('D:\\PythonProject\\MaskRCNN\\workspace\\images\\' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('D:\\PythonProject\\MaskRCNN\\workspace\\images\\' + folder +
                       '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()