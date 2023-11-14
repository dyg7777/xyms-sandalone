Attribute VB_Name = "Module1"
Public Const ET_S_SUCCESS = &H0                                                        ' 操作成功*/
Public Const ET_E_KEY_REMOVED = &HF0000001                                            ' 设备未连接，或者被移除*/
Public Const ET_E_INVALID_PARAMETER = &HF0000002                                      ' 参数错误*/
Public Const ET_E_COMM_ERROR = &HF0000003                                             ' 通讯错误，例如数据传输超时*/
Public Const ET_E_INSUFFICIENT_BUFFER = &HF0000004                                    ' 缓冲区空间不足*/
Public Const ET_E_NO_LIST = &HF0000005                                                ' 没有找到设备列表*/
Public Const ET_E_DEVPIN_NOT_CHECK = &HF0000006                                       ' 开发商口令没有验证*/
Public Const ET_E_USERPIN_NOT_CHECK = &HF0000007                                      ' 用户口令没有验证*/
Public Const ET_E_RSA_FILE_FORMAT_ERROR = &HF0000008                                  ' RSA文件格式错误*/
Public Const ET_E_DIR_NOT_FOUND = &HF0000009                                          ' 目录没有找到*/
Public Const ET_E_ACCESS_DENIED = &HF000000A                                          ' 访问被拒绝*/
Public Const ET_E_ALREADY_INITIALIZED = &HF000000B                                    ' 产品已经初始化*/
Public Const ET_E_INCORRECT_PIN = &HF0000C00                                          ' 密码不正确*/
Public Const ET_E_DF_SIZE = &HF000000D                                                ' 指定的目录空间大小不够*/
Public Const ET_E_FILE_EXIST = &HF000000E                                             ' 文件已存在*/
Public Const ET_E_UNSUPPORTED = &HF000000F                                            ' 功能不支持或尚未建立文件系统*/
Public Const ET_E_FILE_NOT_FOUND = &HF0000010                                         ' 未找到指定的文件*/
Public Const ET_E_ALREADY_OPENED = &HF0000011                                         ' 卡已经被打开*/
Public Const ET_E_DIRECTORY_EXIST = &HF0000012                                        ' 目录已存在*/
Public Const ET_E_CODE_RANGE = &HF0000013                                             ' 虚拟机内存地址溢出*/
Public Const ET_E_INVALID_POINTER = &HF0000014                                        ' 虚拟机错误的指针 */
Public Const ET_E_GENERAL_FILESYSTEM = &HF0000015                                     ' 常规文件系统错误 */
Public Const ET_E_OFFSET_BEYOND = &HF0000016                                          ' 文件偏移量超出文件大小*/
Public Const ET_E_FILE_TYPE_MISMATCH = &HF0000017                                     ' 文件类型不匹配*/
Public Const ET_E_PIN_BLOCKED = &HF0000018                                            ' PIN码锁死*/
Public Const ET_E_INVALID_CONTEXT = &HF0000019                                        ' ETContext 参数错误*/
Public Const ET_E_ERROR_UNKNOWN = &HFFFFFFFF                                          ' 未知的错误*/

Public Const MAX_ATR_LEN = 16                                                         ' 最大ATR长度 */
Public Const MAX_ID_LEN = 8                                                           ' 最大硬件ID长度*/

Public Const ET_USER_PIN = &H0                                                        ' 用户PIN*/
Public Const ET_DEV_PIN = &H1                                                         ' 开发商PIN*/

Public Const ET_CREATE_NEW = &H0                                                      ' 创建新文件*/
Public Const ET_UPDATE_FILE = &H1                                                     ' 更新数据文件*/

Public Const ET_CREATE_ROOT_DIR = &H0                                                 ' 创建根目录*/
Public Const ET_CREATE_SUB_DIR = &H1                                                  ' 创建当前目录的子目录*/


Public Const ET_LED_UP = &H1                                                          ' LED灯亮*/
Public Const ET_LED_DOWN = &H2                                                        ' LED灯灭*/
Public Const ET_LED_WINK = &H3                                                        ' LED灯闪烁*/


Public Const ET_GET_DEVICE_TYPE = &H11                                                ' 获得设备类型*/
Public Const ET_GET_SERIAL_NUMBER = &H12                                              ' 获取硬件序列号*/
Public Const ET_GET_DEVICE_USABLE_SPACE = &H13                                        ' 获得设备空间大小*/
Public Const ET_GET_DEVICE_ATR = &H14                                                 ' 获得设备ATR*/
Public Const ET_GET_CUSTOMER_NAME = &H15                                              ' 获得客户号*/
Public Const ET_GET_MANUFACTURE_DATE = &H16                                           ' 获得生产日期*/
Public Const ET_GET_DF_AVAILABLE_SPACE = &H17                                         ' 获得当前目录的剩余空间*/
Public Const ET_GET_EF_INFO = &H18                                                    ' 获得指定文件信息*/
Public Const ET_GET_COS_VERSION = &H19                                                ' 获得COS版本信息*/
Public Const ET_GET_CURRENT_TIME = &H20                                               ' 获得时钟锁的当前时间
Public Const ET_GET_PRODUCT_NAMEID = &H32                                             ' 获取产品名称

Public Const ET_SET_DEVICE_ATR = &H21                                                 ' 设置设备ATR*/
Public Const ET_SET_TOKEN_TYPE = &H22                                                 ' 设置卡类型*/
Public Const ET_SET_SHELL_KEY = &H23                                                  ' 设置8字节外壳加密种子码*/

Public Const ET_RESET_DEVICE = &H31                                                   ' 复位设备*/


Public Const ET_TOKEN_TYPE_PKI = &H1                                                  ' 身份验证锁类型*/
Public Const ET_TOKEN_TYPE_DONGLE = &H2                                               ' 加密锁类型*/
Public Const ET_TOKEN_TYPE_EMPTY = &H4                                                ' 空锁类型*/


Public Const ET_DEFAULT_TRY = &HFF                                                    ' 默认重试次数（无限次）*/

Public Const ET_DEFAULT_DEV_PIN = "123456781234567812345678"
Public Const ET_DEFAULT_USER_PIN = "12345678"
Public Const ET_DEV_PIN_LEN = 24
Public Const ET_USER_PIN_LEN = 8


Public Const ET_EXCLUSIZE_MODE = 0                                                    ' 独占模式*/
Public Const ET_SHARE_MODE = 1                                                        ' 共享模式*/



Public Const FILE_TYPE_EXE = 0                                                        ' 可执行文件*/
Public Const FILE_TYPE_DATA = 1                                                       ' 数据文件*/
Public Const FILE_TYPE_RSA_PUBLIC = 2                                                 ' RSA 公钥文件*/
Public Const FILE_TYPE_RSA_PRIVATE = 3                                                ' RSA 私钥文件*/
Public Const FILE_TYPE_INTERNAL_EXE = 4                                               ' 可执行文件（不可读写）*/

  


Public Type ET_CONTEXT
    dwIndex                         As Long                 ' 设备索引，从0开始编号
    dwVersion                       As Long                 ' 版本号
    hLock                           As Long                 ' 设备句柄
    reserve(0 To 11)                As Byte                 ' 系统保留
    dwCustomer                      As Long                 '客户号
    bAtr(0 To MAX_ATR_LEN - 1)      As Byte                 ' ATR信息
    bID(0 To MAX_ID_LEN - 1)        As Byte                 ' ID号
    dwAtrLen                        As Long                 ' ATR长度
End Type

Public Type ET_MANUFACTURE_DATE
    byYear                      As Byte                      ' 年
    byMonth                     As Byte                      '月
    byDay                       As Byte                      '日
    byHour                      As Byte                      '时
    byMinute                    As Byte                      '分
    bySecond                    As Byte                      '秒
End Type

Public Type ET_DONGLE_TIME
    tm_sec                      As Long                      'seconds after the minute - [0,59]
    tm_min                      As Long                      'minutes after the hour - [0,59]
    tm_hour                     As Long                      'hours since midnight - [0,23]
    tm_mday                     As Long                      'day of the month - [1,31]
    tm_mon                      As Long                      'months since January - [0,11]
    tm_year                     As Long                      'years since 1900
    tm_wday                     As Long                      'days since Sunday - [0,6]
    tm_yday                     As Long                      'days since January 1 - [0,365]
    tm_isdst                    As Long                      'daylight savings time flag
End Type


Public Type ET_OPENINFO
    dwETOpenInfoSize    As Long
    dwShareMode         As Long
End Type

Public Type ET_CREATEDIRINFO
    dwETCreateDirInfoSize   As Long
    szAtr(0 To MAX_ATR_LEN - 1)           As Byte
End Type

Public Declare Function ETEnum Lib "ET199_32" ( _
                                        ByRef pETContextList As ET_CONTEXT, _
                                        ByRef pdwDeviceCount As Long _
                                        ) As Long
                                        
Public Declare Function ETOpen Lib "ET199_32" ( _
                                        ByRef pETCtx As ET_CONTEXT _
                                        ) As Long
                                        
Public Declare Function ETOpenEx Lib "ET199_32" ( _
                                        ByRef pETCtx As ET_CONTEXT, _
                                        ByRef pETOpenInfo As ET_OPENINFO _
                                        ) As Long

                                        
Public Declare Function ETClose Lib "ET199_32" ( _
                                        ByRef pETCtx As ET_CONTEXT _
                                        ) As Long
                                        
                                        
Public Declare Function ETControl Lib "ET199_32" ( _
                                        ByRef pETCtx As ET_CONTEXT, _
                                        ByVal dwCtlCode As Long, _
                                        ByRef pInBuffer As Any, _
                                        ByVal dwInBufferLen As Long, _
                                        ByRef pOutBuffer As Any, _
                                        ByVal dwOutBufferLen As Long, _
                                        ByRef pdwBytesReturned As Long _
                                        ) As Long

Public Declare Function ETCreateDir Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszDirID As String, _
                                            ByVal dwDirSize As Long, _
                                            ByVal dwFlags As Long _
                                            ) As Long
                                            
Public Declare Function ETChangeDir Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszPath As String _
                                            ) As Long
                                            
Public Declare Function ETEraseDir Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal szDirID As String _
                                            ) As Long

Public Declare Function ETVerifyPin Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByRef pbPin As Byte, _
                                            ByVal dwPinLen As Long, _
                                            ByVal dwPinType As Long _
                                            ) As Long
                                            
Public Declare Function ETChangePin Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByRef pbOldPin As Byte, _
                                            ByVal dwOldPinLen As Long, _
                                            ByRef pbNewPin As Byte, _
                                            ByVal dwNewPinLen As Long, _
                                            ByVal dwPinType As Long, _
                                            ByVal byPinTryCount As Byte _
                                            ) As Long


Public Declare Function ETWriteFile Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszFileID As String, _
                                            ByVal dwOffset As Long, _
                                            ByRef pBuffer As Any, _
                                            ByVal dwBufferSize As Long _
                                            ) As Long
                                            
Public Declare Function ETWriteFileEx Lib "ET199_32" Alias "ETWriteFile" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszFileID As String, _
                                            ByVal dwOffset As Long, _
                                            ByVal pBuffer As Long, _
                                            ByVal dwBufferSize As Long, _
                                            ByVal dwFileSize As Long, _
                                            ByRef pdwBytesWritten As Long, _
                                            ByVal dwFlags As Long, _
                                            ByVal bFileType As Byte _
                                            ) As Long
  
  
Public Declare Function ETExecute Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszFileID As String, _
                                            ByRef pInBuffer As Any, _
                                            ByVal dwInbufferSize As Long, _
                                            ByRef pOutBuffer As Any, _
                                            ByVal dwOutBufferSize As Long, _
                                            ByRef pdwBytesReturned As Long _
                                            ) As Long


Public Declare Function ETCreateDirEx Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszDirID As String, _
                                            ByVal dwDirSize As Long, _
                                            ByVal dwFlags As Long, _
                                            ByRef pCreateDirInfo As ET_CREATEDIRINFO _
                                            ) As Long

 
Public Declare Function ETCreateFile Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszFileID As String, _
                                            ByVal dwFileSize As Long, _
                                            ByVal bFileType As Byte _
                                            ) As Long

Public Declare Function PETWriteFile Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal lpszFileID As String, _
                                            ByVal lpszPCFilePath As String, _
                                            ByRef pdwFileSize As Long, _
                                            ByVal dwFlags As Long, _
                                            ByVal dwFileType As Byte, _
                                            ByRef pdwBytesWritten As Long _
) As Long

                                            

Public Declare Function ETGenRsaKey Lib "ET199_32" ( _
                                            ByRef pETCtx As ET_CONTEXT, _
                                            ByVal wKeySize As Integer, _
                                            ByVal dwE As Long, _
                                            ByVal lpszPubFileID As String, _
                                            ByVal lpszPriFileID As String, _
                                            ByRef pbPubKeyData As Any, _
                                            ByRef dwPubKeyDataSize As Long, _
                                            ByRef pbPriKeyData As Any, _
                                            ByRef dwPriKeyDataSize As Long _
                                            ) As Long
        
 Public Declare Function ETFormatErrorMessage Lib "ET199_32" ( _
                                            ByVal dwCode As Long, _
                                            ByRef lpszMessage As Any, _
                                            ByVal dwMsgBufLen As Long _
                                            ) As Long
                                            

Public Declare Function SendMessage Lib "user32" Alias "SendMessageA" (ByVal hwnd As Long, ByVal wMsg As Long, ByVal wParam As Long, lParam As Any) As Long

Public Declare Function PostMessage Lib "user32" Alias "PostMessageA" ( _
                                            ByVal hwnd As Long, _
                                            ByVal wMsg As Long, _
                                            ByVal wParam As Long, _
                                            ByVal lParam As Long _
                                            ) As Long

Public Declare Function DestroyWindow Lib "user32" ( _
                                            ByVal hwnd As Long _
                                            ) As Long

Public Declare Sub CopyMemory Lib "kernel32" Alias "RtlMoveMemory" ( _
                                            Destination As Any, _
                                            Source As Any, _
                                            ByVal Length As Long _
                                            )
                                            


Public Declare Function GetCurrentDirectory Lib "kernel32" Alias "GetCurrentDirectoryA" ( _
                                            ByVal nBufferLength As Long, _
                                            ByVal lpBuffer As String _
                                            ) As Long



