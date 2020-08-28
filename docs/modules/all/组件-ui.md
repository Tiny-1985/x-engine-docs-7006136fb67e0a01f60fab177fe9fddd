

  desc
我们为您提供了一系列的原生(iOS, Android)提示, 一定程度上提高用户体验, 让您更高的还原原生效果,使用更流畅。
## namespace
```
com.zkty.module.ui
```


# api

## showLoading

- 显示 loading 提示框.

- 需主动调用 `xengine.ui.hideLoading`才能关闭提示框.

- 默认时间2000ms.

- 函数声明
  
  - ui.showLoading(Object)
  

**Object参数说明**	

| 参数  |  类型  | 必填 | 默认值 |
| :---: | :----: | :--: | :----: |
| title | string |  是  |  ---   |

**示例**	

```javascript
xengine.ui.showLoading({
  title:'加载中'
});
```



---



## hideLoading

- 隐藏loading提示框
- 函数声明
  - ui.hideLoading()

**示例**

```javascript
xengine.ui.showLoading({
  title:'加载中'
});
  
setTimeout(function () {
  xengine.ui.hideLoading();
}, 2000);
```


---



## showActionSheet

- 显示操作菜单
- 函数声明
  
  - ui.showActionSheet(Object)
  
  

**Object参数说明**	

|   参数   |     类型      | 必填 | 默认值 |           说明           |
| :------: | :-----------: | :--: | :----: | :----------------------: |
| itemList | Array<string> |  是  |  ---   | 按钮的文字数组,最大长度6 |
|  title   |    string     |  否  |  ---   |        提示的标题        |
| content  |    string     |  否  |  ---   |        提示的内容        |
| success  |   Function    |  否  |  ---   |  接口调用成功的回调函数  |
|   fail   |   Function    |  否  |  ---   |  接口调用失败的回调函数  |

**success返回参数说明**

| 参数     | 类型   | 说明                                |
| -------- | ------ | ----------------------------------- |
| tapIndex | Number | 用户点击的按钮,从上到下顺序,从0开始 |

**示例**	

```javascript
// success / fail
xengine.ui.showActionSheet({
  itemList: ['A', 'B', 'C', 'D', 'E'],
  success: function (res) {
    console.log(res)
  },
  fail: function (error) {
    console.log(error)
  }
})

--------------

// promise
xengine.ui.showActionSheet({
  itemList: ['A', 'B', 'C', 'D', 'E'],
}).then((res) => {
  console.log(res)
}).catch((error) => {
  console.log(error)
})
```



---



## showModal

- 显示模态弹窗，类似于标准 html 的消息框：alert、confirm。
- 函数声明
  - ui.showModal(Object)

**Object参数说明**	

|    参数    |   类型   | 必填 | 默认值 |          说明          |
| :--------: | :------: | :--: | :----: | :--------------------: |
|   title    |  String  |  是  |  ---   |       提示的标题       |
|  content   |  String  |  否  |  ---   |       提示的内容       |
| showCancel | Boolean  |  否  |  true  |    是否显示取消按钮    |
|  success   | Function |  否  |  ---   | 接口调用成功的回调函数 |
|    fail    | Function |  否  |  ---   | 接口调用失败的回调函数 |



**success返回参数说明**

| 参数     | 类型   | 说明                 |
| -------- | ------ | -------------------- |
| tapIndex | Number | 取消返回0, 确定返回1 |

**示例**	

```javascript
// success / fail
xengine.ui.showModal({ 
  title: 'title',
  success: function (res) {
    console.log(res)
  },
  fail: function (error) {
    console.log(error)
  }  
})

--------------

// promise
xengine.ui.showModal({
  title: 'title' 
}).then((res) => {
  console.log(res)
}).catch((error) => {
  console.log(error)
})
```

---



## showToast

- 显示消息提示框。
- 函数声明
  - ui.showToast(Object)

**Object参数说明**		

|   参数   |   类型   | 必填 | 默认值 |            说明             |
| :------: | :------: | :--: | :----: | :-------------------------: |
|  title   |  String  |  是  |  ----  |         提示的标题          |
| duration |  number  |  否  |  2000  | 提示的延迟时间.默认：2000ms |
|   icon   |  String  |  否  |  ---   |    图标,有效值见下方说明    |
| success  | Function |  否  |  ---   |      接口成功回调函数       |
|   fail   | Function |  否  |  ---   |      接口失败回调函数       |

**icon值说明**

| 参数    | 说明         |
| ------- | ------------ |
| success | 显示成功图标 |
| loading | 显示加载图标 |
| none    | 不显示图标   |

**示例**	

```javascript
// success / fail
xengine.ui.showToast({
  title: 'title',
  icon: 'success',
  duration: '2000',
  success: (res) => {
    alert(res);
  },
  fail: (error) => {
    alert(error); 
  }
});


// Promise
const params = {
  title: 'title',
  icon: 'success',
  duration: '2000', 
}
xengine.ui.showToast(params).then((res)=>{
  alert(res)
}).catch((error) => {
  alert(error)  
})
```



---

## hideToast

- 消息提示框。
- 函数声明
  - ui.hideToast()

**示例**	

```javascript
xengine.ui.hideToast();
```



---



## showPickerView

- 嵌入页面的滚动选择器。
- 函数声明
  - ui.showPickerView(Object)

**Object参数说明**		

|          参数          |  类型  | 必填 | 默认值  |           说明            |
| :--------------------: | :----: | :--: | :-----: | :-----------------------: |
|          data          | Array  |  是  |  ----   |        见下方说明         |
| toolBarBackgroundColor | String |  否  | #f5f5f5 |   顶部toolBar的背景颜色   |
| pickerBackgroundColor  | String |  否  | #f7f7f7 |   pickerView的背景颜色    |
|    backgroundColor     | String |  否  | #1E1F20 | 承载pickerView的背景颜色  |
|  backgroundColorAlpha  | String |  否  |   0.7   |   0.1-->1.0的取值范围的   |
|      pickerHeight      | Number |  否  |   250   |       picker的高度        |
|       rowHeight        | Number |  否  |   44    |       每一条的高度        |
|        leftText        | String |  否  |  取消   |   toolBar左上角按钮文字   |
|     leftTextColor      | String |  否  |  blue   | toolBar左上角按钮文字颜色 |
|      leftTextSize      | Number |  否  |   20    | toolBar左上角按钮文字大小 |
|       rightText        | String |  否  |  确定   |   toolBar右上角按钮文字   |
|     rightTextColor     | String |  否  |  blue   | toolBar右上角按钮文字颜色 |

**data值说明**

- 由于屏幕宽度的限制目前只支持1-4组数据.

```javascript
data: [
	["北京A", "北京B", "北京C","北京D", "北京E", "北京F"],
	["1街A", "1街B", "1街C","1街D", "1街E", "1街F"],
	["2街A", "2街B", "2街C","2街D", "2街E", "2街F"],
	["3街A", "3街B", "3街C","3街D", "3街E", "3街F"],
]
```



**示例**	

```javascript
const params = {
  data: [
    ["北京A", "北京B", "北京C","北京D", "北京E", "北京F"],
    ["1街A", "1街B", "1街C","1街D", "1街E", "1街F"],
    ["2街A", "2街B", "2街C","2街D", "2街E", "2街F"],
    ["3街A", "3街B", "3街C","3街D", "3街E", "3街F"],           
  ],            
}
xengine.ui.showPickerView(params).then((res) => {
  console.log(res)  
})
```



---



## handlerPickerViewEnter

- 点击确定按钮的方法
- 函数声明
  - handlerPickerViewEnter()


```javascript
 xengine.ui.handlerPickerViewEnter({
   success: (res) => {
     alert(res.data);
   },
   fail: (error) => {
     alert('error', error); 
   }
 })
```





# iOS
ios hello


# android
## 


