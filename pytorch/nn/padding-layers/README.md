# 填充层



## torch.nn.ReflectionPad1d

一维边界对称填充

主要参数：

> **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) : 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding)。**注意：填充尺寸不能超过或等于原始数据长度。**

~~~python
    m = torch.nn.ReflectionPad1d(2)
    input = torch.tensor([[[1, 2, 3, 4]]], dtype=torch.float32)
    print(input)
    # tensor([[[1., 2., 3., 4.]]])
    output = m(input)
    print(output)
    # tensor([[[3., 2., 1., 2., 3., 4., 3., 2.]]])
~~~

## torch.nn.ReflectionPad2d

二维边界对称填充

主要参数

> **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) : 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding)。**注意：填充尺寸不能超过或等于原始数据长度和宽度。**