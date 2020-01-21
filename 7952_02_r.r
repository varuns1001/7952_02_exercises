Q1
excel_sheets('SaleData.xlsx')
df<-read_excel('SaleData.xlsx',sheet='Sales Data')
item_group<- df %>%group_by(Item)
print(summarise(item_group,min(Sale_amt)))




Q2
excel_sheets('SaleData.xlsx')
df<-read_excel('SaleData.xlsx',sheet='Sales Data')
split<- function(x){
  return(substring(x,1,4))
}
result<-sapply(df$OrderDate,split)
df[,'order_year']<-result
total_sales<- df %>%group_by(Region,order_year)
print(summarise(total_sales,sum(Sale_amt)))




Q3
df<-read_excel('SaleData.xlsx',sheet='Sales Data')
date <- readline(prompt='Enter reference year in format month(abr)-day-year(4 digits)')
ref.date <- as.Date(date,format="%b-%d-%Y")
diff <- function(x){
  return(as.Date(x)-ref.date)
}
result<- sapply(df$OrderDate,diff)
df[,'days_diff']<-result








Q4
excel_sheets('SaleData.xlsx')
df<-read_excel('SaleData.xlsx',sheet='Sales Data')
new_df<-df %>% group_by(Manager)%>% summarise(list_of_salesman=list(unique(SalesMan)))
print(new_df)


Q5
excel_sheets('SaleData.xlsx')
df<-read_excel('SaleData.xlsx',sheet='Sales Data')
new_df<- df %>% group_by(Region) %>% summarise(salesmancount=length(unique(SalesMan)),total_sales=sum(Sale_amt))
print(new_df)





Q6
excel_sheets('SaleData.xlsx')
df<-read_excel('SaleData.xlsx',sheet='Sales Data')
new_df<- df %>% group_by(Manager) %>% summarise(percentsale=(sum(Sale_amt)*100)/1305676)
print(new_df)



Q7
df<-read.csv('imdb.csv')
print(df[5,])


Q8
df<-read.csv('imdb.csv')
title_of_max<-df %>% filter(duration==max(as.numeric(as.character(duration)),na.rm=T))%>%select(title)
title_of_min<-df %>% filter(duration==min(as.numeric(as.character(duration)),na.rm=T))%>%select(title)
print(title_of_max)
print(title_of_min)


Q9
df<-read.csv('imdb.csv')
new_df<- arrange(df,year,desc(imdbRating))

print(new_df)


Q10df<-read.csv('imdb.csv')
new_df<- filter(df,(as.numeric(as.character(duration))/60 > 30),(as.numeric(as.character(duration))/60 < 180))

print(new_df)




Bonus Question
1.
df<-read.csv('imdb.csv')
pd<- data.frame()
df1<-data.frame()

print(class(df$imdbRating))

pd <-df %>% group_by(year,type) %>% summarise(avg_rating=mean(as.numeric(as.character(imdbRating)),na.rm=TRUE))
df1 <-df %>% group_by(year,type) %>% summarise(min_rating=min(as.numeric(as.character(imdbRating)),na.rm=TRUE))
pd[,'min_rating']<-df1$min_rating


df1 <-df %>% group_by(year,type) %>% summarise(max_rating=max(as.numeric(as.character(imdbRating)),na.rm=TRUE))
pd[,'max_rating']<-df1$max_rating


df1 <-df %>% group_by(year,type) %>% summarise(total_runtime=sum(as.numeric(as.character(duration)),na.rm=TRUE))
pd[,'total_runtime']<-df1$total_runtime
df1 <-df %>% group_by(year,type) %>% summarise_if(is.numeric,funs(sum),na.rm=T)
l=list()
for(i in 1:nrow(df1)){
  v<- c()
  for(j in 5:32){
    if(df1[i,j]>0 & (!is.na(df1[i,j]))){
      v <- c(v,colnames(df1)[j])
    }
  }
  l[[i]]=v
  
}

pd[,'genre_combo']<- list(l)
pd[pd=='NULL']<- NA
print(pd)




Q11
df<-read.csv('diamonds.csv')
new_df <- df %>% group_by(carat,cut,color,clarity,depth,table,price,x,y,z) %>% summarise(repeatrows=length(cut))
duplicate_rows<- nrow(filter(new_df,repeatrows > 1))
print(duplicate_rows)


Q13
df<-read.csv('diamonds.csv')
new_df=df[,sapply(df,is.numeric)]
print(new_df)




Q14
df<-read.csv('diamonds.csv')
fd=data.frame(index=rownames(df))
fd['x']<-df['x']

fd[,'volume']<-fd$x*fd$y*fd$zfloat
for(i in 1:nrow(fd)){
  if(fd[i,'depth']<60){
    fd[i,'volume']=8
  }
}
print(fd)

Q15
df<-read.csv('diamonds.csv')
df$price[is.na(df$price)]<-mean(df$price,na.rm=TRUE)
print(df)


