## xengine_config.json

``` json
{
  "appId": "com.zkty.xiaoqu",    // 建议直接设置为应用的 Bundle Identifier
  "appSecret": "8b387ca3ebdd412e9c97ef81ed352ee7",  //随机 md5 值.
  "offlineServerUrl": "https://3rd-public-file.oss-cn-beijing.aliyuncs.com"  //服务器地址,
  "modules":[
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

appId 是应用唯一id，用户指定，服务器判别是否有效。

appSecret 应该由服务器生成。

offlineServerUrl 为离线包更新地址。

> 在没有服务器逻辑，只有类似 ftp 的情况下， appId 与 appSecret 手动指定， 以备日后不时之需。

moduels 里包含了所有的组件配置，见下面 module.json

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
module_id 定义 `<厂商名>.<namespace>`

比如厂商为 `com.zkty` 

`namespace` 为 `bluetooth`





在将以上 json 放入 `xengine_config.json` 时, 引擎必须做以下校验:

在开发时, 引擎版本是否大于 engine_version?

如果否, 则在开发时弹框提示开发者. 在发布时不提示.



在运行时, 引擎必须检验:

当前系统是否大于 minimal_os_version 

如果否, 则将警告写进统计日志.



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
