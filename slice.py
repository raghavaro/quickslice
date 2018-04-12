from PIL import Image
import numpy as np
import argparse
import os
import sys
import math


def read_cct_file(file):
    lines = [line.rstrip('\n') for line in open(file)]
    info = map(int, lines.pop(0).split(','))
    voxels = []
    while len(lines)>0:
        row = np.fromstring(lines.pop(0), dtype=int, sep=',')
        slice = np.reshape(row, (info[1], info[0]))
        voxels.append(slice)
    volume = np.asarray(voxels)
    return volume

def get_slice(volume, plane, threshold):
    volume = np.clip(volume, threshold[0], threshold[1])
    slice = None
    variable = plane[:1] 
    value = float(plane[1:])
    if variable == 'x':
        x = int(math.ceil(value*(volume.shape[2]-1)))
        slice = volume[:,:,x]
    elif variable == 'y':
        y = int(math.ceil(value*(volume.shape[1]-1)))
        slice = volume[:,y,:]
    elif variable == 'z':
        z = int(math.ceil(value*(volume.shape[0]-1)))
        slice = volume[z,:,:]
    return slice
 
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--x', type=float)
    parser.add_argument('-y', '--y', type=float)
    parser.add_argument('-z', '--z', type=float)
    parser.add_argument('-t', '--threshold', type=int, nargs='+',default=[0, 255])
    parser.add_argument('--cct', type=str, required=True)
    args = parser.parse_args()
    if (args.x and args.y) or (args.y and args.z) or (args.z and args.x):
        sys.exit('Only one of x, y, or z allowed')
    plane = None
    if isinstance(args.x, (int, float)) and args.x >= 0 and args.x <= 1:
        plane = '{}{}'.format('x', args.x)
    elif isinstance(args.y, (int, float)) and args.y >= 0 and args.y <= 1:
        plane = '{}{}'.format('y', args.y)
    elif isinstance(args.z, (int, float)) and args.z >= 0 and args.z <= 1:
        plane = '{}{}'.format('z', args.z)
    if not plane:
        sys.exit('Enter a number between range 0-1.00 for x,y, or z')
    volume = read_cct_file(args.cct)
    slice = get_slice(volume, plane, args.threshold)
    if slice is None:
        sys.exit('Cannot generate slice')
    img = Image.fromarray(np.uint8(slice * 255), 'L')
    img.save('output.png')
    img.show()
    
