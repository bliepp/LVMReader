#!/usr/bin/python3
#
# A module to load and export LabView .lvm files
#

class LVMReader():
    """
    Load *.lvm files exported by LabView

    Parameters
    ----------
    path: string
        Location of the file

    Attributes
    ----------
    filename: string
        Filename to export to.
    data: 2D-array
        The converted and cleaned up data.
        Every column is a list inside of the data list.
    transposed: 2D-array
        The data attribute transposed.
        Every row is a list inside of the data list.

    Methods
    -------
    transpose(list)
        Transposes a 2D-array list (e.g. matrix, table, ...)
    export(path="", space="\t", end="", transposed=False)
        Exports the data as a text table to the given
        path with the given file name.
    """

    def __init__(self, path):
        self.filename = path.split("/")[-1][:-4] + ".dat"
        self._raw = list()
        self.__data = list()

        with open(path) as lvm:
            self._raw = lvm.readlines()

        self.__clean()

    def __clean(self):
        # Make table
        for i in range(len(self._raw)):
            self._raw[i] = self._raw[i].replace(",", ".")
            self.__data.append(
                    self._raw[i].strip().split("\t")
                )

        # Remove header
        ## Get last occurence of "End Header"
        if "***End_of_Header***" in self.__data:
            i = len(self.__data) - 1 - self.__data[::-1].index(
                    ["***End_of_Header***"]
                ) + 2
        else: i = 0
        self.__data = self.__data[i:]

        # Convert to floats
        self.__data = [
                [ float(x) for x in row ] for row in self.__data
            ]
        
        self.__data = LVMReader.transpose(self.__data)

    def transpose(array):
        # Transpose
        return list(map(list, zip(*array)))[:]

    def export(array, path="", space="\t", end="", header="", transposed=False):
        """
        Template for universal exporting.
        """
        # inverse logic!
        if not transposed: array = LVMReader.transpose(array)
        # check for header
        if header != "": header += "\n"

        with open(path, "w") as out:
            out.write(header)
            for i in array:
                out.write(space.join("{:E}".format(x) for x in i) + end)
                out.write("\n")
    
    @property
    def columns(self):
        return self.__data[:]

    @property
    def rows(self):
        return LVMReader.transpose(self.__data)

if __name__ == "__main__":
    import sys

    # get filename
    if len(sys.argv) > 1:
        # init lvm file
        lvm = LVMReader(sys.argv[1])
        
        # get out file name
        if len(sys.argv) > 2:
            lvm.filename = sys.argv[2]
        
        # Export and show data
        LVMReader.export(lvm.columns, lvm.filename)
        print(lvm.columns)
