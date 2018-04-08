from PIL import Image
import numpy as np
import argparse
import os


def build_voxel_array(directory, size):
    cct= []
    imagelist = sorted(os.listdir(directory))
    z_step = len(imagelist)//size[2]
    n = 0
    for i in range(size[2]):
        imgfile = imagelist[n]
        image = Image.open(os.path.join(directory, imgfile)).convert('L')
        slice = np.array(image)
        x_step = slice.shape[0]//size[0]
        y_step = slice.shape[1]//size[1]
        slice = slice[::x_step,::y_step]
        cct.append(slice)
        n+=z_step
    cct = np.asarray(cct)
    return cct

def create_cct_file(voxels):
    f = open('file.cct', 'w')
    f.write('{},{},{}'.format(voxels.shape[0], voxels.shape[1], voxels.shape[2]))
    for plane in voxels:
        f.write('\n')
        f.write(','.join(map(str,plane.ravel().tolist())))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, required=True)
    parser.add_argument('--size', type=int, nargs='+',default=[128, 128, 128])
    args = parser.parse_args()
    voxels = build_voxel_array(args.path, args.size)
    create_cct_file(voxels)




