# 组件 - UI交互反馈

- 我们为您提供了一系列的原生(iOS, Android)提示, 一定程度上提高用户体验, 让您更高的还原原生效果,使用更流畅。



### moudle.json

```json
{
  "module_id":"com.zkty.module.ui",
  "name":"UI",
  "tag": "1.0.0",
  "engine_version": "1.0.0",
  "minimal_os_version":{
    "ios": "1.0.0",
    "android_api": '1.0.0',
  }
}
```





---



## API 例表

### showLoading

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



### hideLoading

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



### showActionSheet

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



### showModal

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



### showToast

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


### hideToast

- 消息提示框。
- 函数声明
  - ui.hideToast()

**示例**	

```javascript
xengine.ui.hideToast();
```


