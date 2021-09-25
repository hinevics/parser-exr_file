from re import search
from os import getcwd, listdir, rename

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
    for nf in listdir():
        if search(pattern=r'.exr$', string=nf):
            yield nf


def main():
    for fileexr in opendir():
        pathfile = r'{}\{}'.format(getcwd(), fileexr)
        fb = openfile(path=pathfile)
        comment = search_comment(fb=fb)
        newname = r'{path}\{commet}'.format(path=getcwd(), commet=comment)
        rename(src=pathfile, dst=newname)
    
    
if __name__ == '__main__':
    main()