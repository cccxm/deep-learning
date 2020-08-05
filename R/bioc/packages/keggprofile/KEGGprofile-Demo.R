# Title     : KEGGprofile Demo
# R version : 3.6.3 (2020-02-29)
# Objective : 展示KEGGprofile库的基本使用方式
# Created by: chen
# Created on: 2020/8/5
if (!require(stringr)) {
  install.packages('stringr')
  library(stringr)
}
if (!stringr::str_detect(getwd(), '.temp')) {
  setwd(paste(getwd(), 'R', 'bioc', 'packages', 'keggprofile', '.temp', sep = '/'))
}

options(repos = structure(c(CRAN = "https://mirror.lzu.edu.cn/CRAN/")))

if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

options(BioC_mirror = "https://mirrors.tuna.tsinghua.edu.cn/bioconductor")

if (!require(KEGGprofile)) {
  BiocManager::install("KEGGprofile")
  library(KEGGprofile)
}
##########
# col_by_value Demo
##########
data(pho_sites_count) # pho_sites_count是一个6374*1的Double矩阵
head(pho_sites_count)
#    pho.sites.number
#2                 1
#16                5
#20                1
#22                5
#23                8
#27                9
head(rownames(pho_sites_count))
#[1] "2"  "16" "20" "22" "23" "27"
col <- col_by_value(x = pho_sites_count, col = c('white', 'green', 'black'), breaks = c(0, 5, 8, Inf))
head(col)
#   [,1]
#2  "white"
#16 "white"
#20 "white"
#22 "white"
#23 "green"
#27 "black"

##########
# convertId - Demo
##########
temp <- cbind(rnorm(10), rnorm(10)) # matrix 10*2
row.names(temp) <- c("Q04837", "P0C0L4", "P0C0L5", "O75379", "Q13068",
                     "A2MYD1", "P60709", "P30462", "P30475", "P30479")
colnames(temp) <- c('Exp1', 'Exp2')
head(temp)
#              Exp1        Exp2
#Q04837 -0.49204685 -0.71231288
#P0C0L4 -0.07584076  0.67255037
#P0C0L5 -0.59569305 -0.71189653
#O75379  1.84496906  1.67716858
#Q13068 -0.90369581  0.08408228
#A2MYD1 -0.81876488  0.35165130
convertId(temp, keepMultipleId = T, verbose = T)
# Not run

##########
# download_KEGGfile - demo
##########
download_KEGGfile(pathway_id = '04110', species = 'hsa') # 智人 - 细胞周期相关通路

##########
# parse_XMLfile - demo
##########
gene_data <- parse_XMLfile(pathway_id = '04110', species = 'hsa')
head(gene_data)
#      [,1]    [,2]  [,3]  [,4] [,5] [,6]
#[1,] "1029"  "532" "124" "46" "17" "CDKN2A"
#[2,] "51343" "919" "536" "46" "17" "FZR1"
#[3,] "4171"  "553" "556" "46" "17" "MCM2"
#[4,] "4172"  "553" "556" "46" "17" "MCM2"
#[5,] "4173"  "553" "556" "46" "17" "MCM2"
#[6,] "4174"  "553" "556" "46" "17" "MCM2"

##########
# plot_profile - demo
##########
data(pro_pho_expr)
gene_data <- parse_XMLfile(pathway_id = '04110', species = 'hsa')
out <- plot_profile(pro_pho_expr, pathway_name = 'hsa04110',
                    line_col = c('red', 'blue'),
                    KEGG_database = gene_data,
                    groups = c(rep("Proteome ", 6), rep("Phosphoproteome ", 6)),
                    magnify = 1.2, max_dist = 5)

# TODO other functions