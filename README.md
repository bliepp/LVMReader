# LVMReader
A python reader for LabView's export format (.lvm)

# Using the program as standalone
Make it executable
```bash
chmod 755 lvmReader.py
```
And then use it as following:
```bash
./lvmReader File.lvm [export.file]
```

# Using as a python3 module
## Reading data from lvm-file
```python
from lvmReader import *

# Read file
my_lvm = LVMReader(path="Path/to/file.lvm")

# Auto-cleaned list of columns
my_data = my_lvm.data
# Auto-cleaned list of rows
my_transposed_data = my_lvm.transposed
```
## Exporting to text file
```python
# Change filename and export, autoset to original-filename.dat
my_lvm.filename = "export.dat"
# array must be a 2D-array
LVMReader.export(array, path="", space="\t", end="", transposed=False)
```

## Transpose a 2D-array list
```python
LVMReader.transpose(array)
```
