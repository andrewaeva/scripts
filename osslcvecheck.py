__author__ = 'andrewa'
#!-*-coding-*- utf-8
import pefile
import os
import sys
import getopt
ext = ['.dll', '.exe']

ccs_injection = ['4', '5', '6', '0.9.8i', '0.9.8x', '0.9.8s', '0.9.8d', '0.9.8n', '0.9.8y', '0.9.8j', '0.9.8t', '0.9.8e', '0.9.8o', '0.9.8', '0.9.8k', '0.9.8u', '0.9.8f', '0.9.8p', '0.9.8a', '0.9.8l', '0.9.8v', '0.9.8g', '0.9.8q', '0.9.8b', '0.9.8m', '0.9.8w', '0.9.8h', '0.9.8r', '0.9.8c', '0.9.8m', '1.0.0', '1.0.0j', '1.0.0e', '1.0.0', '1.0.0k', '1.0.0', '1.0.0f', '1.0.0a', '1.0.0l', '1.0.0', '1.0.0g', '1.0.0b', '1.0.0', '1.0.0h', '1.0.0c', '1.0.0', '1.0.0i', '1.0.0d', '1.0.1f', '1.0.1a', '1.0.1g', '1.0.1b', '1.0.1', '1.0.1c', '1.0.1', '1.0.1d', '1.0.1', '1.0.1e', '1.0.1']
heart_bleed = ['1.0.1a', '1.0.1f', '1.0.1b', '1.0.1', '1.0.1c', '1.0.1', '1.0.1d', '1.0.1', '1.0.1e', '1.0.1', '1.0.2']


class PE(object):
    def __init__(self, file):
        self.filename, self.version, self.file_version, self.product_version, self.vendor, self.product \
        = ['', '', '', '', '', '']
        self.dump_info(file)

    def to_s(self):
        return self.product

    def print_version(self):
        print self.version, self.file_version, self.product_version

    def dump_info(self, file):
        f = open(file, 'rb')
        pe = pefile.PE(file)
        try:
            self.version = pe.VS_VERSIONINFO
        except AttributeError:
            pass
        try:
                for fileinfo in pe.FileInfo:
                    #TODO: InternalName, FileVersion, ProductVersion, OriginalFilename
                    if fileinfo.Key == 'StringFileInfo':
                        for st in fileinfo.StringTable:
                            for entry in st.entries.items():
                                if entry[0] == 'CompanyName':
                                    self.vendor = entry
                                if entry[0] == 'ProductName':
                                    self.product = entry[1]
                                if entry[0] == 'FileVersion':
                                    self.file_version = entry
                                if entry[0] == 'ProductVersion':
                                    self.product_version = entry[1]
        except AttributeError:
            #print "PE instance has no attribute \'FileInfo\'"
            pass


def main(argv):
    dir = ''
    info = 0
    try:
        opts, args = getopt.getopt(argv, "h:d:i:", ["dir=", "info="])
    except getopt.GetoptError:
        print 'osslcvecheck.py -d <directory> -i <1,0>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'osslcvecheck.py -d <directory> -i <1,0>'
            print '-i 0 output only vuln version of tested files'
            print '-i 1 output all tested files'
            sys.exit()
        elif opt == '-d':
            dir = arg
            print str('Directory ' + dir + '\n\n')
        elif opt == '-i':
            info = int(arg)
    for dirpath, dirnames, filenames in os.walk(dir):
        for name in filenames:
            fileName, fileExtension = os.path.splitext(name)
            if fileExtension in ext:
                target = os.path.join(str(dirpath), name)
                a = PE(target)
                if info == 1:
                    try:
                        print str(target + '     ' + a.product + ' ' + a.product_version)
                    except:
                        print str(target)
                if a.product.lower().count('openssl'):
                    if a.product_version in ccs_injection:
                        print str(target + ' vuln CCS_injection version: ' + a.product_version)
                    if a.product_version in heart_bleed:
                        print str(target + ' vuln Heartbleed version: ' + a.product_version)


if __name__ == "__main__":
    main(sys.argv[1:])
