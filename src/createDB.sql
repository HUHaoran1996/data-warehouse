-- Creating database
drop database if exists INCOMEDB;
create database INCOMEDB;
use INCOMEDB;

-- Creating dimension tables
drop table if exists WorkClass;
create table WorkClass(
 classId int not null,
 textDecs char(20) null,
 constraint PK_CUSTOMER primary key(classId)
);


drop table if exists Education;
create table Education(
 educationId int not null,
 textDecs char(20) null,
 constraint PK_CUSTOMER primary key(educationId)
);


drop table if exists Marital;
create table Marital(
 maritalId int not null,
 textDecs char(30) null,
 constraint PK_CUSTOMER primary key(maritalId)
);


drop table if exists Occupation;
create table Occupation(
 occupationId int not null,
 textDecs char(30) null,
 constraint PK_CUSTOMER primary key(occupationId)
);


drop table if exists Relationship;
create table Relationship(
 relationshipId int not null,
 textDecs char(30) null,
 constraint PK_CUSTOMER primary key(relationshipId)
);


drop table if exists Race;
create table Race(
 raceId int not null,
 textDecs char(30) null,
 constraint PK_CUSTOMER primary key(raceId)
);


drop table if exists SEX;
create table SEX(
 sexId int not null,
 textDecs char(20) null,
 constraint PK_CUSTOMER primary key(sexId)
);


drop table if exists Country;
create table Country(
 countryId int not null,
 textDecs char(40) null,
 constraint PK_CUSTOMER primary key(countryId)
);


drop table if exists Age;
create table Age(
 ageId int not null,
 textDecs char(20) null,
 constraint PK_CUSTOMER primary key(ageId)
);


drop table if exists WorkingHours;
create table WorkingHours(
 workingHoursId int not null,
 textDecs char(20) null,
 constraint PK_CUSTOMER primary key(workingHoursId)
);


drop table if exists Income;
create table Income(
 incomeId int not null,
 textDecs char(20) null,
 constraint PK_CUSTOMER primary key(incomeId)
);


drop table if exists Income_Fact;
create table Income_Fact(
 userid int not null,
 ageId int null,
 workclassId int null,
 fnlwgt float null,
 educationId int null,
 education_num int null,
 maritalId int null,
 occupationId int null,
 relationshipId int null,
 raseId int null,
 sexId int null,
 capital_gain float null,
 capital_loss float null, 
 workinghoursId int null,
 countryId int null,
 incomeId int not null,
 constraint PK_CUSTOMER primary key(userid)
);