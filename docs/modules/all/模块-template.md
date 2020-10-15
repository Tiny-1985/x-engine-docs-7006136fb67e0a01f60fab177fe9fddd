



# api


`
com.zkty.module.xxxx
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
pod install x-engine-module-xxxx
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-xxxx
```


