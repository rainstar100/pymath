求下面函数的积分：
$$
\int {uv} \, dx
$$
首x先考虑：
$$
f(x)=uv
$$
那么f(x)的原函数F(X)是什么？考虑F(X)可能的形式，初步考虑其有基本形式是基本函数及其他们的四则运算，形式如下：
$$
1)\ F(X)=single(x)
$$
$$
2)\ F(x)=onefunction(x)\ \&\ otherfunciont(x)
$$
$$
3)\ F(x)=U(V(X))
$$
根据导数法则:\
形式1）不符合题设\
形式2）加减法运算不符合题设，而乘法运算符合题设，所以判断:
形式3）没有考虑，有待证实

$$
F(X)=UV 
$$
$$
f(x)=UV'+U'V
$$
$$
\int f(x)dx=\int (UV'+U'V)dx
$$
$$
F(x)+C=\int UV'dx+ \int U'Vdx
$$
$$
UV+C=\int UV'dx+ \int U'Vdx
$$
$$
a) \ \int U'Vdx=UV+C-\int UV'dx

$$
$$
b) \ \int UV'dx=UV+C-\int U'Vdx

$$


按公式a)计算例题：
$$
\int xsin(x)
$$
令：
$$
U'=x
$$
$$
V=sin(x)
$$

可知：
$$
U=\frac {1}{2}x^2
$$
$$
V'=cos(x)
$$
$$
\int xsin(x)dx=\frac {1}{2}x^2 \ sin(x)+C-\int \frac {1}{2}x^2 \ cos(x)dx
$$



按公式b)计算例题：
$$
\int xsin(x)
$$
令：
$$
U=x
$$
$$
V'=sin(x)
$$

可知：
$$
U'=1
$$
$$
V=-cos(x)
$$
$$
\int xsin(x)dx=-xcosx+C-\int -cos(x)dx
$$
$$
\int xsin(x)dx=-xcosx+C-sinx
$$




