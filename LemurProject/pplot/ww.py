import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


#UnInter=[[1.0000,0.4118,0.3250,0.3182,0.2769,0.2688,0.2403,0.2378,0.2222,0.0565,0.0000],
#[0.0909,0.0775,0.0775,0.0632,0.0632,0.0632,0.0632,0.0632,0.0481,0.0000,0.0000],
#[0.3333,0.3143,0.3143,0.2979,0.2969,0.2771,0.2596,0.0786,0.0000,0.0000,0.0000],
#[0.6364,0.6364,0.6000,0.5600,0.0738,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000],
#[0.2500,0.0814,0.0699,0.0691,0.0644,0.0591,0.0591,0.0511,0.0511,0.0000,0.0000],
#[0.1250,0.0962,0.0820,0.0622,0.0448,0.0386,0.0336,0.0336,0.0000,0.0000,0.0000],
#[1.0000,0.8333,0.7500,0.7273,0.6047,0.6047,0.5636,0.5161,0.2483,0.0761,0.0000],
#[1.0000,0.8333,0.7500,0.5833,0.3390,0.2581,0.2240,0.1988,0.1233,0.0438,0.0000]]


#Inter=[[0.4000,0.2000,0.4000,0.3500,0.3000,0.2500,0.1850,0.0800,0.0420],
#[0.0000,0.0000,0.0000,0.0000,0.0333,0.0600,0.0600,0.0600,0.0380],
#[0.2000,0.1000,0.1333,0.3000,0.2667,0.2600,0.1450,0.0660,0.0350],
#[0.4000,0.6000,0.6000,0.5500,0.4667,0.1500,0.0850,0.0420,0.0220],
#[0.2000,0.1000,0.1333,0.1000,0.0667,0.0700,0.0600,0.0580,0.0390],
#[0.0000,0.0000,0.0000,0.0500,0.0667,0.0700,0.0650,0.0400,0.0320],
#[0.8000,0.7000,0.6667,0.7000,0.5667,0.3300,0.1900,0.0800,0.0430],
#[0.8000,0.8000,0.6000,0.6000,0.5333,0.2400,0.1750,0.0760,0.0420]]




UnInteraxis=[0.00,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00]


#U_Oka_stem=[1.0000,0.4118,0.3250,0.3182,0.2769,0.2688,0.2403,0.2378,0.2222,0.0565,0.0000]
#U_Oka_nostem=[0.0909,0.0775,0.0775,0.0632,0.0632,0.0632,0.0632,0.0632,0.0481,0.0000,0.0000]

#U_Laplace_stem=[0.6364,0.6364,0.6000,0.5600,0.0738,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000]
#U_Laplace_nostem=[0.3333,0.3143,0.3143,0.2979,0.2969,0.2771,0.2596,0.0786,0.0000,0.0000,0.0000]


#U_JM_stem=[0.2500,0.0814,0.0699,0.0691,0.0644,0.0591,0.0591,0.0511,0.0511,0.0000,0.0000]
#U_JM_nostem=[0.1250,0.0962,0.0820,0.0622,0.0448,0.0386,0.0336,0.0336,0.0000,0.0000,0.0000]

#U_Two_stem=[1.0000,0.8333,0.7500,0.7273,0.6047,0.6047,0.5636,0.5161,0.2483,0.0761,0.0000]
#U_Two_nostem=[1.0000,0.8333,0.7500,0.5833,0.3390,0.2581,0.2240,0.1988,0.1233,0.0438,0.0000]

###########
Interaxis=[5,10,15,20,30,100,200,500,1000]

#Oka_stem=[0.4000,0.2000,0.4000,0.3500,0.3000,0.2500,0.1850,0.0800,0.0420]
#Oka_nostem=[0.0000,0.0000,0.0000,0.0000,0.0333,0.0600,0.0600,0.0600,0.0380]

#Laplace_stem=[0.4000,0.6000,0.6000,0.5500,0.4667,0.1500,0.0850,0.0420,0.0220]
#Laplace_nostem=[0.2000,0.1000,0.1333,0.3000,0.2667,0.2600,0.1450,0.0660,0.0350]


#JM_stem=[0.2000,0.1000,0.1333,0.1000,0.0667,0.0700,0.0600,0.0580,0.0390]
#JM_nostem=[0.0000,0.0000,0.0000,0.0500,0.0667,0.0700,0.0650,0.0400,0.0320]

#Two_stem=[0.8000,0.7000,0.6667,0.7000,0.5667,0.3300,0.1900,0.0800,0.0430]
#Two_nostem=[0.8000,0.8000,0.6000,0.6000,0.5333,0.2400,0.1750,0.0760,0.0420]


#####################################################################
#ID=['Okapi_stem','Okapi_nostem','Laplace_stem','Laplace_nostem','Jelinek-Mercer_stem','Jelinek-Mercer_nostem','TwoStage_stem','TwoStage_nostem']
##############################

#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
#plt.plot(UnInteraxis,U_Oka_stem,color = 'b', label="Okapi_stem")
#plt.plot(UnInteraxis,U_Oka_nostem,color = 'g', label="Okapi_nostem")
#plt.plot(UnInteraxis,U_Laplace_stem,color = 'r', label="Laplace_stem")
#plt.plot(UnInteraxis,U_Laplace_nostem,color = 'c', label="Laplace_nostem")
#plt.plot(UnInteraxis,U_JM_stem,color = 'm', label="Jelinek-Mercer_stem")
#plt.plot(UnInteraxis,U_JM_nostem,color = 'y', label="Jelinek-Mercer_nostem")
#plt.plot(UnInteraxis,U_Two_stem,color = 'k', label="TwoStage_stem")
#plt.plot(UnInteraxis,U_Two_nostem,color = 'skyblue', label="TwoStage_nostem")


#plt.title("Interpolated Recall - Precision Averages (Query401)",x=0.5, y=1.03)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)

#plt.xlabel("Interpolated Recall")
#plt.ylabel("Precision Averages")
#plt.legend(loc = "best", fontsize=20)
#plt.show()
#################################################################################

#jm01=[0.3333,0.2727,0.2632,0.2500,0.2321,0.2321,0.1971,0.1702,0.0788,0.0000,0.0000]
#jm02=[0.5000,0.2208,0.2208,0.2208,0.1957,0.1929,0.1929,0.1448,0.0905,0.0421,0.0000]

#jm03=[0.5000,0.1857,0.1857,0.1798,0.1695,0.1690,0.1627,0.1293,0.0950,0.0429,0.0000]
#jm04=[0.3333,0.1731,0.1731,0.1683,0.1636,0.1517,0.1517,0.1285,0.0984,0.0000,0.0000]


#jm05=[0.3333,0.1443,0.1443,0.1443,0.1395,0.1340,0.1340,0.1081,0.0973,0.0000,0.0000]
#jm06=[0.2500,0.1216,0.1216,0.1216,0.1216,0.1124,0.1124,0.0899,0.0826,0.0000,0.0000]

#jm07=[0.2500,0.1071,0.1071,0.1023,0.1023,0.0899,0.0826,0.0782,0.0711,0.0000,0.0000]
#jm08=[0.2500,0.0814,0.0699,0.0691,0.0644,0.0591,0.0591,0.0511,0.0511,0.0000,0.0000]

#jm09=[0.2000,0.0465,0.0352,0.0323,0.0323,0.0323,0.0311,0.0000,0.0000,0.0000,0.0000]
#jm10=[0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000]

#################################################################################
#tjm01=[0.2000,0.1000,0.1333,0.2000,0.2333,0.2000,0.1600,0.0760,0.0400]
#tjm02=[0.2000,0.1000,0.0667,0.1000,0.2000,0.1800,0.1550,0.0760,0.0410]

#tjm03=[0.2000,0.1000,0.0667,0.0500,0.1000,0.1600,0.1450,0.0760,0.0410]
#tjm04=[0.2000,0.1000,0.0667,0.1000,0.0667,0.1600,0.1400,0.0740,0.0400]


#tjm05=[0.2000,0.1000,0.0667,0.1000,0.0667,0.1400,0.1200,0.0740,0.0390]
#tjm06=[0.2000,0.1000,0.0667,0.1000,0.0667,0.1000,0.1100,0.0740,0.0400]

#tjm07=[0.2000,0.1000,0.0667,0.1000,0.0667,0.1000,0.0950,0.0680,0.0390]
#tjm08=[0.2000,0.1000,0.1333,0.1000,0.0667,0.0700,0.0600,0.0580,0.0390]

#tjm09=[0.2000,0.1000,0.1333,0.1000,0.0667,0.0400,0.0400,0.0300,0.0300]
#tjm10=[0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000]
###################################################################


#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
#plt.plot(UnInteraxis,jm01,color = 'b', label="lambda 0.1")
#plt.plot(UnInteraxis,jm02,color = 'g', label="lambda 0.2")
#plt.plot(UnInteraxis,jm03,color = 'r', label="lambda 0.3")
#plt.plot(UnInteraxis,jm04,color = 'c', label="lambda 0.4")
#plt.plot(UnInteraxis,jm05,color = 'm', label="lambda 0.5")
#plt.plot(UnInteraxis,jm06,color = 'y', label="lambda 0.6")
#plt.plot(UnInteraxis,jm07,color = 'k', label="lambda 0.7")
#plt.plot(UnInteraxis,jm08,color = 'skyblue', label="lambda 0.8")
#plt.plot(UnInteraxis,jm09,color = 'pink', label="lambda 0.9")
#plt.plot(UnInteraxis,jm10,color = 'Wistia', label="lambda 1.0")


#plt.title("(Query401) Jelinek-Mercer_stem with different lambda",x=0.5, y=1.03)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)

#plt.xlabel("Interpolated Recall")
#plt.ylabel("Precision Averages")
#plt.legend(loc = "best", fontsize=20)
#plt.show()

#########################################################
#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
#plt.plot(Interaxis,tjm01,color = 'b', label="lambda 0.1")
#plt.plot(Interaxis,tjm02,color = 'g', label="lambda 0.2")
#plt.plot(Interaxis,tjm03,color = 'r', label="lambda 0.3")
#plt.plot(Interaxis,tjm04,color = 'c', label="lambda 0.4")
#plt.plot(Interaxis,tjm05,color = 'm', label="lambda 0.5")
#plt.plot(Interaxis,tjm06,color = 'y', label="lambda 0.6")
#plt.plot(Interaxis,tjm07,color = 'k', label="lambda 0.7")
#plt.plot(Interaxis,tjm08,color = 'skyblue', label="lambda 0.8")
#plt.plot(Interaxis,tjm09,color = 'pink', label="lambda 0.9")
#plt.plot(UnInteraxis,jm10,color = 'Wistia', label="lambda 1.0")


#plt.title("(Query401) Jelinek-Mercer_stem with different lambda",x=0.5, y=1.03)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)

#plt.xlabel("At k docs")
#plt.ylabel("Precision")
#plt.legend(loc = "best", fontsize=20)
#plt.show()

#######################################################
ok=[0.5000,0.4118,0.3714,0.3636,0.2778,0.2778,0.2745,0.2519,0.2400,0.0000,0.0000]
U_Oka_stem=[1.0000,0.4118,0.3250,0.3182,0.2769,0.2688,0.2403,0.2378,0.2222,0.0565,0.0000]

ok_=[0.4000,0.4000,0.3333,0.3500,0.3000,0.2600,0.1900,0.0800,0.0400]
Oka_stem=[0.4000,0.2000,0.4000,0.3500,0.3000,0.2500,0.1850,0.0800,0.0420]



ok2=[0.5000,0.3600,0.3600,0.2000,0.1879,0.1879,0.1879,0.1860,0.1188,0.0469,0.0000]
U_Oka_nostem=[0.0909,0.0775,0.0775,0.0632,0.0632,0.0632,0.0632,0.0632,0.0481,0.0000,0.0000]


ok2_=[0.4000,0.3000,0.2667,0.3000,0.3333,0.1700,0.1650,0.0740,0.0410]
Oka_nostem=[0.0000,0.0000,0.0000,0.0000,0.0333,0.0600,0.0600,0.0600,0.0380]
###############################################################################
#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
#plt.plot(UnInteraxis,ok,color = 'b', label="Okapi scoring")
#plt.plot(UnInteraxis,U_Oka_stem,color = 'g', label="tf.idf scoring using BM25TF term weighting")


#plt.title("(Query401) Okapi scoring V.S tf.idf scoring using BM25TF term weighting",x=0.5, y=1.03)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)

#plt.xlabel("Interpolated Recall")
#plt.ylabel("Precision Averages")
#plt.legend(loc = "best", fontsize=20)
#plt.show()
#####################################################################################
#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
#plt.plot(Interaxis,ok_,color = 'b', label="Okapi scoring")
#plt.plot(Interaxis,Oka_stem,color = 'g', label="tf.idf scoring using BM25TF term weighting")


#plt.title("(Query401) Okapi scoring V.S tf.idf scoring using BM25TF term weighting",x=0.5, y=1.03)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)

#plt.xlabel("At k docs")
#plt.ylabel("Precision")
#plt.legend(loc = "best", fontsize=20)
#plt.show()
######################################################################################
#plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
#plt.plot(UnInteraxis,ok2,color = 'b', label="Okapi scoring")
#plt.plot(UnInteraxis,U_Oka_nostem,color = 'g', label="tf.idf scoring using BM25TF term weighting")


#plt.title("(Query401)(Without Stemming) Okapi scoring V.S tf.idf scoring using BM25TF term weighting",x=0.5, y=1.03)
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)

#plt.xlabel("Interpolated Recall")
#plt.ylabel("Precision Averages")
#plt.legend(loc = "best", fontsize=20)
#plt.show()
##################################################################
plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
plt.plot(Interaxis,ok2_,color = 'b', label="Okapi scoring")
plt.plot(Interaxis,Oka_nostem,color = 'g', label="tf.idf scoring using BM25TF term weighting")


plt.title("(Query401)(Without Stemming) Okapi scoring V.S tf.idf scoring using BM25TF term weighting",x=0.5, y=1.03)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.xlabel("At k docs")
plt.ylabel("Precision")
plt.legend(loc = "best", fontsize=20)
plt.show()


########################################################
#np.random.seed(100)

#data = np.random.normal(size = (1000, ), loc = 0, scale= 1)


#plt.boxplot(data, sym ="o", whis = 1.5)

#plt.show()

    