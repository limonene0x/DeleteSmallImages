# Delete the image of the specified size

In the practical application, it is necessary to delete images of very small size in batch, but it consumes a lot of time to delete them through batch selection after sorting (because Windows Explorer sort slowly when there are many images), so the development of batch deletion tool.

### input requirements

- <u>Please input width limit:</u> will require the input width limit to be deleted
- <u>Please input height limit:</u> will require the input length limit to be deleted

*.jpg,.png,.jpeg* image files with width <=(less than or equal to)width limit and length <=(less than or equal to)height limit are deleted

## How to use it (packaged version)

1. Move the DeleteSmallImages.exe program to the folder where you want to delete the image
2. Double-click to run DeleteSmallImages.exe
3. When "Please input width limit:", enter the maximum **width** of the file to be deleted
4. When "Please input height limit:", enter the maximun **height** of the file to be deleted
5. File deletion is completed

## Notes

- **File deletion operation is not reversible, please operate with caution**
- Test the results in a separate folder to avoid deleting important files by mistake