# AnacondaMover
A simple Python script to move your Anaconda base directory after installation with all created environements.

Sometimes you want to move your base directory later after the installation of Anaconda. This small scipt helps you to replace the prefix choice which was done at the very beginning of the environments.

  * Python 3!
  * No guarantee for success!
  * Does not delete your original Anaconda directory!

# How to run it:

To run the full script at once (copy the directory and replace the prefix information) you can run:
```
python anacondamover.py --input /path/to/your/input/anaconda3 --output /path/to/new/anaconda3/
```

If you have copied the Anaconda directory already manually you can run:
```
python anacondamover.py --input /path/to/your/input/anaconda3 --output /path/to/new/anaconda3/ --skip-copy
```
