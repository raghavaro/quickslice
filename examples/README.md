## Example 1

yz plane at x = .5
    
    python main.py slice file.cct -x .5

![example1.png](https://github.com/agu3010/cct/blob/master/examples/example1.png?raw=true)

## Example 2

xz plane at y = .5

    python main.py slice file.cct -y .5

![example2.png](https://github.com/agu3010/cct/blob/master/examples/example2.png?raw=true)

## Example 3

xy plane at z = .5

    python main.py slice file.cct -z .5

![example3.png](https://github.com/agu3010/cct/blob/master/examples/example3.png?raw=true)

## Example 4

yz plane at x = .5 with threshold (103, 120)
    
    python main.py slice file.cct -x .5 -t 103 120

![example4.png](https://github.com/agu3010/cct/blob/master/examples/example4.png?raw=true)

## Example 5

yz plane at x = .5 with threshold (103, 120) with 'viridis' colormap
    
    python main.py slice file.cct -x .5 -t 103 120 -c viridis

![example5.png](https://github.com/agu3010/cct/blob/master/examples/example5.png?raw=true)

## Example 6

yz plane at x = .5 with threshold (103, 120) with 'jet' colormap
    
    python main.py slice file.cct -x .5 -t 103 120 -c jet

![example6.png](https://github.com/agu3010/cct/blob/master/examples/example6.png?raw=true)

## Example 7

yz plane at x = .5 with 'viridis' colormap and no threshold
    
    python main.py slice file.cct -x .5 -c viridis

![example7.png](https://github.com/agu3010/cct/blob/master/examples/example7.png?raw=true)
