## xengine_config.json

``` json
{
  "appId": "com.zkty.xiaoqu",    // 建议直接设置为应用的 Bundle Identifier
  "appSecret": "8b387ca3ebdd412e9c97ef81ed352ee7",  //随机 md5 值.
  "offlineServerUrl": "https://3rd-public-file.oss-cn-beijing.aliyuncs.com"  //服务器地址
}
```

appId 是应用唯一id，用户指定，服务器判别是否有效。

appSecret 应该由服务器生成。

offlineServerUrl 为离线包更新地址。

> 在没有服务器逻辑，只有类似 ftp 的情况下， appId 与 appSecret 手动指定， 以备日后不时之需。





## microApps.json

``` json
{
"msg": "success",
"code": 0,
"data":{
    "code":0,
    "version":8,
    "forceUpdate": 0,
    "data":[
          {
              
            "microAppName":"开门",
            "microAppId":"com.zkty.test",
            "microAppVersion":1
          },
          {
            "microAppName":"物业",
            "microAppId":"com.zkty.xiaoqu.realstate",
            "microAppVersion":2
          },
          {
            "microAppName":"物业",
            "microAppId":"com.zkty.xiaoqu.network",
            "microAppVersion":1
          },
          {
            "microAppName":"物业",
            "microAppId":"com.zkty.xiaoqu.lj",
            "microAppVersion":4
          }
        ]
    }
}
```
