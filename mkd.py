import yadisk
from config import token

y = yadisk.YaDisk(token=token)
if y.check_token():
    if not y.is_dir("/wwww"):
        y.mkdir("/wwww")
        print('Папка "test-dir" создана')

