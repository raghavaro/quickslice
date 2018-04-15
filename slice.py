from PIL import Image
import numpy as np
import argparse
import os
import sys
import math
import colormaps


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
    volume[np.where(volume<threshold[0])] = -1
    volume[np.where(volume>threshold[1])] = -1
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


def apply_transparency(slice):
    alpha_slice = np.zeros_like(slice)
    alpha_slice[np.where(slice!=-1)] = 255
    slice[np.where(slice==-1)] = 255
    rgba_slice = np.zeros((slice.shape[0], slice.shape[1], 4), 'uint8')
    rgba_slice[..., 0] = slice
    rgba_slice[..., 1] = slice
    rgba_slice[..., 2] = slice
    rgba_slice[..., 3] = alpha_slice
    return rgba_slice


def apply_colormap(slice, threshold, colormap):
    colorscale = colormaps.colorscales.get(colormap)
    if colorscale:
        lerp_range = range(threshold[0], threshold[1] + 1)
        max_index = threshold[1]-threshold[0]
        replacer = []
        reds = np.zeros_like(slice)
        blues = np.zeros_like(slice)
        greens = np.zeros_like(slice)
        alphas = np.zeros_like(slice)
        for i in lerp_range:
            replace_from = i
            replace_to_index = (i-threshold[0])*(len(colorscale)-1)/max_index
            upper_index = int(math.ceil(replace_to_index))
            lower_index = int(math.floor(replace_to_index))
            multiplier = replace_to_index - lower_index
            upper_color = np.asarray(colorscale[upper_index])
            lower_color = np.asarray(colorscale[lower_index])
            this_color = np.rint(lower_color + multiplier*(upper_color-lower_color)).astype(int)
            indices = np.where(slice == i)
            reds[indices[0], indices[1]] = this_color[0]
            greens[indices[0], indices[1]] = this_color[1]
            blues[indices[0], indices[1]] = this_color[2]
        alphas[np.where(slice!=-1)] = 255
        rgba_slice = np.zeros((slice.shape[0], slice.shape[1], 4), 'uint8')
        rgba_slice[..., 0] = reds
        rgba_slice[..., 1] = greens
        rgba_slice[..., 2] = blues
        rgba_slice[..., 3] = alphas
        return rgba_slice
    sys.exit('Colormap not found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--x', type=float)
    parser.add_argument('-y', '--y', type=float)
    parser.add_argument('-z', '--z', type=float)
    parser.add_argument('-t', '--threshold', type=int, nargs='+',default=[0, 255])
    parser.add_argument('--cct', type=str, required=True)
    parser.add_argument('-c', '--colormap', type=str)
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
    if args.colormap:
        image_slice = apply_colormap(slice, args.threshold, args.colormap)
    else:
        image_slice = apply_transparency(slice)
    img = Image.fromarray(image_slice, 'RGBA')
    img.save('output.png')
    img.show()
    
