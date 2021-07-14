import requests
from time import sleep
codes = {100: 'Continue', 200: 'OK', 203: 'Non-Authoritative Information', 206: ' Partial Content',
         300: 'Multiple Choices', 303: 'See Other', 306: 'Unused', 400: 'Bad Request'}
cool_len = False
global change_cool


def sleep_cmd(change=2,):
    sleep_count = change + 1
    while True:
        sleep_count -= 1
        print(f'Cooldown {sleep_count}s')
        sleep(1)
        if sleep_count == 1:
            break


def get_site(site):
    try:
        req = requests.get(site, timeout=15).status_code
        status = codes[req]
        print(f'STATUS {req}: {status}')
    except Exception as e:
        print(e)

def config_info():
    print(f'''{'-'*20}\nOPTIONS:\nq = quit\nchange.cool = change cooldown\nchange_cool.reset = reverts to default cooldown\n{'-'*20}''')


while True:
    if cool_len:
        site = str(input(f'Input site link OR name(Cooldown[TRUE]: {change_cool}s): ')).lower()
    else:
        site = str(input(f'Input site link OR name: ')).lower()
    if site[0:5] == 'https':
        get_site(site)
        choice = input('Again? [Y/N]: ').lower()
    else:
        site_w = f'http://www.{site}.com'
        get_site(site_w)
        print(site_w)
        choice = input('Again? [Y/N]: ').lower()

        if choice == 'change_cool':
            change_cool = input('Change Cool-down: ')
            sleep_cmd(int(change_cool))
            cool_len = True
            continue

        if choice == 'change_cool.reset':
            cool_len = False
            print('Resetted')
            continue
        if choice == 'config':
            config_info()
            continue
        if choice == 'y':
            if not cool_len:
                sleep_cmd()
                continue
            else:
                sleep_cmd(int(change_cool))
        elif choice != 'y':
            print('Quitting')
            break
