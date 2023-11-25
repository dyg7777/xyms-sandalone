set proc to D:\xyms-sandalone\PRG\foxjson additive

* test table customer
create cursor customers (id n(5), name c(50), lastname c(50), phone c(30))
insert into customers values (1,'Ignacio','Gutierrez','(653)534-8800')
insert into customers values (2,'Antonio','Esparza','(81)8347-1411')
insert into customers values (3,'David','Flores','(653)534-2755')

function tableToJson
local nRecno,i,oObj, cRetVal,nRec
	if alias()==''
		return ''
	endif
	nRecno = recno()
	nRec = 1
	dimension aInfo[1]
	scan		
		oObj = newObject('myObj')
		for i=1 to fcount()
			oObj.set(Field(i),eval(Field(i)))
		next
		dimension aInfo[nRec]
		aInfo[nRec] = oObj
		nRec = nRec+1
	endscan
	goto nRecno
	cRetVal = json_encode(@aInfo)
	if not empty(json_getErrorMsg())
		cRetVal = 'ERROR:'+json_getErrorMsg()
	endif
return cRetVal


function recordToJson
local nRecno,i,oObj, cRetVal
	if alias()==''
		return ''
	endif
	oObj = newObject('myObj')
	for i=1 to fcount()
		oObj.set(Field(i),eval(Field(i)))
	next
	cRetVal = json_encode(oObj)
	if not empty(json_getErrorMsg())
		cRetVal = 'ERROR:'+json_getErrorMsg()
	endif
return cRetVal


* parse first record
*!*	? 'Json Representing for each customer'
*!*	select customers
*!*	scan
*!*		? recordToJson()
*!*	endscan

?
? 
? 'Now json represent of a whole table'
go top
aa=tableToJson()
?'aa'+aa