#arbitrary edit

Below are the instructions to run our outlier script of the diagnostics data.

# Diagnostics project

Script go in the `scripts` directory.

Library code (such as Python modules or packages) goes in the `packages` directory.

You should put this `packages` directory on your Python PATH.

This file has instructions on how to get, validate and process the data.

## Get the data

    cd data
    curl -LO http://nipy.bic.berkeley.edu/psych-214/group02.tar.gz
    tar zxvf group02.tar.gz
    cd ..

## cloning the our diagnostics-2 repository to your computer

    git clone https://github.com/psych-214-fall-2016/diagnostics-02.git

## Check the data
## the output should confirm that the downloaded data matches the original data.
    python3 scripts/validate_data.py data

## Find outliers
## run the script to get each outlier volume for each run of the data.
    python3 scripts/find_outliers.py data

    This should print output to the terminal:
    1) each run number with its corresponding shape.
        eg: Run 0: (64, 64, 34, 161)
    2) The number of dvars values which should be 1 less than the 4th dimension of the run shape (number of TRs -1).
        eg: dvars 0:160
    3) The outliers for each of the subjects individual runs.
        eg: group02_sub01_run1.nii outliers: [42, 43, 104]

The file OUTLIERDETECTION.txt contains information on the outputted outliers as well as our detection process.
