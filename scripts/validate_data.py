""" Python script to validate data

Run as:

    python3 scripts/validata_data.py data
"""

import os
import sys
import hashlib

def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    # Open the file, read contents as bytes.
    # Open a file in Read Binary mode to read bytes
    fobj = open(filename, 'rb')# Read contents as bytes
    contents = fobj.read() # Read the whole file
    fobj.close()
    # Calculate, return SHA1 has on the bytes from the file.
    return hashlib.sha1(contents).hexdigest()

    raise RuntimeError('No code yet')


def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """
    # Read lines from ``data_hashes.txt`` file.
    hashfile = str(data_directory + '/' + 'data_hashes.txt')
    # Split into SHA1 hash and filename
    for line in open(hashfile, 'rt'):
        i = line.split()
        sha1 = i[0]
        nii_file = i[1]
    # Calculate actual hash for given filename.
    # Generate the SHA1 hash string for these bytes
        actualSHA1string = file_hash('data/' + nii_file)
        if actualSHA1string != sha1:
            # If hash for filename is not the same as the one in the file, raise
            # ValueError
            raise ValueError("Hash doesn't match!!! filename: " + nii_file)
        if actualSHA1string == sha1:
            print('YOU DID IT, THIS HASH MATCHES!' + nii_file)


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
