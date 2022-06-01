import re

def file_name_split(path):
    return path.split('/')[-1].split('.')[0]


def file_name_re(path):
    return re.findall(r'[-\w]+\.', path)[0][:-1]


if __name__ == '__main__':
    print(file_name_split('../mainapp/views.py'))
    print(file_name_re('../mailnapp/views.py'))