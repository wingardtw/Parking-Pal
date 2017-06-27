# Parking Pal

We developed three separate applications for Parking-Pal:


## 1. Parking Data collection (Python Web clawler) and API to retrive those data
### garagerecords.py
Web clawler that collects live data about parking garage availability.
Libraries Used:
  xml, urllib, mysql, threading
<p align="center"><img width="90%" vspace="20" src="https://lh3.googleusercontent.com/qS1PEh2RCFLVRg1O4oO-slQNX0OilA4h7mz9-Ac86GKQ2SQGdy4R_ab8kBfAyrj8CNv1h5Vwa9m0Lodcl2VMTUF3XzcLMG9-C7z-fMZgUptKH_CV8hmpgCbKKbHY-b6wEeIeS1e1XEA7kP2NL7Fr4RnCNB0bAk6zyH_ta_IQvM-vHFMpuPfVcNXeGPHZengjhyF8VM_duNv6VdQ5R1it5f4MDjlYPID3vWQ5Ws8vb5pw1zC890-mQmpy-azMb-ov3Jorqd-c0Hy0ljhFBFsaYuPVqfxXj1W0uOAQBTBAsuBZoyfBvk6piL9zf1mMdaYXo-_m5SPjBLYsW7etKAPHrKBTuGA8fM8QsR_hwiZIHG0iDnSoUrYEHe6silY5jcz_JtnXGiO7PGEz7atk3btrmAkhWWRiUwz4pA2l0rLp3775AHKvuKZthXZpLk-maGuS8qJPpzchYa3SPVEQEQZLJw7SNbF_MTjPnd7n3TPaad3LOeACHw6yMS3OKpvIInWbRkKmqXErPeQ4SbFG565wU2i5acjnA5Z5Nv5yUreuh82x77A6mdpoRPgDB5FDk0bEh57471_8w3OaYY2zmkFxZuf6HCoCoWMTxQCoKuNjn8y8usyn=w2160-h1269-no"></p>

### Parking Pal Data API 
[Parking Pal API](http://104.154.229.56/api.php/availability) - Data collected from garagerecords.py can be access from this api
<p align="center"><img width="90%" vspace="20" src="https://lh3.googleusercontent.com/OhPbsI3yMi3zE_lS0Cl_CofO6BQ5KIIRfHJ4EjL-WJSSQMfp5kDmpDraUCicxkMEn_BeSOwj_3VlqL_jeUaxng_q3IaF3kFX87Wu9xfP59rccB3at6gAa9-_54vUgan8VOlxHxDQBo3vFi5bp3CN1MzYRPJIJyjHj2Iq5JKdTZ-9sfVTOsEfx1YKMFpQHdOnD6RMq5Y4AcsalFvQxePwH2GbhvbYOxH0A3brvYipspz2zs3RSCdUJSG7Ikb5B3vOKZfmla7uUXWY902wiSQNCNonxZaLPw8RAYDH3t2ztSr6qm7CLVu167WYcV1v66WmFBSad2-4E6xkXJYn17-Oi3-DW0i24HPEhkddBwFBffT6RzDQVXMiDNHo3Dh3m_hB__P0Wy2j3N-Nr2FfeSXd19YguFoSQJ_C6-xTd4yEsdb0AkOKPhXZO-gQ3seJcd8hnekRRaku_82P42Q5_E9WHw75sXZKf5BZpJ_e22qkXkUCctHxfOla3kOa9USL72pnA308dra3plER8SGMGyApBZva-7q5tDyQkd76EUqBodI-WWwXeHKaqbqRchBtAQn0nZ29lXa3_Tm1cqvMRqCa3PQC2u38q6p_NcaTwHBaOtW0ooNG0YJt=w636-h1283-no"></p>

They are currently running in our Google Cloud server.


## 2. Parking availability prediction:
Application Predicting Parking trends in San Francisco
### Installation
garage.py
Stores data from SF Park api for garages in San Francisco.
Libraries Used:
  mysql, json, pandas, urllib, xml  

visualization.py
Applies support vector machine analysis to records to try and predict parking availability in the near future
Libraries Used:
  numpy, matplotlib, sklearn, xml

<p align="center"><img width="90%" vspace="20" src="https://lh3.googleusercontent.com/87pmRhWTC3bCtJwrhSGwpuU-9eMc1VeUEuAbqHTQLTKUeu99aw-DOXe5iQRycxVUhwDorFf_3SRf6Yd0dZwak6fe4cNesvELqOrj3S4UWcVKtw5EPyiLvVC3ARYJxvMUN1YVVm68m5TwLn8Bn6D1r23f7DzM2YvuK27ERS4Qnu4wDVeW5F38wpBKsZB14P6BZOB9GqVvjALA7xTh7fUAdKO5BSR1Xv86kvq6XSMvzxlbnIc0PQ2t3l7lYp3V-r8pXK2gsY0QFRn0lnJ6flzaOneNxZRC_oxWC6XGMGy2fz3ToaPKs_usTWpxC-R6_cq4E_4rLdNwHv_DQBIp2NsehEVcV4ST5rkm2EGfOxhNY0EOX8AJgvvfCi74DSAfxGc54b_0FjG15ygdKAa4_bagMZA_fbbz67vkfQmnIPIwFDSqFSTGf2nvNAqRT4l1FP-4EMJGaoCvwI14mUsMCTFiAYG-mBNK60yvfTU0k7A7eG7JKrzDcCTUiScuAUqlD773PYtp6CGYKyBGsUhnAG3vKGMU_w3CZONqioNgLj9l8-piy0IlrbEpoWd2XZ3WRehEfRhm9UUxl2F2HVORG30WznbyzYHnQ1A0Qy_UjbH0M_SREGPOhNst=w635-h471-no"></p>


## 3. Parking Pal Client-side application (Android)
The description of this application is located in this respository: 
[!A|Parking Pal](https://cldup.com/dTxpPi9lDf.thumb.png)](https://github.com/wingardtw/Parking-Pal/tree/master/Parking_Radar(Android))



### License
----
MIT
**Free Software, Feel free to use it!**
