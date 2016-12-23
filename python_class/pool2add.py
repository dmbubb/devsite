#!/usr/bin/env python

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()
#SNG
spool_id = '353369'
#AMS
apool_id = '307841'
#US
upool_id = '263219'


#SNG
shardwareToAdd = [{"id": 227752}, {"id": 280028}, {"id": 280030}, {"id": 279956}, {"id": 237682}, {"id": 227732}, {"id": 155669}, {"id": 258326}, {"id": 140285}, {"id": 257978}, {"id": 329840}, {"id": 197474}, {"id": 329880}, {"id": 329744}, {"id": 251082}, {"id": 114132}, {"id": 133916}, {"id": 251060}, {"id": 220380}]
shardwareToRemove = []
scloudsToAdd = [{"id": 6674700}]
scloudsToRemove = []
adjustsngpool = client['SoftLayer_Network_Bandwidth_Version1_Allotment'].requestVdrContentUpdates(shardwareToAdd, shardwareToRemove, scloudsToAdd, scloudsToRemove, id=spool_id)
print("Singapore Pool")
pp(adjustsngpool)

#AMS
ahardwareToAdd =  [{"id": 268028}, {"id": 137238}, {"id": 180144}, {"id": 177463}, {"id": 132393}, {"id": 997025}, {"id": 997033}, {"id": 997039}, {"id": 465544}, {"id": 465532}, {"id": 997115}, {"id": 997135}, {"id": 997103}, {"id": 997133}, {"id": 997097}, {"id": 743855}, {"id": 997023}, {"id": 219686}, {"id": 265380}, {"id": 955437}, {"id": 162550}, {"id": 160141}, {"id": 180080}, {"id": 185226}, {"id": 185234}, {"id": 281684}, {"id": 305458}, {"id": 281692}, {"id": 281678}, {"id": 281716}, {"id": 281828}, {"id": 185068}, {"id": 132171}, {"id": 99507}, {"id": 167972}, {"id": 185266}, {"id": 180042}, {"id": 162535}, {"id": 127504}, {"id": 87552}, {"id": 109999}, {"id": 209513}, {"id": 253350}, {"id": 462124}]
ahardwareToRemove = []
acloudsToAdd = [{"id": 6674748},{"id": 24541955}]
acloudsToRemove = []
adjustamspool = client['SoftLayer_Network_Bandwidth_Version1_Allotment'].requestVdrContentUpdates(ahardwareToAdd, ahardwareToRemove, acloudsToAdd, acloudsToRemove, id=apool_id)
print("AMS Pool")
pp(adjustamspool)

#US
uhardwareToAdd = [{"id": 249874}, {"id": 166355}, {"id": 214914}, {"id": 283450}, {"id": 315324}, {"id": 249864}, {"id": 99072}, {"id": 315330}, {"id": 315466}, {"id": 314158}, {"id": 315040}, {"id": 140679}, {"id": 137066}, {"id": 174269}, {"id": 134715}, {"id": 224080}, {"id": 206669}, {"id": 219264}, {"id": 196504}, {"id": 243512}, {"id": 252218}, {"id": 284246}, {"id": 146408}, {"id": 283550}, {"id": 322736}, {"id": 133637}, {"id": 382342}, {"id": 85557}, {"id": 315468}, {"id": 314068}, {"id": 314046}, {"id": 314054}, {"id": 158050}, {"id": 133073}, {"id": 152993}, {"id": 253726}, {"id": 253734}, {"id": 128500}, {"id": 179708}, {"id": 218773}, {"id": 219341}, {"id": 186387}, {"id": 193311}, {"id": 320022}, {"id": 218751}, {"id": 271524}, {"id": 351162}, {"id": 320972}, {"id": 315372}, {"id": 314392}, {"id": 323168}, {"id": 323166}, {"id": 284244}, {"id": 321022}, {"id": 211636}, {"id": 315344}, {"id": 314076}, {"id": 315032}, {"id": 314328}, {"id": 315046}, {"id": 314380}, {"id": 314396}, {"id": 314162}, {"id": 136931}, {"id": 200225}, {"id": 175379}, {"id": 200240}, {"id": 224180}, {"id": 224052}, {"id": 219290}, {"id": 206661}, {"id": 219257}, {"id": 224034}, {"id": 323164}, {"id": 323158}, {"id": 323162}, {"id": 323160}, {"id": 192776}, {"id": 206637}, {"id": 206635}, {"id": 85564}, {"id": 94945}, {"id": 170883}, {"id": 89705}, {"id": 100774}, {"id": 95581}, {"id": 106918}, {"id": 172383}, {"id": 196722}, {"id": 84927}, {"id": 94674}, {"id": 224064}, {"id": 154795}, {"id": 83804}, {"id": 84828}, {"id": 218832}, {"id": 134550}]
uhardwareToRemove = []
ucloudsToAdd = [{"id": 16310973}, {"id": 16933015}, {"id": 18190627}, {"id": 6613626}, {"id": 6561080}]
ucloudsToRemove = []
adjustuspool = client['SoftLayer_Network_Bandwidth_Version1_Allotment'].requestVdrContentUpdates(uhardwareToAdd, uhardwareToRemove, ucloudsToAdd, ucloudsToRemove, id=upool_id)
print("US Pool")
pp(adjustuspool)


us_allocated = client['Network_Bandwidth_Version1_Allotment'].getTotalBandwidthAllocated(id=upool_id)
ams_allocated = client['Network_Bandwidth_Version1_Allotment'].getTotalBandwidthAllocated(id=apool_id)
sin_allocated = client['Network_Bandwidth_Version1_Allotment'].getTotalBandwidthAllocated(id=spool_id)

us_hw = client['Network_Bandwidth_Version1_Allotment'].getHardware(id=upool_id)
ams_hw = client['Network_Bandwidth_Version1_Allotment'].getHardware(id=apool_id)
sin_hw = client['Network_Bandwidth_Version1_Allotment'].getHardware(id=spool_id)
