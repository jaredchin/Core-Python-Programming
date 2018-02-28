import os
import subprocess

class UnixCmd(object):
    def __cd__(self, path):
        self.redirect_stdout('cd', path)

    def __ls__(self):
        self.redirect_stdout('dir', os.getcwd())

    def __cat__(self, fname):
        self.redirect_stdout('type', fname)

    def __cp__(self, fname, path):
        self.redirect_stdout('copy', fname, path)

    def __mv__(self, org_name, new_name):
        self.redirect_stdout('ren', org_name, new_name)

    def __rm__(self, fname):
        self.redirect_stdout('del', fname)

    def __more__(self, fname):
        self.redirect_stdout('more', fname)

    @staticmethod
    def redirect_stdout(cmd, *path):
        line = 0
        fp = subprocess.Popen([cmd, path], stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, shell=True)
        for eachline in fp.stdout:
            line += 1
            print(eachline)
            print(str(eachline).strip('\r\n'))
            if line >= 32:
                input('-more-')

def shell():
    cmd = UnixCmd()
    sh_cmd = {'cd': cmd.__cd__, 'ls': cmd.__ls__, 'cat': cmd.__cat__,
              'cp': cmd.__cp__, 'mv': cmd.__mv__, 'rm': cmd.__rm__,
              'more': cmd.__more__}
    while True:
        msg = input('[%s:]$' % os.name).strip()
        sh = msg.split(' ')
        if sh[0] not in sh_cmd.keys():
            print('Invalid command.')
            continue
        if msg == 'ls':
            sh_cmd[msg]()
            continue
        if len(sh) < 2:
            sh.append('')
        if sh[0] in ['cd', 'cat', 'rm', 'more']:
            sh_cmd[sh[0]](sh[1])
            continue
        if len(sh) < 3:
            sh.append('')
        if sh[0] in ['mv', 'cp']:
            sh_cmd[sh[0]](sh[1], sh[2])
        if sh[0] == 'exit':
            break


shell()