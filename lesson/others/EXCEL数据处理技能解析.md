# EXCEL数据处理技能解析

## Excel 常用函数介绍

### 常用四类函数

1. **统计函数**
   - SUM
   - AVERAGE
   - MAX/MIN
   - COUNT

2. **日期和时间函数**
   - TODAY
   - YEAR
   - WEEKDAY
3. **文本函数**
   - TEXT
   - LEFT/RIGHT
4. **逻辑函数**
   - IF逻辑比较
   - IF嵌套
   - AND/OR/NOT

---

### 统计函数

#### 求和函数

**条件求和**

```
=sumif(range,"criteria",sum_range)
```

*如果求和区域与判断条件区域相同，则最后的sum_range部分可省略，条件平均值公式中亦然*

**多条件求和**

```
=sumifs(sum_range,criteria_range1,criteria1,...)
```

#### 平均值函数

**条件平均值**

```
=averageif(range,"criteria",average_range)
```

**多条件平均值**

通常不直接使用averageifs，而是写好多条件判断语句后，利用sum和countif作商间接求得

#### 最值函数

**条件最值**

```
=maxifs(max_range,criteria_range1,criteria1,...)
```

#### 计数函数

**条件计数**

```
=countif(range,criteria)
```

**多条件计数**

```
=countifs(criteria_range1,criteria1,...)
```

### 日期和时间函数

得到当前日期的函数

```
=today()
```

**计算日期间隔**

```
=yearfrac(start_date,end_date,basis)
```

*basis=0计算一月为30天，一年为360天*，不填默认为此方法！

*basis=1为实际日期计算方法，包含闰年*

*basis=3计算一年为365天，不包含闰年*

### 文本函数

#### 格式函数

```
=text(value,format_text)
```

*常用format_text*

- YYYY/MM/DD（字母出现几次代表输出几位） 2020/08/06

- 0.00（保留小数点后2位）

#### 按位取字符函数

```
=left(text,num_chars)
```

### 逻辑函数

#### IF逻辑比较

```
=if(logical_test,value_if_true,value_if_false)
```

*value为文本时，需使用双引号""*

#### IF嵌套

无法再一层if语句中判断时，可在if语句中嵌套if语句

```
=if(criteria1,value_t1,if(criteria2,value_t2,value_f2))
```

#### 与或非函数

用于逻辑判断，各函数用法与数学上一致且较为简单故不再赘述

### VLOOKUP

```
=vlookup(lookup_value,table_array,col_index_num,range_lookup)
```

lookup_value想要查找的内容

table_array要查找的位置，**查找目标一定要位于查找位置的第一列**

col_index_num要返回的值的在所选区域的相对位置

range_lookup=False精确检索、True模糊检索