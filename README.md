# LabVIEW Reader
A python reader for LabVIEW's export format (.lvm)

# Using the program as standalone
Make it executable
```bash
chmod 755 lvmReader.py
```
And then use it as following:
```bash
./lvmReader.py file.lvm [export.file]
```

# Using as a python3 module
## Reading data from lvm-file
```python
from lvmReader import *

# Read file
my_lvm = LVMReader(path="Path/to/file.lvm")

# Auto-cleaned list of columns
my_columns = my_lvm.columns
# Auto-cleaned list of rows
my_rows = my_lvm.rows
```
## Exporting to text file
```python
# Change filename and export, autoset to original-filename.dat
my_lvm.filename = "export.dat" # to change autgenerated filename
# array must be a 2D-array
LVMReader.export(array, path="", space="\t", end="", header="", transposed=False)
```

## Transpose a 2D-array list
```python
LVMReader.transpose(array)
```
