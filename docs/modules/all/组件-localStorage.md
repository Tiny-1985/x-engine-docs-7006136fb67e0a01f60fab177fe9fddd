
# localStorage
### 文档示例

- 以actionSheet为例

```json
{
  "modules":[
    {
      "module_id":"com.zkty.ui",
      "name":"UI",
      "tag": "1.0.0",
      "engine_version": "1.0.0",
      "minimal_os_version":{
        "ios": "11.1.0",
        "android_api": 20
    }  
  }
}

```



### showActionSheet

- 显示操作菜单

- 函数声明

  - ui.showActionSheet(Object)

  - Object参数说明

| 参数     | 类型         | 必填 | 默认值 | 说明                     |
| -------- | ------------ | ---- | ------ | ------------------------ |
| itemList | Arra<string> | 是   | ---    | 按钮的文字数组,最大长度6 |
| title    | string       | 否   | ---    | 提示的标题               |
| content  | string       | 否   | ---    | 提示的内容               |
| success  | function     | 否   | ---    | 接口成功的回调函数       |
| Fail     | function     | 否   | ---    | 接口失败的回调函数       |



- 示例

```javascript
xengine.ui.showActionSheet({ 
  title: 'title',
  content: 'content',
  itemList : ['测试1','测试2','测试3','测试4','测试5']
});
```


# h5
## setLocalStorage

- 将数据存储在移动端指定的 key 中会覆盖掉原来该 key 对应的内容.

- 函数声明
  
  - localStorage.setLocalStorage(Object)
  

**Object参数说明**	

|  参数   |   类型   | 必填 | 默认值 |
| :-----: | :------: | :--: | :----: |
|   key   |  String  |  是  |  ---   |
|  data   |  Object  |  是  |  ---   |
| success | Function |  否  |        |
|  fail   | Function |  否  |        |

**示例**	

```javascript
const data = {
  name: 'cwz',
  age: 18,
}

// success / fail
xengine.localStorage.setLocalStorage({
  key: 'ud',
  data: data,
  success: (res) => {
    alert(res.result); 
  },
  fail: (error) => {  
    alert(error); 
  }  
})

// Promise
xengine.localStorage.setLocalStorage({
  key: 'ud',
  data: data
}).then(res => {
  alert(res.result);
}).catch(error => {
  alert(error);  
});
```



---



## getLocalStorage

- 从本地缓存中获取指定 key 对应的内容。
- 函数声明
  - localStorage.getLocalStorage(Object)

**Object参数说明**	

| 参数 |  类型  | 必填 | 默认值 |
| :--: | :----: | :--: | :----: |
| key  | String |  是  |  ---   |

**示例**

```javascript
const res = xengine.localStorage.getLocalStorage('ud');
alert(res);
```


---



## removeLocalStorage

- 从本地缓存中移除指定 key。
- 函数声明
  
  - localStorage.removeLocalStorage(Object)
  
  

**Object参数说明**	

| 参数 |  类型  | 必填 | 默认值 | 说明 |
| :--: | :----: | :--: | :----: | :--: |
| key  | String |  是  |  ---   | ---  |

**示例**

```javascript
// success / fail
xengine.localStorage.removeLocalStorage({
  key: 'ud',
  success: (res) => {
    alert(res.result) 
  },
  fail: (error) => {
    alert(error); 
  }  
});

// Promise
xengine.localStorage.removeLocalStorage({
  key: 'ud'
}).then(res => {
  alert(res.result) 
}).catch(error => {
  alert(error)  
})
```



# about test 

全局安装 mocha  或 jasmine
``` js
  npm install -g mocha
```



# iOS


# android
## 


