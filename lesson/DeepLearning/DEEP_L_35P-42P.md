# DEEP_L_35P-42P

## Attack ML Models

### Motivation

希望机器可以应对来自人类的恶意攻击，如垃圾邮件、图片噪点干扰、人脸识别干扰、音频噪音干扰

### Attack

#### Non-targeted Attack

训练时，x是固定的，调整θ来训练

无目标攻击时，θ是系统已经训练好的，调整x以使输出产生错误

![image-20200803204117097](https://cdn.jsdelivr.net/gh/kkolento/images/20200803204117.png)

#### Targeted Attack

有目标攻击时，希望系统输出与期望错误输出相近

#### Constraint

无论如何，我都希望
$$
d(x^0-x')\rightarrow \varepsilon,\varepsilon\rightarrow 0
$$
即希望攻击后的数据与原数据相似，不被发现

关于原数据与攻击后数据的差异量化，主要有如下两种方式

![constraint](https://cdn.jsdelivr.net/gh/kkolento/images/20200803204924.png)

#### How to Attack

按照正常梯度下降法进行update，当当前x超出规定差异时，进行修改

![how to attack](https://cdn.jsdelivr.net/gh/kkolento/images/20200803205416.png)

修改方法如下，根据差异量化方法不同，有不同的修改方法

![fix](https://cdn.jsdelivr.net/gh/kkolento/images/20200803205810.png)

#### Attack Approaches

##### Fast Gradient Sign Method(FGSM)

只在乎方向，不在乎大小，可以做到只进行一次就可实现attack

![FGSM](https://cdn.jsdelivr.net/gh/kkolento/images/20200803214927.png)

但想实现attack，需要得到神经网络的参数才能计算

这叫做**白箱攻击**

#### Black Box Attack

通常无法得到神经网络的参数与架构，故需要黑箱架构

只要可以的到目标神经网络的训练集，可以自己训练自己的Proxy Network，然后训练攻击自己的Network，用同样的方法攻击BlackBox通常同样可以成功

![Black Box Attack](https://cdn.jsdelivr.net/gh/kkolento/images/20200803211610.png)

有没有一种无差别攻击可以使所有同类训练都失效

参考文献 **[Universal Adversarial Attack](https://arxiv.org/abs/1610.08401)**

受到杂讯干扰后，没有改变神经网络架构，却直接使神经网络的功能发生改变？

参考文献Gamaleldin F.Elsayed,Ian Goodfellow,Jascha Sohl-Dickstein."Adversarial Reprogramming of Neural Networks",ICLR,2019

#### Attack in the Real World

将攻击时的杂讯可视化，如人脸识别时将攻击干扰的噪音讯号做成眼镜，人戴上这副眼镜后，就会被识别错误

需要注意的是

- 攻击讯号必须可以可视化为现实中可实现的物品
- 相机像素辨识度要足够高

### Defense

#### Passive Defense

+filter 滤波（如平滑处理Smoothing，可以有效减轻噪声干扰）

##### Feature Squeeze

将滤波处理前后的训练结果进行对比，即可发现是否被attack

![feature squeeze](https://cdn.jsdelivr.net/gh/kkolento/images/20200803214630.png)

##### Randomization at Inference Phase 

以毒攻毒

![Randomization at Inference Phase ](https://cdn.jsdelivr.net/gh/kkolento/images/20200803214637.png)

局限性：如果滤波方法泄露，那攻击方进行一次逆操作即可化解

#### Proactive Defense

训练时自己进行attack（自己找漏洞），然后将这些被attack的数据手动添加正确的label，增加训练数据集再进行训练（把洞补起来）

局限性：找漏洞的方法要全面才行，否则还是会被攻击
