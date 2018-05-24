## Example 1

yz plane at x = .5
    
    quickslice slice file.cct -x .5

![example1.png](https://github.com/raghavaro/cct/blob/master/examples/example1.png?raw=true)

## Example 2

xz plane at y = .5

    quickslice slice file.cct -y .5

![example2.png](https://github.com/raghavaro/cct/blob/master/examples/example2.png?raw=true)

## Example 3

xy plane at z = .5

    quickslice slice file.cct -z .5

![example3.png](https://github.com/raghavaro/cct/blob/master/examples/example3.png?raw=true)

## Example 4

yz plane at x = .5 with threshold (103, 120)
    
    quickslice slice file.cct -x .5 -t 103 120

![example4.png](https://github.com/raghavaro/cct/blob/master/examples/example4.png?raw=true)

## Example 5

yz plane at x = .5 with threshold (103, 120) with 'viridis' colormap and transparent background
    
    quickslice slice file.cct -x .5 -t 103 120 -c viridis --transparent

![example5.png](https://github.com/raghavaro/cct/blob/master/examples/example5.png?raw=true)

## Example 6

yz plane at x = .5 with threshold (103, 120) with 'jet' colormap and transparent background
    
    quickslice slice file.cct -x .5 -t 103 120 -c jet --transparent

![example6.png](https://github.com/raghavaro/cct/blob/master/examples/example6.png?raw=true)

## Example 7

yz plane at x = .5 with 'viridis' colormap and no threshold
    
    quickslice slice file.cct -x .5 -c viridis

![example7.png](https://github.com/raghavaro/cct/blob/master/examples/example7.png?raw=true)
