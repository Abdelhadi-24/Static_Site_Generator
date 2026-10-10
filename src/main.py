import os
import shutil


def copy_files(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied {source_path} to {destination_path}")
        else:
            copy_files(source_path, destination_path)


def main():
    copy_files("static", "public")


if __name__ == "__main__":
    main()