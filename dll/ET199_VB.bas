Attribute VB_Name = "Module1"
Public Const ET_S_SUCCESS = &H0                                                        ' �����ɹ�*/
Public Const ET_E_KEY_REMOVED = &HF0000001                                            ' �豸δ���ӣ����߱��Ƴ�*/
Public Const ET_E_INVALID_PARAMETER = &HF0000002                                      ' ��������*/
Public Const ET_E_COMM_ERROR = &HF0000003                                             ' ͨѶ�����������ݴ��䳬ʱ*/
Public Const ET_E_INSUFFICIENT_BUFFER = &HF0000004                                    ' �������ռ䲻��*/
Public Const ET_E_NO_LIST = &HF0000005                                                ' û���ҵ��豸�б�*/
Public Const ET_E_DEVPIN_NOT_CHECK = &HF0000006                                       ' �����̿���û����֤*/
Public Const ET_E_USERPIN_NOT_CHECK = &HF0000007                                      ' �û�����û����֤*/
Public Const ET_E_RSA_FILE_FORMAT_ERROR = &HF0000008                                  ' RSA�ļ���ʽ����*/
Public Const ET_E_DIR_NOT_FOUND = &HF0000009                                          ' Ŀ¼û���ҵ�*/
Public Const ET_E_ACCESS_DENIED = &HF000000A                                          ' ���ʱ��ܾ�*/
Public Const ET_E_ALREADY_INITIALIZED = &HF000000B                                    ' ��Ʒ�Ѿ���ʼ��*/
Public Const ET_E_INCORRECT_PIN = &HF0000C00                                          ' ���벻��ȷ*/
Public Const ET_E_DF_SIZE = &HF000000D                                                ' ָ����Ŀ¼�ռ��С����*/
Public Const ET_E_FILE_EXIST = &HF000000E                                             ' �ļ��Ѵ���*/
Public Const ET_E_UNSUPPORTED = &HF000000F                                            ' ���ܲ�֧�ֻ���δ�����ļ�ϵͳ*/
Public Const ET_E_FILE_NOT_FOUND = &HF0000010                                         ' δ�ҵ�ָ�����ļ�*/
Public Const ET_E_ALREADY_OPENED = &HF0000011                                         ' ���Ѿ�����*/
Public Const ET_E_DIRECTORY_EXIST = &HF0000012                                        ' Ŀ¼�Ѵ���*/
Public Const ET_E_CODE_RANGE = &HF0000013                                             ' ������ڴ��ַ���*/
Public Const ET_E_INVALID_POINTER = &HF0000014                                        ' ����������ָ�� */
Public Const ET_E_GENERAL_FILESYSTEM = &HF0000015                                     ' �����ļ�ϵͳ���� */
Public Const ET_E_OFFSET_BEYOND = &HF0000016                                          ' �ļ�ƫ���������ļ���С*/
Public Const ET_E_FILE_TYPE_MISMATCH = &HF0000017                                     ' �ļ����Ͳ�ƥ��*/
Public Const ET_E_PIN_BLOCKED = &HF0000018                                            ' PIN������*/
Public Const ET_E_INVALID_CONTEXT = &HF0000019                                        ' ETContext ��������*/
Public Const ET_E_ERROR_UNKNOWN = &HFFFFFFFF                                          ' δ֪�Ĵ���*/

Public Const MAX_ATR_LEN = 16                                                         ' ���ATR���� */
Public Const MAX_ID_LEN = 8                                                           ' ���Ӳ��ID����*/

Public Const ET_USER_PIN = &H0                                                        ' �û�PIN*/
Public Const ET_DEV_PIN = &H1                                                         ' ������PIN*/

Public Const ET_CREATE_NEW = &H0                                                      ' �������ļ�*/
Public Const ET_UPDATE_FILE = &H1                                                     ' ���������ļ�*/

Public Const ET_CREATE_ROOT_DIR = &H0                                                 ' ������Ŀ¼*/
Public Const ET_CREATE_SUB_DIR = &H1                                                  ' ������ǰĿ¼����Ŀ¼*/


Public Const ET_LED_UP = &H1                                                          ' LED����*/
Public Const ET_LED_DOWN = &H2                                                        ' LED����*/
Public Const ET_LED_WINK = &H3                                                        ' LED����˸*/


Public Const ET_GET_DEVICE_TYPE = &H11                                                ' ����豸����*/
Public Const ET_GET_SERIAL_NUMBER = &H12                                              ' ��ȡӲ�����к�*/
Public Const ET_GET_DEVICE_USABLE_SPACE = &H13                                        ' ����豸�ռ��С*/
Public Const ET_GET_DEVICE_ATR = &H14                                                 ' ����豸ATR*/
Public Const ET_GET_CUSTOMER_NAME = &H15                                              ' ��ÿͻ���*/
Public Const ET_GET_MANUFACTURE_DATE = &H16                                           ' �����������*/
Public Const ET_GET_DF_AVAILABLE_SPACE = &H17                                         ' ��õ�ǰĿ¼��ʣ��ռ�*/
Public Const ET_GET_EF_INFO = &H18                                                    ' ���ָ���ļ���Ϣ*/
Public Const ET_GET_COS_VERSION = &H19                                                ' ���COS�汾��Ϣ*/
Public Const ET_GET_CURRENT_TIME = &H20                                               ' ���ʱ�����ĵ�ǰʱ��
Public Const ET_GET_PRODUCT_NAMEID = &H32                                             ' ��ȡ��Ʒ����

Public Const ET_SET_DEVICE_ATR = &H21                                                 ' �����豸ATR*/
Public Const ET_SET_TOKEN_TYPE = &H22                                                 ' ���ÿ�����*/
Public Const ET_SET_SHELL_KEY = &H23                                                  ' ����8�ֽ���Ǽ���������*/

Public Const ET_RESET_DEVICE = &H31                                                   ' ��λ�豸*/


Public Const ET_TOKEN_TYPE_PKI = &H1                                                  ' �����֤������*/
Public Const ET_TOKEN_TYPE_DONGLE = &H2                                               ' ����������*/
Public Const ET_TOKEN_TYPE_EMPTY = &H4                                                ' ��������*/


Public Const ET_DEFAULT_TRY = &HFF                                                    ' Ĭ�����Դ��������޴Σ�*/

Public Const ET_DEFAULT_DEV_PIN = "123456781234567812345678"
Public Const ET_DEFAULT_USER_PIN = "12345678"
Public Const ET_DEV_PIN_LEN = 24
Public Const ET_USER_PIN_LEN = 8


Public Const ET_EXCLUSIZE_MODE = 0                                                    ' ��ռģʽ*/
Public Const ET_SHARE_MODE = 1                                                        ' ����ģʽ*/



Public Const FILE_TYPE_EXE = 0                                                        ' ��ִ���ļ�*/
Public Const FILE_TYPE_DATA = 1                                                       ' �����ļ�*/
Public Const FILE_TYPE_RSA_PUBLIC = 2                                                 ' RSA ��Կ�ļ�*/
Public Const FILE_TYPE_RSA_PRIVATE = 3                                                ' RSA ˽Կ�ļ�*/
Public Const FILE_TYPE_INTERNAL_EXE = 4                                               ' ��ִ���ļ������ɶ�д��*/

  


Public Type ET_CONTEXT
    dwIndex                         As Long                 ' �豸��������0��ʼ���
    dwVersion                       As Long                 ' �汾��
    hLock                           As Long                 ' �豸���
    reserve(0 To 11)                As Byte                 ' ϵͳ����
    dwCustomer                      As Long                 '�ͻ���
    bAtr(0 To MAX_ATR_LEN - 1)      As Byte                 ' ATR��Ϣ
    bID(0 To MAX_ID_LEN - 1)        As Byte                 ' ID��
    dwAtrLen                        As Long                 ' ATR����
End Type

Public Type ET_MANUFACTURE_DATE
    byYear                      As Byte                      ' ��
    byMonth                     As Byte                      '��
    byDay                       As Byte                      '��
    byHour                      As Byte                      'ʱ
    byMinute                    As Byte                      '��
    bySecond                    As Byte                      '��
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



