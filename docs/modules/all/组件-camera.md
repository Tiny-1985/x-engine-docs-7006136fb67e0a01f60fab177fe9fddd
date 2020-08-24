




# api

```
npm install @zkty/camera
```

## openImagePicker

打开获取图片的选择方式，选择照相机或者相册

**示例**	

```javascript
xengine.camera.imagePicker({              
  allowsEditing:'False',//是否裁剪             
  savePhotosAlbum:'False',//是否保存到相册              
  cameraFlashMode:-1,//闪光灯 -1:关闭 0：自动 1:打开         
  cameraDevice:"back",//front:前置，back:后置        
});
```

**函数声明**

xengine.camera.openImagePicker(Object)

**Object参数说明**	

|      参数       |  类型  | 必填 | 默认值 |             说明             |
| :-------------: | :----: | :--: | :----: | :--------------------------: |
|  allowsEditing  |  Bool  |  否  | false  |       是否允许裁剪图片       |
| savePhotosAlbum |  Bool  |  否  | false  |      是否允许保存到相册      |
| cameraFlashMode | Number |  否  |   -1   |        是否开启闪光灯        |
|  cameraDevice   | String |  否  | "back" | 选取前置摄像头或者后置摄像头 |

**allowsEditing** 

- false表示不允许裁剪图片
- true表示允许裁剪图片
- 默认为false



**savePhotosAlbum** 

- false表示不允许保存到相册
- true表示允许保存到相册
- 默认为false



**cameraFlashMode** 

- 当打开相机时，选择闪光灯模式
- 只能传-1、0或者1
- -1表示闪光灯关闭模式
- 0表示闪光灯自动模式
- 1表示闪光灯开启模式
- 默认为-1



**cameraDevice** 

- 当打开相机时，选择前置摄像头或者后置摄像头拍取照片
- 只能传"back"或者"front"
- "back"表示选择后置摄像头
- "front"表示选择前置摄像头
- 默认为"back"



## getPhoto

获取图片，得到图片的地址

**示例**	

```javascript
xengine.camera.getPhoto({
  success: (res) => {       
    document.getElementsByClassName('photo')[0].setAttribute( 'src', res+'?w=100&h=100&q=0.5&bytes=1024');             
  },                
  fail: (error) => {                
    console.log('error', error);                
  }           
});
```

**函数声明**

xengine.camera.getPhoto()

**注意:**

- 获取到的图片地址可以拼接参数对图片进行处理

**success 参数说明**

| 参数 |  类型  |   说明   |
| :--: | :----: | :------: |
| res  | String | 图片地址 |

**fail 参数说明**

| 参数  | 类型  | 说明 |
| :---: | :---: | :--: |
| error | Error | 错误 |

**图片地址拼接参数说明**	

| 参数  |  类型  | 必填 | 默认值 |            说明            |
| :---: | :----: | :--: | :----: | :------------------------: |
|   w   | Number |  否  |  ---   |      指定缩略图的宽度      |
|   h   | Number |  否  |  ---   |      指定缩略图的高度      |
|   q   | Number |  否  |  ---   |      指定缩略图的质量      |
| bytes | Number |  否  |  ---   | 指定缩略图大小不超过多少kb |

**`w`和`h`**

- 指定`w`参数和`h`参数，得到新图的宽/高，不会比原图大，即本接口总是缩小图片
- 可以只指定`w`参数或只指定`h`参数，只指定`w`参数时，则新图高度会根据原图宽高比进行缩放，反之，只指定`h`参数同理。
- 不指定`w`参数和`h`参数，则得到原始图宽高

**`q`**

- `q`参数可以指定缩略图的质量，范围为`[0,1]`
- `q`参数默认值为1，即原始图质量
- 不指定`q`参数，则为默认值

**`bytes`**

- `bytes`参数指定缩略图大小限制在多少kb以内，单位为`kb`
- 不指定`bytes`参数，则为原始图大小	


# iOS


# android
hello android


