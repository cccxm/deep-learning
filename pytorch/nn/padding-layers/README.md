# 填充层



## torch.nn.ReflectionPad1d

一维边界对称填充

主要参数：

> **padding** (*int*, *tuple*): 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding)。**注意：填充尺寸不能超过或等于原始数据长度。**

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

> **padding** (*int*, *tuple*) : 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding)。**注意：填充尺寸不能超过或等于原始数据长度和宽度。**

~~~python
    m = torch.nn.ReflectionPad2d((1, 2, 1, 2))
    input = torch.tensor([[[[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12]]]], dtype=torch.float32)
    print(input)
    # tensor([[[[ 1.,  2.,  3.,  4.],
    #           [ 5.,  6.,  7.,  8.],
    #           [ 9., 10., 11., 12.]]]])
    output = m(input)
    print(output)
    # tensor([[[[ 6.,  5.,  6.,  7.,  8.,  7.,  6.],
    #           [ 2.,  1.,  2.,  3.,  4.,  3.,  2.],
    #           [ 6.,  5.,  6.,  7.,  8.,  7.,  6.],
    #           [10.,  9., 10., 11., 12., 11., 10.],
    #           [ 6.,  5.,  6.,  7.,  8.,  7.,  6.],
    #           [ 2.,  1.,  2.,  3.,  4.,  3.,  2.]]]])
~~~

## torch.nn.ReplicationPad1d

一维边界重复填充，复制边界元素填充

主要参数

> **padding** (*int*, *tuple*) : 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding)。

~~~python
input = torch.tensor([[[1, 2, 3, 4, 5]]], dtype=torch.float32)
print(input)
# tensor([[[1., 2., 3., 4., 5.]]])

m = torch.nn.ReplicationPad1d(2)
output = m(input)
print(output)
# tensor([[[1., 1., 1., 2., 3., 4., 5., 5., 5.]]])

m = torch.nn.ReplicationPad1d((1, 2))
output = m(input)
print(output)
# tensor([[[1., 1., 2., 3., 4., 5., 5., 5.]]])
~~~

## torch.nn.ReplicationPad2d

二维边界重复填充

主要参数

> **padding** (*int*, *tuple*): 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding)。

~~~python
input = torch.tensor([[[[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 0]]]], dtype=torch.float32)
print(input)
# tensor([[[[1., 2., 3., 4., 5.],
#           [6., 7., 8., 9., 0.]]]])

m = torch.nn.ReplicationPad2d(1)
output = m(input)
print(output)
# tensor([[[[1., 1., 2., 3., 4., 5., 5.],
#           [1., 1., 2., 3., 4., 5., 5.],
#           [6., 6., 7., 8., 9., 0., 0.],
#           [6., 6., 7., 8., 9., 0., 0.]]]])

m = torch.nn.ReplicationPad2d((1, 1, 2, 2))
output = m(input)
print(output)
# tensor([[[[1., 1., 2., 3., 4., 5., 5.],
#           [1., 1., 2., 3., 4., 5., 5.],
#           [1., 1., 2., 3., 4., 5., 5.],
#           [6., 6., 7., 8., 9., 0., 0.],
#           [6., 6., 7., 8., 9., 0., 0.],
#           [6., 6., 7., 8., 9., 0., 0.]]]])
~~~

## torch.nn.ReplicationPad3d

三维边界重复填充

主要参数

> **padding** (*int*, *tuple*): 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding, front padding, back padding)。

~~~python
input = torch.tensor([[[[[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]],
                        [[10, 11, 12],
                         [13, 14, 15],
                         [16, 17, 18]],
                        [[19, 20, 21],
                         [22, 23, 24],
                         [25, 26, 27]]]]], dtype=torch.float32)
print(input)
# tensor([[[[[ 1.,  2.,  3.],
#            [ 4.,  5.,  6.],
#            [ 7.,  8.,  9.]],
#
#           [[10., 11., 12.],
#            [13., 14., 15.],
#            [16., 17., 18.]],
#
#           [[19., 20., 21.],
#            [22., 23., 24.],
#            [25., 26., 27.]]]]])

m = torch.nn.ReplicationPad3d(1)
output = m(input)
print(output)
# tensor([[[[[ 1.,  1.,  2.,  3.,  3.],
#            [ 1.,  1.,  2.,  3.,  3.],
#            [ 4.,  4.,  5.,  6.,  6.],
#            [ 7.,  7.,  8.,  9.,  9.],
#            [ 7.,  7.,  8.,  9.,  9.]],
#
#           [[ 1.,  1.,  2.,  3.,  3.],
#            [ 1.,  1.,  2.,  3.,  3.],
#            [ 4.,  4.,  5.,  6.,  6.],
#            [ 7.,  7.,  8.,  9.,  9.],
#            [ 7.,  7.,  8.,  9.,  9.]],
#
#           [[10., 10., 11., 12., 12.],
#            [10., 10., 11., 12., 12.],
#            [13., 13., 14., 15., 15.],
#            [16., 16., 17., 18., 18.],
#            [16., 16., 17., 18., 18.]],
#
#           [[19., 19., 20., 21., 21.],
#            [19., 19., 20., 21., 21.],
#            [22., 22., 23., 24., 24.],
#            [25., 25., 26., 27., 27.],
#            [25., 25., 26., 27., 27.]],
#
#           [[19., 19., 20., 21., 21.],
#            [19., 19., 20., 21., 21.],
#            [22., 22., 23., 24., 24.],
#            [25., 25., 26., 27., 27.],
#            [25., 25., 26., 27., 27.]]]]])
~~~

## torch.nn.ZeroPad2d

二维数据的零值填充

主要参数

> **padding** (*int*, *tuple*) : 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding)。

~~~python
input = torch.tensor([[[[1, 2, 3, 4],
                        [5, 6, 7, 8]]]], dtype=torch.float32)
print(input)
# tensor([[[[1., 2., 3., 4.],
#           [5., 6., 7., 8.]]]])

m = torch.nn.ZeroPad2d((1, 1, 2, 2))
output = m(input)
print(output)
# tensor([[[[0., 0., 0., 0., 0., 0.],
#           [0., 0., 0., 0., 0., 0.],
#           [0., 1., 2., 3., 4., 0.],
#           [0., 5., 6., 7., 8., 0.],
#           [0., 0., 0., 0., 0., 0.],
#           [0., 0., 0., 0., 0., 0.]]]])
~~~

## torch.nn.ConstantPad1d

一维常数填充

主要参数

> **padding** (*int*, *tuple*) : 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding)。
>
> **value** (*int*) : 填充值

~~~python
input = torch.tensor([[[2, 2, 2]]], dtype=torch.float32)
print(input)
# tensor([[[1., 2., 3., 4.]]])

m = torch.nn.ConstantPad1d(1, 1)
output = m(input)
print(output)
# tensor([[[1., 2., 2., 2., 1.]]])
~~~

## torch.nn.ConstantPad2d

二维常数填充

> **padding** (*int*, *tuple*): 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding)。
>
> **value** (*int*) : 填充值

~~~python
input = torch.tensor([[[[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12]]]], dtype=torch.float32)
print(input)
# tensor([[[[ 1.,  2.,  3.,  4.],
#           [ 5.,  6.,  7.,  8.],
#           [ 9., 10., 11., 12.]]]])

m = torch.nn.ConstantPad2d((1, 1, 1, 1), 0)
output = m(input)
print(output)
# tensor([[[[ 0.,  0.,  0.,  0.,  0.,  0.],
#           [ 0.,  1.,  2.,  3.,  4.,  0.],
#           [ 0.,  5.,  6.,  7.,  8.,  0.],
#           [ 0.,  9., 10., 11., 12.,  0.],
#           [ 0.,  0.,  0.,  0.,  0.,  0.]]]])
~~~

## torch.nn.ConstantPad3d

三维常数填充

主要参数

> **padding** (*int*, *tuple*): 填充尺寸，若传入int表示两侧填充相等长度，若传入tuple则分别表示(left padding, right padding, top padding, bottom padding, front padding, back padding)。
>
> **value** (*int*) : 填充值

~~~python
input = torch.tensor([[[[[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]],
                        [[10, 11, 12],
                         [13, 14, 15],
                         [16, 17, 18]]]]], dtype=torch.float32)
print(input)
# tensor([[[[[ 1.,  2.,  3.],
#            [ 4.,  5.,  6.],
#            [ 7.,  8.,  9.]],
#
#           [[10., 11., 12.],
#            [13., 14., 15.],
#            [16., 17., 18.]]]]])

m = torch.nn.ConstantPad3d(1, 0)
output = m(input)
print(output)
# tensor([[[[[ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]],
#
#           [[ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  1.,  2.,  3.,  0.],
#            [ 0.,  4.,  5.,  6.,  0.],
#            [ 0.,  7.,  8.,  9.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]],
#
#           [[ 0.,  0.,  0.,  0.,  0.],
#            [ 0., 10., 11., 12.,  0.],
#            [ 0., 13., 14., 15.,  0.],
#            [ 0., 16., 17., 18.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]],
#
#           [[ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]]]]])
~~~

