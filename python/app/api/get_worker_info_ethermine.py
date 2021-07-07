from datetime import datetime
from ethermine import Ethermine
# su dung api
ethermine = Ethermine()
import json
stats = ethermine.pool_stats()
data = stats.get("price")
print('--- Pool ---')
print("1 ETH = ")
data = ethermine.network_stats()
print("{:<18} {:<15}".format('VND',round(stats["price"]["usd"]*23046)))
print("{:<18} {:<15}".format('Diff',data["difficulty"]))

print('--- Worker ---\n')
YourWorker = '0x5C49922c9h49960A009eF515Fb15cb1d5eE8B607'

# Xuat ket qua

def GetRigInfo(wallet):
	dashboard = ethermine.miner_dashboard(wallet)
	info = {}
	json_rig_num = dashboard['currentStatistics']['activeWorkers']
	json_rig_hash = dashboard['currentStatistics']['currentHashrate']
	json_rig_unpaid = dashboard['currentStatistics']['unpaid']
	current = round(json_rig_hash/1000000,2)
	print("active Workers:   ",json_rig_num)
	print("current Hashrate: ",current," MH/s")
	print("unpaid balance:   ",round(json_rig_unpaid/10**18,5)," ETH")

# show the results
print("=== YourWorker ==================")
GetRigInfo(YourWorker)
print("\n========= END ===============")
input("Press Enter to continue...")
# ===========  Output ===========
# --- Pool ---
# 1 ETH = 
# VND                55092386       
# Diff               6561146258395570
# --- Worker ---
# === Michael ==================
# active Workers:    2
# current Hashrate:  367.46  MH/s
# unpaid balance:    0.0642  ETH
# ========= END ===============
# Press Enter to continue...[Cancelled]