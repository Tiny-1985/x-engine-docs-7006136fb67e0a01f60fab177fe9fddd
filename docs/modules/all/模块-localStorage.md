

## desc
localstorage 会根据 host 自动加入 namespace.
默认情况:
http 微应用, 则会使用 host的倒序 作为 namespace.
离线 微应用, 则会使用 appid 作为 namespace.

也可以在调用函数时,传入namespace, 则优先使用




# api


`
com.zkty.module.localstorage
`



## setLocalStorage

 set

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| key | string |  | key |  |
| value | string |  | value |  |
| isPublic | bool |  |  |  |


## getLocalStorage

 get

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| key | string |  | key |  |
| isPublic | bool |  |  |  |


## removeLocalStorageItem

 remoteItem

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| key | string |  | all |  |
| isPublic | bool |  |  |  |


## removeLocalStorageAll

 remoteAll

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| key | string |  | all |  |
| isPublic | bool |  |  |  |

    

# iOS


# android
hello 


