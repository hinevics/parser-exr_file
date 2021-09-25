import re
import os


DEFAULT_PATH_FILE = r'D:\Development\Coding\parser-exr_file\CUBE___1312.exr'

def search_comment(fb:bytes) -> str:
    comment = re.search(pattern=r'comment(?P<comment>.+)comments(?P<comments>.+)compression', string=str(fb))
    print(re.sub(string=comment.groupdict()['comment'], pattern=r'\\x00string\\x00\\t\\x00\\x00\\x00', repl=''))
    # print(re.sub(pattern=r'', )))
    # print(re.search(pattern=r'\\x00string\\x00\\t\\x00\\x00\\x00', string=comment.groupdict()['comment']).group())


def openfile(path:str=DEFAULT_PATH_FILE) -> bytes:
    with open(file=path, mode='br') as file:
        r_0 = file.readline()
    return r_0
   
def opendir() -> list:
    """
    функция находит все файлы расширения exr в директории где находится скрипт
    """
    for nf in os.listdir():
        if re.search(pattern=r'.exr$', string=nf):
            yield nf


def main():
    # fb = openfile(path=DEFUALT_PATH_FILE)
    # search_comment(fb)
    for i in opendir():
        with open(file=r'{a1}\{a2}'.format(a2=i, a1=os.getcwd())) as file:
            print(file)


if __name__ == '__main__':
    main()