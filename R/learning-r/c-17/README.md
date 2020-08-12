# 17 - Making Packages

**章节目标**

- **能够**创建R包
- **了解**如何为函数和数据集编写文档
- **能够**将R包发布到CRAN

[TOC]

## R包目录结构

**必要的文件**

- ***DESCRIPTION*** - 文本文件，包含详细的信息，包括版本，作者以及此包的作用等。

- ***NAMESPACE*** - 文本文件，描述哪些函数是用户可使用的。

**一些可选的文件**

- ***LICENSE or LICENCE*** - 指名该包遵守的协议
- ***NEWS*** - 包升级时指名详细的更新信息
- ***INDEX*** - 所有包中可用对象的名称和描述信息



**必要的目录**

- ***R*** - 包含R代码
- ***man*** - 包含 帮助 文件

**可选的文件夹**

- ***src*** - 包含C/C++等的其他语言代码
- ***demo*** - 包含可运行的demo示例
- ***vignettes*** - 包含长的说明文档，用于详细解释包的使用，通过命令`browseVignettes`查看
- ***doc*** - 存放其他格式的说明文档
- ***data*** - 包含data数据
- ***inst*** - 存放其他文件

## 自动的说明文档

~~~R
#' 函数或数据集的标题，单独一行
#' (空一行)
#' 详细的函数功能说明，可以跨越多行
#' @param param_name description,可以跨越多行
#' @return 返回数据说明,可以跨越多行
#' @note 提示信息，可以跨越多行
#' @autor 作者名
#' @references 引用信息，可以跨越多行，such as
#' \url{http://.......}
#' @seealso Link to functions in the same pakcage with
#' \code{\link{other_function_or_dataset}}
#' @example
#' @import pkg
#' @importFrom pkg function
#' @export
~~~

之后调用devtools生成说明文档并打包

~~~R
devtools::document()
devtools::build()
~~~

打包成功之后使用本地安装

~~~R
install.packages('MyPack_0.0.1.tar.gz',
                 repos = NULL,
                 type = 'source')
library(MyPack)
~~~

