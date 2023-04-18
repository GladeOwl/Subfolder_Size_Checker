import os

folder_path = input("Path of the Folder: ")


def bytes_to_gb(bytes):
    size_in_gb = bytes / (1024 * 1024 * 1024)
    return round(size_in_gb, 2)


def get_subfolder_size(subfolder_path):
    size = 0
    for path, dirs, files in os.walk(subfolder_path):
        for f in files:
            file_path = os.path.join(path, f)
            size += os.path.getsize(file_path)

    return size


def get_folder_size(folder_path):
    print(f"Checking size of :: {folder_path}")
    size = 0

    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        subfolder_size = get_subfolder_size(subfolder_path)
        size += subfolder_size

        print(
            f"{subfolder} :: {bytes_to_gb(subfolder_size)} GB ({subfolder_size} bytes)"
        )

    return size


if __name__ == "__main__":
    total_folder_size = get_folder_size(folder_path)
    print(
        f"Total Size: {bytes_to_gb(total_folder_size)} GB ({total_folder_size} bytes)"
    )
