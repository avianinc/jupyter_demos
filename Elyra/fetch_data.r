# sample R script that rips some data from the web and writes it to a csv file
# data on a sample set from: https://web.cs.ucla.edu/~gulzar/rstudio/basic-tutorial.html

# read in the data
acs <- read.csv(url("http://stat511.cwick.co.nz/homeworks/acs_or.csv"))

# statistical analysis
df <- as.data.frame(summary(acs))

# write dataframe to file (subtract first column with [,-1]
write.csv(df[,-1], "data/dat_from_r.csv", row.names=FALSE)