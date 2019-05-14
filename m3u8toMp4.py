import os
import sys

def convert2Mp4(path, fname):
    print('Convert ', path, fname)
    source = os.path.join(path, fname)
    dest = os.path.join(path, fname.split('.')[0]+'.mp4')
    os.system('ffmpeg -y -v 0 -i %s -vcodec copy -acodec copy -absf aac_adtstoasc %s'%(source, dest))

def walk(path):
    sub_files = os.listdir(path)
    is_dir = True
    for sub_file in sub_files:
        sub_path = os.path.join(path, sub_file)
        if os.path.isdir(sub_path):
            walk(sub_path)
        else:
            is_dir = False
            break
    if not is_dir :
        #print(sub_files)
        target_file = None
        for fname in sub_files:
            if fname.endswith('.m3u8'):
                target_file = fname
        convert2Mp4(path, target_file)


def main(path):
    walk(path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python m3u8toMp4.py path')
    else:
        main(sys.argv[1])
