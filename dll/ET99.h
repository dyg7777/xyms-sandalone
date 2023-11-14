*- ====================================================================

typedef void* ET_HANDLE;

*- 1. 查找计算机上连接的 ET99 设备
*-EXTERN_C int WINAPI et_FindToken(unsigned char* pid,int* TokenCount);

*- 2. 打开指定的加密锁
*-EXTERN_C int WINAPI et_OpenToken(ET_HANDLE * hET99, unsigned char* pid, long index);


*- 3. 关闭指定的加密锁
*-EXTERN_C void WINAPI et_CloseToken(ET_HANDLE hET99);


*- 4. 验证PIN码
*-EXTERN_C int WINAPI et_Verify(ET_HANDLE hET99, int flag, unsigned char* pin);


*- 5. 读取加密锁内容
*-EXTERN_C int WINAPI et_Read(ET_HANDLE hET99, long offset, int Len, unsigned char* buffer);


*- 6. 写入加密锁内容
*-EXTERN_C int WINAPI et_Write(ET_HANDLE hET99, long offset, int Len, unsigned char* buffer);


*- 错误编码 ===========================================================
	
#define	  ET_SUCCESS				0x00			//函数执行成功
#define   ET_ACCESS_DENY            0x01			//访问被拒绝，权限不够
#define   ET_COMMUNICATIONS_ERROR   0x02			//通讯错误，没有打开设备
#define   ET_INVALID_PARAMETER      0x03			//无效的参数，参数出错
#define   ET_NOT_SET_PID            0x04			//没有设置PID
#define   ET_NOTFOUND_DEVICE	    0x05			//打开指定的设备失败
#define   ET_HEAD_ERROR             0x06			//硬件错误
#define   ET_UNKNOWN                0x07

