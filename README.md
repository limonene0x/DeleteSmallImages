# 删除指定大小的图片

在实际应用中需要批量删除大小非常小的图片，但通过排序后批量选择的方式删除非常消耗时间（因为图片多的时候Windows Explorer排序很慢），因此开发批量删除工具。

### 输入要求

- <u>Please input width limit:</u>  会要求输入需要删除的图片宽度限制
- <u>Please input height limit:</u>  会要求输入需要删除的图片长度限制

删除时将会删除当前目录下宽度<=(小于等于)width limit并且长度<=(小于等于)height limit的*.jpg、.png、.jpeg*图片文件

## 使用方法（封装版本）

1. 将DeleteSmallImages.exe程序移动至要删除图片的文件夹下
2. 双击运行DeleteSmallImages.exe
3. 提示Please input width limit:时输入想删除的文件的最大**宽度**并回车
4. 提示Please input height limit:时输入想删除的文件的最大**长度**并回车
5. 文件删除完毕

## 注意事项

- **文件删除操作不可逆，请谨慎操作**

- 不放心删除结果可先在单独文件夹中测试，以免误删重要文件