import optparse
import functions


def get_argument():
    parser = optparse.OptionParser(' [-l length] [-i include] [-o wanted_characters] [-n unwanted_characters] [-r repeat_characters(Y/N)] [-h help]')
    parser.add_option("-l", "--length", dest="length", help="Length to the password")
    parser.add_option("-n", "--no", dest="no", help="Unwanted characters to the password")
    parser.add_option("-i", "--include", dest="include", help="Include characters to the password")
    parser.add_option("-o", "--only", dest="only", help="Only wanted characters to the password")
    parser.add_option("-r", "--repeat", dest="repeat", help="Repeat the characters in the password")
    (options, argument) = parser.parse_args()
    return options


if __name__ == '__main__':
    options = get_argument()
    try:
        print(functions.pass_gen(options.length, options.no, options.only, options.include, options.repeat))
    except Exception:
        pass
