/*
 * Created for the online course on Udemy: "Working with Python® on Windows® and SQL Server® Databases"
 *
 * Course URL: 
 * https://www.udemy.com/course/python-windows-sql-server
 *
 * Author/Instructor: Artemakis Artemiou
 *
 * Disclaimer: This SQL script which is part of the online course on Udemy "Working with Python® on Windows® 
 * and SQL Server® Databasess", is intended to be used only for demo purposes. Do not 
 * use it for Production systems as it is simplified for demo purposes.
 */

use SampleDB2022_1a;
go

insert into tblSample1a
values (1,'test1'), (2,'test2');

create table tblSample1b(
id int,
code varchar(50));
go

insert into tblSample1b
values (1,'test1'), (2,'test2');
go