import os, argparse, shutil, datetime, hashlib

# SHELL ARGUMENTS
parser = argparse.ArgumentParser(description='A program that helps to organize a folder by extension, and remove duplicates.')
parser.add_argument("-f", "--folder", type=str, default="", help="Absolute Path to folder/Leave empty to clean current folder")
parser.add_argument("-i", "--inclpy", action="store_true", help="Type this to include organising this own file")
args = parser.parse_args()

if args.folder:
    if os.path.exists(args.folder):
        os.chdir(args.folder)
    else:
        print("The folder does not exist!")
else:
    os.chdir(os.path.dirname(__file__))

# FOLDER ORGANIZER
directories = os.listdir()
folders = [i for i in directories if os.path.isdir(os.path.join(os.getcwd(), i))]
report = {}
hashes = []
dupes = 0

for item in directories:
    if ((not args.inclpy) and (item==os.path.basename(__file__))) or (not os.path.isfile(item)):
        continue
    
    with open(item, "rb") as file:
        file_hash = hashlib.file_digest(file, "sha256").hexdigest()
    if file_hash in hashes:
        if "Duplicate files" not in folders:
            os.mkdir("Duplicate files")
        shutil.move(os.path.join(os.getcwd(), item), os.path.join(os.getcwd(), "Duplicate files", item))
        dupes += 1
        continue
    else:
        hashes += [file_hash]

    _, extension = os.path.splitext(item)
    fldr_name = extension+" files"

    if fldr_name not in folders:
        os.mkdir(fldr_name)
        folders += [fldr_name]
    shutil.move(os.path.join(os.getcwd(), item), os.path.join(os.getcwd(), fldr_name, item))

    if not extension[1:] in list(report.keys()):
        report[extension[1:]] = 0
    report[extension[1:]] += 1

# REPORT MAKER

time = datetime.datetime.now()
with open(str("Summary log at "+time.strftime("%d%m%Y%H%M%S"))+".txt", "w") as file:
    file.write(f"This is report of the files organized on {time}.\n\n")
    if not report:
            file.write("No files were organized.\n\n")
    else:
        file.write(f"A total of {sum(list(report.values()))} files were organized.\n\n")
        for i in report:
            file.write(f"Number of {i} files organized: {report[i]}\n")

    if not dupes:
        file.write("\nNo duplicate files were found.\n\n")
    else:
        file.write(f"\n{dupes} duplicate files were found and moved to 'Duplicate files'.\n\n")