

  desc
我们为您提供了一系列的原生(iOS, Android)提示, 一定程度上提高用户体验, 让您更高的还原原生效果,使用更流畅。
## namespace
```
com.zkty.module.ui
```


# api


## showAlertAction
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| isAlert | string |  | "1" |  1:alert / 0:sheet |
| title | string | true | "title" | 标题, 第一行显示 |
| content | string | true | "content" | 内容, 第二行显示 |
| showCancel | bool |  | false | 是否显示取消 |
| btnItem | Array\<ZKUIBtnDTO\> |  | [{"title":"btn1","font":{"fontSize":"16"}}] | 按钮集合, 如果为空, 则默认增加[取消]按钮 |


## showLoading
	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "title" | 按钮文字 |
| font | ZKUIFontDTO |  | {"fontSize":"16"} | 字体 |
| __event__ | string | true |  | 回调方法, 如果为空, 则定义为cancel |


## hideLoading



	
**无参数**




## showModal



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| isAlert | string |  | "1" |  1:alert / 0:sheet |
| title | string | true | "title" | 标题, 第一行显示 |
| content | string | true | "content" | 内容, 第二行显示 |
| showCancel | bool |  | false | 是否显示取消 |
| btnItem | Array\<ZKUIBtnDTO\> |  | [{"title":"btn1","font":{"fontSize":"16"}}] | 按钮集合, 如果为空, 则默认增加[取消]按钮 |


## showToast



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "title" | 文字 |
| icon | string |  | "icon" | 图片 |
| duration | string |  | "1" | 显示时间毫秒 |


## hideToast



	
**无参数**




## showPickerView



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| toolBarBackgroundColor | string |  | "#f5f5f5" | 使用下述字段 |
| pickerBackgroundColor | string |  | "#f7f7f7" |  |
| backgroundColor | string |  | "#1E1F20" |  |
| backgroundColorAlpha | string |  | "0.7" |  |
| pickerHeight | number |  | 250 |  |
| rowHeight | number |  | 44 |  |
| leftText | string |  | "取消" |  |
| leftTextColor | string |  | "#0000FF" |  |
| leftTextSize | number |  | 20 |  |
| rightText | string |  | "确定" |  |
| rightTextColor | string |  | "#0000FF" |  |
| rightTextSize | number |  | 20 |  |
| data | Array\<Array\<string\>\> |  | [["1a","2b","3c"],["as","df","cd"]] |  |

      |

    


# iOS
ios hello


# android
## 


