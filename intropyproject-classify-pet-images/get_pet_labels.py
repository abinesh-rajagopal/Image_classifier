#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Abinesh Rajagopal
# DATE CREATED: 11/29/2019
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    pet_images_dict = {}
    pet_images = listdir(image_dir)
    for image in pet_images:
        pet_images_dict[image] = [get_pet_label(image)]
    return pet_images_dict

def get_pet_label(pet_image_name):
    """
    Get the pet label from the pet file name.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     pet_image_name - The image file name of the pet (string)
    Returns:
     Pet Image label (string)
    """
    name_parts = pet_image_name.split("_")
    clean_name = ""
    for name_part in name_parts:
        if name_part.isalpha():
            clean_name += (name_part + " ")
    return clean_name.strip().lower()

if __name__ == "__main__":
    pet_images_dict = get_pet_labels("./pet_images")
    for image_name, pet in pet_images_dict.items():
        print("{}->{}".format(image_name, pet))
#get_pet_label("Basset_hound_01034.jpg")
