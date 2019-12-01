from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from print_functions_for_lab_checks import *
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats


from print_functions_for_lab_checks import *

def print_dict(dict):
    for key, value in dict.items():
        print("{} -> {}".format(key, value))


args = get_input_args()
image_dir = args.dir
model = args.arch
dog_file_name = args.dogfile
#print(args.dir + " "+ args.arch + " "+args.dogfile)



pet_labels_dict = get_pet_labels(image_dir)
#check_creating_pet_image_labels(pet_labels_dict)

classify_images(image_dir, pet_labels_dict, model )
#check_classifying_images(pet_labels_dict)

adjust_results4_isadog(pet_labels_dict, dog_file_name)
#check_classifying_labels_as_dogs(pet_labels_dict)
#print_dict(pet_labels_dict)

stats_dict = calculates_results_stats(pet_labels_dict)
check_calculating_results(pet_labels_dict, stats_dict)
