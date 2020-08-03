# Deep_L_26P-33P

## Explainable Machine Learning

**local explanation**

why do you think this image is a cat?

**global explanation**

what do you think a cat looks like?

**key words:**

interpretable v.s. powerful

decision tree

### Local explanation

**Object x**→Components:
$$
x_1,x_2\cdots x_n\cdots x_N
$$
(for images : pixel, for text : a word)

- 使用mask，对比使用mask后的输出来判断是哪块区域影响系统的判别

- 对components进行修改，如
  $$
  x_1→x_1+△x_1
  $$
  计算修改后对输出△y影响有多大，即计算偏微分

  形成Saliency Map

  ![Saliency Map](https://cdn.jsdelivr.net/gh/kkolento/images/20200803173841.png)

​           但有时会出现**Gradient Saturation**(梯度饱和)

![Gradient Saturation](https://cdn.jsdelivr.net/gh/kkolento/images/20200803173834.png)

​		solution: [Deep LIFT](https://arxiv.org/abs/1704.02685) [Integrated gradient](https://arxiv.org/abs/1611.02639)

​		~~[database for pokemon](https://www.Kaggle.com/kvpratama/pokemon-images-dataset/data)~~

### Global explanation

**Activation Maximization**

例：数字辨识 global explanation

输出 y_i 为感兴趣的数字，则找到输入x^，该输入对应的输出y_i最大，这就是the computer think a number looks like

**但实际上机器学习很容易被杂讯干扰**，故需要增加一个偏差量

![activation maximization](https://cdn.jsdelivr.net/gh/kkolento/images/20200803195051.png)

**Regularization from Generator**

![image Generator](https://cdn.jsdelivr.net/gh/kkolento/images/20200803200427.png)

通过增加这个generator,得到的image x(即explanation)更符合现实，而不会像之前得到的完全为杂讯

不同于GAN：Classifier为之前训练好的，不随着该网络训练

### Using a Model to Explain Another

using an interpretable model to mimic the behavior of an uninterpretable model.

![image-20200803201147948](https://cdn.jsdelivr.net/gh/kkolento/images/20200803201148.png)

**but linear model cannot mimic neural network...**

#### Local Interpretable Model Agnostic Explanations(LIME)

采样感兴趣点***附近***的一系列点，找到拟合这些数据的linear model，用该model来解释黑盒在该点附近的行为

![LIME](https://cdn.jsdelivr.net/gh/kkolento/images/20200803201445.png)

采样点的选取非常重要，会极大的影响所得model

##### 以图像为例

将图片分为多个区块

![example1](https://cdn.jsdelivr.net/gh/kkolento/images/20200803201907.png)

M为区块数量，x_m代表该区块是否存在

![example2](https://cdn.jsdelivr.net/gh/kkolento/images/20200803202410.png)

根据w的值即可判断系统是根据哪些区块作出判断

![example3](https://cdn.jsdelivr.net/gh/kkolento/images/20200803202418.png)

#### Decision Tree

复杂的Decision Tree可以完全模拟黑盒的行为，但为了便于解释（explainable），我们希望这个Decision Tree不要太复杂

用**O(T_θ)**来表示Decision Tree的复杂度

在训练时即将树的复杂度加入训练（如下图）

![example4](https://cdn.jsdelivr.net/gh/kkolento/images/20200803202952.png)

但O(T_θ)如何求gradient descent呢？（套娃，用另一个NN训练算出。。。）
