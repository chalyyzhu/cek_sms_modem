from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from print_color import print
import json
import os, time
login = Connection('http://admin:admin@192.168.8.1/')
client = Client(login)

hp_owner = "085961506487"

def read_sms():
    client.sms.delete_sms('40004')
    sms = client.sms.get_sms_list()
    print("[ SMS LIST ]", color="cyan")
    print(f"\nTotal SMS : {sms['Count']}", color="g")
    for a in sms["Messages"]["Message"]:
        print("===========================================================", color='m')
        print(f'DARI  : {a["Phone"]}',color='y')
        print(f'WAKTU : {a["Date"]}',color='y')
        print(f'\n{a["Content"]}', color="b")
    print("===========================================================", color='m')


def delete_all_sms():
    sms = client.sms.get_sms_list()
    print(f"\nTotal SMS : {sms['Count']}", color="g")
    for a in sms["Messages"]["Message"]:
        print("===========================================================", color='m')
        print(f'DARI  : {a["Phone"]}',color='y')
        print(f'WAKTU : {a["Date"]}',color='y')
        print('\n< PROSES MENGHAPUS PESAN >', color="k")
        client.sms.delete_sms(a["Index"])
    print("===========================================================", color='m')
    sms = client.sms.get_sms_list()
    print(f"\nTotal SMS sekarang: {sms['Count']}", color="g")



def cek_nomor():
    myhost = os.uname()[1]
    print(client.sms.send_sms(hp_owner , f"CEK NOMOR : {myhost}"))
    print(f'{hp_owner} > SUKSES TERKIRIM', tag_color="g", tag="succes")


def send_sms():
    no = input("TUJUAN  : ")
    msg = input("PESAN  : ")
    a = client.sms.send_sms(no , msg)
    if "ok" in a.lower():
        print(f'{hp_owner} > SUKSES TERKIRIM', tag_color="g", tag="succes")


if __name__ == "__main__":
    print("< MAIN MENU >", color="g")
    tx = "\n1. SEND SMS"
    tx += "\n2. READ SMS"
    tx += "\n3. CEK NOMOR"
    tx += "\n4. DELETE ALL SMS"
    print(tx, color="y")
    ch = input("\nPILIH NOMOR : ")

    if ch == "1":
        send_sms()
    if ch == "2":
        read_sms()
    if ch == "3":
        cek_nomor()
    if ch == "4":
        delete_all_sms()
