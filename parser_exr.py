import re

DEFUALT_PATH_FILE = r'E:\Hinevics\Dropbox\Programm\GitHub\parser-exr_file\CUBE___1312.exr'

def search_comment(fb:bytes) -> str:
    comment = re.search(pattern=r'comment(?P<comment>.+)comments(?P<comments>.+)compression', string=str(fb))
    print(re.sub(string=comment.groupdict()['comment'], pattern=r'\\x00string\\x00\\t\\x00\\x00\\x00', repl=''))
    # print(re.sub(pattern=r'', )))
    # print(re.search(pattern=r'\\x00string\\x00\\t\\x00\\x00\\x00', string=comment.groupdict()['comment']).group())


def openfile(path:str=DEFUALT_PATH_FILE) -> bytes:
    with open(file=path, mode='br') as file:
        r_0 = file.readline()
    return r_0
   

def main():
    fb = openfile(path=DEFUALT_PATH_FILE)
    search_comment(fb)


if __name__ == '__main__':
    main()