Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter
>>> import sqlite3
>>> c = sqlite3.connect('esofdb.db')
>>> c.execute('''CREATE TABLE produtos(id INT PRIMARY KEY NOT NULL, nomeP VARCHAR(255) NOT NULL, quantP INT, valorP FLOAT NOT NULL);''')
<sqlite3.Cursor object at 0x0280A6A0>
>>> c.execute('''CREATE TABLE clientes(id INT PRIMARY KEY NOT NULL, nomeC TEXT NOT NULL, contatoC STRING NOT NULL);''')
<sqlite3.Cursor object at 0x02831AA0>
>>> def adcproduto()
SyntaxError: invalid syntax
>>> def adcproduto():
	idP = input()
	nomeP = input()
	quantP = input()
	valorP = input()
	c.execute("INSERT INTO produtos VALUES(?, ?, ?, ?)"(idP, nomeP, quantP, valorP));
	c.commit()

	
>>> def adccliente():
	idC = input()
	nomeC = input()
	contatoC = input()
	c.execute("INSERT INTO clientes VALUES(?, ?, ?)"(idC, nomeC, contatoC));
	c.commit()

	
>>> def reporproduto():
	idP = input()
	novaq = input()
	c.execute("UPDATE produtos set quantP = ? where id = ?"(novaq, idP))
	c.commit()

	
>>> 
