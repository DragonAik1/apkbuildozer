from config import MYSQL_CONNECT, default_folder, token
import os.path
import yadisk
y = yadisk.YaDisk(token=token)


def send_file_to_server(file):
    basename = os.path.basename(file)
    if not y.is_dir("/test-dir"):
        y.mkdir("/test-dir")
        print("Папка создана!")
        y.upload(file, "/test-dir/" + basename)
        print("ok")
    else:
        print("Папка уже существует!")
        y.upload(file, "/test-dir/" + basename)
        print("ok")