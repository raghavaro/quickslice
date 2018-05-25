# quickslice

A simple python package to compress large volumetric data and dynamically extract slices from the compressed volume.


## Usage

Build

    qslice build path/to/directory
    qslice build path/to/directory --size 256 256 256

Slice

    qslice slice file.cct -z 0
    qslice slice file.cct -z 0.5
    qslice slice file.cct -x 0.7
    qslice slice file.cct -y 1



## Files

### quickslice

[quickslice](https://github.com/agu3010/cct/blob/master/quickslice) is the main binary file


### build.py

[build.py](https://github.com/agu3010/cct/blob/master/core/build.py) takes input of a directory containing slices in alphanumeric order and converts it to a CCT (Compressed Computed Tomography) file of size 128 x 128 x 128


### slice.py

[slice.py](https://github.com/agu3010/cct/blob/master/core/slice.py) is used to extract a slice from a cct file. The following command shows the xy plane at z = 0 of [file.cct](https://github.com/agu3010/cct/blob/master/file.cct)


## Additional Stuff

### The z=0 plane output

![-z 0 plane](https://github.com/agu3010/cct/blob/master/output.png?raw=true)


### More examples

More examples and commands with options can be found in [examples](https://github.com/agu3010/cct/tree/master/examples)




# CCT File format

Compressed Computed Tomography Files

CCT files represent GBs of Tomographic Datasets in a single compressed file. The file size depends on the output size. The default size is 128 x 128 x 128 and the size of the output file is between 7 MB to 12 MB

Note: Refrain from using CCT files for in-detail visualisation. CCT files are built using a super-lossy conversion technique and are meant to be used for a small quick preview of planes extracted from 3d volumes.


### Representation:


Line 1:                       sizeX,sizeY,sizeZ

Line 2 to Line (sizeZ + 1):   Z-Slice representation

The following voxels:

    [
        [
            [0,0,1],
            [0,0,1],
            [0,1,1],
            [0,1,1],
            [1,1,1]
        ],
        [
            [0,0,1],
            [0,0,1],
            [0,1,1],
            [0,1,1],
            [1,1,1]
        ],
        [
            [0,0,1],
            [0,0,1],		
            [0,1,1],
            [0,1,1],
            [1,1,1]
        ],
        [
            [0,0,1],
            [0,0,1],
            [0,1,1],
            [0,1,1],
            [1,1,1]
        ] 
    ]


will be represented as


    3,5,4

    0,0,1,0,0,1,0,1,1,0,1,1,1,1,1

    0,0,1,0,0,1,0,1,1,0,1,1,1,1,1

    0,0,1,0,0,1,0,1,1,0,1,1,1,1,1

    0,0,1,0,0,1,0,1,1,0,1,1,1,1,1


### Example
[file.cct](https://github.com/agu3010/cct/blob/master/file.cct) is a 128 x 128 x 128 grayscale tomographic model
