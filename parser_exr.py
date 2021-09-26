from re import search
from os import getcwd, listdir, rename

def search_comment(fb:str) -> str:
    """
    name search
    """
    return search(pattern=r'comment.+(?P<comment>L.+)comments', string=fb).group('comment')
  
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

def parser_exr():
    for fileexr in opendir():
        pathfile = r'{}\file\{}'.format(getcwd(), fileexr)
        fb = openfile(path=pathfile)
        comment = search_comment(fb=fb)
        print(comment)
        # newname = r'{path}\file\{commet}.exr'.format(path=getcwd(), commet=comment)
        # rename(src=pathfile, dst=newname)
        # print('{} -> {}'.format(fileexr, comment))


def parser():
    # Start request 
    command = input('to start write "start" or "s": ')
    if command in ['start', 's']:
        print('START')
        parser_exr()
        print('END')
    else:
        print('error! restart. call the options "start"!')
        
def main():
    parser()
    
    
    
if __name__ == '__main__':
    main()