

**基座扫描测试**
<div id='modulename' style='display:none'>ui</div>
<img id='qrimg' src='https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://192.168.44.52:3000/docs/modules/all/dist/ui/index.html'></img>



# JS


``` bash
npm install @zkty-team/com-zkty-module-ui
```



## showSuccessToast



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| tipContent | string |  | hello |  |
| duration | int |  | 3000 |  |
| icon | string |  | success | success; loading; |


## showFailToast



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| tipContent | string |  | hello |  |
| duration | int |  | 3000 |  |
| icon | string |  | success | success; loading; |


## showToast



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| tipContent | string |  | hello |  |
| duration | int |  | 3000 |  |
| icon | string |  | success | success; loading; |


## hideToast



	
**无参数**




## hiddenHudToast



	
**无参数**




## showLoading



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| tipContent | string |  | 加载提示 |  |


## hideLoading



	
**无参数**




## showModal



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| tipTitle | string | true | 弹窗标题 |  |
| tipContent | string |  | 弹窗内容 |  |
| showCancel | bool |  | true |  |


## showActionSheet



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | hello |  标题 |
| itemList | Array\<string\> | true | ["hello","world","he"] |  子标题? |
| content | string | true | content |  内容 |
| \_\_event\_\_ |  |  |  |  点击子标题回调函数 |


## showPickerView



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| leftText | string |  | 取消 |  tapIndex:string; |
| leftTextSize | int |  | 20 |  |
| leftTextColor | string |  | #3A6BEC |  |
| rightText | string |  | 确定 |  |
| rightTextSize | int |  | 20 |  |
| rightTextColor | string |  | #3A6BEC |  |
| backgroundColor | string |  | #1E1F20 |  |
| backgroundColorAlpha | string |  | 0.7 |  |
| pickerBackgroundColor | string |  | #f7f7f7 |  |
| pickerHeight | string |  | 450 |  |
| rowHeight | string |  | 44 |  |
| data | Array\<Array\<string\>\> |  | [["北京A","北京B","北京C","北京D","北京E","北京F"],["1街A","1街B","1街C","1街D","1街E","1街F"],["2街A","2街B","2街C","2街D","2街E","2街F"],["3街A","3街B","3街C","3街D","3街E","3街F"]] |  |
| toolBarBackgroundColor | string |  | #f5f5f5 |  |
| \_\_event\_\_ | string |  |  |  |

    

# iOS
ios hello


# android
## 


