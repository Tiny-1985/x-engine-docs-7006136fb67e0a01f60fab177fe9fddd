
**localStorage**

hello localStorage


# api

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


# iOS


# android
hello 


