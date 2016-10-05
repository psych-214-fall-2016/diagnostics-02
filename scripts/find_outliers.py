""" Python script to find outliers

Run as:

    python3 scripts/find_outliers.py data
"""

import sys
import numpy as np
import nibabel as nib

def find_outliers(data_directory):
    """ Print filenames and outlier indices for images in `data_directory`.

    Print filenames and detected outlier indices to the terminal.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    None
    """
    # Your code here

    ## MLN:  10-5-16
    # Identify image files in data_directory using names listed in
    # 'hash_list.txt' (executed similarly to validate_data.py)
    hashlist = str(data_directory + '/' + 'hash_list.txt')
    for line in open(hashlist, 'rt'):
        i = line.split()
        imgfile = i[1]
        # Load the image file
        img = nib.load(imgfile, mmap=False)
        # Retrieve data from image array
        data = img.get_data()

    raise RuntimeError('No code yet')


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    find_outliers(data_directory)



if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
