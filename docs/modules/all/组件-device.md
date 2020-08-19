

# init
make init name="module_name"


# api

# getSystemInfo 
- 获取设备信息
- 函数说明
  - device.getSystemInfo(Object)

  

**Object参数说明**	

|    参数    |  类型  | 必填 | 默认值  |       说明       |
| :--------: | :----: | :--: | :-----: | :--------------: |
|   type    | String |  是  |   ---   |   获取设备信息的类型   |

**type传入参数说明**	

|    参数    |     类型      | 必填 |  默认值  |         说明         |
| :--------: | :-----------: | :--: | :------: | :------------------: |
| phoneType  |    String     |  否  |   ---    | 手机型号 |
| systemVersion |    String    |  否  | ---  |   系统版本   |
|    UDID    |    String     |  否  |  ---  |   唯一标识UDID   |
|  batteryLevel |    String     |  否  |  ---  |    电池电量    |
|  preferredLanguage |    String     |  否  |  ---  |    当前语言    |
|  screenWidth  |    String     |  否  | ---   |   屏幕的宽度    |
|  screenHeight |    String     |  否  | ---   |   屏幕的高度    |
|  safeAreaTop  |    String     |  否  | ---   |  安全区域上边距  |
| safeAreaBottom|    String     |  否  | ---   |  安全区域下边距  |
|  safeAreaLeft |    String     |  否  | ---   |  安全区域左边距  |
| safeAreaRight |    String     |  否  | ---   |  安全区域右边距  |
| statusHeight |    String     |  否  | ---   |  状态栏高度  |
| navigationHeight |    String     |  否  | ---   |  导航条高度  |
| tabBarHeight |    String     |  否  | ---   |  tabBar高度  |

**示例**
``` js
xengine.device.getSystemInfo({
  'type':'navigationHeight'
});
```


# iOS


# android
## 


