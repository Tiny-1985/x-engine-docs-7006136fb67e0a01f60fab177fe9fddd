


desc of tools, 推荐使用  typora  编辑文档, 媒体文件,如图片必须存放在md的相对目录 assets 下 如`[](./a.png)`
 
## namespace
```
com.zkty.module.tools
```


# api


`
com.zkty.module.tools
`



## noArgNoRet

 无参数无返回值

	
**无参数**




## noArgRetPrimitive

 无参数有 primitive 返回值

	
**无参数**




## noArgRetSheetDTO

 无参数有返回值

	
**无参数**




## haveArgNoRet



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "hello" |  标题 |
| itemList | Array\<string\> | true | ["hello","world","he"] |  子标题? |
| content | string | true | "content" |  内容 |
| __event__ |  |  | null |  点击子标题回调函数 |


## haveArgRetPrimitive

 have args ret primitive

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "hello" |  标题 |
| itemList | Array\<string\> | true | ["hello","world","he"] |  子标题? |
| content | string | true | "content" |  内容 |
| __event__ |  |  | null |  点击子标题回调函数 |


## haveArgRetSheetDTO

 have args ret Object

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "hello" |  标题 |
| itemList | Array\<string\> | true | ["hello","world","he"] |  子标题? |
| content | string | true | "content" |  内容 |
| __event__ |  |  | null |  点击子标题回调函数 |


## showActionSheet


系统弹出框： 

**demo** 
``` js 
ui.showActionSheet({
    title: "hello",
    itemList: ["a", "b", "c"],
    content: "content",
    __event__: null,
  })
```


	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "hello" |  标题 |
| itemList | Array\<string\> | true | ["hello","world","he"] |  子标题? |
| content | string | true | "content" |  内容 |
| __event__ |  |  | null |  点击子标题回调函数 |

    

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


