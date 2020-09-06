import os
import sys
import argparse
FILE_FORMATS = {'.html5': 'HTML', '.html': 'HTML', '.htm': 'HTML', '.xhtml': 'HTML', '.jpeg': 'IMAGES', '.jpg': 'IMAGES', '.tiff': 'IMAGES', '.gif': 'IMAGES', '.bmp': 'IMAGES', '.png': 'IMAGES', '.bpg': 'IMAGES', 'svg': 'IMAGES', '.heif': 'IMAGES', '.psd': 'IMAGES', '.avi': 'VIDEOS', '.flv': 'VIDEOS', '.wmv': 'VIDEOS', '.mov': 'VIDEOS', '.mp4': 'VIDEOS', '.webm': 'VIDEOS', '.vob': 'VIDEOS', '.mng': 'VIDEOS', '.qt': 'VIDEOS', '.mpg': 'VIDEOS', '.mpeg': 'VIDEOS', '.3gp': 'VIDEOS', '.oxps': 'DOCUMENTS', '.epub': 'DOCUMENTS', '.pages': 'DOCUMENTS', '.docx': 'DOCUMENTS', '.doc': 'DOCUMENTS', '.fdf': 'DOCUMENTS', '.ods': 'DOCUMENTS', '.odt': 'DOCUMENTS', '.pwi': 'DOCUMENTS', '.xsn': 'DOCUMENTS', '.xps': 'DOCUMENTS', '.dotx': 'DOCUMENTS', '.docm': 'DOCUMENTS', '.dox': 'DOCUMENTS', '.rvg': 'DOCUMENTS', '.rtf': 'DOCUMENTS', '.rtfd': 'DOCUMENTS', '.wpd': 'DOCUMENTS', '.xls': 'DOCUMENTS', '.xlsx': 'DOCUMENTS', '.ppt': 'DOCUMENTS', 'pptx': 'DOCUMENTS', '.a': 'ARCHIVES', '.ar': 'ARCHIVES', '.cpio': 'ARCHIVES', '.iso': 'ARCHIVES', '.tar': 'ARCHIVES', '.gz': 'ARCHIVES', '.rz': 'ARCHIVES', '.7z': 'ARCHIVES', '.dmg': 'ARCHIVES', '.rar': 'ARCHIVES', '.xar': 'ARCHIVES', '.zip': 'ARCHIVES', '.aac': 'AUDIO', '.aa': 'AUDIO', '.dvf': 'AUDIO', '.m4a': 'AUDIO', '.m4b': 'AUDIO', '.m4p': 'AUDIO', '.mp3': 'AUDIO', '.msv': 'AUDIO', 'ogg': 'AUDIO', 'oga': 'AUDIO', '.raw': 'AUDIO', '.vox': 'AUDIO', '.wav': 'AUDIO', '.wma': 'AUDIO', '.txt': 'PLAINTEXT', '.in': 'PLAINTEXT', '.out': 'PLAINTEXT', '.pdf': 'PDF', '.py': 'PYTHON', '.xml': 'XML', '.exe': 'EXE', '.sh': 'SHELL'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='Enter source to organise')
    parser.add_argument('--destination', type=str, default='/', help='Enter the destination for organised folder')
    args = parser.parse_args()
    organize_junk(args.source, args.destination)
    sys.stdout.write("Shortcut made successfully")


def organize_junk(x, z):
    os.chdir(x)
    for entry in os.listdir(x):
        y = os.path.abspath(entry)
        if os.path.isfile(y):
            file_path = os.path.abspath(y)
            file_name = os.path.basename(file_path)
            file_format = os.path.splitext(file_path)[1].lower()
            if file_format in FILE_FORMATS:
                directory_path = z+"/"+FILE_FORMATS[file_format]
                os.makedirs(directory_path, exist_ok=True)
                os.symlink(file_path, directory_path+"/"+file_name)
    for entry in os.listdir(x):
        y = os.path.abspath(entry)
        working_dir = os.path.basename(y)+"/"
        if os.path.isdir(y):
            organize_junk(y, z+working_dir)


if __name__ == "__main__":
    main()
