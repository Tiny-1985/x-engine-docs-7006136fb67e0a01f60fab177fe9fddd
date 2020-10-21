

**基座扫描测试**
<div id='modulename' style='display:none'>scan</div>
<img id='qrimg' src='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://192.168.44.52:3000/docs/modules/all/dist/ui/index.html'></img>

扫描模块


# JS


``` bash
npm install @zkty-team/com-zkty-module-scan
```



## openScanView



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| \_\_event\_\_ |  |  | (result)=>{} | 扫码结果 xx(result) |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-scan
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-scan
```


