import os
import shutil


def copy_folder(source, destination, include_root=False, ignore=None):
    ignore = ignore or []

    if include_root:
        destination = os.path.join(destination, os.path.basename(source))

    for src_dir, dirs, files in os.walk(source):
        if os.path.basename(src_dir) in ignore:
            continue

        dst_dir = src_dir.replace(source, destination, 1)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for file_ in files:
            if file_ in ignore:
                continue

            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)

            if os.path.exists(dst_file):
                os.remove(dst_file)

            shutil.copy(src_file, dst_dir)
