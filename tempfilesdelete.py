__author__ = 'nallagun'

import glob, os, sys, shutil


class TempFilesDelete:

    def deletefolders(self, path):

        """
        This method is used to delete anonymous driver profiles from Temp folder

        """
        try:

            self.path = os.path.abspath(path)
            files = glob.glob(path + "anonymous*")

            for file_name in sorted(files):
                shutil.rmtree(file_name)

        except IOError:

            print "The file does not exist, exiting gracefully"


if __name__ == "__main__":

    t = TempFilesDelete()
    t.deletefolders(sys.argv[0])



