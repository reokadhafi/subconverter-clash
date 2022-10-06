from base64 import b64decode
from prettytable import PrettyTable
import os
import json

data_bug = ["api.midtrans.com", "covid19.go.id", "cf-vod.nimo.tv"]


def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name


def akun():
    file = open(real_path('/data.txt')).read().split()
    database = {'data': file}
    db_jenis = []
    for i in range(len(database['data'])):
        db = {}
        sc = database['data'][i]
        if sc[0:8] == 'vmess://':
            db['jenis'] = 'vmess'
            db['proxy'] = sc.replace('vmess://', '')
        elif sc[0:8] == 'trojan:/':
            db['jenis'] = 'trojan'
            db['proxy'] = sc.replace('trojan://', '')
        db_jenis.append(db)
    return db_jenis


def nama_server(server):
    data = open(real_path('/db.json')).read()
    bc = json.loads(data)
    for i in bc:
        for ii in range(len(bc[i])):
            for iii in bc[i][ii]:
                if iii == server:
                    return bc[i][ii][server], i


def parser_trojan(data):
    db1 = {
        'password': '',
        'server': '',
        'port': '443',
        'sni': '',
        'type': 'ws',
        'host': '',
        'path': '',
    }
    rl = (data.replace(" ", "").replace("/", "").replace("%2F", "/"))
    db1['password'] = rl.split("@")[0]
    db1['server'] = rl.split('@')[1].split(':')[0]
    db1['port'] = 443
    dt = rl.split('?')[1].split("&")
    for i in range(len(dt)):
        dt2 = dt[i].split("=")
        db1[dt2[0]] = dt2[1]
    return db1


def parser_v2ray(data):
    # dd = b64decode(data).decode()
    dd = b64decode(data + '=' * (-len(data) % 4)).decode()
    rl = (dd.replace(" ", "").replace("\r", "").replace(
        "\n", "")).replace('"', "'")[1:-1]
    db1 = {
        'add': '',
        'aid': '',
        'host': '',
        'id': '',
        'net': '',
        'path': '',
        'port': '',
        'ps': '',
        'scy': '',
        'sni': '',
        'tls': '',
        'type': '',
        'v': ''
    }
    for i in range(len(rl.split(':'))-1):
        dt = rl.split(",")[i].replace("'", '').split(":")
        db1[dt[0]] = dt[1]
    return db1


def convert():
    db = akun()
    i = 0
    js1 = []
    for i in range(len(db)):
        js2 = {}
        while i < len(db):
            if db[i]['jenis'] == 'vmess':
                js2['convert'] = parser_v2ray(db[i]['proxy'])
            elif db[i]['jenis'] == 'trojan':
                js2['convert'] = parser_trojan(db[i]['proxy'])
            js1.append(js2)
            break
        i += 1
    return js1


cv = convert()
def config_gamemax():
    jenis = akun()
    bug = 'cf-vod.nimo.tv'
    db = []
    for i in range(len(cv)):
        cm = cv[i]['convert']
        dt = {}
        if jenis[i]['jenis'] == 'vmess':
            if cm['add'] in data_bug:
                if nama_server(cm['sni']) is not None:
                    dt['name'] = f"{nama_server(cm['sni'])[0]}-gm"
                else:
                    dt['name'] = f"{cm['sni']:.10}-gm"
                dt['server'] = bug
                dt['port'] = 80
                dt['type'] = 'vmess'
                dt['uuid'] = cm['id']
                dt['alterId'] = 0
                dt['cipher'] = 'auto'
                dt['tls'] = 'false'
                dt['skip-cert-verify'] = 'true'
                dt['servername'] = cm['sni']
                dt['network'] = 'ws'
                if cm['sni'] == '':
                    cm['sni'] = cm['host']
                dt['ws-opts'] = {'path': cm['path'],
                                 'headers': {'Host': cm['sni']}}
                dt['udp'] = 'true'
            else:
                if nama_server(cm['add']) is not None:
                    dt['name'] = f"{nama_server(cm['add'])[0]}-gm"
                else:
                    dt['name'] = f"{cm['add']:.10}-gm"
                dt['server'] = bug
                dt['port'] = 80
                dt['type'] = 'vmess'
                dt['uuid'] = cm['id']
                dt['alterId'] = 0
                dt['cipher'] = 'auto'
                dt['tls'] = 'false'
                dt['skip-cert-verify'] = 'true'
                dt['servername'] = cm['add']
                dt['network'] = 'ws'
                dt['ws-opts'] = {'path': cm['path'],
                                 'headers': {'Host': cm['add']}}
                dt['udp'] = 'true'
        if jenis[i]['jenis'] == 'trojan':
            if nama_server(cm['sni']) is not None:
                dt['name'] = f"{nama_server(cm['sni'])[0]}-gm"
            else:
                dt['name'] = f"{cm['sni']:.10}-gm"
            dt['server'] = bug
            dt['port'] = 443
            dt['type'] = 'trojan'
            dt['password'] = cm['password']
            dt['tls'] = 'true'
            dt['skip-cert-verify'] = 'true'
            dt['sni'] = cm['sni']
            dt['network'] = 'ws'
            dt['ws-opts'] = {'path': cm['path'],
                             'headers': {'Host': cm['sni']}}
            dt['udp'] = 'true'
        db.append(dt)
    return db
        
def result_gamemax():
    db = []
    for i in range(len(config_gamemax())):
        dt = {}
        proxy = (config_gamemax()[i])
        dd = f'{proxy}'
        dt['gamemax'] = dd.replace("'", '')
        db.append(dt)
    return db


gm = result_gamemax()
def config_opok():
    jenis = akun()
    bug = 'covid19.go.id'
    ip = 'covid19.go.id'
    db = []
    for i in range(len(cv)):
        cm = cv[i]['convert']
        dt = {}
        if jenis[i]['jenis'] == 'vmess':
            if cm['add'] in data_bug:
                if nama_server(cm['sni']) is not None:
                    dt['name'] = f"{nama_server(cm['sni'])[0]}-op"
                else:
                    dt['name'] = f"{cm['sni']:.10}-op"
                dt['server'] = ip
                dt['port'] = 443
                dt['type'] = 'vmess'
                dt['uuid'] = cm['id']
                dt['alterId'] = 0
                dt['cipher'] = 'auto'
                dt['tls'] = 'true'
                dt['skip-cert-verify'] = 'true'
                dt['servername'] = bug
                dt['network'] = 'ws'
                if cm['sni'] == '':
                    cm['sni'] = cm['host']
                dt['ws-opts'] = {'path': f"wss://{bug}{cm['path']}",
                                 'headers': {'Host': cm['sni']}}
                dt['udp'] = 'true'
            else:
                if nama_server(cm['add']) is not None:
                    dt['name'] = f"{nama_server(cm['add'])[0]}-op"
                else:
                    dt['name'] = f"{cm['add']:.10}-op"
                dt['server'] = ip
                dt['port'] = 443
                dt['type'] = 'vmess'
                dt['uuid'] = cm['id']
                dt['alterId'] = 0
                dt['cipher'] = 'auto'
                dt['tls'] = 'true'
                dt['skip-cert-verify'] = 'true'
                dt['servername'] = bug
                dt['network'] = 'ws'
                dt['ws-opts'] = {'path': f"wss://{bug}{cm['path']}",
                                 'headers': {'Host': cm['add']}}
                dt['udp'] = 'true'
        if jenis[i]['jenis'] == 'trojan':
            if nama_server(cm['sni']) is not None:
                dt['name'] = f"{nama_server(cm['sni'])[0]}-op"
            else:
                dt['name'] = f"{cm['sni']:.10}-op"
            dt['server'] = ip
            dt['port'] = 443
            dt['type'] = 'trojan'
            dt['password'] = cm['password']
            dt['tls'] = 'true'
            dt['skip-cert-verify'] = 'true'
            dt['sni'] = bug
            dt['network'] = 'ws'
            dt['ws-opts'] = {'path': f"wss://{bug}{cm['path']}",
                             'headers': {'Host': cm['sni']}}
            dt['udp'] = 'true'
        db.append(dt)
    return db


def result_opok():
    db = []
    for i in range(len(config_opok())):
        dt = {}
        proxy = (config_opok()[i])
        dd = f'{proxy}'
        dt['opok'] = dd.replace("'", '')
        db.append(dt)
    return db


op = result_opok()

gb = {'data': akun(), 'gamemax': gm, 'opok': op}
def cetak1(jenis, mode):
    jn = akun()
    for i in range(len(jn)):
        if jn[i]['jenis'] == jenis:
            print(f"  - {gb[mode][i][mode]}")

def cetak(jenis, mode):
    jn = akun()
    for i in range(len(jn)):
        if jn[i]['jenis'] == jenis:
            ct = gb[mode][i][mode].replace('{', '').replace('}','').split(', ')
            print(f"  - {ct[0]}")
            for ii in range(1,len(ct)):
            	if "path" in ct[ii]:
            		ct[ii] = f"{ct[ii].split()[0]}"+"\n"+f"      {ct[ii].split()[1]}" f" {ct[ii].split()[2]}"
            	if "headers" in ct[ii]:
            		ct[ii] = f"  {ct[ii].split()[0]}"+"\n"+f"        {ct[ii].split()[1]}" f" {ct[ii].split()[2]}"
            	print(f"    {ct[ii]}")
            
            	
def batas():
    print("\n")
    print("||======================[CONFIG]=====================||")
    print("\n")


def menu():
    print('GENERATE CONFIG CLASH')
    print('''
Menu:
0. Cek Tabel
1. Trojan Gamemax
2. Trojan OP
3. Vmess Gamemax
4. Vmess OP
5. Trojan & Vmess Gamemax
6  Trojan & Vmess OP
    ''')

    try:
    	pilih = input('Masukan Menu Pilihan: ')
    except EOFError:
    	print("script close")
    	exit()
    if pilih == '0':
        tabel()
    elif pilih == '1':
        batas()
        print('proxies:')
        cetak('trojan', 'gamemax')
        batas()
    elif pilih == '2':
        batas()
        print('proxies:')
        cetak('trojan', 'opok')
        batas()
    elif pilih == '3':
        batas()
        print('proxies:')
        cetak('vmess', 'gamemax')
        batas()
    elif pilih == '4':
        batas()
        print('proxies:')
        cetak('vmess', 'opok')
        batas()
    elif pilih == '5':
        batas()
        print('proxies:')
        cetak('trojan', 'gamemax')
        cetak('vmess', 'gamemax')
        batas()
    elif pilih == '6':
        batas()
        print('proxies:')
        cetak('trojan', 'opok')
        cetak('vmess', 'opok')
        batas()


def tabel():
    tabel1 = PrettyTable(['jenis', 'nama server gamemax',
                         'nama server op'])
    for i in range(len(gb['data'])):
        tabel1.add_row([gb['data'][i]['jenis'], gb['gamemax'][i]
                       ['gamemax'].split('{name: ')[1].split(',')[
            0], gb['opok'][i]
            ['opok'].split('{name: ')[1].split(',')[0]])
    print(tabel1)
    print('\n')


if __name__ == '__main__':
    while True:
        try:
            menu()
        except (UnicodeDecodeError):
            print("\n\nTerjadi Kesalahan Input!!!")
            print("Ulangi Gaaess!!!\n\n")
            exit()
