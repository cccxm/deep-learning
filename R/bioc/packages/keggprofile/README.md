# BIOC包：'KEGGprofile'

> 标题：在KEGG通路中用于多重类型(multi-types)和多组数据(multi-groups)的**注释和可视化**包。
>
> 维护者：Shilin Zhao shilin.zhao@vanderbilt.edu
>
> 描述：KEGGprofile是一个注释和可视化工具，能够将表达谱和功能注释集成在KEGG通路图中。 多类型和多组表达数据可以在一个路径图中可视化。 KEGGprofile提供了关于不同基因和样品中特定功能改变内部途径或时间相关性的更详细的分析。
>
> 首页地址：https://www.bioconductor.org/packages/release/bioc/html/KEGGprofile.html

[TOC]

## API documents

### col_by_value

> 该函数会将数据矩阵转换为颜色矩阵，其中颜色表示数字矩阵的值。

函数定义如下：

~~~R
function(x, col, range = NA, breaks = NA, showColorBar = T)
    # x - matrix: 表示value的数字矩阵
    # col - vector: 用于表示value的颜色列表
    # range - vector: 设置value的范围，超出范围的将被截取
    # breaks - vector: 指定对x进行分割的数值向量。
    # showColorBar - logical: 是否显示颜色条
~~~

**注意**：若`breaks`不等于`NA`，则`col`的长度应该等于`breaks-1`，表示按照指定区间填充颜色。

**Value**: 该函数返回值是x矩阵对应的颜色矩阵。该矩阵可以在'plot_profile'函数中使用。

Sample:

~~~R
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
~~~

生成的颜色区间图

![Rplot01 - col_by_value](Rplot01 - col_by_value.png)

### convertId

> 基于'biomatRt'包的ID映射函数

函数定义如下：

~~~R
function(x, dataset = "hsapiens_gene_ensembl", filters = "uniprotswissprot", attributes = c(filters, "entrezgene_id"), genesKept = c("foldchange", "first", "random", "var", "abs"), keepNoId = T, keepMultipleId = F, verbose = F)
    # x - matrix: 表达式矩阵
    # dataset - str: 使用的数据集名称
    # filters - str or list: 设置过滤器，查看所有的过滤器可用函数`biomaRt::listFilters()`
    # attributes - vector: 您要检索的属性。 可以使用`biomaRt::listAttributes()`函数检索可能的属性列表
    # genesKept - vector: 在一个以上的目标中选择目标基因的方法。 “var”-最大变化，“foldchange”-倍数变化，“abs”-绝对值变化，“first”-选择第一目标，“random”-随机选择
    # keepNoId - logical: 是否保留原ID
    # keepMultipleId - logical: 保留多个ID与原ID的相关性
    # verbose - logical: 是否报告进度相关信息
~~~

Sample:

~~~R
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
~~~

### download_KEGGfile

> 此方法将从KEGG站点下载XML文件和原始png文件

~~~R
function(pathway_id = "00010", species = "hsa", target_dir = getwd())
    # pathway_id - str: 通路ID
    # species - str: 物种简称
    # target_dir - str: 本地路径
~~~

**注意**：若`pathway_id	`设置为'all'表示下载KEGG数据库中的全部通路数据。

Sample:

~~~R
download_KEGGfile(pathway_id = '04110', species = 'hsa') # download_KEGGfile(pathway_id = '04110', species = 'hsa')
~~~



![map04110](map04110.png)

### download_latest_pathway

> 该方法会从KEGG站点下载最新的通路基因链接(pathway gene link)

~~~R
function(species)
    # species - str: 物种名称简称
~~~

**Value** - list: 该函数会返回两部分数据。

- keggpathway2gene - 描述每条路径的基因列表
- pathway2name - 描述每条路径的名称列表

### find_enriched_pathway

### newIdMatrix

### parse_XMLfile

> 该函数将会解析KGML文件

~~~R
function(pathway_id, species, database_dir = getwd())
    # pathway_id - str: 通路ID
    # species - str: 物种名称简称
    # database_dir - str: 本地XML文件和png文件路径
~~~

**Value** - matrix: 包含此途径中的基因及其名称位置等的矩阵，可在函数`plot_profile`中用作`KEGG_database`的参数。

Sample:

~~~R
gene_data <- parse_XMLfile(pathway_id = '04110', species = 'hsa')
head(gene_data)
#      [,1]    [,2]  [,3]  [,4] [,5] [,6]
#[1,] "1029"  "532" "124" "46" "17" "CDKN2A"
#[2,] "51343" "919" "536" "46" "17" "FZR1"
#[3,] "4171"  "553" "556" "46" "17" "MCM2"
#[4,] "4172"  "553" "556" "46" "17" "MCM2"
#[5,] "4173"  "553" "556" "46" "17" "MCM2"
#[6,] "4174"  "553" "556" "46" "17" "MCM2"
~~~



### pho_sites_count

### plot_pathway

### plot_pathway_cor

### plot_pathway_overall

### plot_profile

> 在KEGG通路图上绘制基因表达谱

~~~R
function(gene_expr, pathway_name, result_name = paste(pathway_name, "_profile_", type, ".png", sep = ""), KEGG_database, groups, bg_col = "white", text_col = "black", line_col, border_col = "grey", text_cex = 0.25, magnify = 1, type = c("lines", "bg"), pathway_min = 5, genes_kept = c("foldchange", "first", "random", "var", "abs"), species = "hsa", database_dir = getwd(), max_dist, lwd = 1.2, speciesRefMap = TRUE)
    # gene_expr - matrix: 基因表达矩阵，rownames必须是NCBI基因ID，例如67040, 93683
    # pathway_name - str: 物种名和KEGG通路ID，例如’hsa00010’
    # result_name - str: 输出文件名
    # KEGG_database - matrix: 来自‘parse_XMLfile’函数的返回值
    # groups - str or vector: 用于指示不同样本的表达式的字符
    # bg_col - str: 通路图中基因矩形的背景色
    # text_col - str or matrix: 路径图中文本的颜色。在这里可以使用由函数'col_by_value'生成的颜色矩阵 
    # line_col - str or vector: 路线图中不同样本中用于表达的线条颜色，当type=“lines”时有效
    # border_col - str or matrix: 通路图中基因矩形的边框颜色。在这里可以使用由函数`col_by_value`生成的颜色矩阵
    # text_cex - number or matrix: 路径图中文本的CEX。在这里可以使用由函数`col_by_value`生成的颜色矩阵
    # magnify - number: 用于放大基因矩形的系数
    # type - vector: 有两种表示基因表达谱的可视化方法：“bg”和“lines”。第一个仅适用于仅使用一个样本或一种类型的数据进行的分析，该分析将基因多边形划分为几个子多边形以代表不同的时间点。每个子多边形都有特定的背景颜色来表示该时间点的表达式变化。第二种方法在基因多边形中绘制具有不同颜色的线，以表示不同的样本或不同类型的数据。
    # pathway_min - number: 带注释的基因数少于path_min的途径将被忽略
    # genes_kept - vector: 在一个以上的目标中选择目标基因的方法。 “var”-最大变化，“foldchange”-倍数变化，“abs”-绝对值变化，“first”-选择第一目标，“random”-随机选择
    # species - str: 物种名称简称
    # database_dir - str: 本地XML文件和png文件路径
    # max_dist - number: 表达式的变化表示为从基因矩形的底部到顶部的距离，当type=“lines”时有效。此参数用于确保不同基因多边形中的线的动态变化表示相同的变化。默认情况下，将从该途径中基因的最大变化计算得出。如果max_dist = NA，则将在每个基因矩形中从上到下绘制线条
    # lwd - number: line width
    # speciesRefMap - logical: 使用特定物种的图作为参考图。如果设置为FALSE，将使用没有物种信息的参考途径图
~~~

**Value** - matrix: 保存有该通路通路基因map、名称和表达的矩阵。

Sample:

~~~R
data(pro_pho_expr)
gene_data <- parse_XMLfile(pathway_id = '04110', species = 'hsa')
out <- plot_profile(pro_pho_expr, pathway_name = 'hsa04110',
                    line_col = c('red', 'blue'),
                    KEGG_database = gene_data,
                    groups = c(rep("Proteome ", 6), rep("Phosphoproteome ", 6)),
                    magnify = 1.2, max_dist = 5)
~~~

![hsa04110_profile_lines](hsa04110_profile_lines.png)

### pro_pho_expr

