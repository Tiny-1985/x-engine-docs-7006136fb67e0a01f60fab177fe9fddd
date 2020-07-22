# 组件 - UI交互反馈

- 在引擎中, 我们为您提供了一系列的原生(iOS, Android)提示, 一定程度上提高用户体验, 让使用更为流畅。



### moudle.json

```json
{
  "module_id":"com.zkty.net",
  "name":"UI",
  "tag": "1.0.0",
  "engine_version": "0.0.1",
  "minimal_os_version":{
    "ios": "11.1.0",
    "android_api": 20,
  }
}
```



## API 例表

### showLoading

- 显示 loading 提示框.
- 需主动调用 `xengine.ui.hideLoading`才能关闭提示框.
- 默认时间2000ms.

- 函数声明
  - ui.showLoading()

**示例**	

```javascript
xengine.ui.showLoading();// 显示提示框
xengine.ui.hideLoading();// 隐藏提示框
```

 

---



### showModal

- 显示模态弹窗，类似于标准 html 的消息框：alert、confirm。
- 函数声明
  - ui.showModal(Object)

**Object参数说明**	

|    参数    |   类型   | 必填 | 默认值 |          说明          |
| :--------: | :------: | :--: | :----: | :--------------------: |
|   title    |  string  |  否  |  ---   |       提示的标题       |
|  content   |  string  |  否  |  ---   |       提示的内容       |
| showCancel | Boolean  |  否  |  true  |    是否显示取消按钮    |
|  success   | Function |  否  |  ---   | 接口调用成功的回调函数 |
|    fail    | Function |  否  |  ---   | 接口调用失败的回调函数 |

**示例**	

```javascript
xengine.ui.showModal({ 
  title: "title", 
  content: "content", 
  showCancel: 'true'  // 显示取消按钮
});
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

**示例**	

```javascript
xengine.ui.showActionSheet({ 
  title: 'title',
  content: 'content',
  itemList : ['测试1','测试2','测试3','测试4','测试5']
}); 
```



---



### showToast

- 显示消息提示框。
- 函数声明
  - ui.showToast(Object)

**Object参数说明**		

|   参数   |  类型  | 必填 | 默认值 | 说明 |
| :------: | :----: | :--: | :----: | :--: |
|  title   | string | ---- |  ----  | ---- |
| duration | number | ---- |  2000  | ---- |

**示例**	

```javascript
xengine.ui.showToast({
  title: 'toast' 
});
xengine.ui.showSuccessToast({
  title:"成功"
});
xengine.ui.showFailToast({
  title:"失败"
});
```





待添加..............