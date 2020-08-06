# Title     : pathview demo
# R version : 3.6.3 (2020-02-29)
# Objective : 展示 pathview 库的基本使用方式
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

if (!require(pathview)) {
  BiocManager::install("pathview")
  library(pathview)
}
