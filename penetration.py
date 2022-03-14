import optparse

parser = optparse.OptionParser('usage %prog -H'+\
        '<target host. -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', \
        help='specify target port')
parser.add_option('-p', dest='tgtPort', type='int',\
        help='specify target port')
(options, args) = partser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort

if(tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)

