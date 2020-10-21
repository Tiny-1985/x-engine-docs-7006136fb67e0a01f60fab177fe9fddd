

**基座扫描测试**
<div id='modulename' style='display:none'>dcloud</div>
<img id='qrimg' src='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://192.168.44.52:3000/docs/modules/all/dist/ui/index.html'></img>




# JS


``` bash
npm install @zkty-team/com-zkty-module-dcloud
```



## openUniMP

 启动小程序

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appId | string |  | __UNI__11E9B73 |  |


## preloadUniMP

 预加载后打开小程序

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appId | string |  | __UNI__11E9B73 |  |


## openUniMPWithArg



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appId | string |  | __UNI__11E9B73 |  |
| arguments | Map\<string,string\> |  | {"arguments":"Hello uni microprogram"} | 配置启动小程序时传递的参数 |
| redirectPath | string |  | pages/component/view/view |  路径 |
| enableBackground | bool |  |  |  开启后台运行 |
| showAnimated | bool | true |  | 是否开启 show 小程序时的动画效果 默认：true |
| hideAnimated | bool | true |  | 是否开启 hide 时的动画效果 默认：true |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-dcloud
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-dcloud
```


