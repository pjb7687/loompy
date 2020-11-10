#!/usr/bin/env python
#
# loom_to_zarr.py
#
# Author: Jeongbin Park
# Description: Converts loom file to loom.zarr
# Usage: loom_to_zarr.py input.loom

import os
import h5py, zarr
import numpy as np

def hdf5_to_zarr(hdf5_file, zarr_group=None):
    try:
        unicode
    except NameError:
        unicode = str

    opened = False
    if isinstance(hdf5_file, (bytes, unicode)):
        hdf5_filename = hdf5_file
        hdf5_file = h5py.File(hdf5_file, "r")
        opened = True
    else:
        hdf5_filename = hdf5_file.filename

    if zarr_group is None:
        zarr_name = os.path.splitext(hdf5_filename)[0] + os.extsep + "zarr.loom"
        zarr_group = zarr.open_group(zarr_name, mode="w")

    def copy(name, obj):
        if isinstance(obj, h5py.Group):
            zarr_obj = zarr_group.create_group(name)
        elif isinstance(obj, h5py.Dataset):
            if obj.dtype == "|O":
                # string
                try:
                    # string array
                    zarr_obj = zarr_group.create_dataset(name, data=obj[:].astype(np.string_), chunks=obj.chunks)
                except:
                    # string scalar
                    obj = str(obj[()])
                    zarr_obj = zarr_group.create_dataset(name, data=obj)
                print(name, obj)
            else:
                zarr_obj = zarr_group.create_dataset(name, data=obj, chunks=obj.chunks)
        else:
            assert False, "Unsupport HDF5 type."

        try:
            zarr_obj.attrs.update(obj.attrs) 
        except AttributeError:
            pass

    hdf5_file.visititems(copy)

    if opened:
        hdf5_file.close()

    return zarr_group

if __name__ == "__main__":
    import sys
    hdf5_to_zarr(sys.argv[1])
