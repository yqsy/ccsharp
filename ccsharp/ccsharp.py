import os

from bs4 import BeautifulSoup

PATH = 'C:/work/source/kstp_new'

EXTENSION = ['.csproj']


def print_proj_info(file):
    with open(file, encoding='utf-8-sig') as fd:
        file_str = fd.read()
        soup = BeautifulSoup(file_str, 'lxml')

        propertygroups = soup.project.find_all('propertygroup')

        for propertygroup in propertygroups:
            if not propertygroup.has_attr('condition'):
                assemblyname = propertygroup.find_all('assemblyname')
                if assemblyname:
                    assert (len(assemblyname) == 1)
                    print(assemblyname[0].text, end=' ')

                platform = propertygroup.find_all('platform')
                if platform:
                    assert (len(platform) == 1)
                    print(platform[0].text, end=' ')

                configuration = propertygroup.find_all('configuration')
                if configuration:
                    assert (len(configuration) == 1)
                    print(configuration[0].text, end=' ')

        print('')


def delete_x86_propertygroup(file):

    # replace ol file
    soup = ''

    with open(file, encoding='utf-8-sig') as fd:
        file_str = fd.read()
        soup = BeautifulSoup(file_str, 'lxml')

        propertygroups = soup.project.find_all('propertygroup')

        for propertygroup in propertygroups:
            if propertygroup.has_attr('condition'):
                if 'x86' in propertygroup['condition']:
                    propertygroup.decompose()

    with open(file, 'w') as fd:
        fd.write(str(soup))


def recursion():
    for root, _, files in os.walk(PATH):
        for file in files:
            file = os.path.join(root, file)
            _, file_extension = os.path.splitext(file)
            if file_extension in EXTENSION:
                # print_proj_info(file)
                delete_x86_propertygroup(file)


def main():
    recursion()
    # print_proj_info('C:/work/source/kstp_new/vs2015源代码/KSIITS/SysCommon/SysCommon.csproj')


if __name__ == '__main__':
    main()
