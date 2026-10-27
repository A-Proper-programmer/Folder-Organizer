import os, argparse, shutil, datetime, hashlib

# SHELL ARGUMENTS
parser = argparse.ArgumentParser(description='A program that helps to organize a folder by extension, and remove duplicates.')
parser.add_argument("-f", "--folder", type=str, default="", help="Absolute Path to folder/Leave empty to clean current folder")
parser.add_argument("-i", "--inclpy", action="store_true", help="Type this to include organising this own file")
args = parser.parse_args()

def gtcwd(_f):
    if _f:
        if os.path.exists(_f):
            os.chdir(_f)
            return _f
        else:
            print(f"The folder does not exist! [{_f}]\n")
    else:
        os.chdir(os.path.dirname(__file__))
        return os.path.dirname(__file__)

def main(_f, _i):
    global DUPES, REPORT
    
    gtcwd(_f) # CWD

    # FOLDER ORGANIZER
    directories = os.listdir()
    folders = [i for i in directories if os.path.isdir(os.path.join(os.getcwd(), i))]
    hashes = []

    for item in directories:
        if ((not _i) and (item==os.path.basename(__file__))) or (not os.path.isfile(item)) or (item == "README.md"):
            continue
        if len(item)>20:
            if item[:14] == "Summary log at":
                continue
        
        with open(item, "rb") as file:
            file_hash = hashlib.file_digest(file, "sha256").hexdigest()
        if file_hash in hashes:
            if "Duplicate files" not in folders:
                os.mkdir("Duplicate files")
            shutil.move(os.path.join(os.getcwd(), item), os.path.join(os.getcwd(), "Duplicate files", item))
            DUPES += 1
            continue
        else:
            hashes += [file_hash]

        _, extension = os.path.splitext(item)
        fldr_name = extension+" files"

        if fldr_name not in folders:
            os.mkdir(fldr_name)
            folders += [fldr_name]
        shutil.move(os.path.join(os.getcwd(), item), os.path.join(os.getcwd(), fldr_name, item))

        if not extension[1:] in list(REPORT.keys()):
            REPORT[extension[1:]] = 0
        REPORT[extension[1:]] += 1


REPORT = {}
DUPES = 0

orig_cwd = gtcwd(args.folder)
sd = [os.getcwd()]+[os.path.join(_r, s) for _r, sub, _f in os.walk(os.getcwd()) for s in sub if s[0]!="."]
for __f in sd:
    main(gtcwd(__f), args.inclpy)

os.chdir(orig_cwd)
time = datetime.datetime.now()
with open(str("Summary log at "+time.strftime("%d%m%Y%H%M%S"))+".txt", "w") as file:
    file.write(f"This is report of the files organized on {time}.\n\n")
    if not REPORT:
            file.write("No files were organized.\n\n")
    else:
        file.write(f"A total of {sum(list(REPORT.values()))} files were organized.\n\n")
        for i in REPORT:
            file.write(f"Number of {i} files organized: {REPORT[i]}\n")

    if not DUPES:
        file.write("\nNo duplicate files were found.\n\n")
    else:
        file.write(f"\n{DUPES} duplicate files were found and moved to 'Duplicate files'.\n\n")
