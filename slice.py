from PIL import Image
import numpy as np
import argparse
import os
import sys
import math

temporary_voxel = -1

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
        x = int(math.ceil(value*(volume.shape[0]-1)))
        slice = volume[:,:,x]
    elif variable == 'y':
        y = int(math.ceil(value*(volume.shape[1]-1)))
        slice = volume[:,y,:]
    elif variable == 'z':
        z = int(math.ceil(value*(volume.shape[2]-1)))
        slice = volume[z,:,:]
    return slice


def threshold_to_temporary_voxel(volume, threshold):
    volume[volume < threshold[0]] = temporary_voxel
    volume[volume > threshold[1]] = temporary_voxel
    return volume

def get_view(volume, plane, direction, threshold):
    view = None
    axis = plane[:1] 
    axis_intercept = float(plane[1:])
    zero_slice = None
    if (axis_intercept == 0 and direction < 0) or (axis_intercept == 1 and direction > 0) or (direction == 0):
        return get_slice(volume, plane, threshold)
    new_volume = None
    if axis == 'x':
        x = int(round(axis_intercept*(volume.shape[0]-1)))
        new_volume = volume[:,:,x:volume.shape[0]] if direction > 0 else volume[:,:,x:0:-1] 
        new_volume = threshold_to_temporary_voxel(new_volume, threshold)
        i = 0
        slice = new_volume[:,:,i]
        current_view = slice
        print current_view
        incomplete = np.any(current_view == temporary_voxel)
        print incomplete
        print new_volume.shape
        while (incomplete and i<new_volume.shape[2]-1):
            i+=1
            slice = new_volume[:,:,i]
            current_view = np.where(current_view!=temporary_voxel, current_view, slice)
        current_view[current_view == temporary_voxel] = 254
        print current_view
        return current_view
            

    elif axis == 'y':
        y = int(round(axis_intercept*(volume.shape[1]-1)))
        new_volume = volume[:,y:volume.shape[1],:] if direction > 0 else volume[:,y:0:-1,:]
    elif axis == 'z':
        z = int(round(axis_intercept*(volume.shape[2]-1)))
        new_volume = volume[z:volume.shape[2],:,:] if direction > 0 else volume[z:0:-1,:,:]
    #thresholding
    
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--x', type=float)
    parser.add_argument('-y', '--y', type=float)
    parser.add_argument('-z', '--z', type=float)
    parser.add_argument('-t', '--threshold', type=int, nargs='+',default=[106, 140])
    parser.add_argument('-d', '--direction', type=int, default=0)
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
    view = get_view(volume, plane, args.direction, args.threshold)
    if view is None:
        sys.exit('Cannot generate slice')
    img = Image.fromarray(np.uint8(view * 255), 'L')
    img.save('output.png')
    img.show()
    
