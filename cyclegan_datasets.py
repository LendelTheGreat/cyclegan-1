"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
	'rainy2sunny': 624
}

"""The path to the output csv file."""
PATH_TO_CSV = {
	'rainy2sunny': './rainy2sunny_results.csv'
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
	'rainy2sunny': '.jpg'
}
