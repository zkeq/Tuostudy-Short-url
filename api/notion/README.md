### 使用 `notion` 的 `database` 做数据源

1. 创建一张 `database` 表；创建一个集成；给集成加 `读权限`

2. 获取到你的 notion `sk`

3. 将 `SK` 和 `database`的 `id`  填入 `/api/notion/index.py` 中

4. `databese` 数据表格式如下图

![2](https://p19.qhimg.com/t0151751b6a75ac7c22.png)


### 接口示例

| 序号 | 说明                   | 示例                                       |
| :--: | ---------------------- | ------------------------------------------ |
|  1   | vercel-notion-api | http://tuo.icodeq.com/api/notion/?dream  |
