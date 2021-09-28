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
    fileexr = [nf for nf in listdir(path=format(getcwd()))
               if search(pattern=r'.exr$', string=nf) and (not search(pattern=r'^L', string=nf))]
    if fileexr:
        for nf in fileexr: 
            yield nf
    else:
        print('Exr file not found!')

def search_number_file(path:str) -> str:
    return search(pattern=r'_(?P<number_file>\d+).exr$', string=path).group('number_file')

def parser_exr():
    for fileexr in opendir():
        pathfile = r'{}\{}'.format(getcwd(), fileexr)
        fb = openfile(path=pathfile)
        comment = search_comment(fb=fb)
        number_file = search_number_file(path=pathfile)
        newname = r'{path}\{commet}__{number_file}.exr'.format(path=getcwd(), commet=comment, number_file=number_file)
        print('{} -> {}'.format(fileexr, comment))
        rename(src=pathfile, dst=newname)


def parser():
    # Start request 
    command = input('to start write "start" or "s": ')
    if command in ['start', 's']:
        print('START')
        parser_exr()
        print('END')
        input('Press Enter to finish')

    else:
        print('error! restart. call the options "start"!')
        
def main():
    parser()
    
    
    
if __name__ == '__main__':
    main()