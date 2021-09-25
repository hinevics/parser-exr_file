from re import search
from os import getcwd, listdir, rename
import argparse

def search_comment(fb:str) -> str:
    """
    name search
    """
    return search(pattern=r'comment.+\\x00\\x00(?P<comment>.+)comments', string=fb).group('comment')
  
def openfile(path:str) -> str:
    """
    the function opens files and returns the first bits where the information is stored
    """
    with open(file=path, mode='br') as file:
        r_0 = file.readline()
    return str(r_0)
   
def opendir() -> list:
    """
    the function finds all exr files in the directory where the script is located
    """
    fileexr = [nf for nf in listdir(path=r'{}\{}'.format(getcwd(), 'file'))
               if search(pattern=r'.exr$', string=nf)]
    if fileexr:
        for nf in fileexr: 
            yield nf
    else:
        print('Exr file not found!')

def parser():
    for fileexr in opendir():
        pathfile = r'{}\file\{}'.format(getcwd(), fileexr)
        fb = openfile(path=pathfile)
        comment = search_comment(fb=fb)
        newname = r'{path}\file\{commet}'.format(path=getcwd(), commet=comment)
        rename(src=pathfile, dst=newname)
        print('{} -> {}'.format(fileexr, comment))


def parser_exr(arguments):
    if arguments.command == 'start':
        print('START')
        parser()
        print('END')
    else:
        print('error! restart. call the options "start"!')
        
def set_parser(parser):
    parser.add_argument("-c", '--command', help="This is the 'a' variable")
    parser.set_defaults(callback=parser_exr)
    
def main():
    parser = argparse.ArgumentParser(
        description='This program (%(prog)s) creates an Inverted Index from a set of documents',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    set_parser(parser)
    args = parser.parse_args()
    args.callback(args)  # callback for branches
    
    
    
if __name__ == '__main__':
    main()