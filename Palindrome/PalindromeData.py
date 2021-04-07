# Assignment started 2021/04/07 13:40

import pandas as pd

# create dataframe and open .txt file to write results
results = open('results.txt', 'w')
results.write("My results:\n")
df = pd.read_excel('pone.0212445.s004.xlsx', header=1)

# calculations for totals by 'Survey' results
total_NoPLHIV = sum(df[df["Estimate"]=="Survey"]["NoPLHIV"])
print(f"Total NoPLHIV: {total_NoPLHIV}")
results.write(f"Total NoPLHIV: {total_NoPLHIV}\n")

total_NoPLHIV_LCL = sum(df[df["Estimate"]=="Survey"]["NoPLHIV_LCL"])
print(f"Total NoPLHIV lower estimate: {total_NoPLHIV_LCL}")
results.write(f"Total NoPLHIV lower estimate: {total_NoPLHIV_LCL}\n")

total_NoPLHIV_UCL = sum(df[df["Estimate"]=="Survey"]["NoPLHIV_UCL"])
print(f"Total NoPLHIV upper estimate: {total_NoPLHIV_UCL}")
results.write(f"Total NoPLHIV upper estimate: {total_NoPLHIV_UCL}")

# calculations for averages for 'Xhariep' with sum/len
main_Xhariep = (df[df["District"]=="Xhariep"]["NoPLHIV"])
avg_Xhariep = sum(main_Xhariep)/len(main_Xhariep)
print(f"Average in Xhariep: {avg_Xhariep}")
results.write(f"Average in Xhariep: {avg_Xhariep}")

lower_Xhariep = (df[df["District"]=="Xhariep"]["NoPLHIV_LCL"])
avg_Xhariep_lcl = sum(lower_Xhariep)/len(lower_Xhariep)
print(f"Average in Xhariep lower estimate: {avg_Xhariep_lcl}")
results.write(f"Average in Xhariep lower estimate: {avg_Xhariep_lcl}")

upper_Xhariep = (df[df["District"]=="Xhariep"]["NoPLHIV_UCL"])
avg_Xhariep_ucl = sum(upper_Xhariep)/len(upper_Xhariep)
print(f"Average in Xhariep upper estimate: {avg_Xhariep_ucl}")
results.write(f"Average in Xhariep upper estimate: {avg_Xhariep_ucl}")

#output new CSV file with new Column
df["Non_HIV"]=round(df["NoPLHIV"]/df["Prevalence_%"]*(100-df["Prevalence_%"]))
df.to_csv('Pone_output.csv', index=False)

# create subset dataframes for cities and metros, but separate 'Survey' and 'Fay' totals
sub_df = df[df['Estimate']=="Survey"]

cities_total = sum(sub_df[sub_df["District"].str.contains('City|Metro')]["NoPLHIV"])
print(f"Cities and Metros total by survey: {cities_total}")
results.write(f"Cities and Metros total by survey: {cities_total}")

sub_df = df[df['Estimate']!="Survey"]

cities_total = sum(sub_df[sub_df["District"].str.contains('City|Metro')]["NoPLHIV"])
print(f"Cities and Metros total by Fay-Harriot: {cities_total}")
results.write(f"Cities and Metros total by Fay-Harriot: {cities_total}")


# Assignment completed 2021/04/07 15:54
# total time spent: 2h14m
