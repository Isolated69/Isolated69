import requests; import concurrent.futures; import os ; import shutil ; from time import sleep


def bulk_download(user):
    global img, loc
    img_urls = []
    count = 0
    sizes = []
    user_split = user.split(' ')
    if user_split[0].endswith('.txt'):
        loc = f'{os.getcwd()}\\{user_split[0]}'
    else:
        loc = f'{os.getcwd()}\\{user_split[0]}.txt'
    try:
        with open(loc, 'r') as file:
            links = file.read().splitlines()
            for link in links:
                img_urls.append(link)
    except:
        print(f'{loc} does not exist')
        return False
    try:
        os.mkdir(fr'{os.environ["USERPROFILE"]}\Desktop\\BulkImages\\')
        print('Creating needed directories')
        sleep(1)
    except:
        print('Directory already exists...')
        pass
    sleep(0.5)
    print('Downloading...')
    try:
        for img in img_urls:
            img_bytes = requests.get(img).content
            name = f'img-{count}.{user_split[1]}'
            count += 1
            with open(name, 'wb') as f:
                f.write(img_bytes)
                sizes.append(os.path.getsize(name))
                print(f'{name} downloaded')
    except:
        if len(img) > 10:
            print(f'\'{img[0:9]}[...]\' is not valid')
        else:
            print(f'\'{img}\' is not valid')
    print('Moving files to destination...')
    sleep(1)
    files = os.listdir()
    for f in files:
        if os.path.splitext(f)[1] in formats_dot:
            try:
                shutil.move(f, destination)
            except:
                count -= 1
                print(f'{f} already exists')
                os.remove(f)
            else:
                pass
    print(f'Images sent to \'{destination}\'')
    print(f'Total: {(sum(sizes) / 1000000).__round__(2)}MB')


print(f'''{'-'*30}\nBulk Image Downloader v1\nCOMMANDS:\n\t/help\n\t /q\nInput example: images.txt png\n{'-'*30}\n''')

destination = fr'{os.environ["USERPROFILE"]}\Desktop\\BulkImages\\'

formats = ['jpg', 'png', 'jpeg', 'gif', 'tif', 'tiff', 'bmp', 'eps']
formats_dot = ['.' + x for x in formats]
while True:
    user = input('Enter txt file and format: ')
    if user == '/q':
        print('Quitting...')
        break
    user_split2 = user.split(' ')
    if len(user_split2) < 2:
        print(f'Missing parameters')
        continue
    if user_split2[1] not in formats:
        print(f'Invalid format \'{user_split2[1]}\'')
        continue

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(bulk_download(user))
