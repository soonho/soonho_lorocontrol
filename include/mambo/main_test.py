from pyparrot.Minidrone import Mambo
from pprint import pprint

bt_mac_01 = "d0:3a:de:8a:e6:37"
# bt_mac_01 = "d0:3a:82:0a:e6:21"

drone_01 = Mambo(address=bt_mac_01, use_wifi=False)


print("trying to connect")
success_01 = drone_01.connect(num_retries=3)
print("drone_01 connected: %s " % success_01)

if (success_01) :#& success_02:
    # get the state information
    print("test stats")
    print("taking off!")
    drone_01.safe_takeoff(5)
    for i in range(10) :
        drone_01.ask_for_state_update()
        pprint(vars(drone_01.sensors))
        drone_01.smart_sleep(0.1)
    drone_01.safe_land(5)
    drone_01.disconnect()