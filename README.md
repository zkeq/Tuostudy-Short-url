#### ðèªå·±åçç­é¾ç½åååç«¯æºç ð (ç®åå·²ç´æ¥å¯¹æ¥ ossï¼

###### [ç®åå·²æ¯æä½¿ç¨ `notion` ç `database` åæ°æ®æº]

###### [ç®åå·²æ¯æ Python å½æ° ç´æ¥è¿è¡ 308 è·³è½¬ ð]

###### [å¦æååæå¤æ¡æ¨èä½¿ç¨ 308 è·³è½¬ï¼è¾è®¯äºå½æ°ï¼]

> ç¤ºä¾å°åï¼ http://tuo.icodeq.com/dream

##### çé¢

![1](https://p18.qhimg.com/t01220de52b24dc1415.png)

##### åç

- æ°çåçä¸º `vercel` è·åå°æ°æ®ï¼ç¶å 308 è·³è½¬ ï¼ç¨æ§ççè¯æ `index-location` æ¹æ `index` å°±è¡äºã

>    - åçå¾ç®åï¼å°±æ¯å©ç¨ `404 é¡µé¢` ä¼æè·ææè¯·æ±è¿ä¸ç¹æ§
>
>    - ç¶ååç¨ `window.location.href` è·åå°å½åè®¿é®ç `url`
>
>    - æ¥çå»è·åä¸ä¸ª `json` æä»¶ï¼å©ç¨ä¸é¢çå½åè®¿é® `url` æ¥å­å¸ï¼æ¥ä¸å°å°±è·³è½¬å°é»è®¤ä¸»é¡µ
>
>    - æ¥å°å­å¸äºå°± `window.location.replace()`

##### Json æ ¼å¼ (ä¸é¨åäºä¸ä¸ªå·¥å·æ¥çæåç»´æ¤è¿ä¸ªæ°æ®ï¼è§ [Releases](https://github.com/zkeq/Tuostudy-Short-url/releases) )

```JSON
{
	"dream": "https://dream-plan.cn/",
	"abcd": "https://tuostudy.vercel.app/api?path=/ðº 020# åè¯è§é¢/ð æè´åè¯ï¼æ°ï¼/æç¦ä¸­çº§.mp4&raw=true",
	"abcde": "https://tuostudy.vercel.app/ðº 020# åè¯è§é¢/ð å®æ¹åçï¼åæ­¥ï¼/ð äººæçé«ä¸­è±è¯­åè¯å¿ä¿®1~éä¿®11",
	"test": "https://tuostudy.vercel.app/ð 030# è¯¾æ¬é³é¢/ð è±è¯­",
	"test2": "https://tuostudy.vercel.app/ð 030# è¯¾æ¬é³é¢/ð è±è¯­/ð 03# é«èå¬å/2019å¹´",
	"vip": "https://tuostudy.vercel.app/ðº 020# åè¯è§é¢/ð ä¸èåè¯ï¼è¶å¨ï¼/ð 07# åºå®æ­éè¯ç»ç­è¯­ç³»åï¼ä»è´¹ï¼",
	"vip1": "https://tuostudy.vercel.app/api?path=/ðº 020# åè¯è§é¢/ð ä¸èåè¯ï¼è¶å¨ï¼/ð 07# åºå®æ­éè¯ç»ç­è¯­ç³»åï¼ä»è´¹ï¼/ä¸­èè¯ç».mp4&raw=true",
	"shanbei": "https://tuostudy.vercel.app/ð 050# åè¯ææ¬/ð 02# æè´åè¯ï¼æ°ï¼/",
	"xiaoxuetxt": "https://tuostudy.vercel.app/ð 050# åè¯ææ¬/ð 01# å¢¨å¢¨åè¯ï¼è¶å¨ï¼/ð 03# å¸¦ä¸­æéä¹ç/1.å¨å½åå¤§ææçæ¬ä¸­å°å­¦åæ­¥/äººæç/",
	"xiaoxuemp3": "https://tuostudy.vercel.app/ð 030# è¯¾æ¬é³é¢/ð è±è¯­/ð 01# ä¸­å°å­¦åæ­¥åè¯è¯¾æå½é³/å°å­¦/äººæç/"
}
```

##### ä»£ç 

- [zkeq/Tuostudy-Short-url: ç­é¾æå¡ (github.com)](https://github.com/zkeq/Tuostudy-Short-url)

- [zkeq/Tuostudy-Short-url: ç­é¾æå¡ (gitee.com)](https://gitee.com/zkeq/Tuostudy-Short-url)

#### ç¨æ³ 

 - æ°çææ¡£ç¨æ³ä¸ºå° `/api/308/index.py` ä¸­ç `OSS` é¾æ¥æ¹æèªå·±çç¶åé¨ç½²è³ `vercel` å°±è½ç¨äº

##### ä»¥ä¸ä¸ºæ§çç¨æ³ï¼`index-location`ï¼

> 1. ä¿®æ¹ `404.html` å `index.html` ä¸­çè¿äºé¨å ( `url` å `long` çå¼)
> 
> ```javascript
>    
>     ajax({
>             method: 'GET',
>             url: 'https://tuo-site.oss-cn-beijing.aliyuncs.com/data.json',
>             success: function (OriginalFromActivity) {
>                 //å¨è¿éå¯¹è·åçæ°æ®ç»å¸¸æä½
>                 console.log(OriginalFromActivity)
>                 url = window.location.href.split('/').pop()
>                 long = OriginalFromActivity[url]
>                 if(long === undefined) { // åªè½ç¨ === è¿ç®æ¥æµè¯æä¸ªå¼æ¯å¦æ¯æªå®ä¹ç
>                      long = 'https://tuostudy.vercel.app'}
>                 console.log(long)
>                 window.location.replace(long)
>                 }
>  })
> ```
> 
> 2. ä¿®æ¹ ç½é¡µåç«¯ï¼æ¹æèªå·±åæ¬¢çæ ·å­
> 
> 3. å°ç½é¡µé¨ç½²å° `github` æè `gitee` æè `vercel` ä¸é¢
> 
> 4. æå¼ å¨ [å¾æ¬§åç­é¾çæå¨-v4.x](https://github.com/zkeq/Tuostudy-Short-url/releases) ä¸è½½ç `å¾æ¬§åç­é¾çæå¨-v4.x` , æèç´æ¥è¿è¡ `/python-CLI` ç®å½ä¸çæºç 
> 
> 5. æ ¹æ®æç¤ºå¼å§æ·»å ç­é¾ ï¼ `OSS` è¯¦æè®¾ç½®è¯·åéå®ç½éç½®ï¼è¥ä¸æ¯ä½¿ç¨ç `OSS` ï¼è¯·ä½¿ç¨ `local` çæ¬ï¼
> 
> ```cmd
> æ¬å·¥å·æåç§æ¨¡å¼
> 
> 1. èªå®ä¹çæç­é¾
> 2. è®¾ç½®è¦çæçç­é¾ä½æ° ï¼èªå¨çæç­é¾
> 3. å é¤æä¿®æ¹ç­é¾æ¨¡å¼
> 4. æ¥éæ¨¡å¼ï¼åªè¯»æ¨¡å¼ï¼
> 0. éåº
> ```
> 
> 6. ~æ·»å ç­é¾å®æåå° `data.json` æä»¶ä¼ å° `Github` æè `Gitee` æè `Vercel` æè `OSS` æèéä¾¿ä¸ä¸ªäºå­å¨~
> 
> 6. æ¬å·¥å·èªå¨åæ­¥ oss ï¼è¯¦æåé  https://github.com/zkeq/Tuostudy-Short-url/releases/tag/v4.0.0 ðððð
> 
> 7. è¯·ç¡®ä¿ä½ ç¬¬å­æ­¥ä¸ä¼ æ°æ®å¾å°ç `url` å¯ä»¥ç´æ¥è®¿é®å¹¶ä¸ç¬¬ä¸æ­¥å¡«åç `url` ä¸­çå¼å®å¨ä¸æ · 
> 
> 8. (ä¸ææ `notion` åæ°æ®æºï¼
>
> 9. ð enjoy ð

#### åç»­ç»´æ¤

- è¯·å¨ `å¾æ¬§åç­é¾çæå¨-v4.x` ä¸­è¿è¡åç»­æä½ã

#### å¦ä¸ç§æè·¯ï¼ä¸å¤§æ¨èï¼

- å©ç¨ `vercel` çäºå½æ°ï¼ä½¿ç¨ `python` æ¸²æå®ææä»¶åè¿ååç«¯

- ç¸å³æºç ï¼[zkeq/Tuostudy-Short-url: ç­é¾æå¡ (github.com)](https://github.com/zkeq/Tuostudy-Short-url/tree/main/api)

### ä½¿ç¨ `notion` ç `database` åæ°æ®æº

[Notion æ¨¡æ¿ï¼ä½ ä¹å¯ä»¥è¯çä¿®æ¹è¿ä¸ªæ°æ®åºæ¥å¢å è®°å½](https://zkeq.notion.site/0ff3d88f8ba143ea869bb2da7c9236c7?v=b5e44e122f524d56a3e331526dd2d935)

1. åå»ºä¸å¼  `database` è¡¨ï¼æ³¨ææ ¼å¼. å­æ®µï¼`Short:str` `url:url` )ï¼åå»ºä¸ä¸ªéæï¼ç»éæå  `è¯»æé`

2. è·åå°ä½ ç notion `sk`

3. å° `SK` å `database` ç `id`  å¡«å¥ `/api/notion/index.py` ä¸­

4. `databese` æ°æ®è¡¨æ ¼å¼å¦ä¸å¾

![2](https://p19.qhimg.com/t0151751b6a75ac7c22.png)

5. ç´æ¥è®¿é® `/api/notion/?dream` å³å¯è·³è½¬ï¼åç«¯æ¸²æå®æåè¿åï¼
å·ä½åè§ï¼**[/api/notion](https://github.com/zkeq/Tuostudy-Short-url/tree/main/api/notion)** 

6. æä½¿ç¨ `/api/notion-back-json` åæ°æ®æºï¼åç«¯åªåæ°æ®åºï¼
å·ä½åè§ï¼**[/api/notion-back-json](https://github.com/zkeq/Tuostudy-Short-url/tree/main/api/notion-back-json)** 

7. æ°æ®æºè¿åç¤ºä¾ https://tuo.icodeq.com/api/notion-back-json


### ç´æ¥ä½¿ç¨ 308 è·³è½¬ `/api/308`

1. å° `/api/308` ç®å½ä¸çå½æ°é¨ç½²è³ `vercel` æ `è¾è®¯äºå½æ°` 

2. èªè¡éç¨æ°æ®åºå¯¹æ¥

3. æå¤æ¡ååçè¯æ´æ¨è `è¾è®¯äºå½æ°` å ä¸ºé¾æ¥å¾å¹²å

4. è `vercel` çè¯ï¼åºè¯¥æ¯è¦æå½æ°æä»¶æ¾å¨ `api` ç®å½ä¸æä¼çæï¼é£ä¹é¾æ¥å°±åé¿äºä¸ç¹ï¼ä¸å¤ä¼é

5. è¾è®¯äºä¸å¤æ¡çæçé¾æ¥å°±æ¯ä¸ªç¬è¯

6. ä½ ç®¡è¿ç©æå«ç­é¾ï¼ð https://service-cetfbmjm-1303831731.gz.apigw.tencentcs.com/release/helloworld-1645706447/dream

> æ³¨ï¼è¿éçè¾è®¯äºå `notion` å¯ä»¥åå«æ¿ä»£ `vercel` å `OSS` å·ä½ç¨æ³èªè¡çè§£ã


> `vercel` ç¤ºä¾: https://tuo.icodeq.com/api/308?dream

### æ¥å£ç¤ºä¾

| åºå· | è¯´æ                   | ç¤ºä¾                                       |
| :--: | ---------------------- | ------------------------------------------ |
|  1   | 404æ ¹ç®å½ä¸»é¾æ¥ | http://tuo.icodeq.com/dream |
|  2   | æ ¹ç®å½ç´¢å¼ | http://tuo.icodeq.com/?dream  |
|  3   | vercel-oss-api | http://tuo.icodeq.com/api/?dream  |
|  3   | vercel-notion-api | http://tuo.icodeq.com/api/notion/?dream  |


#### æºç ä»¥åç¸å³é¾æ¥

| åºå· | è¯´æ                   | é¾æ¥                                       |
| :--: | ---------------------- | ------------------------------------------ |
|  1   | `Github` ä»åº (ä¼æ´æ°) | https://github.com/zkeq/Tuostudy-Short-url |
|  2   | `Gitee` ä»åº (ä¼æ´æ°)  | https://gitee.com/zkeq/Tuostudy-Short-url  |
|  3   | æ¬æPDFæ ¼å¼     | https://lanzoul.com/iDzgM003x1yh  |

### èµå©

æè°¢ `JetBrains` ä¸ºæ¬é¡¹ç®æä¾çè®¸å¯è¯ã

<a href="https://jb.gg/OpenSourceSupport">
<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains Logo (Main) logo." width="8%"/>
<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm.png" alt="PyCharm logo." width="25%">
</a>