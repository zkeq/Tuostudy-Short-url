### 直接使用 308 跳转 `/api/308`

1. 将 `/api/308` 目录下的函数部署至 `vercel` 或 `腾讯云函数` 

2. 自行选用数据库对接

3. 有备案域名的话更推荐 `腾讯云函数` 因为链接很干净

4. 而 `vercel` 的话，应该是要把函数文件放在 `api` 目录下才会生效，那么链接就变长了一点，不够优雅

5. 腾讯云不备案生成的链接就是个笑话

6. 你管这玩意叫短链？😂 https://service-55pgd0rm-1303831731.gz.apigw.tencentcs.com/release/APIGWHtmlDemo-1645366165/dream 

### 修复 腾讯云函数 无法读取 中文的问题（即提前编译好）

步骤

1. 创建的时候先 `pip install requests -t .`
2. 把 `Tencent-SCF-308-index.py` 更改为 `index.py` 然后移动到一个文件夹里面
3. 点击云函数创建按钮
4. 选择 `python3.6` 空白函数！！！（重要）
5. 点击 `上传压缩包` （重要！！）（不要点创建，要不然会出现编码错误）
6. 创建完成后要看到以下目录
```python
bin
certifi
certifi-2021.10.8.dist-info
charset_normalizer
charset_normalizer-2.0.12.dist-info
idna
idna-3.3.dist-info
requests
requests-2.27.1.dist-info
urllib3
urllib3-1.26.8.dist-info
index.py
```
7. 点击测试，应该是不会出现乱码的！
