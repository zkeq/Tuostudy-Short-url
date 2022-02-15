#### 🚀自己写的短链网址前后端源码🚀

##### 界面

![1](https://p18.qhimg.com/t01220de52b24dc1415.png)

##### 原理

- 原理很简单，就是利用 `404 页面` 会捕获所有请求这一特性


- 然后再用 `window.location.href` 获取到当前访问的 `url`
- 接着去获取一个 `json` 文件，利用上面的当前访问 `url` 查字典，查不到就跳转到默认主页
- 查到字典了就 `window.location.replace()`

##### 代码

- [zkeq/Tuostudy-Short-url: 短链服务 (github.com)](https://github.com/zkeq/Tuostudy-Short-url)
- [zkeq/Tuostudy-Short-url: 短链服务 (gitee.com)](https://gitee.com/zkeq/Tuostudy-Short-url)

#### 用法

1. 修改 `404.html` 和 `index.html` 中的这些部分 ( `url` 和 `long` 的值)

```javascript
   
    ajax({
            method: 'GET',
            url: 'https://tuo-site.oss-cn-beijing.aliyuncs.com/data.json',
            success: function (OriginalFromActivity) {
                //在这里对获取的数据经常操作
                console.log(OriginalFromActivity)
                url = window.location.href.split('?')[1]
                long = OriginalFromActivity[url]
                if(long === undefined) { // 只能用 === 运算来测试某个值是否是未定义的
                     long = 'https://tuostudy.vercel.app'}
                console.log(long)
                window.location.replace(long)
                }
 })
```

   

2. 修改 网页前端，改成自己喜欢的样子
3. 将网页部署到 `github` 或者 `gitee` 或者 `vercel` 上面
4. 打开 `图欧君短链生成器-v3.2`
5. 根据提示开始添加短链
6. 添加短链完成后将`data.json` 文件传到 `Github` 或者 `Gitee` 或者 `Vercel` 或者 `OSS` 或者随便一个云存储
7. 请确保你第六步上传数据得到的 `url` 可以直接访问并且第一步填写的`url`中的值完全一样
7. 🚀 enjoy 🚀

#### 后续维护

- 请在 `图欧君短链生成器-v3.2`中进行后续操作，操作完成后将 `data.json ` 再次上传即可。

#### 源码以及相关链接（`v3.2`）（后续更新在 `github` 仓库更新）

| 序号 | 说明                   | 链接                                       |
| :--: | ---------------------- | ------------------------------------------ |
|  1   | `Github` 仓库 (会更新) | https://github.com/zkeq/Tuostudy-Short-url |
|  2   | `Gitee` 仓库 (会更新)  | https://gitee.com/zkeq/Tuostudy-Short-url  |
