SELECT * FROM hqr into CURSOR hqrtmp 
STORE ALLTRIM(hqrtmp.hqrname) TO hqrmc
SELECT LIST1
SELECT * FROM LIST1 INSERT INTO CURSOR PRINTLIST WHERE DELETED()=.F.
I=1
IF FILE(PATHH+"\report\yhfkmxtmp.xlsx") THEN
	DELETE FILE PATHH+"\report\yhfkmxtmp.xlsx"
ENDIF
COPY FILE PATHH+"\report\yhfkmx.xlsx" TO PATHH+"\report\yhfkmxtmp.xlsx"
EOLE=CREATEOBJECT("Excel.application")
EOLE.WORKBOOKS.OPEN(PATHH+"\report\yhfkmxtmp.xlsx",.F.,.F., ,"56971112","56971112")
EOLE.WORKSHEETS("fkmxb").ACTIVATE
SELECT PRINTLIST
REC=RECCOUNT()
GO TOP
I=1
SCAN
	EOLE.CELLS(5+I,1).VALUE='=row()-5'
	EOLE.CELLS(5+I,2).VALUE=ALLTRIM(PRINTLIST.���鵥��)
	EOLE.CELLS(5+I,3).VALUE=ALLTRIM(PRINTLIST.Ʒ��)
	EOLE.CELLS(5+I,4).VALUE=ALLTRIM(PRINTLIST.�ȼ�)
	EOLE.CELLS(5+I,5).VALUE=PRINTLIST.ˮ��
	EOLE.CELLS(5+I,6).VALUE=PRINTLIST.����
	EOLE.CELLS(5+I,7).VALUE=PRINTLIST.����
	EOLE.CELLS(5+I,8).VALUE=PRINTLIST.ʵ�����
	EOLE.CELLS(5+I,9).VALUE=ALLTRIM(PRINTLIST.����)
	EOLE.CELLS(5+I,10).VALUE=ALLTRIM(PRINTLIST.SLRXB)
	EOLE.CELLS(5+I,11).VALUE=ALLTRIM(PRINTLIST.����֤��)
*	EOLE.CELLS(5+I,12).VALUE=PRINTLIST.����-PRINTLIST.����
	EOLE.CELLS(5+I,13).VALUE=ALLTRIM(PRINTLIST.���)
*	EOLE.CELLS(5+I,14).VALUE=
	EOLE.CELLS(5+I,15).VALUE=ALLTRIM(PRINTLIST.�����˿���)
	I=I+1
ENDSCAN
STORE ALLTRIM(PRINTLIST.Ʒ��) TO pm
EOLE.CELLS(1,1).VALUE=ALLTRIM(DW_1)+pm+'��ʳ�ս�����ϸ��'
IF DATE1=DATE2 THEN
	EOLE.CELLS(2,1).VALUE=ALLTRIM(tTOC(DATE1))
ELSE
	EOLE.CELLS(2,1).VALUE=ALLTRIM(tTOC(DATE1))+'��'+ALLTRIM(tTOC(DATE2))
ENDIF
EOLE.CELLS(3,1).VALUE='����ˣ�'+hqrmc
EOLE.CELLS(5,1).VALUE='�ϼ�'
EOLE.CELLS(5,2).VALUE=REC
*!*	EOLE.CELLS(5,9).VALUE='=SUM(i5:i'+ALLTRIM(STR(ROUND(REC+4,0)))+')'
*!*	EOLE.CELLS(5,10).VALUE='=SUM(j5:j'+ALLTRIM(STR(ROUND(REC+4,0)))+')'
*!*	EOLE.CELLS(5,11).VALUE='=SUM(k5:k'+ALLTRIM(STR(ROUND(REC+4,0)))+')'
*!*	EOLE.CELLS(5,12).VALUE='=SUM(l5:l'+ALLTRIM(STR(ROUND(REC+4,0)))+')'
*!*	EOLE.CELLS(5,13).VALUE='=SUM(m5:m'+ALLTRIM(STR(ROUND(REC+4,0)))+')'
*!*	EOLE.CELLS(5,15).VALUE='=SUM(o5:o'+ALLTRIM(STR(ROUND(REC+4,0)))+')'
SELECT PRINTLIST
STORE 0 TO A9,A8
SUM (PRINTLIST.����) TO A7
SUM(PRINTLIST.ʵ�����) TO A6
SCAN
	STORE A9+(����*ˮ��) TO A9
	STORE A8+(����*����) TO A8
ENDSCAN
EOLE.CELLS(5,7).VALUE=A7
EOLE.CELLS(5,8).VALUE=A6
IF A8/A7>0 THEN
	EOLE.CELLS(5,6).VALUE=ROUND(A8/A7,2)
ENDIF
IF A9/A7>0 THEN
	EOLE.CELLS(5,5).VALUE=ROUND(A9/A7,2)
ENDIF
EOLE.ACTIVESHEET.RANGE('a'+ALLTRIM(STR(REC+6,20,0))+':p'+ALLTRIM(STR(REC+6,20,0))).MERGECELLS=.T.
EOLE.ACTIVESHEET.RANGE('a'+ALLTRIM(STR(REC+6,20,0))+':p'+ALLTRIM(STR(REC+6,20,0))).HORIZONTALALIGNMENT=2
EOLE.ACTIVESHEET.RANGE('a'+ALLTRIM(STR(REC+6,20,0))+':p'+ALLTRIM(STR(REC+6,20,0))).VERTICALALIGNMENT=2
EOLE.CELLS(REC+6,1).VALUE='      ��'+SPACE(28)+'        ��'+SPACE(28)+'פ��Ա��'+SPACE(28)+'���Ա��'
EOLE.ACTIVESHEET.RANGE('a5:p'+ALLTRIM(STR(ROUND(REC+5,0)))).BORDERS(1).LINESTYLE=1
EOLE.ACTIVESHEET.RANGE('a5:p'+ALLTRIM(STR(ROUND(REC+5,0)))).BORDERS(2).LINESTYLE=1
EOLE.ACTIVESHEET.RANGE('a5:p'+ALLTRIM(STR(ROUND(REC+5,0)))).BORDERS(3).LINESTYLE=1
EOLE.ACTIVESHEET.RANGE('a5:p'+ALLTRIM(STR(ROUND(REC+5,0)))).BORDERS(4).LINESTYLE=1
EOLE.VISIBLE=.T.
RELEASE EOLE