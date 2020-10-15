


 
gradle read version from config file 
https://stackoverflow.com/questions/47492210/react-native-automatic-version-name-from-package-json-to-android-build-manifes
``` groovy 
// On top of your file import a JSON parser
import groovy.json.JsonSlurper

// Create an easy to use function
def getVersionFromNpm() {
    //  Read and parse package.json file from project root
    def inputFile = new File("$rootDir/../package.json")
    def packageJson = new JsonSlurper().parseText(inputFile.text)

    // Return the version, you can get any value this way
    return packageJson["version"]
}

android {
    defaultConfig {
        applicationId "your.app.id"
        versionName getVersionFromNpm()
    }
}
```

pod  config file 
https://stackoverflow.com/questions/21405457/autoincrement-versioncode-with-gradle-extra-properties


# api


`
com.zkty.module.bluetooth
`



## initBluetooth

初始化蓝牙

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| __event__ | string |  | null |  |


## scanBluetoothDevice

扫描蓝牙设备

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| __event__ | string |  | null |  |


## closeBluetoothDevice

关闭扫描

	
**无参数**




## linkBluetoothDevice

连接蓝牙设备

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| deviceID | string |  | "9E7A382F-1BBD-2431-D7B5-6415DDA4BEFB" |  |
| __event__ | string |  | null |  |


## cancelLinkBluetoothDevice

断开连接蓝牙设备

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| deviceID | string |  | "9E7A382F-1BBD-2431-D7B5-6415DDA4BEFB" |  |
| __event__ | string |  | null |  |


## discoverServices

获取蓝牙设备服务

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| deviceID | string |  | "9E7A382F-1BBD-2431-D7B5-6415DDA4BEFB" |  |
| __event__ | string |  | null |  |


## discoverCharacteristics

获取对应蓝牙设备服务的特征

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| deviceID | string |  | "1A5D368E-68E3-069F-D963-E3781097CCD1" |  |
| serviceId | string |  | "FFF0" |  |
| __event__ | string |  | null |  |


## writeValueForCharacteristic

向对应特征值写入数据

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| characteristicId | string |  | "FFF1" |  |
| __event__ | string |  | null |  |


## readCharacteristic

读取对应特征值

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| characteristicId | string |  | "FFF1" |  |
| __event__ | string |  | null |  |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-bluetooth
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-bluetooth
```


