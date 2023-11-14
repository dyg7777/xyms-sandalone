SET MESSAGE TO '应用软件授权单位：'+DW_1+SPACE(2)+'收购单位税务登记号：'+SWDJ_1+SPACE(5)+'软件版本号：'+ALLTRIM(BBH_1)+SPACE(5)+'软件授权使用时间：'+ALLTRIM(DTOC(SQRQ_1))+SPACE(5)+'鑫奕科技引领粮食收储管理软件先锋。服务电话：13009854012  QQ:50037071'
IF SQRQ_1=DATE() THEN
	=MESSAGEBOX('授权最后日期，请及时联系供应商，以免影响正常使用软件',0,'授权提示')
ENDIF
IF SQRQ_1<DATE() THEN
	=MESSAGEBOX('授权超期，请联系软件供应商，或直接联系软件制造商--鑫奕科技',0,'授权提示')
ENDIF
