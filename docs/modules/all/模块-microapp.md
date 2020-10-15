


desc of microapp, 推荐使用  typora  编辑文档, 媒体文件,如图片必须存放在md的相对目录 assets 下 如`[](./a.png)`
 
## namespace
```
com.zkty.module.microapp
```


# api


`
com.zkty.module.microapp
`



## xxxx



	
**无参数**




## install



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appid | string |  | "" |  |
| version | string |  | "" |  |
| filePath | string |  | "" |  |


## clearInstallDir



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appid | string |  | "" |  |
| version | string |  | "" |  |
| filePath | string |  | "" |  |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-microapp
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-microapp
```


