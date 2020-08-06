# Title     : KEGGprofile Demo
# R version : 3.6.3 (2020-02-29)
# Objective : 展示KEGGprofile库的基本使用方式
# Created by: chen
# Created on: 2020/8/5
options(repos = structure(c(CRAN = "https://mirror.lzu.edu.cn/CRAN/")))
if (!require(stringr)) {
  install.packages('stringr')
  library(stringr)
}
if (!stringr::str_detect(getwd(), '.temp')) {
  setwd(paste(getwd(), 'R', 'bioc', 'packages', '.temp', sep = '/'))
}
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

##########
# find_enriched_pathway - demo
##########
data(pho_sites_count)
head(pho_sites_count)
#    pho.sites.number
#2                 1
#16                5
#20                1
#22                5
#23                8
#27                9
genes <- names(rev(sort(pho_sites_count[, 1]))[1:300])
head(genes)
#[1] "23524" "10250" "4288"  "79026" "7158"  "85456"
pho_KEGGresult <- find_enriched_pathway(genes, species = 'hsa')
head(pho_KEGGresult$stastic)
#        Pathway_Name Gene_Found Gene_Pathway Percentage       pvalue    pvalueAdj
#03013 RNA transport         17          152       0.11 9.057606e-13 2.074192e-10
#03040   Spliceosome         13          128       0.10 1.247701e-09 1.428618e-07
head(pho_KEGGresult$detail)
# $`03013`
# [1] "10250"  "11218"  "129401" "1975"   "1978"   "1981"   "22985"  "4928"
# [9] "5411"   "55746"  "57122"  "57187"  "5903"   "7175"   "8021"   "9669"
# [17] "9972"
# $`03040`
# [1] "10772" "10992" "22985" "23350" "23451" "27316" "29896" "3183"  "3192"
# [10] "55119" "57187" "6432"  "6434"


##########
# newIdMatrix - demo
##########
convertIdTable <- paste("New", c(1, 2, 2, 2, 1, 3, 4, 4, 5, 5))
names(convertIdTable) <- paste("Old", seq_along(convertIdTable))
head(convertIdTable)
#  Old 1   Old 2   Old 3   Old 4   Old 5   Old 6
#"New 1" "New 2" "New 2" "New 2" "New 1" "New 3"
temp <- matrix(rnorm(20), ncol = 2)
row.names(temp) <- names(convertIdTable)
colnames(temp) <- c("Exp1", "Exp2")
head(temp)
#            Exp1        Exp2
#Old 1 -0.9084028  0.18392728
#Old 2  1.1840826  0.64861437
#Old 3  1.3898440  0.50067203
#Old 4 -0.2399096  0.62827512
#Old 5  0.8192186 -0.55391576
#Old 6 -0.3073348  0.09491983
new_temp <- newIdMatrix(temp, convertIdTable, genesKept = "foldchange")
new_temp
#            Exp1        Exp2
#New 1  0.8192186 -0.55391576
#New 2  1.3898440  0.50067203
#New 3 -0.3073348  0.09491983
#New 4 -0.6787377 -0.05339891

##########
# pho_sites_count
##########
data(pho_sites_count)
head(pho_sites_count)
#    pho.sites.number
#2                 1
#16                5
#20                1
#22                5
#23                8
#27                9

##########
# plot_pathway_cor
##########
data(pro_pho_expr)
data(pho_sites_count)
genes <- row.names(pho_sites_count)[which(pho_sites_count >= 10)]
pho_KEGGresult <- find_enriched_pathway(genes, species = 'hsa')
result <- plot_pathway_cor(gene_expr = pro_pho_expr, kegg_enriched_pathway = pho_KEGGresult)
head(result)
#                   DNA replication                     RNA transport
#                       0.08767729                        0.07181928
#   Ubiquitin mediated proteolysis                        Cell cycle
#                       0.29992077                        0.72446442
#Ribosome biogenesis in eukaryotes                       Spliceosome
#                       0.43376060                        0.05778624

##########
# plot_pathway_overall
##########
data(pro_pho_expr)
data(pho_sites_count)
gene_values <- pro_pho_expr[row.names(pho_sites_count)[which(pho_sites_count >= 10)],]
plot_pathway_overall(gene_values = gene_values[, 1:3])