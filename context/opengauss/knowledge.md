# openGauss

## HCIA-openGaussV1.0TrainingMaterials.pdf

01 openGauss Overview

Huawei Confidential
1
Foreword

Database emerged in the 1960s as a new discipline for automating information management,
and has since become an important branch of computer science. Data processing and
database technology have found their way into more and more computer applications as
such applications have developed. And while a database is a product of data management,
data management is the core task involving a database. It involves data classification,
organization, encoding, storage, retrieval, and maintenance. This section describes the
development and features of the openGauss database.

Huawei Confidential
2
Objectives
Upon completion of this course, you will be able to:
Understand what a database is, as well as the history behind the development of the 
technology.
Be familiar with how the architecture of relational databases has evolved.
Understand the main applications for relational databases.
Understand where the openGauss database is positioned, and the history of its 
development.
Understand the technical specifications and basic functions of openGauss.

Huawei Confidential
3
Contents
1.
Database Overview
2.
Introduction to openGauss
3.
openGauss Technical Specifications
4.
Basic Functions

Huawei Confidential
4
What Is a Database?

Data is facts or statistics used to represent something for observation or analysis.

Data can represent carrier of information as symbols, text, numbers, voices, images, or videos. Data and information are inseparable and data is
basically a form of information. Data itself is meaningless. Data becomes information only when it is put to use.

Data in a computer system is expressed as various letters, digits, sounds, graphs, images, and more, which are formed through binary units "1" and
"0". Binary is converted into more conventional forms of data with processing.

Forms

Digital data: data consisting of discrete symbols, characters, and numerals. For example, statistics or measurement data stored on a computer.

Analog data: refers to a continuous range of values over an interval. This data takes a physical form, such as video, image, text, or audio.

Huawei Confidential
5
Database
A database is an, often large, collection of organized data that is stored in a computer, often for a long time, and with 
the ability to be accessed. Data in a database is organized, described, and stored according to a data model. The data in 
a database is efficient, relatively independent, and scalable, and can be accessed by various users.
Permanent
Organized
Sharable

Huawei Confidential
6
DBMS

A database management system (DBMS) consists of a collection of interconnected data and a set of programs used
to access the data. This dataset is usually called a database. The main purpose of DBMS is to provide a convenient
and efficient way to access database information.

A DBMS acts as an interface between a database and its users or programs, allowing users to retrieve, update, and
manage information in an organized and optimized manner. In addition, the DBMS helps monitor and control the
database and provides various management operations, such as performance monitoring, optimization, backup, and
recovery.

Typical database management systems include Oracle, Microsoft SQL Server, Access, MySQL, and PostgreSQL.

Huawei Confidential
7
DBMS - Functions

Data definition: The DBMS provides a data definition language (DDL), through which users can easily define data objects in a 
database.

Data manipulation: The DBMS also provides a data manipulation language (DML), which can be used by users to manipulate data 
and perform basic operations on the database, such as query, insert, delete, and modify.

Database operation management: The DBMS manages and controls the creation, operation, and maintenance of databases in a 
unified manner to ensure data security and integrity, concurrent use of data by multiple users, and and to ensure the system 
recovers after a fault.

Interfaces and tools for convenient and effective database access: Programmers can develop database applications through an 
interface. Database administrators (DBAs) can use tools to manage databases.

Database creation and maintenance: include the input and conversion of initial data to the database, the dump and restoration of 
the database, the reorganization of the database, and the performance monitoring and analysis. These functions are usually 
implemented in software.

Huawei Confidential
8
DBS

A database system (DBS) includes hardware and software. 
Hardware is there as storage through a medium such as a 
hard drive. It is also there to support the software, which 
mainly includes the DBMS, the operating system (OS) that 
supports the operation of the DBS, and the access 
technology that supports the application development in 
multiple languages.

The DBS is the sum of all the database components. A 
complete DBS consists of the database, DBMS, application 
development tool, application system, database 
administrator, and users.
Database
DBMS
Application development 
tool
Application system
User
User
User
Database
Administrator
OS
Developer

Huawei Confidential
9
Three Stages of Development: Data Management Technologies
Data management is to classify, organize, encode, query, and maintain various forms of data. It mainly goes through 
three stages: manual management, file system, and DBS, each of which has evolved towards reducing data redundancy, 
enhancing data independence, and facilitating data operations.
1950
1960
1970
1980
1990
2000
2010
2020
Manual 
management
File system
DBS
Hierarchical database
Network database
Relational database
Object-oriented database
NoSQL
NewSQL

Huawei Confidential
11
Comparison of Data Management at Different Stages

Each stage of data management has its own background and features, and the data management technology is 
continuously improving in each stage. The following table compares data management at the three stages.
Stage
Manual Management (Mid 1950s)
File System (Late 1950s to Mid 1960s)
DBS (Late 1960s)
Application
Scientific computing
Scientific computing and management
Management of large-scale data and distributed data
Hardware
No direct access storage devices
Tapes, disks, and magnetic drums
Large-capacity disks, erasable CD-ROMs, and tape drives 
supporting on-demand capacity expansion
Software
No dedicated management software
File system
DBS
Data Processing Method
Batch processing
Online real-time processing and batch 
processing
Online real-time processing, batch processing, and 
distributed processing
Data Manager
User/Program
File system
DBMS
Data Application and 
Extension
Oriented to a certain application, difficult 
to expand
Oriented to a certain application system, 
difficult to expand
Oriented to multiple application systems, easy to expand
Data Sharing
No sharing and high redundancy
Poor sharing and high redundancy
Good sharing and low redundancy
Data Independence
Poor data independence
Good physical independence but poor logical 
independence
High physical independence and good logical 
independence
Data Structuring
Unstructured data
Structured only within the record, but 
unstructured on the whole
Unified data model and overall structuring
Data Security
Application protection
File system protection
Comprehensive security protection

Huawei Confidential
12
Why Do We Use Databases?

A database can store data efficiently and orderly, enabling us to manage data more quickly and conveniently:
o
Databases can store a large amount of information, and therefore 
data, in a structured manner, facilitating effective retrieval and 
access by users.
o
The database can effectively maintain the consistency and 
integrity of data information and reduce data redundancy.
o
The database can meet the sharing and security 
requirements of applications. In most cases, data is stored 
in databases for security purposes.
o
The database technology can be easily and intelligently 
analyzed to produce new and useful information.

Huawei Confidential
13
Database Models

Since the middle of the 20th century, many interesting database models, such as hierarchical model, network model, and relational 
model, have emerged. Some database models are no longer used, while others are still playing a significant role.
Hierarchical model
Network model
Relational model

Huawei Confidential
15
Database Models: Hierarchical, Network, and Relational Models
Hierarchical model
Network model
Relational model
College
Major
Department
Teaching plan
Teacher
Class
Student
Course
College
Major
Department
Teaching plan
Teacher
Class
Student
Course
Select
ID
Name
Title
College
2001
Li San
Professor
Economic 
management
2002
Zhang Si
Lecturer
Software
2003
Wang Wu
Professor
Finance
Course No.
Course Name
Credit 
Hour
Credit
X2001
Economics
64
4
X2002
Finance
48
3
X2003
Software 
engineering
64
4
ID
Course No.
Semester
Max 
Classmates
2001
X2001
Spring
100
2003
X2002
Autumn
120
2002
X2003
Autumn
100
Teacher information
Class 
information
Tuple
Code (key)
Attribute
Course information

Relational model

It is based on a rigorous data concept.

Relationships must be normalized.

The component of a relationship must be 
an indivisible data item.

Network model

Allows more than one node to 
have no parent.

A node can have more than one 
parent.

Hierarchical model

If there is only one node that has no 
parent, the node is called "root".

All nodes except the root node have 
only one parent node.

Huawei Confidential
16
SQL

Structured Query Language (SQL) is the standard language for relational databases. SQL is a general-purpose and powerful
relational database language. It is a standard interface for accessing relational data and is also the basis for interoperation between
different database systems.

SQL is based on relational algebra and tuple relationship calculations. It integrates data query, data operations, data definition, and
data control functions. The scope of SQL includes data insertion, query, update, and deletion, database schema creation and
modification, and data access control.
1986
1989
1992
1999
2003
2008
2011
2016
2019
SQL-86
SQL-89
SQL-92
(SQL2)
SQL:1999
(SQL3)
SQL:2003
SQL:2008
SQL:2011
SQL:2016
SQL:2019
ANSI standardizes the SQL 
for the first time.
Added integrity 
constraints.
Most significant version.
Introduced the standard 
classification concept.
Standard developed by 
ANSI called ANSI-SQL
ISO started to develop 
SQL standards.
Version with the most 
significant change
Introduced XML and 
Window functions.
Introduced
TRUNCATE, etc.
Introduced
the time series 
database.
Introduced 
JSON.

Huawei Confidential
18
Transaction

A transaction is a logical unit of program execution, consisting of a series of operations for accessing or updating data in the system.
In computer terminology, a transaction usually refers to a database transaction.

A database transaction usually contains a sequence of read/write operations on the database. Transactions in a database
environment have two main purposes:

1. To provide a method for restoring the database operation sequence from a failure while keeping database consistency even in case of system 
failure.

2. To provide isolation between programs accessing a database concurrently, so that they do not interfere with one another.

Transaction status:

A transaction is atomic and is regarded as a whole. That is, it can only be in one of the following three states at any time: active, committed, and 
failed.
Active
Failed
Committed
End
Begin

Huawei Confidential
20

Atomicity

A transaction is the logical working unit of a database. Atomicity means 
that you guarantee that either all operations in the transaction succeed 
or none do. 

Consistency

This ensures that a transaction can only transit from one consistent 
state to another consistent state.

Isolation

This ensures that transactions do not interfere one another. That is, the 
internal operations and data used in a transaction are isolated from 
other transactions, and concurrent transactions do not affect each 
other.

Durability

Once a transaction is committed, changes made to data in the database 
are permanent. Operations or faults occurring after the commit do not 
affect the result of the transaction.
ACID Feature of Relational Databases
Atomicity
Consistency
Isolation
Durability
Transaction

Huawei Confidential
22
The History of Relational Database Development
Relational database theory
1970 E.F.Codd
System R
1973-1977
Ingres 
project
1974-?
SDL
1977-1979
RSI
1979-1983
Oracle
1983-
System R
1980-1982
DB2 1983-
Ingres
1982-
Infomix 1984-
Sybase 1984-
Postgres 95
1995-
SQL server 1992-
PostgresSQL
1997-
MySQL
1994-
Oracle
Exadata
DB2 9.7
Compatible with Oracle
Infomix UE
Sybase ASE
SQL server 2008
China-developed 
databases
Enterprise DB
Green Plum
MySQL 5.5
MySQL Cluster
Maria DB
Scale DB
Clustrix
H-store 2007-
Volt DB 2010
Oracle
IBM
IBM
SAP
Microsoft
Oracle
Oracle
MySQL
substitutes
Relational database 
theory
Scale-up improvement
SQL specifications and 
optimization
Enhanced reliability 
of OLAP MPP 
technology
In-memory DB, new hardware 
optimization, distributed 
deployment, and OLTP&OLAP 
convergence
1970s
1980s
1990s
2000s

Huawei Confidential
25
Database Challenges
The databases of large enterprises need to support very complex searches, with users expecting responses almost in real time. As such, database 
administrators often need to adopt various methods to help enterprises improve performance. Some of the common challenges they face include:

Sharp increase in data volume. The explosive growth of data from sensors, networked devices, and many other sources has kept database 
administrators busy with data management and organization.

Ensuring data security. Nowadays, data is everywhere posing great leakage risks, and hackers' attack methods are emerging. Therefore, it is 
more important than ever to ensure data security while ensuring that users can easily access data.

Meeting ever-changing requirements. In today's fast-growing business environment, enterprises need to access data in real time to make the 
best decisions in a timely manner and seize new opportunities.

Managing and maintaining databases and infrastructure. Database administrators need to continuously monitor problems in the database and 
perform preventive maintenance, application software upgrades, and patch installations. As databases become increasingly complex and data 
volumes increase, enterprises need to recruit more personnel to monitor and optimize databases, increasing costs.

Breaking the scalability limitation. In order to survive, modern enterprises must continue to develop, and the corresponding data management 
must keep pace with the times. However, it is often difficult for database administrators to predict the future data volume of an enterprise, 
especially if the database is deployed locally.

Huawei Confidential
26
NoSQL

NoSQL, short for Not Only SQL, is a DBMS different from traditional relational databases. NoSQL is used to store ultra-large-scale data. These types of 
databases do not require fixed storage modes and can be scaled out without extra operations. Based on the structuring method and application 
scenario, the databases are classified into the following types:

Key-value database oriented to high-performance concurrent read/write

Key-value databases feature high concurrent read/write performance. A key-value database is a database that stores data using key-value pairs. 
It is similar to the map in Java. The entire database can be regarded as a large map, and each key corresponds to a unique value.

Document database oriented to massive data access

The main feature of this database is that data can be quickly queried from a large amount of data. Document storage typically uses an internal 
notation that can be processed directly in the application, primarily in JSON. JSON documents can also be stored as plain text in a key-value store 
or in a relational DBS.

Search engine for content searching

The search engine is a NoSQL DBS that is used to search for data content. It is mainly used for quasi-realtime processing and analysis of massive 
data and can be used for machine learning and data mining.

Distributed database oriented to scalability

Huawei Confidential
28
NoSQL – CAP Theory

The basic demand of NoSQL is to support distributed storage. Strict consistency and availability need to be balanced.

CAP theory: A distributed system cannot meet consistency (C), availability (A), and partition fault tolerance (P) requirements at the same time, and 
can meet at most two of them. Partition fault tolerance is a basic requirement for a distributed system. Otherwise, the system cannot be called a 
distributed system. Therefore, a balance needs to be achieved between C and A.

Consistency
Consistency indicates that after the update operation is successful and 
the result is returned to the client, the data of all nodes at the same 
time is consistent. The notion of consistency is different from that in 
the ACID feature.

Availability
It means that a timely and correct response can be made for each 
request, but it is not guaranteed that the request result is based on 
the latest written data.

Partition tolerance
Partition fault tolerance means that a distributed system can still 
provide services that meet consistency and availability requirements 
when a node or network partition is faulty.
A
C
P
Pick Two
CA
AP
CP
RDBMSs Aster Data
(MySQL, Greenplum
PostgreSQL, vertica,
etc.)
Dynamo
Voldemort
Tokyo Cabinet
KAI
Cassandra
SimpleDB
CouchDB
Riak
BigTable
Hypertable
Hbase
MongoDB
Terrastore
Scalaris
BerkeleyDB
MemcacheDB
Redis
Relational
Key-Value
Column-Oriented/
Tabular
Document-Oriented
Data Model: 
Availability:
Each client can always 
read and write.
Consistency:
All clients 
always view 
the same data.
Partition Tolerance:
The system works well 
despite physical 
network partitions.

Huawei Confidential
29
NewSQL

NewSQL is defined as the development direction of next-generation databases, which refers to all various new scalable and high-performance 
databases. It has the massive storage management capability of the NoSQL database and the ACID feature and SQL convenience of the relational 
database.

Simply speaking, SQL + NoSQL = NewSQL. Although the internal structure of NewSQL systems varies greatly, all the NewSQL systems have three 
significant common features. They all support the relational data model, use SQL as the main interface, and meet the features of the distributed 
database.

The internal structure of NewSQL systems varies in supporting the relational database transaction feature and the distributed database feature. You 
can learn it from the architecture, SQL engine, and sharding mode aspects.

New architecture: Representative databases are Google Spanner, VoltDB, Clustrix and NuoDB which work on distributed nodes in a cluster, data 
is stored in shards, and SQL query is performed on shards on different nodes.

SQL engine: Representative databases are TokuDB and MemSQL. This type of databases has a highly optimized SQL engine.

Transparent sharding: Representative databases are ScaleBase, dbShards, and Scalearc. The system provides a sharding middleware layer. Data is 
automatically split and executed on multiple nodes.

Huawei Confidential
30
Relational Database Architecture
As the service scale increases, the amount of data stored in the database and the service pressure on the database 
increase. Therefore, the database architecture needs to be changed to provide stable and efficient data services for 
upper-layer applications.
Evolution 1: Separation of database read and write; evolution 2: Database vertical sharding; evolution 3: Database and 
table horizontal sharding.
Database architecture
Single node
Multi-node
Single node
Standalone 
system
Grouping
Sharding 
Master/Backup
Master/Slave
Multi-Master
Shared-Nothing/MPP

Huawei Confidential
31
Single Node
To prevent application services and database services from competing for resources, the single-node database 
architecture evolves from the single-host mode to the standalone mode, separating applications from data services. For 
application services, you can increase the number of servers, balance the load, and enhance the concurrent capability 
of the system.
Users
OS
Application
Database
Single host
Database server
Application
Database
Standalone system
Application 
server
Users

Advantage: centralized deployment and easy O&M.

Disadvantages:

Scalability: The single-node database architecture can only be 
scaled up. That is, the performance can only be improved by 
adding hardware configurations. However, the hardware 
resources that can be configured for a single host may reach the 
upper limit.

Single point of failure (SPOF): During scale-up, services need to be 
stopped. If a hardware fault occurs, the entire service is 
unavailable and even data is lost.

Single-node performance bottleneck
Scale up
Scale up

Huawei Confidential
32
Grouping - Master/Backup
Master/Backup architecture:

The database is deployed on two servers. The server that provides data read and write services is called the master server. The
other server uses the data synchronization mechanism to copy the data of the primary server, which is called a backup server. Only
one server provides data services at a time.

Advantages

No extra effort needs to be paid during application development against database 
faults.

Compared with the single-node architecture, this architecture improves data error 
tolerance.

Disadvantages

Resources are wasted. The master and backup servers have the same 
configuration. However, resources in the standby server are basically idle for a long 
time and cannot be utilized.

The performance pressure is still concentrated on a single node, which cannot 
solve the performance bottleneck problem.

When a fault occurs, the switchover between the master and backup servers 
requires manual intervention or monitoring.
Master
Backup
Synchronize data
Application
Application
Data read and 
write
Data read and 
write

Huawei Confidential
33
Grouping - Master/Slave
Master/Slave architecture

The deployment mode is similar to the master/backup mode. However, the backup server becomes the slave server and provides certain data
services. Pressures are balanced by read/write isolation:

Write, modify, and delete operations are performed on the write database (master server), and query requests are allocated to the read 
database (slave server).

Advantages

It improves resource utilization and applies to scenarios where read operations are more 
frequent than write operations.

In high-concurrency read scenarios, load balancing is employed to balance loads among 
servers.

The scalability of slave servers is flexible, and scaling does not affect services.

Disadvantages

There is a delay when data is synchronized to slave databases. As such, applications need to 
tolerate temporary inconsistency. This mode is not applicable to scenarios that have high 
consistency requirements.

The performance pressure of write operations is still concentrated on the master server.

If the master server is faulty, a master/slave switchover is required, where manual 
intervention requires response time and automatic switchover is complex.
Master
Slaves
Synchronize 
data
Application
Application
Write
Read

Huawei Confidential
34
Grouping - Multi-Master
Two database servers can function as the master and slave servers for each other.
Master/Slave
Master/Slave 
replication
Application
Application
Data read and 
write
Data read and 
write
Master/Slave

Advantages

This improves resource utilization and reduces the risk of SPOF.

Disadvantages

Data is written to both servers and must be synchronized bidirectionally. 
Bidirectional replication also causes latency, and data may be lost in 
extreme cases.

With the increase of database servers, the data synchronization 
becomes very complex. In actual practice, the two-server cluster mode is 
commonly used.

Huawei Confidential
35
Shared Disk
Shared disk is a special multi-master architecture. Database servers share data storage, and load 
balancing is implemented among multiple servers.

Advantages

Multiple compute servers are deployed providing high availability. 
Scalability is achieved, avoiding the SPOF of the server cluster.

Convenient scale-out can improve the parallel processing capability of 
the entire system.

Disadvantages

Difficult to implement.

When the storage interface bandwidth is saturated, adding servers 
does not improve performance. The storage I/O may become the 
performance bottleneck of the entire system.
Node 1
Application
Application
Data read and 
write
Data read and 
write
Node 2
Node 3
Shared disk
Network
SAN/FC

Huawei Confidential
36
Sharding

Sharding is a database architecture mode based on horizontal partitioning. In this mode, rows in a table are partitioned into different tables (called 
extents). Each extent has the same schema and columns, but each table has completely different rows. Similarly, the data stored in each extent is 
unique and independent of the data stored in other extents.

It may be helpful to understand from the aspect of relationship between horizontal partitioning and vertical partitioning. In a vertical partitioning 
table, all columns are separated and put into a new, distinct table. Data in each vertical shard (VS) is independent of data in all other shards, and each 
shard contains different rows and columns.
Employee ID
Name
Title
Course Name
College
2001
Li San
Professor
Economics
Economic 
management
2002
Zhang Si
Lecturer
Software engineering
Software
2003
Wang Wu
Professor
Finance
Finance
Original table
Employee 
ID
Name
Title
Course Name
2001
Li San
Professor
Economics
2002
Zhang Si
Lecturer
Software 
engineering
2003
Wang Wu
Professor
Finance
Employee 
ID
College
2001
Economic 
management
2002
Software
2003
Finance
Vertical shards
VS 1
VS 2
Employee 
ID
Name
Title
Course Name
College
2001
Li San
Professor
Economics
Economic 
management
2002
Zhang Si
Lecturer
Software 
engineering
Software
Employee 
ID
Name
Title
Course Name
College
2003
Wang Wu
Professor
Finance
Finance
Horizontal shards
HS 1
HS 2
Shard Key

Huawei Confidential
37
Shared Nothing

Each processing unit has its own CPU, memory, and hard disk, and these units
do not share resources, similar to the MPP mode. These processing units
communicate with each other using protocols, achieving better parallel
processing and scalability.

Nodes are independent of each other and each node processes its own data.
The processing results may be summarized and sent to the upper layer, or
transferred among different nodes.

The shared nothing system usually distributes its data to different databases on
multiple nodes (different computers process queries from different users) or
requires each node to retain its own application data backup by using some
coordination protocols. This is usually called database sharding.
DB 1
DB 2
DB 3
Storage
disks
Storage
disks
Storage
disks
...
...
Network
Proxy/Master

Huawei Confidential
38
Massively Parallel Processing (MPP)
MPP distributes tasks to multiple servers and nodes in parallel. After the calculation on each node is complete, the results of each
node are summarized to obtain the final result. It features high performance, high availability, and high scalability. It also provides
a cost-effective universal computing platform for hyperscale data management and is widely used to support various data
warehouse systems, BI systems, and decision support systems.
DB 1
DB 2
DB 3
Storage
disks
Storage
disks
Storage
disks
...
...
Network
Master
Standby 
Master
DB 1
DB 2
DB 3
Storage
disks
Storage
disks
Storage
disks
...
...
Network

Parallel task execution

Distributed data storage

Distributed computing

Scale-out

Shared nothing

Huawei Confidential
39
Typical Applications of Relational Databases
Online Transaction Processing (OLTP)
Online Analytical Processing (OLAP)
• OLTP is a typical application of traditional relational 
databases. It is a highly-available online system that 
processes basic and routine transactions, such as bank 
transactions, mainly with small-sized transactions and small-
sized queries.
• The OLTP system emphasizes on the database memory 
efficiency. When evaluating an OLTP system, check the 
number of transactions executed per second and the number 
of Execute SQL statements. It emphasizes the command rates 
of memory metrics, bound variables, and concurrent 
operations.
• OLAP is a typical application of the data warehouse system. 
It supports complex analysis, focuses on decision support, 
and provides query results that are easy to understand. In 
the OLAP system, the quantity of the executed statements 
is not an evaluation standard, because if the execution time 
of a statement is long, the read data is huge.
• The OLAP system focuses on data analysis. The evaluation 
standards are the throughput (bandwidth) of the disk 
subsystem, SQL execution duration, disk I/O, and 
partitioning.
Business processes
Business data warehouse
OLTP
OLAP
Process data 
transactions
Business policy
Analyze
Business decision-making
Operations data

Huawei Confidential
40
Comparison Between OLTP and OLAP
Item
OLTP
OLAP
Feature
Operation processing
Information processing
Orientation
Transaction
Analysis
User
Clerks, DBAs, and database professionals
Analysis and decision-making personnel
Purpose
Routine operations
Long-term information and decision-making support
Data
Current and latest
Maintained periodically
Summary
Original, highly detailed
Consolidated and integrated
Working unit
Short and simple transactions
Complex query
Access
Read/Write
Mostly read
Focus
Data input
Information output
Operation
Index or hash on the primary keyword
Large-scale scan
Number of access 
records
Dozens
Millions
DB scale
100 MB to GB
100 GB to TB
Advantages
High performance and availability
High flexibility and end user autonomy
Measurement
Transaction throughput
Query throughput and response time

Huawei Confidential
41
Contents
1.
Database Overview
2.
Introduction to openGauss
3.
openGauss Technical Specifications
4.
Basic Functions

Huawei Confidential
42
openGauss
High Reliability
Easy O&M
High Performance
High Security
As a leading database at enterprise level, openGauss is developed in collaboration with global partners. This multi-core-oriented open-
source relational database provides ultimate performance, full-link service and data security, AI-based tuning, and efficient O&M 
capabilities. openGauss is released under the Mulan Permissive Software License v2. It deeply integrates Huawei's years of R&D 
experience in the database field and continuously builds competitive features based on enterprise-level scenario requirements.

Huawei Confidential
43
openGauss Evolution
• Core data warehouse of bank G and 
commercial use of DWS on HUAWEI CLOUD
• Bank Z's core service system upgrade with 
the commercial database
• Supporting the commercial use of 30,000 
sets of Huawei's more than 40 flagship 
products, serving over 70 carriers and 2 
billion users worldwide
• GaussDB global release on May 15th, 
2019
• Building an ecosystem with global 
partners
• Compatible with mainstream industry 
ecosystems and complete 
interconnection with industries such as 
finance
• openGauss goes open source on June 
30, 2020.
2001 – 2011
Internal use
Productization
• Enterprise-level in-
memory database
Cloud & Open source
• Sharing enterprise-level data 
management capabilities
• Leading ecosystem 
construction
• Promoting the development 
of database education
Ecosystem building
Incubation for internal use
Joint innovation for 
productization
Ecosystem building
2011 – 2019
2019 – 2020
2021 – Future

Huawei Confidential
44
openGauss: Commercial Use + Internal Use + Open Source, Long-
Term Kernel Evolution
Customer
Single
kernel
Cloud database service
Computing industry ecosystem
GaussDB 100 cloud service
(distributed transactional database)
openGauss
Device 
Cloud
Huawei's internal service
Carrier
IT
GaussDB kernel development project
High performance
High availability
High security
openGauss
Huawei internal mappings, HUAWEI CLOUD GaussDB, and open-source openGauss share the code baseline.
HUAWEI CLOUD/Hybrid cloud
Government
Carrier
Finance
Public 
security
Large 
enterprise
Partner
openGauss
commercial edition

Huawei Confidential
46
openGauss Positioning
Value
Key features
openGauss provides multi-core ultimate performance, full-link service and data security, AI-based optimization, and efficient O&M capabilities.
Huawei works with partners to build world-leading enterprise-class open-source relational databases.
Users and Partners Access Enterprise-Class Database Capabilities
Full Openness

Adopts the Mulan Permissive 
Software License, allowing 
code to be freely modified, 
used, and referenced.

Opens database kernel 
capabilities.

Open O&M monitoring, 
development, and migration 
tools.

Open partner certification, 
training system, and university 
courses.
Easy O&M

Optimizes parameters using AI 
and automatically recommends 
AI parameters. 

Provides slow SQL diagnosis and 
multi-dimensional self-
monitoring to help you 
understand system performance 
in real time.

Provides online self-learning SQL 
time prediction, quick locating, 
and quick optimization.
③
High Performance

Two-channel Kunpeng
performance: 1,500,000 
tpmC;

Concurrency control 
technology for multi-core 
architecture;

NUMA-Aware data structure

SQL-Bypass intelligent traffic 
steering execution technology;

Memory engine for real-time 
high-performance scenarios;
①
④
High Availability & Security

Hitless service and RTO <10s;

Refined security 
management: fine-grained 
access control and multi-
dimensional audit;

All-round data protection: 
encrypted storage, 
transmission, and export, 
dynamic masking, and fully 
encrypted computing;
②
⑤

Huawei Confidential
47
Huawei Computing Business Strategy
Huawei
Partner
Empowering 
partners
Enable 90% of software to run on Kunpeng in three years.
•
Help partners migrate applications and software.
Open-
source 
software
Redistribute software profits to new ISVs and redefine the software value chain.
•
Open-source AI framework MindSpore
•
openLooKeng open-source data virtualization engine
•
openGauss open-source database (OLTP standalone edition), building a Kunpeng
database ecosystem
•
openEuler open-source OS, helping partners commercially release their OSs
Open 
hardware
Lower the threshold, change market trends, and redefine the value chain of 
the entire system
• Provides open boards and components (such as SSDs, NICs, and RAID 
controller cards) based on Huawei Kunpeng processors for partners to develop 
their own components, servers, and PCs.
Huawei's 
focus
•
Kunpeng processor R&D, all-scenario chips, and Kunpeng
cloud services
Mainboard
OS
Application
HUAWEI CLOUD
Processor
AI framework
Component
Device
Database
Middleware

Huawei Confidential
48
Comparing openGauss and PG
Storage engine
SQL Engine
SQL interface
SQL parser
SQL optimizer Parallel execution
AI self-tuning
ABO optimizer
In-DB ML
Extensible function 
framework
Database thread pool
MVCC row-store engine
In-memory 
engine
Column-store engine
Database main process
Database background processes
Writer
Log write
Vacuum
Statistics collection
Checkpoint
Archive
Multi-process shared memory pool
Database process n
...
Data cache
Xlog buffer
Key Differentiation Factor
openGauss
PostgreSQL
Transaction 
processing 
mechanism
Concurrency control
64-bit transaction ID. CSNs are used to resolve the dynamic 
snapshot expansion problem. The NUMA-Aware engine is 
optimized to resolve the "five big locks" problem.
Transaction IDs are wrapped around. The long-term running performance 
greatly fluctuates due to the ID wraparound period. Five big locks cause 
bottlenecks in transaction execution efficiency and multi-processor multi-
core scalability.
Logs and checkpoints Incremental checkpoint, with the performance fluctuation less 
than 5%
Full checkpoint, with the short-term performance fluctuation more than 
15%
Kunpeng NUMA
NUMA reconstruction, cache-line padding, and native spin-lock Weak NUMA multi-core capability; a single dual-CPU server < 600,000 
tpmC
Data storage and 
organization
Multi-engine
Row-store, column-store, and in-memory engines; DFV storage 
under development and in-place update
Row-store only
Query optimizer
Optimizer
Supports CBO to absorb optimization capabilities in large 
enterprise scenarios.
Supports CBO. The optimization capability in complex scenarios is average.
SQL parsing
ANSI/ISO standard SQL92, SQL99, SQL2003,
and enterprise extension package
ANSI/ISO standard SQL92, SQL99, and SQL2003
openGauss architecture
PostgreSQL architecture
VS

Huawei Confidential
49
openGauss Community: Jointly Building an Ecosystem and 
Discussing the Development Direction
openGauss's
open source 
announcement
openGauss community's
first meetup
Partner case release 
on HUAWEI CONNECT
The source code of 
openGauss is officially 
open
Key organizations 
within the 
community begin
work
2019-09-19
2020-08
2020-09
2020-06-30
2020-07
2021 – Now
The openGauss community 
certifies
user groups.
Operation progress
TC
Makes decisions regarding the technical 
development direction of the 
community.
Committers
Monitor the code quality and integrate 
code modifications.
Contributors
Raise requirements, send bug feedback, 
and implement relevant solutions 
through development.
Maintainers
Attend to the project code.
Community role
Technical Committee (TC)
SQL Engine
SIG
Organizational structure
Storage Engine
Connectors
Docs
Infra
Security
Source
548459
Total views
Total visitors
50675
Open-source protocol: Mulan PSL v2
•
Official website views: 548459l; visitors to the official website: 50675; 
downloads of the installation package on the official website: 68274
•
Followers of the official WeChat account: 1630; members of the 
WeChat group: 718
•
Community users D0 (IP addresses for downloading the installation 
package): 8024
•
Community participants D1 (Star, Fork, and Watch): 442
•
Community contributors D2 (committing issues and PRs): 239

Huawei Confidential
50
Contents
1.
Database Overview
2.
Introduction to openGauss
3.
openGauss Technical Specifications
4.
Basic Functions

Huawei Confidential
51
openGauss Architecture
Instance
maintain_work_mem
wal_mem
cstore buffer
MOT
temp buffer
wal buffer
Share buffer
wal_mem
wal_mem
wal_mem
wal_mem
...
jemalloc_bg_thd
Stat_collector
Auditor
LWLockMonitor
sysLogger
Jobworker
percentworker
snapshotworker
WalSender
WalReceiver
AutoVacLauncher
...
GaussDB thread
GaussDB thread
GaussDB thread
GaussDB thread
GaussDB thread
...
Pagewriter thread
Bgwriter thread
Walwriter thread
Checkpointer thread
GaussMaster thread
Background auxiliary 
process
postgresql.conf
pg_hba.conf
pg_ident.conf
gaussdb.state
Archived WAL
pg_audit
pg_replslot
pg_perf
Database
base
pg_xlog
pg_twophase
global
pg_clog
pg_serial
pg_tblspc
pg_csnlog
pg_multixact
Link driver
(JDBC/ODBC/Libpq)
Client

Huawei Confidential
52
openGauss Logic Modules
Large memory buffer 
management
NUMA-Aware data 
structure
Memory table
Index management
Parallel log replay
Lock manager
Column-store
Free space management
Log management
SQL execution
Incremental checkpoint
CSN snapshot
Row store (local update)
SQL parsing
SQL query rewriting
SQL optimization
Thread 
management
Service processing
Thread pool
Client driver
CLI
JDBC
ODBC
Log write thread
Data page write 
thread
Checkpoint thread
Statistics thread
Log sending thread
Log receiving thread
Cleanup thread
Manager thread
SQL engine
Storage engine
Security 
management
Identity 
management
Access control
Communication 
encryption
Audit
Archive thread
Universal 
component
Data dictionary
Memory 
management
Data type
Built-in function
Control command signal 
processing
Communication protocol 
processing
Communication 
management
DDL command processing
Stored procedure parsing
Storage management 
adaptation
Tools
Client
CLI tool
Database instance 
control tool
Physical backup/
restoration tool
Logical import/
export tool
OM installation
Hardware & OS platforms
ARM + openEuler
x86 + CentOS
Kernel
Common 
capabilities
OM&CM

Huawei Confidential
53
openGauss Query Optimization
Statistics
Row estimation
Cost estimation
Access path 
generation
Plan generation
Physical optimization, based on 
table/column-level statistics
Cost estimation, based on base 
table statistics
Execution cost of the current 
operator, calculated based on 
the number of relational rows
Access path, calculated based on 
the execution costs of several 
operators
Convert the queried execution 
path into PlanTree and output it to 
the executor for query execution.
Physical optimization technologies:
1. Table/Column-level statistics
Describes features of base table data, including unique values and 
MCV values, which are used to estimate the number of rows.
2. Row estimation
Estimates the size of the baserel, joinrel, and aggregation result sets 
to prepare for cost estimation.
3. Cost estimation
Estimates the execution costs of different operators based on the 
data volume. The sum of the costs of all operators is the total plan 
cost.
4. Access path generation
Solves the optimal path algorithm (for example, dynamic 
programming and genetic algorithm) to deal with the access path 
search process, with the minimum search space to find the optimal 
access path.

Huawei Confidential
54
openGauss Execution Engine
Scan
(Seq)
Sort
Merge 
join
Scan
(Index)
Union
Loop 
Join
Scan
(Seq)
Scan
(Seq)
The relational database is used to calculate relation sets, and the execution engine is 
used as the control logic of the calculation and is implemented based on the relational 
calculation. The operators can be classified as follows:
1.
Scan plan node
The scan node extracts data from the underlying data source, which may come 
from the file system or the network. Generally, the scan node is located on the 
leaf node of the execution tree and functions as the input source of execution 
data. Typical scan nodes include SeqScan, IndexScan, and SubQueryScan.
Key features: input data, leaf node, and expression filtering
2.
Control plan node
Generally, control operators do not map algebra operators, and are introduced by 
executors to complete some special processes, such as Limit, RecursiveUnion, and 
Union.
Key feature: used to control the data process
3.
Materialize plan node
These operators generally refer to algorithm requirements. When operator logic 
processing is performed, lower-layer data needs to be cached. As the amount of 
data returned by lower-layer operators cannot be predicted in advance, it is 
necessary to consider scenarios where data cannot be completely stored in the 
memory, such as Agg and Sort.
Key feature: Data is returned only after all data is scanned.
4.
Join plan node
These operators are used to deal with the most common join operations in the 
database. They are classified into MergeJoin, SortJoin, and HashJoin based on the 
processing algorithm and data source.
Key feature: multiple inputs

Huawei Confidential
55
openGauss Storage Engine
Query execution
Heap&Index access
Lock manager
Buffer pool manager
Transaction manager
Catalog data dictionary
Storage manager
File manager
Log manager
Disk
Redo logs

Huawei Confidential
56
Optimal Performance of openGauss on Multi-core Servers
DRAM
CPU 1
DIE 1
DIE 2
DRAM
DRAM
CPU 2
DIE 1
DIE 2
DRAM
1
2
3
4
hydra
hydra
Typical Kunpeng multi-core CPU architecture
Two Kunpeng chips with 128 cores: 1,500,000 tpmC
X86
鲲鹏
OLTP – TPCC Benchmark
1.5x
Note: When two x86 Intel Xeon 6148 processors are used in the lab environment (configurations are identical except for the processors), the 
performance of various databases is as follows: Oracle < 1 million tpmC; PG < 700,000 tpmC; MySQL < 500,000 tpmC
Kunpeng
x86

Huawei Confidential
57
openGauss Fully-encrypted Equality Query
Client encryption key (CEK) 
transmission based on trusted 
channels
•
Provides a plaintext environment that is 
isolated from the ciphertext
environment.
•
Provides SQL query and computing 
capabilities.
•
The data is stored in ciphertext
and cannot be decrypted.
•
Plaintext key information is not 
stored.
Intel x86/Huawei Kunpeng ARM
Trusted execution 
environment (TEE)
Rich execution 
environment (REE)
secGear
EulerOS/SuSE
GaussDB Kernel
ODBC/JDBC
Encryption driver (user side)
Data encryption 
and decryption
Ciphertext 
data
Ciphertext
data
Ciphertext data
Plaintext data
Encryption key
Trusted channel
Application API

Huawei Confidential
58
openGauss Technical Specifications
Technical Specifications
Maximum Value
Database capacity
Varies depending on the OS and hardware
Size of a single table
32 TB
Size of data in a single row
1 GB
Size of a single field in each record
1 GB
Number of records in each table
248
Number of columns in a single table
250 to 1600 (varies with field type)
Number of indexes on a single table
Unlimited
Number of columns contained in a composite index
32
Number of constraints in a single table
Unlimited
Number of concurrent connections
10000
Number of partitions in a partitioned table
32768 (range partitioning)/64 (hash or list partitioning)
Size of each partition in a partitioned table
32 TB
Number of records in a single partition of a partitioned 
table
255

Huawei Confidential
59
Contents
1.
Database Overview
2.
Introduction to openGauss
3.
Technical Specifications
4.
Basic Functions

Huawei Confidential
60
openGauss Supports Standard SQL

SQL is a standard programming language used to control the access to databases and manage data in 
databases. SQL:2011 standards are classified into core features and optional features. Most databases do 
not fully support SQL standards.

openGauss is a high-performance HA rational database that supports the SQL2003 standard and 
primary/standby deployment. In addition, openGauss supports most of the core features of SQL:2011 as 
well as some optional features, providing a unified SQL interface for users.

With standard SQL, all database vendors use unified SQL interfaces, reducing the costs associated with 
learning languages and migrating applications.

Huawei Confidential
61
openGauss Supports ODBC-based Development APIs

Open Database Connectivity (ODBC) is a Microsoft API used to access databases based on the X/OPEN CLI. Applications interact 
with the database through the APIs provided by ODBC, which enhances their portability, scalability, and maintainability.

openGauss supports ODBC 3.5 in the following environments.

The ODBC Driver Manager running on UNIX or Linux can be either unixODBC or iODBC. Select unixODBC-2.3.0 here as the component for 
connecting to the database.

Windows has a native ODBC Driver Manager. You can locate Data Sources (ODBC) by choosing Control Panel > Administrative Tools.
OS
Platform
CentOS 6.4/6.5/6.6/6.7/6.8/6.9/7.0/7.1/7.2/7.3/7.4
x86_64
CentOS 7.6
ARM64
EulerOS 2.0 SP2/SP3
x86_64
EulerOS 2.0 SP8
ARM64
OS Supported by ODBC
ODBC system structure
openGauss
Driver
ODBC Driver Manager
ODBC API
User application
Standard API
Driver management program
Driver program
Network

Huawei Confidential
62
openGauss Supports JDBC-based Development APIs

Java Database Connectivity (JDBC) is a Java API used to run SQL statements. It provides unified access APIs for 
different relational databases, based on which applications process data. The openGauss library supports JDBC 4.0 
and requires JDK 1.8 for code compiling. It does not support JDBC-ODBC bridging.
openGauss supports the JDBC 4.0 standard API.
Standard ODBC and JDBC APIs are provided to ensure quick migration of user services to openGauss.
A function to connect JDBC to a third-party log framework has been added, enabling JDBC to interconnect with a third-party 
log framework to meet the log management and control requirements of users.

Huawei Confidential
63
openGauss Database Transaction

Transaction ACID

Atomicity (A): ensures that each transaction is treated as a single "unit", which either succeeds completely, or fails completely.

Consistency (C): ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants.

Isolation (I): ensures that an unfinished transaction does not expose its result to subsequent other transactions before it is committed.

Durability (D): ensures that the result of a committed transaction will not be lost due to faults which occur later.

Example: Bank transfer (Zhang and Li transfer money to Wang.)
•
The ACID features ensure that Wang's account balance is CNY400 after the server 
restarts.
•
Atomicity: After Zhang cancels the transfer, the account balance of Wang is still 
CNY100.
•
Consistency: Li's account balance is CNY300 less, and Wang's is CNY300 more. The 
sum of the two accounts remains unchanged.
•
Isolation: The CNY200 transferred by Zhang is invisible to Li. Otherwise, the result is 
CNY700.
•
Durability: After the server is restored from a fault, Li's transfer is still valid.
•
Wang's account balance is CNY400.
Wang's account balance is 
CNY100.
Time (t)
Zhang transfers 
CNY200 to Wang.
Time t1
Time t3
Time t5
Server fault
Time t2
Li transfers CNY300 to 
Wang.
Zhang cancels the transfer, and 
the system rolls back the 
transaction.
Time t4
Li finishes the transfer, and 
the system commits the 
transaction.
Wang's account 
balance: CNY?

Huawei Confidential
64
openGauss Database Transaction Mechanism
1. Transaction durability is implemented by using the 
write-ahead log (WAL) algorithm. When a 
transaction is committed, a redo log is written to 
disks using the WAL method.
2. Checkpoint: Write the data in the dirty buffer 
queue to the data file.
Data buffer
Redo buffer
Data files
Redo log files
Data checkpoint 1
Checkpoint 1
Update 
1
Update 
2
Update 
3
1
1
2
3
2
3
1
2
3
Commit

Huawei Confidential
65
openGauss Supports Functions and Stored procedures

Functions and stored procedures are important database objects. They encapsulate SQL statement sets used for 
certain functions so that the statements can be easily invoked. openGauss supports functions and stored procedures 
compliant with the SQL standard. These stored procedures are compatible with certain mainstream stored 
procedure syntax, improving their usability and offering the following advantages:
Allows customers to modularize program design and encapsulate SQL statement sets, making them easy to invoke.
Caches the compilation results of stored procedures to accelerate SQL statement set execution.
Allows system administrators to restrict permission to execute a specific stored procedure and control access to the 
corresponding type of data. This prevents access from unauthorized users and ensures data security.

Huawei Confidential
66
openGauss Is Compatible with PG APIs

The basic PostgreSQL publication contains only two client APIs:
libpq is included because it is a C language API on which many other client APIs depend.
ECPG is included because it relies on the server-side SQL syntax and is therefore very sensitive to changes in 
PostgreSQL.

openGauss is compatible with the PostgreSQL clients and standard APIs, and can be seamlessly 
interconnected with PostgreSQL ecosystem tools.

Huawei Confidential
67
openGauss Supports SQL Hints

Plan hints enable you to specify a join order. You can also join, stream, and scan operations, the number 
of rows in a result, and redistribution skew information to tune an execution plan, improving query 
performance.

openGauss supports SQL hints, which can override any execution plan and thus improve SQL query 
performance.

Huawei Confidential
68
Quiz
1.
(Single-choice) Which of the following is not a component of a database system?
A.
Database:
B.
DBMS
C.
Database application
D.
Database storage medium
2.
(Single-choice) Which of the following statements about the ACID feature of database transactions is incorrect?
A.
A indicates atomicity, whereby operations in a transaction are either all successful or all failed.
B.
C refers to consistency, whereby the system status can only be the status before the transaction or after the transaction is
successful. No inconsistent intermediate status can occur.
C.
I refers to availability, whereby the database system must provide the highest availability possible for transaction execution in
order to ensure as many successfully executed transactions as possible.
D.
D refers to durability, whereby the status of a successful transaction can be maintained, even if the machine is powered off.

Huawei Confidential
69
Quiz
3.
(Multiple-choice) Which of the following phases are involved in the development of data management
technologies?
A.
Manual management
B.
File system
C.
DBS
D.
AI management

Huawei Confidential
70
Summary

This chapter describes database development and evolution, database classification and data models, 
database system composition, and the openGauss database. This document describes the database 
definition and technology development history, architecture evolution of relational databases, main 
application scenarios, development history of openGauss database, product positioning, basic 
indicators, and basic functions.

Huawei Confidential
71
Recommendations
HUAWEI CLOUD:
https://www.huaweicloud.com/
openGauss help document:
https://opengauss.org/zh/docs/2.0.0/docs/installation/installation.html
openGauss code repository:
https://gitee.com/opengauss

Huawei Confidential
72
Acronyms and Abbreviations
Acronym and Abbreviation
Full Spelling
DB
Database
DBMS
Database management system
DDL
Data definition language
DML
Data manipulation language
DBA
Database administrator
DBS
Database system
SQL
Structured query language
MPP
Massive parallel processing
OLTP
On-line transaction processing 
OLAP
On-line analytical processing
DWS
Data warehouse service
RTO
Recovery time objective
JDBC
Java Database Connectivity
ODBC
Open Database Connectivity
WAL
Write-ahead log
CLI
Command-line interface
tpmC
transactions per minute C

02 Database Installation and Deployment

Huawei Confidential
74
Foreword
openGauss is a relational database. It uses a client/server, single-process multi-thread 
architecture and supports standalone and one-primary multi-standby deployment. 
When primary/standby deployment is used, the standby node can be read too, and HA 
and read expansion are supported. This chapter describes how to set up the 
environment, how to install and deploy a database, and the functions and applications 
of openGauss-related O&M tools.

Huawei Confidential
75
Objectives
Upon completion of this course, you will:
Understand the installation and deployment of the openGauss database.
Understand openGauss database connection and authentication.
Understand the functions and operations of common openGauss database tools.
Understand how to uninstall an openGauss database.

Huawei Confidential
76
Contents
1.
openGauss Installation
2.
Connection and Authentication
3.
openGauss Tools
4.
Database Uninstallation

Huawei Confidential
77
openGauss Installation Process
Start
Prepare for installation.
Obtain the installation 
package.
Configure the XML file.
Upload the installation 
package and XML file.
Decompress the installation 
package.
Initialize the installation 
environment.
Perform the installation.
Set the standby node to 
readable.
End
Process
Description
Prepare for 
installation.
Before the openGauss installation, prepare the software and hardware environment 
and complete necessary configurations. This document provides the minimum 
requirements for the openGauss installation. 
Obtain the 
installation 
package.
You need to download the installation package from the openGauss open-source 
community and check the package content.
Configure the 
XML file.
Before installing openGauss, create an XML configuration file. The configuration file 
contains information about the server where openGauss will be deployed, the
installation path, IP address, and port. This file guides how to deploy the openGauss. 
You need to configure the XML configuration file based on deployment requirements.
Initialize the 
installation 
environment.
To initialize the installation environment, upload the installation package and the XML 
file, decompress the installation package, and use gs_preinstall to prepare the 
environment.
Perform the 
installation.
Use gs_install to install the openGauss.
Set the standby 
node to readable.
This operation is optional, but making the standby node readable improves data 
consistency.

Huawei Confidential
78
Obtaining the Installation Package

Step 1: Download the installation package of the corresponding platform from the openGauss open-source community.

Log in to the openGauss open-source community at https://opengauss.org/zh/download.html, select 2.0.0 in the Version field, and 
download the corresponding simplified installation package.

Click Download.

Step 2: Check the installation package. Decompress the package and confirm that installation directory is correct and all the files
are there.

Run the following command in the directory where the installation package is stored:

The ls command should display information similar to the following:
tar -jxf openGauss-x.x.x-openEuler-64bit.tar.bz2
ls -1b
total 90296 
drwx------ 3 root root
4096 Mar 31 21:18 bin 
drwx------ 3 root root
4096 Mar 31 21:18 etc
drwx------ 3 root root
4096 Mar 31 21:18 include 
drwx------ 4 root root
4096 Mar 31 21:18 jre
drwx------ 5 root root
4096 Mar 31 21:18 lib 
-rw------- 1 root root 92427499 Apr  1 09:43 openGauss-2.0.0-openEuler-64bit.tar.bz2 
drwx------ 5 root root
4096 Mar 31 21:18 share 
drwx------ 2 root root
4096 Mar 31 21:18 simpleInstall
-rw------- 1 root root
32 Mar 31 21:18 version.cfg

Huawei Confidential
79
Hardware Requirements

The following table lists the minimum hardware requirements for openGauss server. During hardware planning for the actual product, you have
to consider how much data will be involved and the database response speed you want to see.
Item
Configuration
Memory
It is recommended that there be at least 32 GB of memory available for function debugging.
In performance testing and commercial deployment, it is recommended that there be at least 128 GB of memory for single-instance deployment.
Complex queries require much more memory, so there may not be enough memory for high-concurrency scenarios. For high-concurrency scenarios, it 
is recommended that a large-memory server or load management be used to restrict concurrency on the system.
CPU
At least one 8-core 2.0 GHz CPU should be used for function debugging.
For performance testing and commercial deployment, a single 16-core 2.0 GHz CPU is recommended for single-instance deployment.
You can configure the CPUs for hyper-threading or non-hyper-threading.
For individual developers, the minimum configuration is 2 cores with 4 GB of memory, but the recommended configuration is 4 cores and 8 GB of 
memory. Currently, openGauss supports only the Kunpeng-powered servers and x86_64-based universal PC servers.
Disk
Hard disks used for installing openGauss must meet the following requirements:
•
At least 1 GB is used to install the openGauss applications.
•
Each host requires at least 300 MB for data storage.
•
More than 70% of the remaining space is used for data storage.
You are advised to configure the system disk to RAID 1 and data disk to RAID 5 and plan four groups of RAID 5 data disks for installing openGauss. RAID 
configurations are not described in this document. You can configure RAID by following instructions in the hardware vendor's manuals. Set Disk Cache 
Policy to Disabled to avoid data loss in the event of an unexpected power-off.
openGauss supports using an NVMe SSD with the SAS API deployed in RAID mode as the primary storage device of the database.
Network 
requirements
300 Mbit/s or faster Ethernet.
You are advised to bind two NICs for redundancy.

Huawei Confidential
80
Software Requirements and Dependencies
Software Type
Configuration
Linux operating 
system (OS)
• ARM: openEuler 20.3 LTS (recommended); Kirin V10
• x86: openEuler 20.3 LTS; CentOS 7.6
Note: Ensure that the OS language is set to English, or the installation 
package cannot be installed properly.
Linux file system
It is recommended that there be at least 1.5 billion available iNodes
remaining.
Tools
bzip2
Python
• openEuler: Python 3.7.X
• CentOS: Python 3.6.X
• Kirin: Python 3.7.X
Note: Python needs to be built using --enable-shared.
Software
Recommended Version
libaio-devel
0.3.109-13
flex
2.5.31 or later
bison
2.7-4
ncurses-devel
5.9-13.20130511
glibc-devel
2.17-111
patch
2.7.1-10
lsb_release
4.1
readline-devel
7.0-13
libnsl (in the openEuler + x86 
environment)
2.28-36
Dependencies
Software requirements

Huawei Confidential
81
Modifying OS Configurations (1)

Disable the OS firewall to ensure that the openGauss can be used properly when the firewall is enabled.

Step 1: Change the value of SELINUX in the /etc/selinux/config file to disabled.

1. Use vim to open the config file.

2. Change the value of SELINUX to disabled and enter :wq to save the change and exit.

Step 2: Reboot the system.

Step 3: Check whether the firewall is disabled.

If the firewall status is active (running), the firewall is not disabled. Go to step 4.

If the firewall status is inactive (dead), the firewall is disabled. Skip step 4.

Step 4: Disable the firewall.

Step 5: Repeat step 1 to step 4 on each host.
vim /etc/selinux/config
SELINUX=disabled
reboot
systemctl status firewalld
systemctl disable firewalld.service
systemctl stop firewalld.service

Huawei Confidential
82
Modifying OS Configurations (2)

Set the character set parameters.

Set the same character set for all database nodes. You can add export LANG=Unicode to the /etc/profile file.

Set the time zone and time.

Ensure that the time zone and time on each database node are consistent.

Step 1: Run the following command to check whether the time and time zone of each database node are consistent: If they are not, perform steps 2 to 3.

Step 2: Run the following command to copy the /etc/localtime file to the /usr/share/zoneinfo/ directory of each database node:

Step 3: Set the time of each database node to the same time. For example:
vim /etc/profile
export LANG=en_US.UTF-8
date
cp /usr/share/zoneinfo/$Locale/$Time zone /etc/localtime
date -s "Sat Sep 27 16:00:07 CST 2020"

Huawei Confidential
83
Modifying OS Configurations (3)

Disable RemoveIPC.

On each database node, disable RemoveIPC. In CentOS 7.6, RemoveIPC is disabled by default, and you can skip this step.

Step 1: Change the value of RemoveIPC in the /etc/systemd/logind.conf file to no.

Use vim to open the logind.conf file.

Change the value of RemoveIPC to no.

Step 2: Change the value of RemoveIPC in the /usr/lib/systemd/system/systemd-logind.service file to no.

Use vim to open the systemd-logind.service file.

Change the value of RemoveIPC to no.

Step 3: Reload the configuration parameters.

Step 4: Check whether the modification takes effect.

Step 5: Repeat steps 1 to 4 on each host.
vim  /etc/systemd/logind.conf
RemoveIPC=no
vim /usr/lib/systemd/system/systemd-logind.service
RemoveIPC=no
systemctl daemon-reload 
systemctl restart systemd-logind
loginctl show-session | grep RemoveIPC
systemctl show systemd-logind | grep RemoveIPC

Huawei Confidential
84
Modifying OS Configurations (4)

Set the NIC MTU.

Set the NIC MTU on each database node to the same value.

Step 1: Query the NIC name of the server:

In the example shown here, the server IP address is 10.244.53.173, and the NIC name for the server is eth0.

Step 2: Set the NIC MTU on each database node to the same value. For x86, the recommended MTU value is 1500. For ARM, the recommended MTU 
value is 8192.
ifconfig
ifconfig NIC name mtu value

Huawei Confidential
85
Enabling Remote Login for root

During openGauss installation, the root account is required for remote login. This section describes how to enable remote login for root.

Step 1: Modify the PermitRootLogin configuration to enable remote login as root.

Open the sshd_config file.

Modify permissions for root using either of the following methods:

Comment out PermitRootLogin no.

Change the value of PermitRootLogin to yes.

Run the :wq command to save the modification and exit.

Step 2: Modify the Banner configuration to delete the welcome information displayed when you connect to the system. The welcome information
affects remote operations during the installation.

Edit the sshd_config file.

Comment out the line where Banner is.

Run :wq to save the modification and exit.

Step 3: Restart sshd to make the settings take effect:

Step 4: Log in to the system as user root again.
vim /etc/ssh/sshd_config
#PermitRootLogin no
PermitRootLogin yes
vim /etc/ssh/sshd_config
#Banner XXXX
systemctl restart sshd.service
ssh xxx.xxx.xxx.xxx

Huawei Confidential
86
Installation User and User Group

To minimize the account permissions during the installation and ensure system security of openGauss after the installation is
complete, the installation script automatically creates a database installation user and this user will be used as the administrator
for subsequent operations and maintenance of the openGauss.

During openGauss installation, when gs_install is executed, a database user omm, with the same name as the installation user is
created. This user has the highest operation permissions on the database. The initial password of this user is specified by the user.
User/Group 
Name
Type
Planning Suggestions
dbgrp
OS
Plan a separate user group, for example, dbgrp.
The database installation user will belong to this group. This user group is specified by the -G parameter during 
installation environment initialization. If this user group does not exist, the installation script automatically creates it.
Alternatively, you can create a user group before the installation by running groupadd dbgrp. 
User permissions are checked when the gs_preinstall script is executed. The gs_preinstall script automatically grants 
access and execution permissions for the installation directory and data directory to all users in this user group.
omm
OS
You are advised to plan the user omm for openGauss operation and maintenance.
The user omm is the OS user specified by the -U parameter during initialization of the installation environment. If this 
user already exists, delete it or change the initial user. For security purposes, the group for this user is dbgrp.

Huawei Confidential
87
Installing openGauss – Installing openGauss on a Single Node (1)

Prerequisites

A user group and a common user have been created.

All the server OSs and networks are functioning properly.

Common users must have the read, write, and execute permissions on the database package decompression directory and installation directory, and the 
installation directory must be empty.

Common users have the execution permission for the downloaded openGauss package.

Before the installation, check whether the specified openGauss port is occupied. If the port is occupied, change the port number or stop the process that 
uses the port.

Procedure

Step 1: Log in to the host where the openGauss package is installed as a common user and decompress the openGauss package to the installation 
directory.

Step 2: Assuming the decompressed package is stored in /opt/software/openGauss, go to the simpleInstall directory.

Step 3: Run the install.sh script to install openGauss.
tar -jxf openGauss-x.x.x-openEuler-64bit.tar.bz2 -C /opt/software/openGauss
cd /opt/software/openGauss/simpleInstall
sh install.sh  -w xxxx

Huawei Confidential
88
Installing openGauss – Installing openGauss on a Single Node (2)

Procedure

Step 4: After the installation is complete, use ps and gs_ctl to check whether the process is normal.
Running ps command should display information similar to the following:
Running gs_ctl should display information similar to the following:
>> ps ux | grep gaussdb 
omm      24209 11.9  1.0 1852000 355816 pts/0  Sl   01:54   0:33 /opt/software/openGauss/bin/gaussdb -D 
/opt/software/openGauss/single_node 
omm      20377  0.0  0.0 119880  1216 pts/0    S+   15:37   0:00 grep --color=auto gaussdb
>> gs_ctl query -D /opt/software/openGauss/data/single_node
gs_ctl query ,datadir is /opt/software/openGauss/data/single_node
HA state: 
local_role
: Normal 
static_connections
: 0 
db_state
: Normal 
detail_information
: Normal 
Senders info: 
No information 
Receiver info: 
No information

Huawei Confidential
89
Installing openGauss – Installing openGauss on One Primary Node and One 
Standby Node (1)

Prerequisites

A user group and a common user have been created.

All the server OSs and networks are functioning properly.

Common users must have the read, write, and execute permissions on the database package decompression directory and installation directory, and the 
installation directory must be empty.

Common users must have the execution permission on the downloaded openGauss package.

Before the installation, check whether all ports in the specified openGauss port matrix are occupied. If they are occupied, change the ports or stop the 
processes that use the ports. For details about the port number, see the parameter description in step 3.

Procedure

Step 1: Log in to the host where the openGauss package is installed as a common user and decompress the package to the installation directory.

Step 2: Assuming that the decompressed package is stored in the /opt/software/openGauss directory, go to the simpleInstall directory.

Step 3: Run the install.sh script to install openGauss.
tar -jxf openGauss-x.x.x-openEuler-64bit.tar.bz2 -C /opt/software/openGauss
cd /opt/software/openGauss/simpleInstall
sh install.sh  -w xxxx --multinode

Huawei Confidential
90
Installing openGauss – Installing openGauss on One Primary Node and One 
Standby Node (2)

Procedure

Step 4: After the installation is complete, use ps and gs_ctl to check whether the process is normal.
Running ps should display information similar to the following:
>> ps ux | grep gaussdb
omm 4879 11.8 1.1 2082452 373832 pts/0  Sl
14:26   8:29 /opt/software/openGauss/bin/gaussdb -D 
/opt/software/openGauss/data/master -M primary 
omm 5083  1.1  0.9 1819988 327200 pts/0  Sl
14:26   0:49 /opt/software/openGauss/bin/gaussdb -D 
/opt/software/openGauss/data/slave -M standby 
omm
20377  0.0  0.0 119880  1216 pts/0    S+   15:37   0:00 grep --color=auto gaussdb

Huawei Confidential
91
Installing openGauss – Installing openGauss on One Primary Node and One 
Standby Node (3)

Procedure

Step 5: After the installation is complete, use ps
and gs_ctl to check whether the process is 
normal. Running gs_ctl should display 
information similar to the right:
>> gs_ctl query -D /opt/software/openGauss/data/master
gs_ctl query ,datadir is /opt/software/openGauss/data/master 
HA state: 
local_role
: Primary 
static_connections
: 1 
db_state
: Normal 
detail_information
: Normal 
Senders info: 
sender_pid
: 5165 
local_role
: Primary 
peer_role
: Standby 
peer_state
: Normal 
state                          : Streaming 
sender_sent_location
: 0/4005148 
sender_write_location
: 0/4005148 
sender_flush_location
: 0/4005148 
sender_replay_location
: 0/4005148 
receiver_received_location
: 0/4005148 
receiver_write_location
: 0/4005148 
receiver_flush_location
: 0/4005148 
receiver_replay_location
: 0/4005148 
sync_percent
: 100% 
sync_state
: Sync 
sync_priority
: 1 
sync_most_available
: Off 
channel                        : 10.244.44.52:27001-->10.244.44.52:35912 
Receiver info: 
No information

Huawei Confidential
92
Starting and Stopping openGauss

Starting openGauss

Step 1: Log in to the primary database node as omm.

Step 2: Start openGauss:

Stopping openGauss

Step 1: Log in to the primary database node as omm.

Step 2: Stop openGauss:
gs_om -t start
gs_om -t stop
>> gs_om -t start 
Starting cluster. 
========================================= 
========================================= 
Successfully started. 
>> gs_om -t stop 
Stopping cluster. 
========================================= 
Successfully stopped cluster. 
========================================= 
End stop cluster.
Start openGauss:
Stop openGauss:

Huawei Confidential
93
Contents
1.
openGauss Installation
2.
Connection and Authentication
3.
openGauss Tools
4.
Database Uninstallation

Huawei Confidential
94
Setting the Client Authentication Policy

The current default values for parameters in the openGauss configuration file (pg_hba.conf) are all for standalone deployment. Applications can set
parameters as needed by invoking gs_guc. For more details, see Developer Guide. Set the client authentication policy and send semaphores to the
database process.
gs_guc [ set | reload ] [-N NODE-NAME] [-I INSTANCE-NAME | -D DATADIR] -h "HOSTTYPE DATABASE 
USERNAME IPADDR-WITH-IPMASK AUTHMEHOD authentication-options" 
•
set
Modifies only parameters in the configuration file.
•
reload
Modifies the parameters in the configuration file and sends 
semaphores to the database process for reloading the 
configuration file.
•
-N
Specifies the name of the host to be set.
Value: the name of the existing host
When this parameter is set to ALL, all the hosts in 
openGauss are configured.
•
-I INSTANCE-NAME
Specifies the name of the instance to be configured.
Value: the name of the existing instance
When this parameter is set to ALL, all the instances in the 
host are to be set.
•
-D
Specifies the openGauss instance directory where the 
command is run. When the encrypt command is used, this 
parameter indicates the directory where the generated 
password file is stored.
• -h host-auth-policy
Specifies the client authentication policy added to the pg_hba.conf configuration file. Values 
supported:
o HOSTTYPE DATABASE USERNAME IPADDR IPMASK [authentication-options]
o HOSTTYPE DATABASE USERNAME IPADDR-WITH-IPMASK [authentication-options]
o HOSTTYPE DATABASE USERNAME HOSTNAME [authentication-options ]
The HOSTTYPE parameter is mandatory and can be set to any of the following values:
o Local
o Host
o Hostssl
o hostnossl
local is a Unix domain socket. host is a common or SSL-encrypted TCP/IP socket. hostssl is an 
SSL-encrypted TCP/IP socket. hostnossl is a TCP/IP-only socket. The authentication-options
parameter is optional and can be set to any of the following values:
o trust
o reject
o md5
o sha256
o cert
o gss
For details about the parameters, see their description in the pg_hba.conf configuration file.

Huawei Confidential
95
Setting Parameters in the Configuration File

The current default values for parameters in the openGauss configuration file (postgresql.conf) are all for standalone deployment. Applications can
set parameters as needed by invoking gs_guc.

Modifying parameters in the configuration file (postgresql.conf).

Resetting parameters to their default values.
gs_guc set [-N NODE-NAME] [-I INSTANCE-NAME | -D DATADIR] -c 
"parameter = value"
gs_guc [ set | reload ] [-N NODE-NAME] [-I INSTANCE-NAME | -D 
DATADIR] -c "parameter"
•
set
Modifies only parameters in the configuration file.
•
reload
Modifies the parameters in the configuration file and sends 
semaphores to the database process for reloading the configuration 
file.
•
-N
Specifies the name of the host to be configured.
Value: the name of the existing host
When this parameter is set to ALL, all the hosts in openGauss are 
configured.
•
-I INSTANCE-NAME
Specifies the name of the instance to be configured.
Value: the name of the existing instance
When this parameter is set to ALL, all the instances in the host are 
configured.
•
-D
Specifies the openGauss instance directory where the command is 
run. When the encrypt command is used, this parameter indicates 
the directory for storing the generated password file.
• -c parameter=value
Specifies the name and value of the openGauss configuration 
parameter to be set.
Value range: all the parameters in the postgresql.conf file
• -U, --keyuser=USER
Example 1: You can modify database node parameters. For 
example, you could change the maximum number of connections 
allowed by a database to 800. The database must be restarted for 
the change take effect.
gs_guc set -N all -I all -c "max_connections = 800" 
Total instances: 21. Failed instances: 0. 
Success to perform gs_guc!

Huawei Confidential
96
gsql Client Connection – Confirming the Connection Information

The client tool connects to the database through the primary database node. Before connecting to the database, you need the IP address and port for the server where the
primary database node is located.

Step 1: Log in to the primary database node as user omm.

Step 2: Run the gs_om-t status--detail command to query instances in openGauss.

In the command output shown here, 192.168.10.11 is the IP address of the server where the primary database node instance is deployed. The data 
directory of the primary database node is /srv/gaussdb/data1/dbnode.

Step 3: Check the port for the primary database node. Check the port in the postgresql.conf file in the data directory of the primary database node obtained in step 2. For
example:
gs_om -t status --detail
[ DBnode State ] 
node        node_ip
instance                                  state 
-----------------------------------------------------------------------------
1  plat1 192.168.0.11  5001 /srv/BigData/gaussdb/data1/dbnode Normal
cat /srv/BigData/gaussdb/data1/dbnode/postgresql.conf | grep port
port = 8000    # (change requires restart) 
#comm_sctp_port = 1024   # Assigned by installation (change requires restart) 
#comm_control_port = 10001  # Assigned by installation (change requires restart) 
# supported by the operating system: 
# e.g. 'localhost=10.145.130.2 localport=12211 remotehost=10.145.130.3 remoteport=12212, localhost=10.145.133.2 
localport=12213 remotehost=10.145.133.3 remoteport=12214' 
# e.g. 'localhost=10.145.130.2 localport=12311 remotehost=10.145.130.4 remoteport=12312, localhost=10.145.133.2 
localport=12313 remotehost=10.145.133.4 remoteport=12314' 
#   %r = remote host and port 
alarm_report_interval = 10 
support_extended_features=true

Huawei Confidential
97
Connecting to a Database Locally Using gsql (1)

gsql is a CLI database connection tool provided by openGauss. gsql provides both basic and more advanced database functions to facilitate user operations. By default, if a
client idle after connecting to a database, the client automatically disconnects from the database after a period specified by session_timeout. To disable session timeouts, set
session_timeout to 0.

Step 1: Log in to the primary database node as omm.

Step 2: Connect to the database. After the database is installed, the postgres database is generated by default. The first time you connect, you can connect to this database.
Run the following command to connect to the database:
postgres is the name of the database to be connected, and 8000 is the port of the primary database node. Replace the values as required.
If information similar to the following is displayed, the connection was successful:
If you log in and connect to the database as administrator omm, DBNAME=# is displayed. If you log in and connect to the database as a common user, DBNAME=> is
displayed. Non-SSL connection indicates that the database connection is not using SSL. For improved secu
