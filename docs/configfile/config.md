## xengine_config.json
``` json
{
  "appId": "com.zkty.xiaoqu",    // 建议直接设置为应用的 Bundle Identifier
  "appSecret": "8b387ca3ebdd412e9c97ef81ed352ee7",  //随机 md5 值.
  "offlineServerUrl": "https://3rd-public-file.oss-cn-beijing.aliyuncs.com"  //服务器地址,
  "moduels":[
  	{
  		"module_id":"com.zkty.ui",
  		"name":"ui",
  		"tag": "1.0.0",
 			"engine_version": "0.0.1",
  		"minimal_os_version":
  			{
					"ios": "11.1.0",
  				"android_api": 20
				} 
  
		}
  ]
}
```

## module.json

在开发组件模板时的配置文件, 定义了

``` json
{
  "module_id":"com.zkty.bluetooth",
  "name":"蓝牙",
  "tag": "1.0.0",
  "engine_version": "0.0.1",
  "minimal_os_version":{
		"ios": "11.1.0",
  	"android_api": 20,
	} 
}
```



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
