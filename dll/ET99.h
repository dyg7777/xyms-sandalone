*- ====================================================================

typedef void* ET_HANDLE;

*- 1. ���Ҽ���������ӵ� ET99 �豸
*-EXTERN_C int WINAPI et_FindToken(unsigned char* pid,int* TokenCount);

*- 2. ��ָ���ļ�����
*-EXTERN_C int WINAPI et_OpenToken(ET_HANDLE * hET99, unsigned char* pid, long index);


*- 3. �ر�ָ���ļ�����
*-EXTERN_C void WINAPI et_CloseToken(ET_HANDLE hET99);


*- 4. ��֤PIN��
*-EXTERN_C int WINAPI et_Verify(ET_HANDLE hET99, int flag, unsigned char* pin);


*- 5. ��ȡ����������
*-EXTERN_C int WINAPI et_Read(ET_HANDLE hET99, long offset, int Len, unsigned char* buffer);


*- 6. д�����������
*-EXTERN_C int WINAPI et_Write(ET_HANDLE hET99, long offset, int Len, unsigned char* buffer);


*- ������� ===========================================================
	
#define	  ET_SUCCESS				0x00			//����ִ�гɹ�
#define   ET_ACCESS_DENY            0x01			//���ʱ��ܾ���Ȩ�޲���
#define   ET_COMMUNICATIONS_ERROR   0x02			//ͨѶ����û�д��豸
#define   ET_INVALID_PARAMETER      0x03			//��Ч�Ĳ�������������
#define   ET_NOT_SET_PID            0x04			//û������PID
#define   ET_NOTFOUND_DEVICE	    0x05			//��ָ�����豸ʧ��
#define   ET_HEAD_ERROR             0x06			//Ӳ������
#define   ET_UNKNOWN                0x07

