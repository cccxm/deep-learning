# BIOC包：'pathview'

> 标题：用于基于路径的数据集成和可视化的工具集。
>
> 维护者：Weijun Luo luo_weijun@yahoo.com
>
> 描述：Pathview是用于基于路径的数据集成和可视化的工具集。 它在相关路径图上绘制并绘制了多种生物学数据。 所有用户需要的是提供他们的数据并指定目标途径。Pathview会自动下载路径图数据，解析数据文件，将用户数据映射到路径，并使用映射的数据渲染路径图。此外，Pathview还无缝集成了途径和基因集（富集）分析工具，以进行大规模和全自动分析。
>
> 首页地址：http://www.bioconductor.org/packages/release/bioc/html/pathview.html

[TOC]

## API documents

### data: cpd.accs

> 化合物或基因ID与KEGG accession之间的映射数据

~~~R
> head(cpd.accs)
#   COMPOUND_ID        SOURCE                    TYPE ACCESSION_NUMBER
# 1         495 KEGG COMPOUND KEGG COMPOUND accession           C00641
# 2           4 KEGG COMPOUND KEGG COMPOUND accession           C07721
# 3           7 KEGG COMPOUND     CAS Registry Number         498-15-7
# 4           7 KEGG COMPOUND KEGG COMPOUND accession           C11382
# 5          12 KEGG COMPOUND KEGG COMPOUND accession           C03036
# 6          14 KEGG COMPOUND     CAS Registry Number         464-43-7
~~~

~~~R
> head(cpd.names)
#     COMPOUND_ID    TYPE        SOURCE                         NAME ACCESSION_NUMBER
#4507        5585    NAME KEGG COMPOUND                          H2O           C00001
#4506        5585 SYNONYM KEGG COMPOUND                        Water           C00001
#3304        2359    NAME KEGG COMPOUND                          ATP           C00002
#3303        2359 SYNONYM KEGG COMPOUND    Adenosine 5'-triphosphate           C00002
#8643        7422    NAME KEGG COMPOUND                         NAD+           C00003
#8639        7422 SYNONYM KEGG COMPOUND Diphosphopyridine nucleotide           C00003
~~~



### fun: combineKEGGnodes

> `CombineKEGGnodes`在KEGG路径图中将节点合并为一组。 

~~~R
function(nodes, graph, combo.node)
    # nodes - str: 要合并的名字的名字
	# graph - object of 'graphNEL': KEGG通路图的解析图
    # combo.node - str: 合并后节点的名字
~~~

`CombineKEGGnodes`不仅可以合并图形对象中的节点，还可以合并KEGG通路对象中的相应节点数据。此功能对于KEGG定义的参与同一反应的组节点和已解析的酶组是必需的。

**Value** - object of '`graphNEL`': `CombineKEGGnodes`返回的结果是`graphNEL`类的组合图。 

### fun: reaction2edge

> `reaction2edge`将反应转换为KEGG通路图中的边。

~~~R
function(path, gR)
    # gR - object of 'graphNEL': 转换自KEGG通路图的解析图
    # path - object of 'KEGGPathway': 解析过的KEGG通路图
~~~

 `reaction2edge`将反应转换为底物和酶以及酶和产物之间的两个连续边缘。需要此功能以在KEGG通路的Graphviz样式视图中忠实地显示复合酶节点及其相互作用。

**Value** - list: `reaction2edge`返回的结果是3个元素的列表：`gR`-转换后的图形(`graphNEL`); `edata.new`-新的边缘数据(`KEGGEdge`); `ndata.new`-新的节点数据(`KEGGNode`)。

### fun: node.color

> 在路径图上将分子数据编码为伪色。node.color将映射的分子（基因，蛋白质或代谢物等）数据转换为路径节点上的伪色。 col.key在路径图上绘制用于映射分子数据的颜色键。

~~~R
function(plot.data = NULL, discrete = FALSE, limit = 1, bins = 10, both.dirs = TRUE, low = "green", mid = "gray", high = "red", na.col = "transparent", trans.fun = NULL)
    # plot.data - data.frame:node.map函数返回的结果。它是一个data.frame，由解析的KGML数据和每个映射节点的摘要分子数据组成。行是映射的节点，列是经过解析或映射的节点数据
    # discrete - logical: 是否将分子数据或节点摘要数据视为离散数据
    # limit - list of number: 以“gene”和“cpd”为名称的两个数字元素的列表。此参数指定将gene.data和cpd.data转换为伪色时的极限值。列表中的每个元素的长度可以为1或2。长度1表示离散数据或1个方向（正值）数据，或2个方向数据的绝对限制。长度2表示2个方向数据。默认 limit = list(gene = 0.5,cpd = 1)
    # bins - list of integer: 以“gene”和“cpd”为名称的两个数字元素的列表。此参数指定将gene.data和cpd.data转换为伪色时的级别或容器的数量。默认 bins = list(gene=10, cpd=10).
    # both.dirs - list of logical: 以“gene”和“cpd”为名称的两个逻辑元素的列表。此参数指定将gene.data和cpd.data转换为伪色时是1向还是2向数据。 默认 both.dirs = list(gene = T, cpd = T)
    # low, mid, high - 颜色名称列表。此参数指定色谱图以编码gene.data和cpd.data。当数据是1方向的（两个目录中均为TRUE值）时，仅使用中和高来指定色谱。 默认数据（低-中-高）的“绿色”-“灰色”-“红色”和“蓝色”-“灰色”-“黄色”分别用于gene.data和cpd.data。 “ low，mid，high”的值可以指定为颜色名称（“red”），绘图颜色索引（2 = red）和HTML样式的RGB（“ \＃FF0000” = red）。
~~~

