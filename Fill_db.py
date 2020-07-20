import requests

url_register = 'http://127.0.0.1:5000/register'
url_report = 'http://127.0.0.1:5000/report'

CHECKPOINT_LIST =[
  {
    "guid": "CAA63B87-DA1E-488B-BD8B-C5E04FE06EC2",
    "longitude": -86.167178,
    "latitude": 39.77143
  },
  {
    "guid": "992E7ABA-2A6A-46E3-9145-367C4EBAC37A",
    "longitude": -86.167221,
    "latitude": 39.769509
  },
  {
    "guid": "1B94B303-98F3-4430-B538-D9F81131CC49",
    "longitude": -86.170145,
    "latitude": 39.769406
  },
  {
    "guid": "0111F9C4-E3F3-406F-8A36-01E44AE37CA8",
    "longitude": -86.170091,
    "latitude": 39.771542
  },
  {
    "guid": "9AB62103-3823-4B5B-BD5E-7C9959522DB1",
    "longitude": -86.168688,
    "latitude": 39.770447
  },
  {
    "guid": "C2A886EC-A687-49B9-8417-D80418D9F9FF",
    "longitude": -86.17035,
    "latitude": 39.769044
  },
  {
    "guid": "D348EE8C-3EAB-4A84-ADBD-A3CC15CEA20A",
    "longitude": -86.167292,
    "latitude": 39.767492
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "longitude": -86.169451,
    "latitude": 39.768391
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "longitude": -86.169462,
    "latitude": 39.769087
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "longitude": -86.168141,
    "latitude": 39.768225
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "longitude": -86.170528,
    "latitude": 39.768411
  },
  {
    "guid": "ACA29BF9-D2F8-4479-91F9-D7BEFACF3F07",
    "longitude": -86.170544,
    "latitude": 39.767483
  },
  {
    "guid": "61AEF95A-20ED-4CEE-A138-942D580BFE46",
    "longitude": -86.167451,
    "latitude": 39.766716
  },
  {
    "guid": "5A9300C0-74BF-4C20-BD15-C9AC0E640C01",
    "longitude": -86.168199,
    "latitude": 39.767007
  },
  {
    "guid": "43006C5D-4AB3-414C-9228-0DE9CAFEE4F1",
    "longitude": -86.168934,
    "latitude": 39.767143
  },
  {
    "guid": "CD073B4C-DFAA-4B76-A6AF-989EE5A74D3A",
    "longitude": -86.169208,
    "latitude": 39.766273
  },
  {
    "guid": "C421E2D3-A8C1-4210-98D8-F3289999EF2C",
    "longitude": -86.168197,
    "latitude": 39.765933
  },
  {
    "guid": "751C3E69-90D2-4568-B8B9-50E048EC2A23",
    "longitude": -86.168267,
    "latitude": 39.766356
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "longitude": -86.16887,
    "latitude": 39.766558
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "longitude": -86.167341,
    "latitude": 39.765762
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "longitude": -86.167352,
    "latitude": 39.764904
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "longitude": -86.167368,
    "latitude": 39.763692
  },
  {
    "guid": "2C447E8B-9737-44A1-9CC5-D5380A0CAEF9",
    "longitude": -86.169423,
    "latitude": 39.763865
  },
  {
    "guid": "25F0AC88-6CC1-42DE-84FD-DC9BA7890519",
    "longitude": -86.169119,
    "latitude": 39.765798
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "longitude": -86.167529,
    "latitude": 39.765618
  },
  {
    "guid": "01C7E775-5F71-4B32-9A83-F0ABB92AA975",
    "longitude": -86.169428,
    "latitude": 39.764987
  },
  {
    "guid": "B97F72E0-FE4F-4C15-889B-1D3392F3C174",
    "longitude": -86.169557,
    "latitude": 39.764455
  },
  {
    "guid": "4A9206B6-0A7F-4385-BEB5-25FF3EA0A51D",
    "longitude": -86.168935,
    "latitude": 39.764109
  },
  {
    "guid": "4533F1DB-FA34-42D1-A193-B5B6F2350307",
    "longitude": -86.166516,
    "latitude": 39.765701
  },
  {
    "guid": "BD21ABE4-4B49-4E42-B7A9-485BC1963FDB",
    "longitude": -86.165352,
    "latitude": 39.765717
  },
  {
    "guid": "C73783DD-3325-41D8-BCB8-B16CEECEE009",
    "longitude": -86.163968,
    "latitude": 39.765701
  },
  {
    "guid": "9E5A56D5-0750-41E9-8226-30DD08EF94DE",
    "longitude": -86.162037,
    "latitude": 39.765647
  },
  {
    "guid": "78117E33-DB69-4E76-8953-9F73CBA0BFFA",
    "longitude": -86.161973,
    "latitude": 39.764468
  },
  {
    "guid": "CFEF3FD9-D97A-4437-AF8E-46E538484BB9",
    "longitude": -86.162011,
    "latitude": 39.763161
  },
  {
    "guid": "64B30ECB-13B7-48E0-838D-DBA5B268B290",
    "longitude": -86.162032,
    "latitude": 39.761672
  },
  {
    "guid": "016AFCCB-09B8-4B31-BFB2-23320479B144",
    "longitude": -86.163904,
    "latitude": 39.761651
  },
  {
    "guid": "2F40CDF7-168D-42CD-BB83-ED423000B2FA",
    "longitude": -86.165449,
    "latitude": 39.761705
  },
  {
    "guid": "B08A6324-6294-4590-BF8F-1BB5ADA623B8",
    "longitude": -86.16679,
    "latitude": 39.764167
  },
  {
    "guid": "CF917C21-071D-447D-B78E-01CDA555B2BD",
    "longitude": -86.16547,
    "latitude": 39.765925
  },
  {
    "guid": "7052A7F8-5FFA-44FB-97FE-7D0D3205A895",
    "longitude": -86.164483,
    "latitude": 39.765933
  },
  {
    "guid": "960DA0D2-5F45-445F-8035-0934196EFF14",
    "longitude": -86.163442,
    "latitude": 39.765921
  },
  {
    "guid": "4E10B82C-8095-4FC8-B235-F2D54FAF4993",
    "longitude": -86.161876,
    "latitude": 39.765851
  },
  {
    "guid": "C3AAB609-D291-4562-B420-972714715B29",
    "longitude": -86.161838,
    "latitude": 39.767034
  },
  {
    "guid": "68BD176B-01EE-48D7-A5E3-1C1B32AF38BA",
    "longitude": -86.162879,
    "latitude": 39.76658
  },
  {
    "guid": "7402F681-1E5F-493A-92A9-42A40849833D",
    "longitude": -86.162831,
    "latitude": 39.767083
  }
]

EXPOSED_CHECKPOINT_LIST = [
  {
    "guid": "CAA63B87-DA1E-488B-BD8B-C5E04FE06EC2",
    "epoch": 5
  },
  {
    "guid": "992E7ABA-2A6A-46E3-9145-367C4EBAC37A",
    "epoch": 6
  },
  {
    "guid": "1B94B303-98F3-4430-B538-D9F81131CC49",
    "epoch": 1
  },
  {
    "guid": "0111F9C4-E3F3-406F-8A36-01E44AE37CA8",
    "epoch": 5
  },
  {
    "guid": "9AB62103-3823-4B5B-BD5E-7C9959522DB1",
    "epoch": 84
  },
  {
    "guid": "C2A886EC-A687-49B9-8417-D80418D9F9FF",
    "epoch": 2
  },
  {
    "guid": "D348EE8C-3EAB-4A84-ADBD-A3CC15CEA20A",
    "epoch": 48
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 14
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 58
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 24
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 75
  },
  {
    "guid": "ACA29BF9-D2F8-4479-91F9-D7BEFACF3F07",
    "epoch": 15
  },
  {
    "guid": "61AEF95A-20ED-4CEE-A138-942D580BFE46",
    "epoch": 54
  },
  {
    "guid": "0111F9C4-E3F3-406F-8A36-01E44AE37CA8",
    "epoch": 54
  },
  {
    "guid": "9AB62103-3823-4B5B-BD5E-7C9959522DB1",
    "epoch": 95
  },
  {
    "guid": "C2A886EC-A687-49B9-8417-D80418D9F9FF",
    "epoch": 32
  },
  {
    "guid": "D348EE8C-3EAB-4A84-ADBD-A3CC15CEA20A",
    "epoch": 96
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 5
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 48
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 68
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "epoch": 58
  },
  {
    "guid": "2C447E8B-9737-44A1-9CC5-D5380A0CAEF9",
    "epoch": 78
  },
  {
    "guid": "25F0AC88-6CC1-42DE-84FD-DC9BA7890519",
    "epoch": 94
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "epoch": 48
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 78
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "epoch": 64
  },
  {
    "guid": "2C447E8B-9737-44A1-9CC5-D5380A0CAEF9",
    "epoch": 28
  },
  {
    "guid": "4A9206B6-0A7F-4385-BEB5-25FF3EA0A51D",
    "epoch": 48
  },
  {
    "guid": "4533F1DB-FA34-42D1-A193-B5B6F2350307",
    "epoch": 36
  },
  {
    "guid": "BD21ABE4-4B49-4E42-B7A9-485BC1963FDB",
    "epoch": 47
  },
  {
    "guid": "C73783DD-3325-41D8-BCB8-B16CEECEE009",
    "epoch": 85
  },
  {
    "guid": "9E5A56D5-0750-41E9-8226-30DD08EF94DE",
    "epoch": 95
  },
  {
    "guid": "78117E33-DB69-4E76-8953-9F73CBA0BFFA",
    "epoch": 63
  },
  {
    "guid": "43006C5D-4AB3-414C-9228-0DE9CAFEE4F1",
    "epoch": 79
  },
  {
    "guid": "CD073B4C-DFAA-4B76-A6AF-989EE5A74D3A",
    "epoch": 80
  },
  {
    "guid": "C421E2D3-A8C1-4210-98D8-F3289999EF2C",
    "epoch": 15
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 19
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 30
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "epoch": 35
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 36
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 39
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 37
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 5
  },
  {
    "guid": "ACA29BF9-D2F8-4479-91F9-D7BEFACF3F07",
    "epoch": 6
  },
  {
    "guid": "61AEF95A-20ED-4CEE-A138-942D580BFE46",
    "epoch": 1
  },
  {
    "guid": "0111F9C4-E3F3-406F-8A36-01E44AE37CA8",
    "epoch": 5
  },
  {
    "guid": "9AB62103-3823-4B5B-BD5E-7C9959522DB1",
    "epoch": 84
  },
  {
    "guid": "C2A886EC-A687-49B9-8417-D80418D9F9FF",
    "epoch": 2
  },
  {
    "guid": "D348EE8C-3EAB-4A84-ADBD-A3CC15CEA20A",
    "epoch": 48
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 14
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 58
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 24
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "epoch": 75
  },
  {
    "guid": "2C447E8B-9737-44A1-9CC5-D5380A0CAEF9",
    "epoch": 15
  },
  {
    "guid": "25F0AC88-6CC1-42DE-84FD-DC9BA7890519",
    "epoch": 54
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "epoch": 54
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 95
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "epoch": 32
  },
  {
    "guid": "4A9206B6-0A7F-4385-BEB5-25FF3EA0A51D",
    "epoch": 96
  },
  {
    "guid": "4533F1DB-FA34-42D1-A193-B5B6F2350307",
    "epoch": 5
  },
  {
    "guid": "BD21ABE4-4B49-4E42-B7A9-485BC1963FDB",
    "epoch": 48
  },
  {
    "guid": "C73783DD-3325-41D8-BCB8-B16CEECEE009",
    "epoch": 68
  },
  {
    "guid": "9E5A56D5-0750-41E9-8226-30DD08EF94DE",
    "epoch": 58
  },
  {
    "guid": "78117E33-DB69-4E76-8953-9F73CBA0BFFA",
    "epoch": 78
  },
  {
    "guid": "4A9206B6-0A7F-4385-BEB5-25FF3EA0A51D",
    "epoch": 94
  },
  {
    "guid": "4533F1DB-FA34-42D1-A193-B5B6F2350307",
    "epoch": 48
  },
  {
    "guid": "BD21ABE4-4B49-4E42-B7A9-485BC1963FDB",
    "epoch": 78
  },
  {
    "guid": "C73783DD-3325-41D8-BCB8-B16CEECEE009",
    "epoch": 64
  },
  {
    "guid": "9E5A56D5-0750-41E9-8226-30DD08EF94DE",
    "epoch": 28
  },
  {
    "guid": "78117E33-DB69-4E76-8953-9F73CBA0BFFA",
    "epoch": 48
  },
  {
    "guid": "0111F9C4-E3F3-406F-8A36-01E44AE37CA8",
    "epoch": 36
  },
  {
    "guid": "9AB62103-3823-4B5B-BD5E-7C9959522DB1",
    "epoch": 47
  },
  {
    "guid": "C2A886EC-A687-49B9-8417-D80418D9F9FF",
    "epoch": 85
  },
  {
    "guid": "D348EE8C-3EAB-4A84-ADBD-A3CC15CEA20A",
    "epoch": 95
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 63
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 79
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 80
  },
  {
    "guid": "B01A86E5-4E9A-4408-A8CA-79447B2E20D8",
    "epoch": 15
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 19
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 30
  },
  {
    "guid": "61AEF95A-20ED-4CEE-A138-942D580BFE46",
    "epoch": 35
  },
  {
    "guid": "0111F9C4-E3F3-406F-8A36-01E44AE37CA8",
    "epoch": 36
  },
  {
    "guid": "9AB62103-3823-4B5B-BD5E-7C9959522DB1",
    "epoch": 39
  },
  {
    "guid": "016AFCCB-09B8-4B31-BFB2-23320479B144",
    "epoch": 37
  },
  {
    "guid": "2F40CDF7-168D-42CD-BB83-ED423000B2FA",
    "epoch": 68
  },
  {
    "guid": "016AFCCB-09B8-4B31-BFB2-23320479B144",
    "epoch": 58
  },
  {
    "guid": "2F40CDF7-168D-42CD-BB83-ED423000B2FA",
    "epoch": 78
  },
  {
    "guid": "016AFCCB-09B8-4B31-BFB2-23320479B144",
    "epoch": 94
  },
  {
    "guid": "2F40CDF7-168D-42CD-BB83-ED423000B2FA",
    "epoch": 48
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 78
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 64
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 28
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 48
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 36
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 47
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 85
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 95
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 63
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 79
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 80
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 15
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 19
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 63
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 79
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 80
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 15
  },
  {
    "guid": "07DC82E5-B08C-41DC-AA3E-BA3E961CC4EA",
    "epoch": 19
  },
  {
    "guid": "9FDE7E47-289F-4763-B41B-92D6023BBB57",
    "epoch": 30
  },
  {
    "guid": "F51636D9-23FF-47BF-92E7-22EEC4FF6A77",
    "epoch": 35
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 36
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 39
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 37
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 5
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 6
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 1
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 5
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 84
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 2
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 48
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 14
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 58
  },
  {
    "guid": "754A3DF2-6710-4767-A61E-A2E12C3C1C81",
    "epoch": 24
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 75
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "epoch": 15
  },
  {
    "guid": "01C7E775-5F71-4B32-9A83-F0ABB92AA975",
    "epoch": 54
  },
  {
    "guid": "B97F72E0-FE4F-4C15-889B-1D3392F3C174",
    "epoch": 58
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "epoch": 78
  },
  {
    "guid": "01C7E775-5F71-4B32-9A83-F0ABB92AA975",
    "epoch": 94
  },
  {
    "guid": "B97F72E0-FE4F-4C15-889B-1D3392F3C174",
    "epoch": 48
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "epoch": 78
  },
  {
    "guid": "01C7E775-5F71-4B32-9A83-F0ABB92AA975",
    "epoch": 64
  },
  {
    "guid": "B97F72E0-FE4F-4C15-889B-1D3392F3C174",
    "epoch": 28
  },
  {
    "guid": "0A7BE093-FD6B-428E-B021-539B3F2652C6",
    "epoch": 48
  },
  {
    "guid": "01C7E775-5F71-4B32-9A83-F0ABB92AA975",
    "epoch": 36
  },
  {
    "guid": "B97F72E0-FE4F-4C15-889B-1D3392F3C174",
    "epoch": 47
  },
  {
    "guid": "7052A7F8-5FFA-44FB-97FE-7D0D3205A895",
    "epoch": 85
  },
  {
    "guid": "960DA0D2-5F45-445F-8035-0934196EFF14",
    "epoch": 95
  },
  {
    "guid": "4E10B82C-8095-4FC8-B235-F2D54FAF4993",
    "epoch": 63
  },
  {
    "guid": "7052A7F8-5FFA-44FB-97FE-7D0D3205A895",
    "epoch": 79
  },
  {
    "guid": "960DA0D2-5F45-445F-8035-0934196EFF14",
    "epoch": 80
  },
  {
    "guid": "4E10B82C-8095-4FC8-B235-F2D54FAF4993",
    "epoch": 15
  },
  {
    "guid": "7052A7F8-5FFA-44FB-97FE-7D0D3205A895",
    "epoch": 19
  },
  {
    "guid": "960DA0D2-5F45-445F-8035-0934196EFF14",
    "epoch": 24
  },
  {
    "guid": "4E10B82C-8095-4FC8-B235-F2D54FAF4993",
    "epoch": 75
  },
  {
    "guid": "D348EE8C-3EAB-4A84-ADBD-A3CC15CEA20A",
    "epoch": 15
  },
  {
    "guid": "15A5607A-4283-42D2-ACA0-5ADED1EF6977",
    "epoch": 54
  },
  {
    "guid": "0A0D9954-BABD-4359-B9D6-BC53B1313602",
    "epoch": 15
  },
  {
    "guid": "03C6AA58-F5B2-4614-8680-064BDCE6A76D",
    "epoch": 94
  }
]

# populate CHECKPOINT table
for obj in CHECKPOINT_LIST:
    requests.post(url_register,json=obj)
    print(obj)

# populate EXPOSED CHECKPOINT table
for obj in EXPOSED_CHECKPOINT_LIST:
    requests.post(url_report,json=obj)
    print(obj)

print("done")
