import pandas as pd

# Define the columns
columns = ['Ref','Year', 'Subjects' , 'Treatment methods' , 'Evaluation tools', 'Age', 'Biomarker', 'Treatment Response' , 'Metric Evaluation', 'Supplementary information']

# Create a DataFrame with the specified columns
df = pd.DataFrame(columns=columns)

# Enter information for two rows


df.loc[1] = ['06','2022', '175' , 'viloxazine extended-release' , 'machine learning LASSO model', '18-60 years', 'Dose,Age,Body weight,BMI,CGI-I score,AISRS Total score', '≥50% , AISRS', 'Sen = 80%,Spec = 74%']
df.loc[2] = ['12','2016', '75' , 'MPH' , 'LR', '6-17 years', 'GRIN2B rs2284411 genotype', '≥40% ,ADHD-RS', 'OR = 4.35,p = 0.023']
df.loc[3] = ['17','2015', '83' , 'MPH' , 'SVM', '9.5 ± 2.6 years', 'ODD', 'ADHD-RS-IV', 'Acc = 84.6%,AUC = 84%']
df.loc[4] = ['20','2014', '95' , 'ATX' , 'ANCOVA', '7-12 years', 'TMS-SICI', 'ADHD-RS,CGI', 't(41) = 2.88, p = .0063']
df.loc[5] = ['24','2014', '250' , 'MPH' , 't-test,linear regression', '≥ 18 years', 'higher severity', 'SNAP-IV', 't = 14.298 , b = 0.77 , p < 0.001']
df.loc[6] = ['32','2011', '125' , 'MPH' , 't-test', '5-17 years', 'combined subtype\ncomorbidity with ODD\nlevels of maternal ADHD symptoms', 'SNAP-IV', 'p < 0.001\np = 0.03\np < 0.001']
df.loc[7] = ['33','2010', '571' , 'ATX' , 'CART', 'Children', '-', '≥25% ,ADHD-RS', 'PPV = 77.9%,NPV = 77.5%']
df.loc[8] = ['35','2009', '88' , 'MPH' , 'LR', '6-18 years', 'response time variability', 'ADHD-RS', 'R^2  = 0.136 ,  p < 0.01']
df.loc[10] = ['45','1999', '36' , 'MPH' , 'MANOVA', '7-11 years', 'Hyperactivity at school\nAge', 'ADHD-RS', ' p = 0.015\np = 0.042']
df.loc[11] = ['47','2024', '146(72 SMR training ,15 TBR training,59 MPH )' , 'NF,MPH' , 't-test', '7-13 years', 'BRIEF global score(SMR training)\nBRIEF global score(MPH)\nCPT commission errors(MPH)  \nhit reaction time variability(MPH)', 'ADHD-RS', 't(67) = 4.41,p < 0.001\nt(55) = 6.81, p < 0.001\nt(58) = 6.24, p < 0.001\nt(53) = 3.79, p < 0.001']
df.loc[12] = ['51','2022', '145 ADHD\n83 HC' , 'MPH' , 'pearson correlation', '8.9 ± 2.2 years', 'miR-140-3p\nmiR-27a-3p\nmiR-486-5p\nmiR-151-5p', '≥30%,ADHD-RS', ' r = 0.354, p = 0.012\nr = 0.432, p = 0.002\nr = 0.395, p = 0.005\nr = 0.304, p = 0.032']
df.loc[14] = ['59','2019', '123' , 'MPH' , 't-test', '≥ 18 years', 'Variability\nSkewness', 'CGI-I rating ≤ 2 and ADHD-RS ≤ 18', 'p = 0.038\np = 0.02 ']
df.loc[15] = ['62','2021', '1397' , 'viloxazine extended-release' , 'machine learning LASSO regression', '6-17 years', 'ADHD-RS-5 Total score and CGI-I score', '≥50% , ADHD-RS', 'Sen = 80%,Spec = 74%']
df.loc[16] = ['69','2016', '564' , 'MPH' , 'LR', 'Adults' , 'rs1800544 in ADRA2A', '2 questionnaires', 'p = 0.033']
df.loc[17] = ['70','2017', '157' , 'MPH' , 'machine learning  GPR and SVM', '6-17 years' , '-', 'SNAP-IV', 'AUC = 75–77%']
df.loc[18] = ['75','2014', '43' , 'MPH' , 'SVM', '-' , 'Parents’ ADHD Conner’s score', '-', 'Acc = 77%']
df.loc[19] = ['77','2012', '345' , 'MPH' , 'LR', '6-15 years' , 'LD\n\nODD/CD', '≥25%,CPRS\n≥25%,CTRS', 'b = 0.75\nb = 0.44,p<0.01\nb = 0.53,p<0.05\nb = 0.47,p<0.01']
df.loc[20] = ['79','2009', '618' , 'ATX' , 'LR', '6-18 years', 'ADHD-RS-Parent Version', '≥25% ,ADHD-RS', 'Sen = 81%,Spec = 72%']
df.loc[21] = ['87','2023', '148' , 'MPH' , 'linear regression', '10-16 years', 'sex\nage\ncomorbidity', '≥40% ,ADHD-RS', 'β = 0.177,p =  0.024\nβ = − 0.237,p = 0.002\nβ = 0.181,p =  0.029']
df.loc[22] = ['88','2020', '73' , 'cognitive training ' , 'Post-hoc tests', '5-9 years', 'Working memory test\nFlanker accuracy incongruent trials\nFlanker reaction time\nNo-Go trial accuracy', '≥30%,SNAP-IV', 'p = 0.009\np = 0.02\np = 0.003\np = 0.01']
df.loc[23] = ['98','2016', '223' , 'MPH' , 'multivariate LR', '6-15' , 'Maternal ASRS Anxiety/Depression', '≥25%,CPRS or CTRS', 'OR = .95,p < 0.05']
df.loc[24] = ['102','2012', '103' , 'MPH' , 'multivariate LR', '9.1 ± 2.1 years' , 'NE	 G1287A\nDAT1 VNTR × NET1 G1287A\nDRD4 VNTR·ADRA2A MspI\nADRA2A DraI · NET1 G1287A', '≥50%,ADHD-RS', 'β = - 0.564,p = 0.012\nβ = 0.72,p = 0.026\nβ = -0.419,p = 0.045\nβ = 0.517,p = 0.029']
df.loc[25] = ['109','2018', '158' , 'MPH' , 'LR', '7-11 years' , 'SCT Sluggish/sleepy factor\nSluggish/sleepy×dose', 'VADPRS,VADTRS', 'p = 0.04\np = 0.004', '-']
df.loc[26] = ['110','2018', '71' , 'vitamin-mineral' , 'LR', '7-12 years' , 'Folate\nB12', '≥30% ,ADHD-RS subscales', 'β = −0.079,p =  0.03\nβ = −0.004,p =  0.026', '10-week']
df.loc[27] = ['114','2019', '518 ' , 'MPH' , 'LR', '11.4 ± 3.3 years' , 'ODD score\nTotal IQ\ncommission errors', '≥30% ,ADHD-RS and CGI-S = 1,2', 'Wald = 4.58,p =  .032\nWald = 4.62,p =  .032\nWald = 3.87,p =  .049']
df.loc[28] = ['115','2020', '43 ' , 'MPH' , 'linear regression', '8-16 years' , 'Emotional dysregulation', 'ADHD-RS', 'p =  .04']
df.loc[29] = ['138','2008', '173' , 'MPH' , 'chi-square', 'Children' , 'Val-allele\nVal/Val genotype', '≥30% ,ADHD-RS and CGI-S rating ≤ 2', 'χ^2  = 6.87,p = 0.009\nχ^2  = 6.78,p = 0.034']
df.loc[30] = ['143','2007', '83' , 'MPH' , 'chi-square', '7-12 years' , '4-repeat allele at DRD4', '>50% ,ADHD-RS', 'χ^2  = 12.926,df = 1,p < 0.01']
df.loc[31] = ['145','1995', '52' , 'MPH' , 'MANOVA', '6-13 years' , 'inattentiveness at school\nage\nSeverity of disorder\nanxiety at home', 'CTRS,CPRS', 'p = 0.038\np = 0.02\np = 0.019\np = 0.02']



# Save the DataFrame to an Excel file
df.to_excel('dataframe_output_clinicalp.xlsx', index=False)

print("DataFrame is saved as 'dataframe_output.xlsx'.")



# Display the DataFrame
print(df)


