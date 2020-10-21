

**基座扫描测试**
<div id='modulename' style='display:none'>tools</div>
<img id='qrimg' src='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://192.168.44.52:3000/docs/modules/all/dist/ui/index.html'></img>




# JS


``` bash
npm install @zkty-team/com-zkty-module-tools
```



## unZipFile



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| filePath | string |  |  | 文件路径 |
| unZipPath | string | true |  | 解压到 路径 |
| \_\_event\_\_ | string | true |  | 压缩进度 |


## zipFile



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| filePath | string |  |  | 文件路径 |
| toZipPath | string | true |  | 压缩到 路径 |
| \_\_event\_\_ | string | true |  | 解压缩进度 |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-tools
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-tools
```


