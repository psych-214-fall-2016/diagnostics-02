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
        #take the mean of each volume and put into a column in the vol_means array
        vol_means[str(k)] = np.mean(data, axis = (0,1,2))
        k+=1

    #print(vol_means)
    # print(volumes[str(1)].shape)  #making sure this gives the shape of 1 run
    #plot with subplots the means for each volume for each run
    fig, ax = plt.subplots(20,1)
    for i, ax in enumerate(ax):
        ax.plot(vol_means[str(i)])
        ax.set_ylabel('Run ' + str(i))
        ax.set_xlim(0,162)
        print(len(vol_means[str(i)]))
    plt.show()

    iqr_proportion = 1.5
    for line in vol_means:
        q1, q3 = np.percentile(vol_means[line], [25, 75])
        iqr = q3 - q1
        up_thresh = q3 + iqr * iqr_proportion
        down_thresh = q1 - iqr * iqr_proportion
        print(np.logical_or(vol_means[line] > up_thresh, vol_means[line] < down_thresh))






    #making a residuals dictionary that contains a more linear version
    # of the mean data. It gets rid of any drift in the data.


    residuals = {}
    for i in range(len(vol_means)):
        data = vol_means[str(i)]
        shape = data.shape[0]  # number of volumes
        X = np.ones((shape, 2))  # make a 2 column  vector containing ones
        drift = np.linspace(-1, 1, shape) # make an array of numbers stretching from -1 to 1
        X[: , 1] = drift # puts the values of drift into the second column of X
        beta = np.linalg.pinv(X).dot(data) # numpy function to give values of intercept and slope of best fitting line
        fitted = X.dot(beta)  #creating the best fitted line
        residual = data - fitted  #difference between mean array and the fitted array
        residuals[str(i)] = residual + beta[0]  #adds the intercept to show the fitted version against the original mean value version

        #print(np.corrcoef(drift, residual))
        #print(beta)
        #plt.plot(fitted)
        #plt.show()

        #plt.plot(vol_means[str(6)]) #looking at one of the mean plots
        #plt.plot(residuals[str(6)]) #looking at one of the residual plots
        #plt.show()



# this function calculates the Dvars of the volumes
    dvars = {}

    for i in range(len(volumes)):
        nvoxels = volumes[str(i)].shape[0] * volumes[str(i)].shape[1] * volumes[str(i)].shape[2]
        num_vols = volumes[str(i)].shape[-1]
        dvarsFirst = []
        for elm in range(num_vols - 1):
            data = volumes[str(i)]
            diffs = data[:,:,:,elm] - data[:,:,:,elm + 1]
            diffs = diffs**2 # Square the differences;
            sumdiffs = sum(diffs.ravel()) # Sum over voxels for each volumevoxels;
            avgdiffs = sumdiffs/nvoxels #divide by number of voxels
            sqdiffs = np.sqrt(avgdiffs) # Return the square root of these values.
            dvarsFirst.append(sqdiffs)
        dvars[str(i)] = dvarsFirst
        #print(dvars[str(i)])

    fig, ax = plt.subplots(20,1)
    for i, ax in enumerate(ax):
        ax.plot(dvars[str(i)])
        ax.set_ylabel('Run ' + str(i))
    plt.show()







            #return dvars
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
            #"hast_list" '''




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
