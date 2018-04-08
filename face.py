from PIL import Image
import numpy as np
import argparse
import os
import sys



def read_cct_file(file):
    lines = [line.rstrip('\n') for line in open(file)]
    info = map(int, lines.pop(0).split(','))
    voxels = []
    while len(lines)>0:
        row = np.fromstring(lines.pop(0), dtype=int, sep=',')
        slice = np.reshape(row, (info[1], info[0]))
        voxels.append(slice)
    voxels = np.asarray(voxels)
    return voxels

def get_face_at_threshold(voxels, face, threshold):
    print voxels.shape
    print face
    print threshold
    slice = None
    if face == 'xy0':
        slice = voxels[0,:,:]
    elif face == 'xy1':
        slice = voxels[voxels.shape[2]-1,:,:]
    elif face == 'x0z':
        slice = voxels[:,0,:]
    elif face == 'x1z':
        slice = voxels[:,voxels.shape[1]-1,:]
    elif face == '0yz':
        slice = voxels[:,:,0]
    elif face == '1yz':
        slice = voxels[:,:,voxels.shape[0]-1]
    return slice
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--face', type=str, required=True)
    parser.add_argument('-t', '--threshold', type=int, nargs='+',default=[0, 255])
    parser.add_argument('--cct', type=str, required=True)
    args = parser.parse_args()
    possible_faces = ['xy0', 'xy1', 'x0z', 'x1z', '0yz', '1yz']
    if not args.face in possible_faces:
        sys.exit('cannot determine face')
    #face = [args.face[0], args.face[1], args.face[2]]
    voxels = read_cct_file(args.cct)
    slice = get_face_at_threshold(voxels, args.face, args.threshold)
    if not slice:
        sys.exit('An error occured')
    img = Image.fromarray(np.uint8(slice * 255), 'L')
    img.save('output.png')
    img.show()
    
