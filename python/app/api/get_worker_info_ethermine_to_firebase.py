from datetime import datetime
from ethermine import Ethermine
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time

cred = credentials.Certificate(
    "Your json file here.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your firebase url.firebaseio.com/'
})

# su dung api
ethermine = Ethermine()

stats = ethermine.pool_stats()
data = stats.get("price")
print('--- Pool ---')
print("1 ETH = ")
data = ethermine.network_stats()
print("{:<18} {:<15}".format('VND', round(stats["price"]["usd"]*23046)))
print("{:<18} {:<15}".format('Diff', data["difficulty"]))

print('--- Worker ---\n')
Your_wallet = '0x5C49922c9cos860A008eF53m9b15cb1d5eE8D39d'

# def logFirebase(ten,sl,nd=""):
# 	ref = db.reference('-L8SwnVwWKy3sOUVnBET') #rig database
# 	ref.push({
#     'name': ten,
#     'worker': sl,
#     'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#     'message': nd
# 	})
# dong bo voi fire base neu co 1 rig k hoat dong

# Get info from firebase


def GetRigInfo(wallet, default_num):
    ref = db.reference('-L8SwnVwWKy3sOUVnBET')  # Your key
    info = {}
    json_string = dashboard['workers']
    json_rig_num = dashboard['currentStatistics']['activeWorkers']
    json_rig_hash = dashboard['currentStatistics']['currentHashrate']
    json_rig_unpaid = dashboard['currentStatistics']['unpaid']
    current = round(json_rig_hash/1000000, 2)
    # Kiểm tra xem có lỗi đang tồn tại hay ko
    if (wallet[-4:] == "B607"):
        name = "Truong_worker"
    elif (wallet[-4:] == "3C7C"):
        name = "Lieu_worker"
    else:
        name = "Nghi_worker"

    if json_rig_num < default_num:
        info = {
            str(name)+' crash': thoigian,
            name: 'thiếu card:'+str(json_rig_num)+'/'+str(default_num)
        }
    else:
        info = {
            # 'time crash':thoigian,
            name: 'OK',
            str(name)+' crash': 'None'
        }
    ref.update(info)
    print("active Workers:   ", json_rig_num)
    print("current Hashrate: ", current, " MH/s")
    print("unpaid balance:   ", round(json_rig_unpaid/10**18, 5), " ETH")


def CheckRig():
    # show the results
    print("    TRUONG                     ")
    GetRigInfo(truong, 2)
    print("\n=== LIEU = ==================")
    GetRigInfo(lieu, 1)
    print("\n=== NGHI== ==================")
    GetRigInfo(nghi, 6)
    print("\n========= END ===============")


while True:
    CheckRig()
    time.sleep(10)  # loop every 3min
