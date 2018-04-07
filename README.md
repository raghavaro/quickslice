CCT File format

Compressed Computed Tomography Files

Line 1:                       sizeX,sizeY,sizeZ
Line 2 to Line (sizeZ + 1):   Slice representation

Example:

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


