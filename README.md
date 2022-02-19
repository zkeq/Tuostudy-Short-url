#### 🚀自己写的短链网址前后端源码🚀 (目前已直接对接oss）

###### [目前已支持使用 `notion` 的 `database` 做数据源]

> 示例地址： http://tuo.icodeq.com/dream

##### 界面

![1](https://p18.qhimg.com/t01220de52b24dc1415.png)

##### 原理

- 原理很简单，就是利用 `404 页面` 会捕获所有请求这一特性

- 然后再用 `window.location.href` 获取到当前访问的 `url`

- 接着去获取一个 `json` 文件，利用上面的当前访问 `url` 查字典，查不到就跳转到默认主页

- 查到字典了就 `window.location.replace()`

##### Json 格式 (专门写了一个工具来生成和维护这个数据，见 [Releases](https://github.com/zkeq/Tuostudy-Short-url/releases) )

```JSON
{
	"dream": "https://dream-plan.cn/",
	"abcd": "https://tuostudy.vercel.app/api?path=/📺 020# 单词视频/📁 扇贝单词（新）/托福中级.mp4&raw=true",
	"abcde": "https://tuostudy.vercel.app/📺 020# 单词视频/📁 官方原版（同步）/📁 人教版高中英语单词必修1~选修11",
	"test": "https://tuostudy.vercel.app/🔊 030# 课本音频/📁 英语",
	"test2": "https://tuostudy.vercel.app/🔊 030# 课本音频/📁 英语/📁 03# 高考听力/2019年",
	"vip": "https://tuostudy.vercel.app/📺 020# 单词视频/📁 不背单词（超全）/📁 07# 固定搭配词组短语系列（付费）",
	"vip1": "https://tuostudy.vercel.app/api?path=/📺 020# 单词视频/📁 不背单词（超全）/📁 07# 固定搭配词组短语系列（付费）/中考词组.mp4&raw=true",
	"shanbei": "https://tuostudy.vercel.app/📜 050# 单词文本/📁 02# 扇贝单词（新）/",
	"xiaoxuetxt": "https://tuostudy.vercel.app/📜 050# 单词文本/📁 01# 墨墨单词（超全）/📁 03# 带中文释义版/1.全国各大教材版本中小学同步/人教版/",
	"xiaoxuemp3": "https://tuostudy.vercel.app/🔊 030# 课本音频/📁 英语/📁 01# 中小学同步单词课文录音/小学/人教版/"
}
```

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
                url = window.location.href.split('/').pop()
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

4. 打开 在 [图欧君短链生成器-v4.x](https://github.com/zkeq/Tuostudy-Short-url/releases) 下载的 `图欧君短链生成器-v4.x`, 或者直接运行 `/python-CLI` 目录下的源码

5. 根据提示开始添加短链 （`OSS` 详情设置请参阅官网配置，若不是使用的 `OSS` ，请使用 `local` 版本）

```cmd
本工具有四种模式

1. 自定义生成短链
2. 设置要生成的短链位数 ，自动生成短链
3. 删除或修改短链模式
4. 查阅模式（只读模式）
0. 退出
```

6. ~添加短链完成后将 `data.json` 文件传到 `Github` 或者 `Gitee` 或者 `Vercel` 或者 `OSS` 或者随便一个云存储~

6. 本工具自动同步 oss ，详情参阅  https://github.com/zkeq/Tuostudy-Short-url/releases/tag/v4.0.0 🚀🚀🚀🚀

7. 请确保你第六步上传数据得到的 `url` 可以直接访问并且第一步填写的`url`中的值完全一样 

8. (下文有 `notion` 做数据源）

9. 🚀 enjoy 🚀

#### 后续维护

- 请在 `图欧君短链生成器-v4.x`中进行后续操作。

#### 另一种思路（不大推荐）

- 利用 `vercel` 的云函数，使用 `python` 渲染完成文件后返回前端

- 相关源码：[zkeq/Tuostudy-Short-url: 短链服务 (github.com)](https://github.com/zkeq/Tuostudy-Short-url/tree/main/api)

### 使用 `notion` 的 `database` 做数据源

1. 创建一张 `database` 表；创建一个集成；给集成加 `读权限`

2. 获取到你的 notion `sk`

3. 将 `SK` 和 `database`的 `id`  填入 `/api/notion/index.py` 中

4. `databese` 数据表格式如下图

![2](https://p19.qhimg.com/t0151751b6a75ac7c22.png)

5. 直接访问 `/api/notion/?dream` 即可跳转

6. 或使用 `api/notion-back-json` 做数据源

7. 数据源返回示例 https://tuo.icodeq.com/api/notion-back-json


### 接口示例

| 序号 | 说明                   | 示例                                       |
| :--: | ---------------------- | ------------------------------------------ |
|  1   | 404根目录主链接 | http://tuo.icodeq.com/dream |
|  2   | 根目录索引 | http://tuo.icodeq.com/?dream  |
|  3   | vercel-oss-api | http://tuo.icodeq.com/api/?dream  |
|  3   | vercel-notion-api | http://tuo.icodeq.com/api/notion/?dream  |


#### 源码以及相关链接

| 序号 | 说明                   | 链接                                       |
| :--: | ---------------------- | ------------------------------------------ |
|  1   | `Github` 仓库 (会更新) | https://github.com/zkeq/Tuostudy-Short-url |
|  2   | `Gitee` 仓库 (会更新)  | https://gitee.com/zkeq/Tuostudy-Short-url  |
|  3   | 本文PDF格式     | https://lanzoul.com/iDzgM003x1yh  |

