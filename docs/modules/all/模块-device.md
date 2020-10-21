

**基座扫描测试**
<div id='modulename' style='display:none'>device</div>
<img id='qrimg' src='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://192.168.44.52:3000/docs/modules/all/dist/ui/index.html'></img>




# JS


``` bash
npm install @zkty-team/com-zkty-module-device
```



## getPhoneType

设备类型

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getSystemVersion

系统版本

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getUDID

UDID

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getBatteryLevel

电池电量

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getPreferredLanguage

当前语言

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getScreenWidth

屏幕宽度

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getScreenHeight

屏幕高度

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getSafeAreaTop

安全区域上边距

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getSafeAreaBottom

安全区域下边距

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getSafeAreaLeft

安全区域左边距

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getSafeAreaRight

安全区域右边距

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getStatusHeight

状态栏高度

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getNavigationHeight

导航条高度

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |


## getTabBarHeight

tabBar高度

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ | string |  |  |  |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-device
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-device
```


