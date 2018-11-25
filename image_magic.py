import os
import shutil
import subprocess


source = "Source"
current_dir = os.path.dirname(os.path.abspath(__file__))


def squeze_img():
    source_directory = os.path.join(current_dir, 'Source')
    source_content = os.listdir(source_directory)


    try:
        os.mkdir("Result")
    except FileExistsError:
        pass

    for file in source_content:
        full_path = os.path.join(source_directory, file)
        result_img = shutil.copyfile(full_path, 'Result/{}'.format(file))
        subprocess.run(["sips", "--resampleWidth", "200", result_img])


def main():

    squeze_img()


if __name__ == '__main__':
    main()