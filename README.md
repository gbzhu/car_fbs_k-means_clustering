# k-means clustering for car reviews
## Three dataset as below
### Tags before cluster

   ||car_reviews|edmunds|thecarconnection
   :-:|:-:|:-:|:-:
   1|Audio and Infotainment|comfort|green
   2|Cargo Space and Storage|driving|performance
   3|Driving Impressions and Performance|interior|quality
   4|Exterior Design and Dimensions|performance & mpg|safety
   5|Fuel Economy and Driving Range|safety|styling
   6|Interior and Passenger Space|technology|
   7|Powertrain and Charging|trim levels & features|
   8|Safety and Driver Assistance|utility|
   9|Warranty and Maintenance Coverage|
   10|Engine and Transmission|
 
## Result of k-means cluster with difference dataset
* **car reviews**
    * result (version 1)
        ```
        Top terms per cluster: None
        Cluster 0: with standard wheel is automatic speed on for all drive
        Cluster 1: assigns stars overall nhtsa cars five rating an out quicker
        Cluster 2: to it is of in its that but for as
        Cluster 3: visibility by laser roof pillar width location pillars blind spots
        Cluster 4: system infotainment inch touchscreen is standard to apple android carplay
        Cluster 5: seat rear seats space of in cargo to front is
        Cluster 6: highway mpg our fuel loop on economy epa 200 mile
        Cluster 7: usb devices current all response amps latency ports following times
        Cluster 8: sound decibels pressure at of meter while is 70 cruising
        Cluster 9: safety iihs pick tests top vehicles highway nhtsa crashworthiness evaluate
        Cluster distribution:
        {0: 5189, 2: 10189, 6: 1563, 4: 1780, 5: 3180, 8: 1015, 1: 823, 3: 1921, 7: 1046, 9: 706}
        0.853754658731952
        ```
    * result (version 2)
        ```
        Top terms per cluster: None
        Cluster 0: safety nhtsa cars stars iihs assigns rating overall five pick
        Cluster 1: steering wheel car drive sport ride like class driving road
        Cluster 2: sound decibels pressure meter 70 15 cruising seconds mph noise
        Cluster 3: pillars visibility highway replicate fuel attempt test economy people devised
        Cluster 4: laser width pillar location visibility machine point road determine device
        Cluster 5: usb devices frame response infotainment various measure ports latency following
        Cluster 6: michigan 94 entails procedure 200 loop mile out and back
        Cluster 7: seat rear seats space cargo front row storage interior legroom
        Cluster 8: liter speed automatic transmission engine four cylinder six turbocharged drive
        Cluster 9: standard system inch features infotainment available touchscreen package safety optional
        Cluster distribution:
        {0: 1531, 1: 11442, 2: 801, 3: 1294, 4: 1313, 5: 1292, 6: 361, 7: 3347, 8: 2309, 9: 3722}
        0.8708904899684552
        ```

    * cost trend (version 1)
    
        ![car reviews](pictures/car_review_(5,15)_v1.png)
        ```
        27412 documents
        Cluster distribution:
        Cluster 5: {0: 2271, 1: 21821, 2: 1051, 3: 1577, 4: 692} 0.8931739140359255
        Cluster 6: {0: 20436, 1: 1186, 2: 1101, 3: 2799, 4: 361, 5: 1529} 0.8844235485391917
        Cluster 7: {0: 862, 1: 856, 2: 2604, 3: 7652, 4: 1718, 5: 13063, 6: 657} 0.8795675106660413
        Cluster 8: {0: 942, 1: 800, 2: 1202, 3: 1892, 4: 893, 5: 6581, 6: 14553, 7: 549} 0.8701556685113421
        Cluster 9: {0: 16918, 1: 1165, 2: 780, 3: 3081, 4: 800, 5: 1457, 6: 745, 7: 709, 8: 1757} 0.8558720335350157
        Cluster 10: {0: 1024, 1: 13240, 2: 991, 3: 3405, 4: 704, 5: 544, 6: 655, 7: 4002, 8: 1691, 9: 1156} 0.8517616401189498
        Cluster 11: {0: 814, 1: 10887, 2: 1346, 3: 1074, 4: 1306, 5: 997, 6: 3396, 7: 1037, 8: 654, 9: 4023, 10: 1878} 0.8457740803778363
        Cluster 12: {0: 568, 1: 715, 2: 1352, 3: 12767, 4: 4198, 5: 440, 6: 699, 7: 1013, 8: 1525, 9: 2183, 10: 990, 11: 962} 0.8307214349288249
        Cluster 13: {0: 1236, 1: 10372, 2: 3556, 3: 1068, 4: 2020, 5: 996, 6: 3961, 7: 677, 8: 204, 9: 745, 10: 1033, 11: 1174, 12: 370} 0.8286565026891466
        Cluster 14: {0: 990, 1: 3929, 2: 1449, 3: 2052, 4: 798, 5: 689, 6: 354, 7: 627, 8: 939, 9: 361, 10: 10006, 11: 640, 12: 1573, 13: 3005} 0.8121522578356923
        ```
    * cost trend (version 2)
    
        ![car reviews](pictures/car_review_(5,15)_v2.png)


* **edmunds**
    * result (version 1)
        ```
        Top terms per cluster: None
        Cluster 0: are available on of there to as for seats in
        Cluster 1: mph 60 in seconds testing edmunds from zero to feet
        Cluster 2: system power inch with package rear wheels adds an heated
        Cluster 3: to it of you can be but in is that
        Cluster 4: mpg speed transmission automatic combined city manual six highway is
        Cluster 5: torque liter hp lb ft of pound feet horsepower produces
        Cluster 6: is in of with for on as trim available that
        Cluster 7: side airbags impact for frontal front stars crash safety curtain
        Cluster distribution:
        {6: 54532, 0: 16175, 3: 38871, 2: 27526, 1: 5957, 4: 11925, 5: 8323, 7: 8939}
        0.8781821498579485
        ```
    * result (version 2)
        ```
        Top terms per cluster: None
        Cluster 0: ride interior cabin quality materials design comfortable suspension quiet high
        Cluster 1: system navigation audio package optional warning camera rear also parking
        Cluster 2: speed transmission automatic six manual standard five drive wheel four
        Cluster 3: available rear side also front standard feet drive 60 trim
        Cluster 4: torque liter hp lb ft pound feet horsepower engine produces
        Cluster 5: mpg combined city highway epa fuel economy estimated estimates 22
        Cluster 6: like driving power engine steering electric car feel v6 much
        Cluster 7: power inch wheels heated seats leather front rear steering adds
        Cluster distribution:
        {0: 12724, 1: 16336, 2: 7719, 3: 92691, 4: 8642, 5: 5673, 6: 9337, 7: 19126}
        0.8989701809877638
        ```
    * cost trend (version 1)
    
        ![edmunds](pictures/edmunds_(5,15)_v1.png)
        
        ```
        172248 documents
        {0: 109887, 1: 13993, 2: 9173, 3: 30612, 4: 8583}
        5 0.9012698050052816
        {0: 9149, 1: 106555, 2: 8560, 3: 5963, 4: 12332, 5: 29689}
        6 0.889721494694458
        {0: 8556, 1: 17490, 2: 17163, 3: 5959, 4: 28760, 5: 4850, 6: 89470}
        7 0.8858911655005254
        {0: 14060, 1: 12957, 2: 16034, 3: 4496, 4: 9189, 5: 22483, 6: 5553, 7: 87476}
        8 0.8796700664810887
        {0: 65859, 1: 8258, 2: 9029, 3: 38090, 4: 5944, 5: 18060, 6: 14403, 7: 5569, 8: 7036}
        9 0.8658370227351719
        {0: 8252, 1: 31105, 2: 53068, 3: 10689, 4: 4551, 5: 4840, 6: 5522, 7: 16049, 8: 32716, 9: 5456}
        10 0.8662924133979836
        {0: 8159, 1: 26257, 2: 6670, 3: 7306, 4: 27240, 5: 7777, 6: 5916, 7: 49504, 8: 15057, 9: 13828, 10: 4534}
        11 0.8661859018849154
        {0: 13568, 1: 7016, 2: 5562, 3: 5955, 4: 8319, 5: 4831, 6: 17276, 7: 34364, 8: 4605, 9: 4281, 10: 59403, 11: 7068}
        12 0.845146120840502
        {0: 9851, 1: 8310, 2: 5932, 3: 13905, 4: 11330, 5: 12478, 6: 4598, 7: 5542, 8: 13509, 9: 4343, 10: 70715, 11: 6913, 12: 4822}
        13 0.840640235763226
        {0: 6091, 1: 8184, 2: 12987, 3: 11967, 4: 4755, 5: 4584, 6: 64184, 7: 8931, 8: 5914, 9: 5446, 10: 10445, 11: 10195, 12: 13032, 13: 5533}
        14 0.8402796078490573
        ```
    * cost trend (version 2)
    
        ![edmunds](pictures/edmunds_(5,15)_v2.png)
        ```
        172248 documents
        Cluster distribution:
        {0: 5733, 1: 131837, 2: 9028, 3: 16375, 4: 9275} 5 0.9150191194684022
        {0: 9235, 1: 31662, 2: 100199, 3: 8677, 4: 7728, 5: 14747} 6 0.9093592075442383
        {0: 95990, 1: 14582, 2: 5595, 3: 31058, 4: 10391, 5: 5885, 6: 8747} 7 0.8954610745906639
        {0: 103684, 1: 8691, 2: 31773, 3: 4491, 4: 7708, 5: 4883, 6: 4844, 7: 6174} 8 0.8862422868799427
        {0: 86767, 1: 16153, 2: 5677, 3: 6125, 4: 7620, 5: 8608, 6: 13358, 7: 18746, 8: 9194} 9 0.8768866770665451
        {0: 8149, 1: 8520, 2: 7427, 3: 4493, 4: 4770, 5: 7937, 6: 18405, 7: 85456, 8: 16069, 9: 11022} 10 0.881543905095435
        {0: 105546, 1: 1776, 2: 1598, 3: 4848, 4: 4517, 5: 4321, 6: 2438, 7: 19874, 8: 16132, 9: 2304, 10: 8894} 11 0.8917586699694955
        {0: 75274, 1: 18088, 2: 4863, 3: 13558, 4: 4729, 5: 6101, 6: 8420, 7: 4463, 8: 6830, 9: 15897, 10: 7956, 11: 6069} 12 0.861746858647752
        {0: 3945, 1: 14090, 2: 6087, 3: 72374, 4: 17804, 5: 5666, 6: 9075, 7: 8383, 8: 7409, 9: 6294, 10: 8058, 11: 4310, 12: 8753} 13 0.8606385284952195
        {0: 70139, 1: 6658, 2: 15814, 3: 4478, 4: 11507, 5: 8408, 6: 4852, 7: 5555, 8: 15208, 9: 6062, 10: 10308, 11: 3534, 12: 4704, 13: 5021} 14 0.8453955357082513
        ```


* **thecarconnection**
    * result (version 1)
        ```
        Top terms per cluster:None
        Cluster 0: safety crash side for test airbags iihs of in features
        Cluster 1: mpg highway city combined epa at drive with fuel rated
        Cluster 2: of it to is in that with on its for
        Cluster 3: seats seat space in for comfort of rear room is
        Cluster 4: speed engine to liter with of automatic is in torque
        Cluster distribution:
        {3: 14693, 2: 64812, 4: 12831, 0: 10143, 1: 5236}
        0.9117029397988335
        ```
    * result (version 2)
        ```
        Top terms per cluster: None
        Cluster 0: speed engine liter automatic horsepower transmission mph torque hp 60
        Cluster 1: safety crash side test iihs airbags features standard scores top
        Cluster 2: mpg highway city combined epa drive fuel rated wheel 22
        Cluster 3: car like interior steering look road well cars fuel new
        Cluster 4: seats seat space comfort rear front room cargo row back
        Cluster distribution:
        {0: 11423, 1: 10444, 2: 5516, 3: 65745, 4: 14587}
        0.9344144267916032
        ```

    * cost trend (version 1)
    
        ![thecarconnection](pictures/thecarconnection_(3,8)_v1.png)
        ```
        107715 documents
        Cluster distribution:
        Cluster 3: {0: 79077, 2: 18331, 1: 10307} 0.9248839267944382
        Cluster 4: {2: 55226, 3: 36969, 0: 10188, 1: 5332} 0.918130590608453
        Cluster 5: {1: 14711, 0: 64793, 4: 12830, 3: 10145, 2: 5236} 0.9117029461838286
        Cluster 6: {1: 13305, 2: 22135, 4: 47575, 5: 9897, 0: 9604, 3: 5199} 0.9067644559857724
        Cluster 7: {6: 36020, 1: 13401, 2: 18572, 5: 16371, 3: 8934, 4: 9251, 0: 5166} 0.9035498516286458
        ```
    * cost trend (version 2)
    
        ![thecarconnection](pictures/thecarconnection_(3,8)_v2.png)
        ```
        107715 documents
        Cluster distribution:
        {0: 10604, 1: 20721, 2: 76390} 3 0.9497155380672195
        {0: 15756, 1: 5718, 2: 10498, 3: 75743} 4 0.94166350625464
        {0: 13807, 1: 61575, 2: 16764, 3: 10347, 4: 5222} 5 0.9365327696440205
        {0: 4147, 1: 58090, 2: 16395, 3: 5156, 4: 13694, 5: 10233} 6 0.9328593402751485
        {0: 11724, 1: 53601, 2: 8284, 3: 10201, 4: 5397, 5: 8470, 6: 10038} 7 0.9250371903541582
        ```


  