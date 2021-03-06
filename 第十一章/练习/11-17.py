# (a)
# 【名词解释】Currying：因为是美国数理逻辑学家哈斯凯尔·加里(Haskell Curry)发明了这种函数使用技巧，所以这样用法就以他的名字命名为Currying，中文翻译为“加里化”。
#
# 我感觉很多人都对函数加里化(Currying)和偏函数应用(Partial Application)之间的区别搞不清楚，尤其是在相似的上下文环境中它们同时出现的时候。
#
# 偏函数解决这样的问题：如果我们有函数是多个参数的，我们希望能固定其中某几个参数的值。
#
# 几乎所有编程语言中都有非常明显的偏函数应用。在C语言中：
#
# int foo(int a, int b, int c) {
#
#   return a + b + c;
# }
#
# int foo23(int a, int c) {
#   return foo(a, 23, c);
#
# }
#
# foo23函数实际上就是一个foo函数的偏函数应用，参数b的值被固定为23。
#
# 当然，像这样明显的偏函数并没有太大的用处；我们通常会希望编程语言能提供我们某些偏函数特征。
#
# 例如，在Python语言中，我们可以这样做：
#
# from functools import partial
#
# def foo(a,b,c):
#
#   return a + b + c
#
# foo23 = partial(foo, b=23)
#
# foo23(a = 1, c = 3)  # => 27
#
# 函数加里化(Currying)明显解决的是一个完全不同的问题：如果我们有几个单参数函数，并且这是一种支持一等函数(first-class)的语言，如何去实现一个多参数函数？函数加里化是一种实现多参数函数的方法。
#
# 下面是一个单参数的Javascript函数:
#
# var foo = function(a) {
#
#   return a * a;
# }
#
# 如果我们受限只能写单参数函数，可以像下面这样模拟出一个多参数函数：
#
# var foo = function(a) {
#
#   return function(b) {
#     return a * a + b * b;
#
#   }
# }
#
# 通过这样调用它：(foo(3))(4)，或直接 foo(3)(4)。
#
# 注意，函数加里化提供了一种非常自然的方式来实现某些偏函数应用。如果你希望函数foo的第一个参数值被固定成5，你需要做的就是var foo5 = foo(5)。这就OK了。函数foo5就是foo函数的偏函数。注意，尽管如此，我们没有很简单的方法对foo函数的第二个参数偏函数化(除非先偏函数化第一个参数)。
#
# 当然，Javascript是支持多参数函数的：
#
# var bar = function(a, b) {
#
#   return a * a + b * b;
#
# }
#
# 我们定义的bar函数并不是一个加里化的函数。调用bar(5)并不会返回一个可以输入12的函数。我们只能像bar(5,12)这样调用这个函数。
#
# 在一些其它语言里，比如 Haskell 和 OCaml，所有的多参数函数都是通过加里化实现的。
#
# 下面是一个把上面的foo函数用OCaml语言写成的例子：
#
# let foo = fun a ->
#
#   fun b ->
#     a * a + b * b
#
# 下面是把上面的bar函数用OCaml语言写成的例子：
#
# let bar = fun a b ->
#
#   a * a + b * b
#
# 头一个函数我们叫做“显式加里化”，第二个叫做“隐式加里化”。
#
# 跟Javascript不一样，在OCaml语言里，foo函数和bar函数是完全一样的。我们用完全一样的方式调用它们。
#
# # foo 3 4;;
# - : int = 25
# # bar 3 4;;
# - : int = 25
#
# 两个函数都能够通过提供一个参数值来创造一个偏函数：
#
# # let foo5 = foo 5;;
# val foo5 : int -> int = <fun>
#
# # let bar5 = bar 5;;
# val bar5 : int -> int = <fun>
# # foo5 12;;
# - : int = 169
# # bar5 12;;
# - : int = 169
#
# 事实上，我们可以把下面这个匿名函数：
#
# fun arg1 arg2 ... argN -> exp
#
# 当作是下面这个函数的简写：
#
# fun arg1 -> fun arg2 -> ... -> fun argN -> exp
#
# 函数加里化和偏函数应用的总结
#
#     偏函数应用是找一个函数，固定其中的几个参数值，从而得到一个新的函数。
#     函数加里化是一种使用匿名单参数函数来实现多参数函数的方法。
#     函数加里化能够让你轻松的实现某些偏函数应用。
#     有些语言(例如 Haskell, OCaml)所有的多参函数都是在内部通过函数加里化实现的。

f