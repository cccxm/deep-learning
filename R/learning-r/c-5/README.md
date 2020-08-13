# Chapter 5 - Lists and Data Frames

章节目标

- **能够**创建list和data.frame
- **能够**使用`length`,`names`以及一些其他的检查和操作这些变量的函数

- **理解**什么是`NULL`以及如何使用它
- **理解**递归变量和原子变量的不同
- **了解**关于list和data.frame的基本操作

[TOC]

## Lists

List可以理解为其中元素类型可以不同的向量。

### 创建链表

使用`list`函数可以创建一个链表。

~~~R
> my_list <- list(c(1,2,3),matrix(c(1,2,3,4),nrow = 2))
> my_list
[[1]]
[1] 1 2 3

[[2]]
     [,1] [,2]
[1,]    1    3
[2,]    2    4
~~~

和向量不同的是，链表中不会合并数据。

使用`names`函数可以给链表中的元素命名。

~~~R
> names(my_list) <- c('vector','matrix')
> my_list
$vector
[1] 1 2 3

$matrix
     [,1] [,2]
[1,]    1    3
[2,]    2    4
~~~

除了使用`names`函数外，也可以在链表创建时指定名称

~~~R
> my_list <- list(
+   vector=c(1,2,3),
+   matrix=matrix(1:4,nrow = 2)
+ )
> my_list
$vector
[1] 1 2 3

$matrix
     [,1] [,2]
[1,]    1    3
[2,]    2    4
~~~

### 原子变量和递归变量

由于链表的特性，链表中的元素仍然可以是一个链表，所以链表可以被认为是一个可递归的变量。

使用`is.atomic`和`is.recursive`函数可以判断变量的类型

~~~R
> is.atomic(list())
[1] FALSE
> is.atomic(numeric())
[1] TRUE
~~~

### 链表的长度与运算

链表的长度只与它顶层元素的数量有关。

~~~R
> length(my_list)
[1] 2
~~~

链表不能像矩阵那样测量维度，行数，列数等信息，但是提供了一个类似名称的函数。

~~~R
> nrow(my_list)
NULL
> NROW(my_list)
[1] 2
> NCOL(my_list)
[1] 1
~~~

木的灵魂的两个函数。

**关于运算**：链表不能像向量一样直接在其对象上运算。

~~~R
> 1:4 + 2:5
[1] 3 5 7 9
> list(c(1:4))+list(c(2:5))

# Error in list(c(1:4)) + list(c(2:5)): 二进列运算符中有非数值参数
~~~

直接在链表上的运算会提示错误。

需要将待运算的数据转换成向量之后才能正常运算结果。例如

~~~R
> list(c(1:4))[[1]]+list(c(2:5))[[1]]
[1] 3 5 7 9
~~~

### 链表的索引操作

假设链表结构如下

~~~R
> my_list <- list(
+   first = 1,
+   second = 2,
+   thrid = list(
+     alpha = 3.1,
+     beta = 3.2
+   )
+ )
~~~

与向量操作类似，可以直接使用方括号形式的索引获取元素。

~~~R
> my_list[1:2]
$first
[1] 1

$second
[1] 2

> my_list[-3]
$first
[1] 1

$second
[1] 2

> my_list['first']
$first
[1] 1

> my_list[c(T,F,F)]
$first
[1] 1
~~~

**注意：**以上通过索引方式获取的对象仍然是个链表。如果我们需要获取对应的内容，则需要使用双重中括号。

~~~R
> typeof(my_list[1])
[1] "list"
> typeof(my_list[[1]])
[1] "double"
~~~

除了使用`typeof`输出类型的名称，还可以用逻辑运算函数`is.list`来判断当前是否是链表类型。

除了使用方括号索引获取对象，还可以使用`$`加名称查找对应的元素，**注意**：只要表示唯一，可以使用名字的简写。

~~~R
> l <- list(
+   same1 = 1:4,
+   same2 = 5:8,
+   other = 9:12
+ )
> l$other
[1]  9 10 11 12
> l$o
[1]  9 10 11 12
> l$same
NULL
~~~

`$`符号的作用是取值，等价于双重中括号

~~~R
> typeof(l['other']) == typeof(l$other)
[1] FALSE
> typeof(l[['other']]) == typeof(l$other)
[1] TRUE
~~~

### 链表和向量的转换

`as.*`函数可以实现类型的转换。

~~~R
> as.list(1:4)
[[1]]
[1] 1

[[2]]
[1] 2

[[3]]
[1] 3

[[4]]
[1] 4

> as.vector(list(1:4))
[[1]]
[1] 1 2 3 4

> as.vector(list(a=1:2,b=3:4))
$a
[1] 1 2

$b
[1] 3 4

> unlist(list(a=1:2,b=3:4))
a1 a2 b1 b2 
 1  2  3  4 
~~~

### 链表的拼接

`c`函数可以应用于链表表示拼接。使用方式如下

~~~R
> com_list <- c(list(1:3), 4)
> com_list
[[1]]
[1] 1 2 3

[[2]]
[1] 4

> typeof(com_list)
[1] "list"
~~~

使用矩阵函数`cbind`或者`rbind`同样可以实现链表的拼接

~~~R
> cbind(
+   list(a = 1, b = 2),
+   list(c = 3, d = 4)
+ )
  [,1] [,2]
a 1    3   
b 2    4   
> rbind(
+   list(a = 1, b = 2),
+   list(c = 3, d = 4)
+ )
     a b
[1,] 1 2
[2,] 3 4
~~~

## Data Frame

数据框是一种表格结构的对象，与矩阵类似，但不要求类型相同。

### 创建数据框对象

使用`data.frame`函数就可创建一个数据框对象。

~~~R
> data.frame(
+   x = 1,
+   y = 2:3,
+   z = 4:7
+ )
  x y z
1 1 2 4
2 1 3 5
3 1 2 6
4 1 3 7
~~~

### 基本的数据框操作

**转置**

~~~R
> df <- data.frame(
+   x = 1,
+   y = 2:3,
+   z = 4:7
+ )
> df
  x y z
1 1 2 4
2 1 3 5
3 1 2 6
4 1 3 7
> t(df)
  [,1] [,2] [,3] [,4]
x    1    1    1    1
y    2    3    2    3
z    4    5    6    7
~~~

**列合并**

将一个数据框追加到另一个数据框的右侧

~~~R
> df1 <- data.frame(
+   x = 1,
+   y = 2:3,
+   z = 4:7
+ )
> df2 <- data.frame(
+   a = letters[1:4],
+   b = letters[5:8]
+ )
> cbind(df1, df2)
  x y z a b
1 1 2 4 a e
2 1 3 5 b f
3 1 2 6 c g
4 1 3 7 d h
~~~

**行合并**

将两个数据框按照行扩展的方式追加

~~~R
> df1 <- data.frame(
+   x = 1,
+   y = 2:3,
+   z = 4:7
+ )
> df2 <- data.frame(
+   x = 1:3,
+   y = 4:6,
+   z = 7:9
+ )
> rbind(df1, df2)
  x y z
1 1 2 4
2 1 3 5
3 1 2 6
4 1 3 7
5 1 4 7
6 2 5 8
7 3 6 9
~~~

**有条件合并**

~~~R
> df1 <- data.frame(
+   names = c('apple', 'orange'),
+   price = c(6.9, 8.9)
+ )
> df2 <- data.frame(
+   names = c('apple', 'orange'),
+   color = c('red', 'orange')
+ )
> merge(df1, df2, by = 'names')
   names price  color
1  apple   6.9    red
2 orange   8.9 orange
~~~

