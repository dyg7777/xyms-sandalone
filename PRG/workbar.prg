SET MESSAGE TO 'Ӧ�������Ȩ��λ��'+DW_1+SPACE(2)+'�չ���λ˰��ǼǺţ�'+SWDJ_1+SPACE(5)+'����汾�ţ�'+ALLTRIM(BBH_1)+SPACE(5)+'�����Ȩʹ��ʱ�䣺'+ALLTRIM(DTOC(SQRQ_1))+SPACE(5)+'���ȿƼ�������ʳ�մ���������ȷ档����绰��13009854012  QQ:50037071'
IF SQRQ_1=DATE() THEN
	=MESSAGEBOX('��Ȩ������ڣ��뼰ʱ��ϵ��Ӧ�̣�����Ӱ������ʹ�����',0,'��Ȩ��ʾ')
ENDIF
IF SQRQ_1<DATE() THEN
	=MESSAGEBOX('��Ȩ���ڣ�����ϵ�����Ӧ�̣���ֱ����ϵ���������--���ȿƼ�',0,'��Ȩ��ʾ')
ENDIF
