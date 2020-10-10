

##  desc

打开 App 时自动更新



流程如下：

 \- 启动

  \- 请求服务器获取 microApp.json getMicroAppJson()

   \- 请求成功:

​    \- 循环:url,version = locateMicroAppByMicroappId

​     \- url != nil: 通过 appid 对比版本号

​      \- 本地版本低, 下载远程新版本,并解压到沙盒

​      \- 本地版本一样或更高, 返回

​     \- url 为 nil: 下载远程新版本,并解压到沙盒

   \- 请求失败: 不做任何事



 \- (url) locateMicroAppByMicroappId(&version)

  \- 从沙盒找

   \- 成功, 返回 index.html 位置与版本

   \- 失败, 从工程找

​    \- 成功 返回 index.html 位置与版本

​    \- 失败 返回 (nil,-1)





``` json
{
  "appId": "com.zkty.microapp",
  "appSecret": "8b387ca3ebdd412e9c97ef81ed352ee7",
  "offlineServerUrl": "http://127.0.0.1:8000"
}

```

 



# api



# iOS


# android
hello


