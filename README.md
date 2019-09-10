# AnacondaMover
A simple Python script to move your Anaconda base directory after installation with all created environements.

Sometimes you want to move your base directory later after the installation of Anaconda. This small script helps you to replace the prefix choice which was done at the very beginning of the environments.

Hints:
  * Python 3!
  * No guarantee for success!
  * Does not delete your original Anaconda directory! Do it manually afterwards

# How to run it:

To run the full script at once (copy the directory and replace the prefix information) you can run:
```
python anacondamover.py --input /path/to/your/input/anaconda3 --output /path/to/new/anaconda3/
```

If you have copied the Anaconda directory already manually you can run:
```
python anacondamover.py --input /path/to/your/input/anaconda3 --output /path/to/new/anaconda3/ --skip-copy
```
# Known issues:
As expected, it runs not smooth :) - Here is a list of known issues:

* If you run e.g. ROOT (CERN data analysis framework) or anything related to the downloaded gcc in Anaconda it might crash. Possible solution is to install gcc again in the environments ('conda install gcc')
