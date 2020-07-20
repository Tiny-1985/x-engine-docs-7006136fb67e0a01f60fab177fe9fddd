## xengine_config.json
``` json
{
  "appId": "com.zkty.xiaoqu",    // 建议直接设置为应用的 Bundle Identifier
  "appSecret": "8b387ca3ebdd412e9c97ef81ed352ee7",  //随机 md5 值.
  "offlineServerUrl": "https://3rd-public-file.oss-cn-beijing.aliyuncs.com"  //服务器地址,
  "moduels":[
  	{
  		... //module.json
		}
  ]
}
```

## modules.json

``` json
{
  "module_id":"com.zkty.bluetooth",
  "name":"蓝牙",
  "tag": "1.0.0",
  "engine_version": "0.0.1",
  "mini_platform":{
		"ios": "11.1.0",
  	"android_api": 20,
	},
	"exclude_brand":[
    {
      "brand_name":"华为",
      "device_id":"ry-10"
    }
  ]
}
```





## microApps.json

``` json
{
  "code":0,
  "version":3,     // microApps.json 版本标识
  "forceUpdate" true,  // 是否强制更新
  "data":
        [
          {
            "microAppName":"开门",
            "microAppId":"com.zkty.xiaoqu.opendoor",
            "microAppVersion":2
          },
          {
            "microAppName":"物业",
            "microAppId":"com.zkty.xiaoqu.realstate"
            "microAppVersion":1
          }
        ]
  }
```
