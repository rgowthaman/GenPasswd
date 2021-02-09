import optparse
from . import genpasswd


def get_argument():
    parser = optparse.OptionParser(usage='genpasswd [options]', version='genpasswd 1.1.6')
    parser.add_option("-l", "--length", dest="length", help="To set length to the password")
    parser.add_option("-r", "--repeat", dest="repeat", action='store_true', default=False,
                      help="To repeat the characters in the password")
    parser.add_option("-n", "--no", dest="ignore", help="To ignore unwanted characters to the password")
    parser.add_option("-o", "--only", dest="only", help="To create password only using wanted characters")
    parser.add_option("-i", "--include", dest="include", help="To include characters to the password")
    (options, argument) = parser.parse_args()
    return options


def gen_Password(rep, passlen=False, wanted=False, ign=False, inc=False):
    arg = genpasswd.Password(length=passlen, only=wanted, ignore=ign, include=inc, repeat=rep)
    passwd = arg.generate()
    return passwd


def main():
    options = get_argument()
    print(f"\n{gen_Password(options.repeat, options.length, options.only, options.ignore, options.include)}")


if __name__ == "__main__":
    main()
