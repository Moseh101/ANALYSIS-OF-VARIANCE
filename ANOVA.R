#INSTALLING THE REQUIRED LIBRARIES
install.packages("agricolae")
library(agricolae)
install.packages("doebioresearch")
library(doebioresearch)
library(AgroR)
install.packages("AgroR")

#ANOVA FOR EXAMPLE 1
Block <- factor(rep(1:4, each=3))
Treatment <- factor(rep(c("A", "B", "C"), times=4))
Response <- c(10,12,9,15,18,14,12,15,11,18,20,16)
Data=data.frame(Block,Treatment,Response)
Data
Model=aov(Response~Treatment + Block, data=Data)
summary(Model)



#ANOVA FOR EXAMPLE 2
Block2 <- factor(rep(1:5, each=3))
Treatment2 <- factor(rep(c("A", "B", "C"), times=5))
Response2 <- c(18,7,15,19,9,22,16,17,27,35,39,36,2,8,10)
Data2=data.frame(Block2,Treatment2,Response2)
Data2
Model2=aov(Response2~Treatment2 + Block2, data=Data2)
summary(Model2)



