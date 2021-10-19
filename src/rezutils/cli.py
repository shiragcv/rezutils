import sys
import argparse

from rezutils import build


def copy_folder(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-s',
        '--source',
        type=str,
        required=True,
        help='Source folder'
    )

    parser.add_argument(
        '-d',
        '--destination',
        type=str,
        required=True,
        help='Destination folder'
    )

    parser.add_argument(
        '-ir',
        '--include-root',
        dest='include_root',
        default=False,
        action='store_true',
        help='Include root'
    )

    parser.add_argument(
        '-i',
        '--ignore',
        nargs='+',
        help='Folders and files to ignore'
    )

    args = parser.parse_args(argv)

    try:
        build.copy_folder(
            source=args.source,
            destination=args.destination,
            include_root=args.include_root,
            ignore=args.ignore
        )

    except Exception as e:
        sys.stderr.write(str(e))

        return 1

    return 0
