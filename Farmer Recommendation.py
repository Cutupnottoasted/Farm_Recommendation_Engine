#-*- coding = utf-8 -*-
import math
import numpy as np
rice = [79.890000,47.580000,39.870000,23.689332,82.272822,6.425471,236.181114]


maize = [77.760000,48.440000,19.790000,22.389204,65.092249,6.245190,84.766988]


chickpea = [40.090000,67.790000,79.920000,18.872847,16.860439,7.336957,80.058977]


kidneybeans = [20.750000,67.540000,20.050000,20.115085,21.605357,5.749411,105.919778]


pigeonpeas = [20.730000,67.730000,20.290000,27.741762,48.061633,5.794175,149.457564]


mothbeans = [21.440000,48.010000,20.230000,28.194920,53.160418,6.831174,51.198487]


mungbean = [20.990000,47.280000,19.870000,28.525775,85.499975,6.723957,48.403601]


blackgram = [40.020000,67.470000,19.240000,29.973340,65.118426,7.133952,67.884151]


lentil = [18.770000,68.360000,19.410000,24.509052,64.804785,6.927932,45.680454]


pomegranate = [18.870000,18.750000,40.210000,21.837842,90.125504,6.429172,107.528442]


banana = [100.230000,82.010000,50.050000,27.376798,80.358123,5.983893,104.626980]


mango = [20.070000,27.180000,29.920000,31.208770,50.156573,5.766373,94.704515]


grapes = [23.180000,132.530000,200.110000,23.849575,81.875228,6.025937, 69.611829]


watermelon = [99.420000,17.000000,50.220000,25.591767,85.160375,6.495778,50.786219]


muskmelon = [100.320000,17.720000,50.080000,28.663066,92.342802,6.358805,24.689952]


apple = [20.800000,134.220000,199.890000,22.630942,92.333383,5.929663,112.654779]


orange = [19.580000,16.550000,10.010000,22.765725,92.170209,7.016957,110.474969]


papaya = [49.880000,59.050000,50.040000,33.723859,92.403388,6.741442,142.627839]


coconut = [21.980000,16.930000,30.590000,27.409892,94.844272,5.976562,175.686646]


cotton = [117.770000,46.240000,19.560000,23.988958,79.843474,6.912675, 80.398043]


jute = [78.400000,46.860000,39.990000,24.958376,79.639864,6.732778,174.792798]


coffee = [101.200000,28.740000,29.940000,25.540477,58.869846,6.790308,158.066295]



#soil = [input(), input(), input(), input(), input(), input(), input()]
soil = [1,2,3,4,5,6,7]
crops = [rice,maize,chickpea,kidneybeans,pigeonpeas,mothbeans,mungbean,blackgram,lentil,pomegranate,banana,mango,grapes,watermelon,muskmelon,apple,orange,papaya,coconut,cotton,jute,coffee]

def find_Difference(myList, myList2):
    differences = []
    length = len(myList)
    for i in range(length):
        difference = myList[i] - myList2[i]
        differences.append(difference)
    return differences

def find_Distance(differences):
    square_sum = 0
    for i in range(0,6):
        square_sum = int(square_sum + differences[i] * differences[i])
    distance = "{:.2f}".format(math.sqrt(square_sum))
    return distance

def find_all_distances(soil,crops):
  all_distances=[]
  for crop in crops:
   distance = find_Distance(find_Difference(soil,crop))
   all_distances.append(distance)
  return all_distances

list_of_all_distances = find_all_distances(soil,crops)

list(np.float_(list_of_all_distances))

print(list_of_all_distances)

# print(find_all_distances(find_Distance(find_Difference(soil, crops))))
#
# def find_crop_and_distance(crops,all_distances):
#   crop_and_distance = {}
#   for i in range(len(crops)):
#      crop_and_distance[crops[i]] = all_distances[i]
#   smallest_distance = min(crop_and_distance.values())
#   return crop_and_distance
#
# find_crop_and_distance(crops,find_all_distances(soil,crops))
# print(crop_and_distance)

