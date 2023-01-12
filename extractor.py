import zipfile

def extract_archive(arc_path,dest_dir):
    with zipfile.ZipFile(arc_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("compressed.zip","Extracted")