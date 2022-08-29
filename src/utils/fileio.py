# -*- coding: utf-8 -*-
"""Helper functions for file system operations."""

import csv
import os

def make_dir(d):
    """Creates a folder if it does not exist."""
    if not os.path.exists(d): 
        os.mkdir(d)
    return d

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, data, header=None):
    """Saves the CSV file from path provided.

    Args:
        csvpath (Path): The CSV file path.
        data (list of lists): A list of the rows of data for the CSV file.
        header (list): An optional header for the CSV.

    """
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)


def load_log(logpath):
    """Reads the LOG file from path provided.

    Args:
        logpath (Path): The log file path.

    Returns:
        A list of lists that contains the rows of data from the LOG file.

    """
    with open(logpath, "r") as logfile:
        data = []
        csvreader = csv.reader(logfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_log(logpath, data, header=None):
    """Saves the LOG file from path provided.

    Args:
        logpath (Path): The LOG file path.
        data (list of lists): A list of the rows of data for the LOG file.
        header (list): An optional header for the LOG.

    """
    with open(logpath, "w", newline="") as logfile:
        csvwriter = csv.writer(logfile, delimiter=',')
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)
