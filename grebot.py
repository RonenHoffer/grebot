from os import walk
from os.path import abspath, join
from argparse import ArgumentParser
from re import findall, sub, IGNORECASE


class Grebot(object):

    LINE_FORMAT = '%s:\t%s'

    def __init__(self, function_name, extensions, base_dir=None, sensitive=False, color=False):
        self._search_word = '%s|%s|%s|%s' % (function_name, function_name.replace('_', ' '),
                                             sub('(.)([A-Z][a-z_]+)', r'\1 \2', function_name),
                                             function_name.replace(' ', '_'))
        self._base_dir = base_dir
        self._is_case_sensitive = 0 if sensitive else IGNORECASE
        self._word_format = '\033[91m%s\033[0m' if color else '%s'
        self._extensions = '|'.join(['\w+\.%s$' % extension for extension in extensions.split(',')])

    def main(self):
        for current_dir, dirs, files in walk(self._base_dir, followlinks=False):
            [self._find_in_file(abspath(join(current_dir, f)))
             for f in files if findall(self._extensions, f)]

    def _find_in_file(self, path):
        to_print = []
        with open(path, 'rb') as f:
            data_lines = f.readlines()
        for line_num, line in enumerate(data_lines):
            result = findall(self._search_word, line, self._is_case_sensitive)
            if result:
                to_print.append(self.LINE_FORMAT % (line_num + 1, line.replace(result[0], self._word_format % result[0])))
        if to_print:
            print 'in file: %s' % path
            print ''.join(to_print)


def get_parser():
    parser = ArgumentParser()
    parser.usage = '%(prog)s function_name [-despch]'
    parser.add_argument('-c', '--color', action='store_true', default=False,
                        help='show matched words in color')
    parser.add_argument('-s', '--sensitive', action='store_true', default=False,
                        help='Be case sensitive')
    parser.add_argument('-p', '--path', type=str, default='.',
                        help='path to check to start recursive check from')
    parser.add_argument('-e', '--extensions', type=str, default='txt,robot,py',
                        help='which file extensions to check')
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='show exception in case of fail')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args, word = parser.parse_known_args()
    try:
        function_name = ' '.join(word)
        if function_name:
            Grebot(function_name, args.extensions, args.path, args.sensitive, args.color).main()
    except:
        if args.debug:
            raise
        print parser.format_usage()
