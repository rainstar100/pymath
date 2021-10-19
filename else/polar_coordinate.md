# Integrate at polar coordinate

## compare with cartersin coordinate

name | divide | area | accumulate
:-:|:-:|:-:|:-:
cartersin | rectangle | $  f(x)dx $ | $  \int f(x)dx $
polar | ? | ? |

## think about polar coordinate

### what we know?

1. $ r=f(\theta) $

2. $ \theta,f(\theta+d\theta),f(\theta),d\theta \rightarrow 0, $

3. $ \lim \limits_{d\theta \rightarrow 0} f(\theta + d\theta)=f(\theta) $
    that means we can replace $ f(\theta +d\theta)$ with $ f(\theta) $   when $ d
    \theta \rightarrow 0 $

    这里好像不正确，今天先这样

4. we know  $ \theta ,f(\theta),f(\theta) $ ，and then consider 2 cases: divide into triange or sector

### 2 cases(divided)
name | area
:-:|:-:|:-:
triangle |  $ \frac {1}{2}f(\theta)f(\theta)sin\theta $
sector |  $ \frac {1}{2}f(\theta)f(\theta)\theta $

### who is the more apporximate

- $ \lim\limits_{\theta \rightarrow 0} \frac {sin\theta}{\theta}=1 $ 
- $ \lim\limits_{\theta \rightarrow 0} \frac{\sqrt{2-2cos\theta}f(\theta)}{f(\theta)\theta}=1 $
- So we know both are equivalent

### finally
we accumulate the divided area

##
$ \int \frac{1}{2}f^2(\theta)\theta $