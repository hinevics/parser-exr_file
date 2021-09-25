import re
import os


def search_comment(fb:str) -> str:
    """
    поиск названия
    """
    return re.search(pattern=r'comment.+\\x00\\x00(?P<comment>.+)comments', string=fb).group('comment')
    # comment = re.search(pattern=r'comment(?P<comment>.+)comments(?P<comments>.+)compression', string=str(fb))
    # print(comment.groupdict()['comment'])
    # print(re.sub(string=comment.groupdict()['comment'], pattern=r'(\\x00string\\x00\\t\\x00\\x00\\x00)|(\\x00string\\x00\\x0c\\x00\\x00\\x00)', repl=''))
    # print(re.sub(pattern=r'', )))
    # print(re.search(pattern=r'\\x00string\\x00\\t\\x00\\x00\\x00', string=comment.groupdict()['comment']).group())


def openfile(path:str) -> str:
    """
    функция открывает файлы и возврщает первые биты, где хранится информация
    """
    with open(file=path, mode='br') as file:
        r_0 = file.readline()
    return str(r_0)
   
def opendir() -> list:
    """
    функция находит все файлы расширения exr в директории где находится скрипт
    """
    for nf in os.listdir():
        if re.search(pattern=r'.exr$', string=nf):
            yield nf


def main():
    for fileexr in opendir():
        pathfile = r'{}\{}'.format(os.getcwd(), fileexr)
        fb = openfile(path=pathfile)
        comment = search_comment(fb=fb)
        newname = r'{path}\{commet}'.format(path=os.getcwd(), commet=comment)
        os.rename(src=pathfile, dst=newname)
    # os.rename(src='{}\{}', dst='\')
    # rename_file(path='{}\{}'.format(os.getcwd(), 'test.exr'), newname='{}\{}'.format(os.getcwd(), 'CUBE___1312.exr'))
    # rename_file(path=r'D:\Development\Coding\parser-exr_file\CUBE___1312.exr', newname=r'D:\Development\Coding\parser-exr_file\test.exr')
    # for i in enopendir():
    #     fb = openfile(path=i)
        # print(search_comment(fb=str(fb)))
        # print(rename_file(path=i, newname=r'{a1}\{a2}'.format(a1=os.getcwd(), a2='test')))

if __name__ == '__main__':
    main()