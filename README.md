# loompy v3.0.6 with Zarr support

loompy with an experimental Zarr support.

- Open zarr.loom:
```python
>>> import loompy
>>> ds = loompy.connect('test.zarr.loom', 'r+')
```

- Create zarr.loom:
```python
>>> import loompy
>>> ds = loompy.new('test2.zarr.loom', 'r+', backend='zarr')
```

- Modify attributes:
```python
>>> ds.ra.keys()
['Gene']
>>> ds.ra['Gene']
array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'J', 'K', 'L',
       'M', 'N', 'O', 'P', 'Q', 'R', 'S'], dtype=object)
>>> ds.ra['Gene2'] = ["G_" + gene for gene in ds.ra['Gene']]
>>> ds.ra['Gene2']
array(['G_A', 'G_B', 'G_C', 'G_D', 'G_E', 'G_F', 'G_G', 'G_H', 'G_I',
       'G_L', 'G_J', 'G_K', 'G_L', 'G_M', 'G_N', 'G_O', 'G_P', 'G_Q',
       'G_R', 'G_S'], dtype=object)
>>> del ds.ra['Gene2']
>>> ds.ra.keys()
['Gene']
```

- Modify matrix
```python
>>> ds[:, :]
array([[0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])
>>> ds[0, 0] = 1
>>> ds[:, :]
array([[1., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])
```

# loompy v3.0

⭐ Loompy v3.0 was released Sep. 24, 2019!

To get started, head over to [the documentation](http://loompy.org)!

Loom, loompy, and the [loom-viewer](https://github.com/linnarsson-lab/loom-viewer) are being developed by members of the [Linnarsson Lab](http://linnarssonlab.org).

