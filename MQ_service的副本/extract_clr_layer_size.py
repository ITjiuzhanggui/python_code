#!/usr/bin/env python
import sys
import getopt
import os


class DockerSize(object):
    def __init__(self, fname):
        self.dockerfile = fname
        self.baselayersize = 0.0
        self.microservicelayersize = 0.0
        self.defbaselayersize = 0.0
        self.defmicroservicelayersize = 0.0
        self.totalsize = 0.0
        self.isbaselayer = 0
        self.sizestartpoint = 0
        self.layersize = 0

    def dumpdockerinfo(self):
        #        print("run  docker image history docker_image --no-trunc")
        if self.dockerfile == 'base':
            os.system('sudo docker image history clearlinux --no-trunc > tmp.dockersize')
        #            print("clearlinux:base")
        else:
            os.system('sudo docker image history clearlinux/' + self.dockerfile + ' --no-trunc > tmp.dockersize')
            #            print("clearlinux/" + self.dockerfile)
            os.system('sudo docker image history ' + self.dockerfile + '  --no-trunc > tmp.defdockersize')

    def show(self):
        print("default base layer Size:               %f MB" % self.defbaselayersize)
        print("default microservice added layer Size: %f MB" % self.defmicroservicelayersize)
        print("clearlinux base layer Size:               %f MB" % self.baselayersize)
        print("clearlinux microservice added layer Size: %f MB" % self.microservicelayersize)
        os.system('rm tmp.dockersize')
        os.system('rm tmp.defdockersize')

    def extractsizefromaline(self, oneline):
        #        print("\nextract the size info from a string: %s" % oneline)
        if 'MB' in oneline:
            self.layersize = float(oneline.split('MB')[0])
        elif 'GB' in oneline:
            self.layersize = float(oneline.split('GB')[0]) * 1000
        elif 'kB' in oneline:
            self.layersize = float(oneline.split('kB')[0]) / 1000
        elif 'B' in oneline:
            self.layersize = float(oneline.split('B')[0]) / 1000000

    def getdockersizeinfo(self):
        #        print("extracing docker base layer and microservice layer info")
        with open("./tmp.dockersize", 'r') as dockerhistory:
            lines = dockerhistory.readlines()
            for line in lines:
                if self.sizestartpoint == 0:
                    self.sizestartpoint = line.find('SIZE')
                #                    print("\nSIZE starts from: %d" % self.sizestartpoint)
                else:
                    # ADD is always used for the base layer
                    if 'ADD' in line:
                        self.isbaselayer = 1
                    self.extractsizefromaline(line[self.sizestartpoint:])
                    if self.isbaselayer == 0:
                        self.microservicelayersize += self.layersize
                    else:
                        self.baselayersize += self.layersize
        self.isbaselayer = 0
        self.sizestartpoint = 0

        with open("./tmp.defdockersize", 'r') as defdockerhistory:
            lines = defdockerhistory.readlines()
            for line in lines:
                if self.sizestartpoint == 0:
                    self.sizestartpoint = line.find('SIZE')
                else:
                    if 'ADD' in line:
                        self.isbaselayer = 1
                    self.extractsizefromaline(line[self.sizestartpoint:])
                    if self.isbaselayer == 0:
                        self.defmicroservicelayersize += self.layersize
                    else:
                        self.defbaselayersize += self.layersize


def help_menu():
    '''show usages'''
    print('''Usage: get_clearbaselayersize [options]
    Options:
    -h: display help menu
    -f: clearlinux docker image to be analyzed, such as: php; base means clearlinux:base''')


def main(argv):
    '''main function to get the image size info of a clearlinux docker image'''
    try:
        opts, _ = getopt.getopt(argv, "hf:")
    except getopt.GetoptError:
        help_menu()
        sys.exit(2)

    fname = ""
    for opt, arg in opts:
        if opt == '-h':
            help_menu()
            sys.exit()
        elif opt == '-f':
            fname = arg
    if not fname:
        print("Please specify a docker image, such as: php for clearlinux/php, or base for clearlinux:base!\n")
        help_menu()
        sys.exit(1)

    lp = DockerSize(fname)
    lp.dumpdockerinfo()
    lp.getdockersizeinfo()

    #    lp.calc()
    lp.show()


if __name__ == "__main__":
    main(sys.argv[1:])
