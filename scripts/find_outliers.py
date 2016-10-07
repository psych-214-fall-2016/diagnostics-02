""" Python script to find outliers

Run as:

    python3 scripts/find_outliers.py data
"""

import sys
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

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

    #make an empty string array that will ultimately store which volumes
    #are outliers
    outlierarr = []

    # Identify image files in data_directory using names listed in
    # 'hash_list.txt' (executed similarly to validate_data.py)
    hashlist = str(data_directory + '/' + 'hash_list.txt')

    #iterating through to add to an array which contains the values for each volume for each files
    k = 0
    vol_means = {}
    volumes = {}

    for line in open(hashlist, 'rt'):
        i = line.split()
        imgfile = str(data_directory + '/' + i[1]) #making this filename a string with full path
        #print(imgfile) #testing to see through printing whether the data reads in
        # Load the image file
        img = nib.load(imgfile, mmap=False)
        # Retrieve data from image array
        data = img.get_data()

        volumes[str(k)] = data
        #take the mean of each volume and put into the vol_means dictionary
        vol_means[str(k)] = np.mean(data, axis = (0,1,2))
        k+=1

    #plot with subplots the means for each volume for each run
    fig, ax = plt.subplots(20,1)
    for i, ax in enumerate(ax):
        ax.plot(vol_means[str(i)])
        ax.set_ylabel('Run ' + str(i))
        ax.set_xlim(0,162)
        print(len(vol_means[str(i)]))
    plt.show()


        # Now here is where we do some dummy outlier code
        #for volume in data(:,:,:,volumeidx)
            # Do something mathematical to this volume
            # such as find its mean amount and then
            # put that value in an array for later comparison
            # with the next future volumes
            #volmath = [avgVal_vol1 avgVal_vol2 etc]

        # if volume > criterion_for_being_outlier
        #outlierarr[volume] = str[imgfile + '_' + volume]
            #print(outlierarr)
            #prints all vols that are outliers for this nifty file, then
            #advances to the next nift file  named on the next line of
            #"hast_list"




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
