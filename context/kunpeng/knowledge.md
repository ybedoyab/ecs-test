# Kunpeng

## HCIA-KunpengV1.0TrainingMaterials.pdf

Introduction to Kunpeng

Foreword
This
course
describes
the
Kunpengcomputing industry,Kunpeng
ecosystem, Kunpeng processors,
TaiShan
servers, openEulerOS, and
openGauss database.
Huawei Confidential
HUAWEI

Objectives
On completion of this course; you will:
D Be familiar with the computing industry trend; the Kunpeng computing indust
Kunpeng ecosystem_
Know the specifications and technological innovation of Kunpeng processor
Know TaiShan 200 rack servers and high-density servers.
Know the features of the openEuler OS and the functions of the openEuler ope
community.
Know how to run basic openEuler commands.
Understand the positioning, features, and basic operations of the openGauss da
Huawei Confidential
HUAWEI

Contents
1
Kunpeng Ecosystem
Computing Industry Trend
D Kunpeng Overview
Kunpeng Computing Industry
D Kunpeng Ecosystem
2
Kunpeng Processors
3.
TaiShan Servers
4
openEuler OS
5
openGauss Database
Huawei Confidential
HUAWEI

Computing Industry Overview
The computing industry
is constantly changingas
more
and
more
disruptiveIT
technologies are released in the industry.
Cloud computing,
data, AI, blockchain;
computing, IoT, and more,
are some of the major recent powerful computi
technologies.
NLP'
Huawei Confidential
HUAWEI
big
edge

Data Technologies Constrain Computing Power
Big Data 1.0
Big Data 2.0
Big Data 3.0
Cognitive computing
AI, knowledge exploration discovery /management
MapReduce
Spark
Elk /Solr
Storm
Batch
(In-memory
Interactive
Stream
Converged data processing platform
processing
computing
analysis
computing
Spark /Data Intensive Streaming
Technologies
Batch computing framework
Yarn
Yarn
Intelligent resource management across
MapReduce
Unified resource management
regions in data centers
Storage layer for massive data
Unified data storage
Intelligent cross-region data center storage
HDFS/HBase
HDFSIHBase/MPPDB
HDFS HBase /MPPDB
Internet services
Mobile Internet
IoT connections
Demands
require distributed storage and parallel
needs real-time analysis and processing
demand ultra-low latency for
computing of massive unstructured data.
of mass, high-concurrency data.
streaming data and Al analysis in milliseconds.
Single batch computing
Converged computing
Cognitive computing
single server cannot handle big
Distributed parallel computing
High concurrency is critical to
data.
framework becomes a standard solution.
improving big data performance.
5
Huawei Confidential
HUAWEI
Big
Key

Challenges of Al Computing Power
Explosive data growth raises higher
Unit: ZB (1 ZB = 10244 GB)
computing power requirements.
60
55.7
Enterprise resource investment and
50
computing power costs
increasing.
39.5
40
Moore's Law is coming to an end,
F and
CPU performance improvement
30
28.2
encounters bottlenecks. Conventional
21.3
18.9
20
15.5
servers cannot meet computing power
12
11.3
requirements:.
10
6.2
8.3
7.7
4.7
5.3
3.6
3.5
0.8
0.9
1.5
23
The performance and efficiency of the
0
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
Al computing system need to be
Structured data
Unstructured data
improved
Source: China Al Computing Power Development Assessment R
Huawei Confidential
HUAWEI
keep

Challenges of AloT Computing Power
PC era (Internet,
Mobile Internet era
AloT era
enterprise network)
1985
2007
2016
2018
2019
Windows 1X
First-generation
5G Polar Code is
The global public cloud
5G licenses are
iPhone
determined as the
service and infrastructure
issued in China
control channel codingexpenditures reach
scheme at the 87th
0S$169.628 billion.
meeting of 3GPP.
Industry Saa5
Heterogeneous
Al and
data mining
computing
Cloud services
Midrange
Multiple architectures like
Cloud computing
computers x86 servers
x86 servers
laa5 and Paa5
power
Network
2G
Network
Low latency
Network
Fixed
Virtualization
3G
Virtualization 5G
network
Ultra-high bandwidth
SDN
4G
SDN
Device computing
x86 PC
x86 PCs
Arm-based
Embedded AI
Low power
power
iatelligent devices
Arn-based
consumption
x86 PCs
loT devices
intelligent devices
Single, closed
Open, coexisting
Diversified communities
Huawei Confidential
HUAWEI
big

Diverse Application Scenarios and Data Types Re
Computing Architectures
10101010
Integer
00100
computations
00115
Text processing
Big data analysis
Applications
Data
Computing
Mobile terminals
Text
IoT
Image
Autonomous driving
Speech
Floating-point
Video
computations
Scientific computing
Video processing
Huawei Confidential
HUAWEI

Emerging Computing Trends Driving New Comput
PCs ->Intelligent mobile terminals
A world where all things are connected
1.6 billion mobile terminals and 250 million
Over 23 billion global devices were
PCs were deployed in 2018.
connected in 2018
Smart energy
Safe
Smart hore
IoT
Autonomous
General-purpose compu
driving
Al computing power
Widespread use of mobile terminals
New computing
Processing of massive data requires high
leads to a multitude of application
requirements
bandwidth and high concurrency.
scenarios.
Homogeneous computing power is required on Data collection -> Real-time
Processor: x86
29 Arm
the cloud data center side and device side.
intelligent data analysis
Deployment model: PC applications
> Mobile
High-performance, high-concurrency, and high -
Cloud data center: analyzes, processes, and
applications
27 Mobile applications on thethroughput computing power is required.
stores large data volumes
cloud
Al computing power accounts for 80% of the data
Cloud-edge collaboration: Central trainin
Mobile terminal access mode: 3G -> 4G -> 5G
center computing power.
Edge inference
Huawei Confidential
HUAWEI
city
tng
Edge:

Combined Multiple Computing Architectures for Diverse
Computing
Redefinition of Moore's Law
Optimal approach: combined computing
architectures
107 ~
106
Processor
105 ~
10 
1.1x per year
x86
Arm
Power
10~1
1.5x per year
CISC
RISC
10 ~
GPU
NPU
DSP
NP
1980
1990
2000
2010
2020
Other processing units
Data of introduction
10
Huawei Confidential
HUAWEI

Kunpeng Ascend Build Core Computing Power
Multi-scenario
Da Vinci architecture
optimization
and instruction set
Multi-core
Suited for all
concurrency
scenarios
evotinioous
KunpengJ
Ascend
Scalpblein
General-purpose
Al processors
Compatible with
processors
Ultra-high memory
the Arm ecosystem
and interconnection
bandwidth
11
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
0 Computing Industry Trend
Kunpeng Overview
Kunpeng Computing Industry
D Kunpeng Ecosystem
2
Kunpeng Processors
3.
TaiShan Servers
4
openEuler OS
5
openGauss Database
12
Huawei Confidential
HUAWEI

Kunpeng Overview
Computing
Ecosystem
Soc
Platform
Applications
CPU Die
CPU Die
M0 Die
Kunpeng open hardware platform: Processor
Enabling
Enabling industry
23 Single node -> Cluster
partners
applications
Applications
data
Kunpeng open
Kunpeng servers
Middleware
Software-defined
motherboards
storage
Complete software toolchain:
Databases
High-performance
Leading process: 7 nm, multi-die chiplet
maximizes Kunpeng performance
computing
Multi-core kernel: The Huawei-developed
OSs
Native
CPU cores increase computing power by
applications
509, along with Huawei-developed inter -
chip interconnection and multi-channel
Servers and PCs
Cloud services
interconnection:
Kunpeng Porting Advisor
Kunpeng Hyper Tuner
First to support next-generation
networks and interfaces: 8-channel
memory controllers and 1OOGE ports
13
Huawei Confidential
HUAWEI
Big

Contents
1 . Kunpeng Ecosystem
D Computing Industry Trend
D Kunpeng Overview
Kunpeng Computing Industry
D Kunpeng Ecosystem
2
Kunpeng Processors
3.
TaiShan Servers
4
openEuler OS
5
openGauss Database
14
Huawei Confidential
HUAWEI

Computing Market of
US41 Trillion
The ICT industry is being shaped by innovative technologies and architecture that; combined 
connections and big data, are buildingnew computing industry chains
and ecosystemswith opportunities
for
startups and other vendors.
Software: OSs, virtualization software; databases; middleware; big data platforms, and enterprise
Hardware: servers, components, and enterprise storage devices
Cloud services and data center management services
Infrastructure
software
Public
1525 billion
clouds
Servers
Databases
Iaas
112.1 bllllon
56.9 billion
141 billlon
Big data
platforms
41 billlon
Enterprise
Middleware
application
Data center
43,4 billion
management
Enterprise
software
services
storage
402 billion
159.5 billion
31.1 billion
Global investment (US$) in the computing industry in 2023
15
Huawei Confidential
HUAWEI

Kunpeng Computing Industry
Full-stack Kunpeng
covers
processors,
servers, storage devices, OSs, middleware  virtualiza
software; and databases, in addition to applications, cloud; consulting; and manage
Kunpeng Computing
Industry
Government
Finance
Gaming
Media and
Industry applications
entertainment
Carrier
Cloud services
Databases
Kunpeng ECSKunpeng BMS Kunpeng
Kunpeng RDSKunpeng DWS
container
Middleware
openEuler O5
Compatible with various OSs,openGauss database
middleware, and database software
OSs
Virtualization
TaiShan 2280
TaiShan 5280
TaiShan X6OO0
OceanStor VG/F
Storage
PCs
Balanced server
Storage server High-density server V6 storage
Servers
Kunpeng
Huawei Kunpeng
Intelligent SSD
SmartNIC
Intelligent
Ascend
processors
processor
controller chip
chip
management Al processors
chip
16
Huawei Confidential
HUAWEI
PCs,

Evolution of Kunpeng Processors
architecture innovation
Huawei-developed kernel and cutting -
SoC design
Device; edge; and cloud scenarios
Outstanding competitiveness
Chip technology innovation
AArch64 chip technology and
cutting-edge manufacturing
process
Data centers
Same performance, with better
Kunpeng 920
computing efficiency
1* 7 nm data
center processor
Chip capability accumulation
Kunpeng 916
Arm chip technology and IP
Hi1612
multi-channel
2019
design capability
Arm processor
(Kunpeng 912)
Communications and
terminal domains
K3
Arm-based
1s Arm-based
64-bit processor
2016
1s Arm-based
mobile processor
wireless base
15 ASIC
for
station chip
2014
transmission network
1991
2005
2009
17
Huawei Confidential
HUAWEI
Chip
edge
15t
75t
chip

TaiShan: Huawei-Developed Server Series
AI
Huawei-developed
Management
TaiShan servers
Storage
Computing
BMIC
CPU
Intelligent
management chip
CPU
SSD
Transmission
Processor chip
controller chip
NIC
Intelligent network chip
Computing
Storage
Transmission
Management
AI
Huawei
Hi1812
Hi1822
Hi1710
Ascend 310/910
Kunpeng 920
Intelligent SSD
Intelligent; converged
Intelligent
Al chip
Arm chip
controller chip
network chip
management chip
Convergence of PCle NVMe
Da Vinci architecture;
1s 7 nm Arm processor
and SAS
Convergence of Ethernet andBuilt-in intelligent
ultimate efficiency and
with 32/48/64 cores at
Intelligent acceleration and the Fibre Channel protocol, management engine;
performance
2.6 GHz
advanced wear leveling protocol acceleration; and
intelligent fault
algorithm
programmable design
management
18
Huawei Confidential
HUAWEI

Open Source OS
Ultimate performance
Ultimate performance
(Multi-core Self-optimization
Acceleration)
Three-level intelligent scheduling; 60%
lower multi-process latency
Robust reliabilityKunpeng Open source
Smart full-stack optimization (self-
Dynamic configurationecosystem
Community-based
adjustment, self-awareness, and
Fault management
Global cooperation
adaptation)
Multi-core acceleration, software and
hardware virtualization, and efficient
Application software
containers
Big data
Software-defined storage
Robust reliability
Database
Middleware
Dynamic configuration; fault
management; and cold and hot patches
openEuler
Multi-core
Virtualization
High-speed
System
Security
Open source
acceleration
IContainers
I/Os
monitoring hardening
Global reach:
10 in kernel
Linux kernel
contributions;
4 in the Docker
Kunpeng computing platform
community
Global cooperation and open source
19
Huawei Confidential
HUAWEI
self -
top
top

Advantages of the Kunpeng Computing Industry
Incubate and improve
industry applications in
1
the Chinese market to
2
form a virtuous
Advantages
with the global industry.
Merge a well-
performing ecosystem
with Arm to accelerate
development.
20
Huawei Confidential
HUAWEI
cycle

Typical Applications of the Kunpeng Computing Indu
Software-defined
Native
Cloud
Big Data
Databases
Storage
Applications
Services
Oar
300 performance
20% IOPS increase
RoCE low-latency network
Arm native, no
Kunpeng BMS
increase
Compression and
Multi-core scheduling
performance loss
Kunpeng ECS
Encryption and
decompression engine
algorithm
Enterprise-class
Kunpeng Kubernetes
decryption engine
Hybrid deployment
NUMA optimization
reliability solution
container
Hybrid deployment
with x86
algorithm
An ecosystem with 1
with x86
million+ applications
Superior
Multi-core
High
Native Compucing
Performance
Concurrency
Throughput
Power
21
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
D Computing Industry Trend
D Kunpeng Overview
Kunpeng Computing Industry
Kunpeng Ecosystem
2
Kunpeng Processors
3.
TaiShan Servers
4
openEuler OS
5
openGauss Database
22
Huawei Confidential
HUAWEI

Kunpeng Computing Industry Ecosystem Panorama
Huawei works with industry technology vendors and partners to build an open, inclusive Kunpeng computing industry e
specific solutions. It also provides developers with a community platform and contests, and cooperates with universitie
02
Collaboration with universities
Technology ecosystem
03
Continuously cultivate qualified personnel
Technology
for the computing industry.
Build an open technology ecosystem
ecosystem
Collaboration
University-enterprise joint courses
compatible with popular 0Ss, databases,
University-enterprise joint publication
and middleware.
with
Training centers in universities
universities
Developer ecosystem
01
Developer
Industry ecosystem
Encourage developers to develop and ecosystem
Huawei cooperates with partners to
innovate services
Industry
develop industry-specific solutions.
Kunpeng developer contest
Kunpeng
ecosystem 04
IPTV
Kunpeng online courses
ecosystem
Kunpeng rerote lab
Government
Finance
Gaming
Medla and
Kunpeng career certification
enterlainnenL
Community
Community building
building
Partner
Partner ecosystem
The Kunpeng Partner Programs provide
The Kunpeng community provides
ecosystem
partners with comprehensive support in
customers, partners, and developers with06
training, technology, marketing; and sa
abundant resources and an open; fair
Kunpeng Partner Program
space for technical exchange.
05
openEuler Partner Program
23
Huawei Confidential
HUAWEI

An Overview of Kunpeng Computing Industry Deve
The  Kunpeng   computing industry strives
to
build
a mature ecosystemfor developers and industry expert
It
collaborates with industry alliances, open
source communities, OpenLabs, and industry standard organ
to
improve the industry chain and create a full-stack industry, with Kunpeng becoming a globa
Huawei
Application
Partner
Provides Kunpeng DevKit and Kunpeng BoostKit to help
Partner
partners
their applications quickly to Kunpeng, simplifying
Middleware
enablement
development and maximizing performance:.
Big data
openGauss enterprise-class open source database
Database
Open source
enabling partners to develop their own database products
software
Open source openEuler, enabling partners to develop the
O5
own 05 products
Server
Provide motherboards and components (such as SSDs, NICs,
Components
Open
and RAID controller cards) for partners to develop their own
hardware
components, servers, and PCs.
Mainboard
Huawei Cloud
Huawei's
Architecture innovation; processor R&D; and cloud services
Computing
focus
architecture
24
Huawei Confidential
HUAWEI
port

Collaborating Towards a Kunpeng Industry Ecosy
Regional Leaders in
Industry
Kunpeng Talent
Technology and Innovation
Aggregation
Development
China
=made OS, toolchain,
Regional Science and Technology City, Huawei
database, middleware,
Kunpeng Academy, Kunpeng senior
Kunpeng Lab, National Kunpeng certification
software, and
talent introduction, developer
organizations, Kunpeng industry bases
application
community; technical training
other industries
Kunpeng
Kunpeng Eco Innovation Center
Innovative Kunpeng Ecosystem Aggregation Circle
One-stop Kunpeng
Kunpeng ecosystem labsGovernment policy support
Partner gathering
developer community
Online resources
Offline operation support
Policy support
Ecosystem cultivation
Open source 05
Kunpeng innovation
Support fund
Kunpeng alliance
center flagship store
Open source database
Talent incentives
Porting from *86
Joint Kunpeng lab
Open Kunpeng board
Led by public sectors
Joint solutions
Kunpeng micro certification
Kunpeng toolkit
Kunpeng training
Localization standards
Joint marketing
25
Huawei Confidential
HUAWEI

Technology Ecosystem: Compatible with Mainst
Source Components and China-developed Components
Web
Middleware
Databases
Data
Nginx: high-performance
Merncached: distributed
MySQL: relational database
Hadoop: distributed system
web server
merory-caching server
server
infrastructure
Apache: efficient HTTP
Redis: high-perforrance
MariaDB: 0 branch of MySQL Hive: Hadoop-based data
server
value dalabase
PostgreSQL: database server
warehouse platform
Kafka: distributed messaging
Cassandra: distributed
HBase: distributed database
system
value database
Spark: large-scale data
RabbitMQ; AMQP message
MongoDB: distributed storage
computing engine
queue service
database
ZooKeeper: distributed
SQLite: lightweight relational
application scheduling service
database
MyCAT; database shardingLevelDB: Ct+-based storage
middleware
database
Applications
Management and
Compilers
Development Tools
OSs
Monitoring
Elasticsearch: distributed
Graylog: log aggregation and
Ruby: server scripting
OpenJDK: open source Java
CentOs
search engine
analysis
language
development platform
Ubuntu
Yarn; JavaScript package
Ansible; OgM automation tool Perl: programring language GDB: program debugging toolNeokylin OS
manager
Gradle: open source build
Python; object-oriented
in UNIX
Deepin
Tesseract: OCR engine
automation tool
programming language
JMeter: Java-based
Neoshine
FastDFS: lightweight
Kubernetes; container
PHP: scripting language for performance test tool
Asianux
distributed file syster
managerent platform
developing dynamic web
OpenSSL: software library thatKylin OS
Kibana; log analysis platform
Zabbix: web monitoring tool pages
provides secure
openEuler
Robot Framework: test
Logstash: l0g management toolLinaro GCC: C/C++ compiler communications
automation framework
Maven: software project
Lua: lightweight and
Libxml2; function library that
managerent and
compact scripting language parses XML documents
TypeScript: superset of
comprehension tool
SHC: shell script encryption tool
JavaScript
26
Huawei Confidential
HUAWEI
Big
key -
key-

Teaming Up with Universities to Cultivate Kunpeng
Computing Experts
In 2020, invested CNYIO
Carry out training andWork with education
Align with Huawei's
Million to develop core innovative practices fororganizations to
certification standards.
computer courses and
teachers and students.
ways of improving talent
practice resources.
cultivation and
cooperation:
27
Huawei Confidential
HUAWEI
explore

Partner Ecosystem: Kunpeng Partner Programs
openEuler
Kunpeng
Partner
Partner
Program
Program
(openEuler 05)
(Huawei TaiShan servers)
Kunpeng Partner Programs
28
Huawei Confidential
HUAWEI

Community Ecosystem
: Building a Kunpeng Zone on th
Cloud
https:/ /wwwhikunpeng.com/enl
Complete toolchain
Kunpeng Community
Code hostingPipeline compilation
Release
Maintenance and upgrade
Porting guidance
Web, HPC, database; big data, middleware,
development tools, application tools,
management and monitoring; compilers,
and drivers
Open community forum
SharingDiscussionQ&A Live streaming
Positioning
Mission
Vision
A technical support;
Empowers customers,
Aims to build an open
Ecosystem incubation platform
knowledge sharing, andpartners, and developers Kunpeng ecosystem that
This platform provides online and offline
industry cooperation
to develop competitive
accelerates partners'
consulting and tutoring services for startup
platform built by Huawei computing products and
business success. Together
helping them grow and apply Kunpeng
based on the Kunpeng
industry solutions based with partners we will
technology system:
on the Kunpeng
expand the Kunpeng
technologies.
technology system:
industry.
29
Huawei Confidential
HUAWEI
OS5,

Developer Ecosystem: Huawei Developer Program
Training
Educational Support
2.0
Huawei Certification
US$ |@5 billion
Huawei Developer Pragram
2019-2024 Industry Ecosystem Development 
OpenLabs
Joint Marketing
Ascend
Kunpeng
Innovation Funding
Innovation Workshops
30
Huawei Confidential
HUAWEI

Quiz
1
(Multiple-answerquestion) Which
of the   following
are
Huawei
Kunpengcomputing
products?
A Kunpeng processors
B
TaiShan servers
C Huawei Cloud Kunpeng services
2
(Multiple-answer question)Which of the following support does
Huawei  provide for the
Kunpeng computing industry?
)
A
Toolchains
B
Cloud services
C. Community services
D. Professional services
31
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
Processor Architectures
D Kunpeng Processor Overview
D Kunpeng Processor Models and Specifications
D Innovative Technologies Driving Huawei Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
32
Huawei Confidential
HUAWEI

Processor Architectures
x86 is an Intel CPU architecture that consists of a family of complex instruction set compute
Arm is another popular CPU architecture.
Unlike Intel and AMD that uses CISC, the Arm architecture is a family o
reduced instruction
set computer (RISC)
architectures. IoT and AI applications
accelerate the developmentof
microprocessor   technologies  among
which Arm embedded processorshave been widely used.
Arm embedded
processorsare small, and boast
power consumption; greater affordability, faster instruction exe
compatibility with 8-bit and 16-bit components.
x86
Arm
Instruction
CISC
RISC
set
Mainly Intel and AMD;
Open authorization strategy and
Supplier
monopolized by Intel
multiple _suppliers
Industry
Mature
Developing rapidly
chain
33
Huawei Confidential
HUAWEI
low
good

Application Fields of Arm Processors
Currently, more than 90% of mobile terminals use Arm processors
As IoT, 1 Al, and cloud services are developing fast, Arm will extend its presence to the da
center market.
Enterprise
Exascale supercomputing
Ultra-large cloud
applications
systems
data centers
Japan's exascale
AWS released their Arm
Software-
supercomputer "Post-K" uses processor Graviton and
90%
defined storage
Big data
the Fujitsu Arm processor
EC2 instances (A1).
Arn native
A64x.
Market share of Arm
processors in mobile
terminals
34
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
D Processor Architectures
Kunpeng Processor Overview
D Kunpeng Processor Models and Specifications
D Innovative Technologies Driving Huawei Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
35
Huawei Confidential
HUAWEI

Kunpeng Processor Panorama
Huawei Kunpeng processors
are
a series
of Arm-based enterprise-class processors,
which
include computing; storage; transmission; management; and Al processors
General
Embedded
Kunpeng
KunpengKunpeng
Kunpeng
Kunpeng
Kunpeng
Mij3a
CPU
processor
processorprocessor
PC processor
PC processor
PC processor
purpose
(initiated)
gen)
(2r gen)
gen)
(1s5 gen)
gen)
gen)
computing
SSD
SSD
SSD
SSD
RAID
SSD
controller
controller
controller
controller
controller
controller
Storage
51
Hi811
Hi18id
Hi1812
(3" gen)
Hi81ze
gen)
HH8BO
(1* gen)
Ki7813
gen)
(1 gen)
gen)
Multi-CPU
SmartNIC
Multi-CPU
SmartNIC
SmartNIC
Transmission
gen)
Hi1821
Hi1so3
interconnection chip
Hi1822
gen)
Hib23
(3rd gen)Hij5zo
interconnection chip
gen)
gen)
Intelligent
Intelligent
Intelligent
Management
Hi171o
management chip
HI17h1
management chip
management
Hi17i2
gen)
gen)
chip
gen)
Inference chip
Training
MDC chip
Inference
Training chip
MDC chip
Al computing
51
Aeud
gen)
4120 d chip
gen)
(1 gen)
chip
J2D
gen)
(1st gen)
gen)
2004
2011
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
36
Huawei Confidential
HUAWEI
(2nd
(3rd
(4t
(1st
(4th
(5th
(2"d
(2nd
(15t
(2na
(1st
(2nd
(3rd
(1st
(2nd
(1st
(2nd
(2nd

Features of the Kunpeng Processor Architecture
Advantages:
Uses the Arm architecture.To provide specific functions and performance; the Kunpeng
occupies a small area; consumes low power, and adopts high integration:
More hardware CPU cores
are provided for better concurrent processing:
Supports 64-bit instruction sets and is compatible with various application sc
and devices to clouds.
Performs most data operations in the registers to accelerate instruction execution
Uses the RISC instruction set, which features a fixed instruction length, flexible and simple
addressing modes, and high execution efficiency.
Disadvantage:
Kunpeng is a newcomer in the data center field and is still developing its ecosystem
37
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
D Processor Architectures
D Kunpeng Processor Overview
Kunpeng Processor Models and Specifications
D Innovative Technologies Driving Huawei Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
38
Huawei Confidential
HUAWEI

Kunpeng General-Purpose Computing Processors
Kungzng 920
Kperg
Kunpeng 912
Kunpeng
Kunpeng
(Hi1612)
916
920
First Arm-based
Industry's first Arm
Industry's first 7
nm
64-bit processor
processor with
data center-level Arm
multiple sockets
processor
2014
2016
2019
39
Huawei Confidential
HUAWEI

Specifications of Kunpeng 920
32, 48, or 64 cores
The instruction set is compatible with Armv8.2 and the
frequency reaches 2.6 GHz.
64 KB L1 I/D cache per core
Exclusive 512 KB L2 cache per core
1 MB L3 cache per core on average
8 x DDR4 controller, up to 2933 MT/s
PCle and SAS interfaces
PCle 4.0, compatible with PCle 3.0, 20, and 1.0
PCle 4.0 x16, x8, X4, x2, or x1, with a PCle controller
16 x SASISATA 3.0 controller
Kunpeng 920
CCIX interface and accelerator cache coherence
2 x 100 Gbit/s RoCE v2 and 25GE,
F 5OGE, or
1OOGE standard NICs
2P or 4P expansion
Package size: 60 mm x 75 mm
40
Huawei Confidential
HUAWEI

Advantages of Kunpeng 920
930+, 25%
Superior
performanceEstimated SPECint_rate_base2006 score
Memory bandwidth:
46%
High
Total I/0 bandwidth: 660
throughput Network bandwidth
4x
Kunpeng 920
Deep
4-in-1 chip
integration
High energy 309
efficiency
Note: Compared with Intel Skylake 8180
41
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
D Processor Architectures
D Kunpeng Processor Overview
Kunpeng Processor Models and Specifications
Innovative Technologies Driving Huawei Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
42
Huawei Confidential
HUAWEI

Innovative Technologies Driving Huawei Kunpen
Huawei-developed kernel
Memory/Network port &
Huawei-developed CPU cores,
protocol
improving computing power
by 50%
8-channel DDR4 controller
Huawei-developed
with
100 Gbit/s RoCE ports
2-socket or 4-socket
PCle 4.0/CCIX protocol
interconnection
Multiple Huawei-developed
hardware acceleration engines
Leading manufacturing process
Improved reliability
Industry's first 7
nm data
center-level Arm processor
Industry-leading Chip on
The Kunpeng processor
Wafer on Substrate (CoWoS)
supports 45 RAS features
packaging technology used to
that are popular and
incorporate multiple dies
profitable.
43
Huawei Confidential
HUAWEI
I/0
chips,

Huawei-developed Kernel
Kunpeng 920 (64 cores)
Kunpeng 920
Estimated SPECint_ rate_base2006 score
Kunpeng 920-6426 (64-core 26 GHz)930+ 1
GPu
RoCE
SAS
SouthbridgeCPU
Skylake Platinum 8180
750
NIC
controller
4-in-1 CPU
Kunpeng 920 (32 or 48 cores)
Kunpeng 916 (32 cores)
Kunpeng-4826
5.03
{
Skylake Gold 5115
0.31
Kunpeng-3226
4.52
1
Kunpeng 916 0.25
Skylake Gold 6148
3.63
Lower power consumption per
unit of SPECint performance
f
Higher SPECint performance
Tested by the Huawei lab. Results may vary acc
per unit of power consumption
to test environments.
44
Huawei Confidential
HUAWEI
0

Acceleration Engines Built in Kunpeng 920
Built-in SSL acceleratlon engine
Built-in encryption algorithm acceleration engine
User
ELB
Application serverDatabase server
CPU
HTTPS
CPU core
CPU core
HITPS
Encryption Decryption
SSL acceleration server
Nginx worker
acceleration engine
TaiShan server
OpenSsL API
On-chip bus
Data
(2 x Kunpeng 920 CPU)
HTTPS
OpenSSL libssl
EVP API
Nginx node
OpenSSL libcrypto
ESL accelerator
OpenSSL Engine API
Memory controller
Storage controller
Kunpeng CPU accelerator engine
Kunpeng 920 acceleralor self-defined API
I/o
Nginx node
Kunpeng CPU accelerator Vser-mode |ibrary User modeMemory
Plaintext data
Ciphertext data
SSL acceleratorl
Kernel
Kunpeng CPU accelerator kurnel-modcmode
Data is encrypted and decrypted in the CPU, and the
is stored in the secure
Nginx traffic path Nginx cluster
zone. Only specific programs can write the
into the secure zone and only the
HTTP
Kunpeng CPU accelerator hardware
CPU can directly read theto the CPU.
Kunpeng 920 SSL accelerator invoking process
Intel I54-L acceleration (us)Taishan hardware acceleratlon (Hs)
Shorter file compression time with the built-in compression engine
40
35.3
30
23.5
24.9
19.1
20
16.1
11.2
11.5
10.9
5
5.7
8.2
5,8
7,5
10
2.4
4.5
3.8
0
compress
IKB
compress
4KB
compress_ BKB
compress_ 16KB
decompressIKB
decompress_4KB decompress8KB
decompress16KB
45
Huawei Confidential
HUAWEI
key
key
key
key

Kunpeng 920 Acceleration Engine
Logical architecture of the Kunpeng
Acceleration Engine Overview
920 acceleration engine
The acceleration engines support the f
Applications
algorithms:
OpenSSL/zlib standard API
Digest algorithm SM3
Symmetric encryption algorithm SM4, which
Application library
Unified driver
supports CTR and CBC modes
subsystem
interface Wrap
(OpenSSL/zlib)
Asymmetric algorithm RSA
1 which supports
Unified driver
asynchronous models and
sizes 1024, 2048,
interface
3072, and 4096
Accelerator driver subsystem
Compression and decompression algorithms,
which support zlib and gzip formats
Register access
ACPI table
Installation method: using an RPM installation
reporting
License
package or using source code.
Chip acceleratorInitialization
BIOS
control
subsystem
Enablement subsystemData read
BMC subsystem
46
Huawei Confidential
HUAWEI
key
Wrap

Improved Reliability
The Huawei Kunpeng 920 CPU incorporates 45
new
RAS features to better fulfill IT
service requirements.
Type
Feature
Precise count of correctable errors
Memory
Adaptive Double DRAM Device
Correction (ADDDC)
PCIE
Online Error Recovery (OER)
CPU
Poison Data Containment (PDC)
Error recovery
System
Threshold and count of correctable
errors
47
Huawei Confidential
HUAWEI

Quiz
1 (Multiple-answer question) Which of the following statements about the H
Kunpeng 920 CPU are true?
A
It adopts 7 nm manufacturing.
B. It supports the 8-channel DDR4 controller.
C. It supports the PCle 4.0 interface and is compatible with PCle 3.0/2.0/1.0.
D It supports multiple accelerators.
2
(Multiple-answer question) Which of the following descriptions about th
Kunpeng 920 CPU accelerators are true?
A. SSL acceleration engine
B Encryption/Decryption acceleration engine
C. Compression/Decompression acceleration engine
48
Huawei Confidential
HUAWEI

What Is a Server?
A server is a computer that provides services for client machines on a network.
Servers are high-performance computers that are controlled by a What is a server used for?
network OS, and provide shared resources (such as queries, storage
and computing resources) for the client machines (such as PCs)
running on the network.
A server boasts high-speed CPU computing
Service
Service Name
capabilities; can run reliably over long periods; and is capable of
Cateqory
ERP
powerful I/0 throughput.
Core services
CRM
Database
Virtualization
Email and instant messaging
Basic services
Web service
Files and printing
Internet
Search
services
Content server
HPC
Innovative
services
Hadoop
Server SAN
49
Huawei Confidential
HUAWEI

Server Development Timeline
The world 5 earliest calculating
In 1964, IBM launched the first
device; the abacus, was invented in
mainframe; System/360, which
China 2600 years ag0
became a real server.
Intcls Rclentless Fursuit Df
Moore's Law
5991
2603
7005
CPUs, the core component of servers,
In 1989, Compaq launched the
In 19905, low-cost midrange
have
developing based on
world's first Intel Architecture (IA)
servers Were
developed for small -
Moore'5 Law Most servers use *86-
server SystemPro; which uses the
and medium-sized enterprises.
based Intel processors;
Intel 486 microprocessor;
50
Huawei Confidential
HUAWEI
been

Components of a Server
A server
is composedof three
major parts, CPUs, memory modules,
and drives, alongwith
basic
hardware
such
a5 power supplyunits
(PSUs) ,motherboard, and chassis,to  provideinformation
services.
CPUs
Memory
Drives
PCle cards
1
PSUs
Motherboard
Fans
Chassis
51
Huawei Confidential
HUAWEI

Main Server Types
Complex instruction set
Reduced instruction set
computer (CISC)
computer (RISC)
(typically x86 architecture)
(non-x86 architecture)
By instruction
set
High-density
Single-socket server
Rack server
(1 CPU)
server
By form
By CPU
factor
Servers
Multi-socket server
(4 or more CPUs)
Dual-socket
Blade server
Tower server
server (2 CPus)
By CPU instruction set By form factor
By load type
By application level
Arm server
Tower, rack, blade; and
Database server
Entry-level server
x86 server
high-density servers
Application server
Workgroup server
Web server
Department server
Access server
Enterprise server
File server
52
Huawei Confidential
HUAWEI

Application Scenarios of Servers
Application scenario 1:
mission-critical services
(e.g., core databases in the
financial industry)
Application scenario 3:
converged architecture
2
(high-performance data
analysis, HPC, and all-in-
g
one data centers)
Application scenario 2:
(database,
Internet-like services
Application scenario 4:
virtualization, hot
(ultra-large data centers, big
SSD-based application
data caching, big data analysis, public clouds
acceleration
data, HPC; etc)
and web applications)
53
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
0 General Server Knowledge
TaiShan Server Overview
TaiShan 200 Rack Servers
D TaiShan 200 High-Density Servers
4
openEuler OS
5
openGauss Database
54
Huawei Confidential
HUAWEI

Building Server Computing Capabilities Based on
Processors
Efficient ComputingRobust Reliability
Open Ecosystem
Arm-compatible high -
Kunpeng processors use An open platform that supports
performance Kunpeng
Huawei-developed kernel;
mainstream hardware and software; &
processors and TaiShan servers
TaiShan servers use Huawei-
thriving Kunpeng ecosystem through
and solutions power data
developed computing chips.collaboration between developers,
centers with efficient
High quality underpinned bypartners; and industry organizations to
computing.
17 years of experience in build the foundation for new
computing innovation:
intelligent computing:
Huawei Kunpeng 920
Industry's 15t 7
nm data center _
level processor
Huawei Kunpeng 916
Hi1612
Industry's 1st Arm
2019
(Kunpeng 912)
processor with
multiple sockets
1st Arm-based
K3
s[
64-bit processor
2016
1 Arm-based
1s Arm-based
wireless base
mobile CPU
TaiShan 200
15tASIC chip for
station
2014
Kunpeng 920-based
transmission network
2009
TaiShan 100
2005
1991
Kunpeng 916-based
55
Huawei Confidential
HUAWEI
chip

TaiShan Servers
TaiShan 100 Server
TaiShan 200 Server
Kunpeng 916-based
Kunpeng 920-based
Up to 16 DDR4 DIMMs
Up to 32 DDR4 DIMMs
5 PCle 3.0 slots
Up to 8 PCle 4.0 slots
SASISATA HDDs and SSDs
NVMe SSDs, SASISATA HDDs and SSD
GEIIOGE LOM
1OOGE LOM
Board-level and full liquid cooling
56
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
0 General Server Knowledge
TaiShan Server Overview
TaiShan 200 Rack Servers
D TaiShan 200 High-Density Servers
4
openEuler OS
5
openGauss Database
57
Huawei Confidential
HUAWEI

TaiShan 200 Server Portfolio
17 years of engineering
and process experience
Passivebackplane & triple
Board-level
anti-vibration design
High-
Liquid
speed
Reliability
Quality
cooling
intercon
design
control
nection
Huawei TaiShan server
56 Gbit/s board-level
15% lower failure rate
interconnection
than the industry average
Data center
computing
Storage-intensive
Compute-intensive
2280
1280
5290
5280
2480
X6ooo
2U 2-socket
10 2-socket
2280E
4U 72-drive
4U 40-drive
2U 4-socket high-2U 4-node high-density
storage model
storage model
balanced
high-density
performance model
model
model
model
model
58
Huawei Confidential
HUAWEI
Edge
Edge

Specifications and Highlights of the TaiShan 2280
Balanced Server
Front view
Model
2280
Highlights
Form factor
2U rack server
Superior performance
CPU
2 X Kunpeng 920
The Kunpeng 920 processor
delivers x86 high-end model
Memory
32 x DDR4-2933 DIMM
performance.
16 x 3.5-inch SASISATA HDD
8-channel memory technology
Local storage
27 x 25-inch SASISATA HDD
supporting 32 DDR4 DIMM slots
16 x 2.5-inch NVMe SSD
and up to 4 TB memory
Huawei Atlas 300 Al accelerator
8
RAID level
RAID 0, 1, 5, 6, 10, 50, and 60
cards and ES3O00 VS NVMe SSDs
PCle
Up to 8 x PCle 4.0 x8 or 3 x PCle 4.0 x16 + 2 x
Rear view
expansion
PCle 4.0 x8 slot
Flexible adaptation
9
Multiple I/0 modules for various
Two LOM NICs (4 x GE electrical port, 4 x 1OGEdrive configurations
Onboard NIC
optical port; or 4 x 25GE optical port per NIC)
Flexible onboard NICs and
2 x 900 W or 2000 W hot-swappable PSU in 1+1
GE/1OGE/25GE network
Power supply
redundancy, 220 V AC or 240 V DC
configurations
Fan module
hot-swappable fan modules in N+1 redundancy
Robust reliability
Huawei-developed computing
chips
Temperature
5 Cto 40 C (41 F to 104'F)
China-made server components,
for sustainable supply
59
Huawei Confidential
HUAWEI

Internal Structure of TaiShan 2280
6 x PCle 4.0 x8 FH slot,
or 2 x 3.5-inch/2.5-inch
1/0 module 2
I/0 module 1
SASISATA/SSD drive
2 PSUs
2 Kunpeng 920
I/0 module 3
processors
Drive enclosure A: 12 x 3.5-inch SASISATA
2
GE, serial port,
management
hetwork port
Drive enclosure B: 25 x 25-inch SASISATA
FlexlO card 1
FlexlO card 2
4 x 25-inch rear SASISATA/SSDI
NVMe drive, or 2 x PCle 4.0 x8
FHHL slot
Drive enclosure C: 8 x 25-inch
SAS/SATA + 12 x NVMe
4 fan modules
32 DDR4 DIMM slots
Built-in RAID controller card
60
Huawei Confidential
HUAWEI

Specifications and Highlights of the TaiShan 5280
Server
Front view
Model
5280
Highlights
Form factor
4U rack server
Ultra-large storage capacity
Up to 40 x 3.5-inch drive; with a
CPU
2 x Kunpeng 920
local storage capacity of 560 TB
32 x DDR4 DIMM, with a memoryof up to
The Kunpeng 920 processor
Memory
2933 MTIs
delivers performance
comparable to x86 high-end
24 x 3.5-inch front SASISATA/SSD drive, up to 16 x
models and supports efficient
Local storage
3.5-inch rear SASISATA/SSD drive; and 4 x 2.5-inch
data storage.
8
NVMe SSD
8-channel memory technology;
supporting 32 DDR4 DIMM slots
and up to 4 TB memory
Rear view
RAID support
RAID 0, 1, 5, 6, 10, 50, or 60; supercapacitor for
9
power failure protection
Flexible adaptation
Multiple I/0 modules for various
Up to 8 x PCle 4.0 x8 or 3 x PCle 4.0 x16 + 2 x PCle
drive configurations
PCle expansion
x8
Flexible onboard NICs and
GEJIOGEI2SGE network
FlexlO card
4 x GE, 4 x IOGE, or 4 x 25GE
configurations
Power supply 2 hot-swappable ZOOOW PSUs in 1+1 redundancy
Robust reliability
Huawei-developed computing
Fan module
hot-swappable fan modules in N+1 redundancy
chips
Operating
China-made server components,
5'C to 35'C (41"F to 95'F)
for sustainable supply
temperature
61
Huawei Confidential
HUAWEI
speed

Internal Structure of TaiShan 5280
6 x PCle 4.0 x8 FH slot2 x PCle 4.0 x8 FHHL slot
32 DDR4 DIMMs,
2 Kunpeng 920
with the memory
processors
speed up to 2933
MT/s
Drive enclosure: 24 x 3.5-inch
SASISATA
FlexlO card
4 x GE
2 x GE, serial port,
management network port
Rear drives: 4 x 2.5-inch
SASISATA/NVMe
Rear drives:
4 x 3.5-inch
SASISATA
PSUs, in 1+1
4 fan modules, in
redundancy
N+1 redundancy
Rear drives: 12 x 3.5-inch SASISATA
62
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
0 General Server Knowledge
TaiShan Server Overview
TaiShan 200 Rack Servers
TaiShan 200 High-Density Servers
4
openEuler OS
5
openGauss Database
63
Huawei Confidential
HUAWEI

Specifications of the XGOOO Chassis
Front view
Rear view
Internal view
Node
Fan module
Drive
Server node 1 and 2
Server node 3 and 4XA320 V2 node
PSU
health indicators
health indicators
Drive panel
PSU
Product
High-density server
Form factor
2U chassis, 4 x half-width XA3ZO/XA3ZOC server
PSU
Two hot-swappable 3000 W PSUs in 1+1 redundancy
Power supply
100 V to 240 V AC; 240 V DC
Fan module
Four hot-swappable fan modules in N+1 redundancy
Operating temperature
5 C to 35 C (41 F to 95 F)
Dimensions (Hx Wx D)
86.1 mm x 436 mm x 818.9 mm (3.39 in. x 17.17 in. x 32.24 in.)
64
Huawei Confidential
HUAWEI

Specifications of XA320 and XA3ZOC Compute No
Internal view
XA320
Rear view
Internal view
XA3ZOC
Rear view
2 x CPU
Memory
PCle slot 1
PCle slot 2
Water pipe
PCle slot 2
High-
2 x GE
iBMC
1 x 10oG
CPU metal
Memory
High-
2 x GE
iBMC
1 x IOOGE
densityelectrical management   optical
cold plate
slots
densityelectrical management optica
port
port
port
port
port
port
port
Form factor
XA320 compute node
XABZOC compute node
Remarks
Processor
2 x Kunpeng 920 (48 cores
2.6 GHz)2 x Kunpeng 920 (48 or 64 cores @ 26 GHz)
Coming in Q3: air cooling support for 64 cores 
DIMM slot
16 x DDR4 2933
32 GB currently_and 64 GB coming in 2023 03
The air-cooled (XA320) configuration supports only 
drives.
Drive
2 to 6 x 2.5-inch SAS/ SATA
The liquid-cooled (XA3ZOC) 48-core configurati
supports 6 drives.
The liquid-cooled (XA3ZOC) 64-core configuration
supports only 2 drives
LOM
2 x GE electrical port + 1 x 1OOGE optical port
PCle expansion
2 x PCle HHHL standard expansion slot
1 x PCle HHHL standard expansion slot
"F
Each node supports two drives when operating in th
Operating temperature
5 Cto 35 C (41
to 95*F)
ambient terperature of 35'C (41'F)
Dimensions (HxWxD)
40.5 mm x 177.9 mm x 545.5 mm (1.59 in x 700 in x 21.48 in )
65
Huawei Confidential
HUAWEI

Powerful HPC with 3000 W PSUs and Liquid Cooling
Computing Power Comparison with Intel Scalable Processors (2P)
The X6OO0 power turbo chassis improves the HPC
CFD
capability of a single cabinet by 209
CPU Model
Total
Frequency Maximum
Memory
Application
Cores
(GHz)
TDP (W)
Bandwidth
Compared with the x86 6248 solution; the comput
Performance*
2 x Gold 6248
40
25
150
192 GB/5
1
power per cabinet in the computational fluid
2 x Kunpeng 920
dynamics (CFD) scenario is increased by 20%.
96
2.6
150
287 GB/5
1.2
4826
The service performance is increased by 20% i
same footprint.
The CFD simulation time is shortened by 209.
High-Density Deployment with Fixed Computing Power
Number of
Number
CFD
The X6OO0 power turbo chassis reduces the quantity 
Footprint
Solution
Chassis Per
of
Application
Cabinet
Cabinets
Performance*
Saving
HPC cluster cabinets by 339.
2 x Kunpeng 920 4826 with15
4
240
To build an HPC cluster with fixed application
air cooling
2 x Kunpeng 920 4826 with
3396
computing power, XGOOO air cooling needs f
20
3
240
full liquid cooling
cabinets.
OpenFOAM is used for evaluation. Huawei lab data is used as test data, XGOOO full liquid cooling needs only three ca
which may vary according to test environments.
66
Huawei Confidential
HUAWEI

Quiz
1
(Multiple-answer question)
Which of the following
are
models of TaiShan 200
rack servers?
A 2280
B 5280
C. 2480
D RH2288
67
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
Linux OSs
D openEuler OS
Embedded OSs
D Basic openEuler Commands
5
openGauss Database
68
Huawei Confidential
HUAWEI

OS Definition
An OS is
9 program that manages computer hardware and software resources, and
is the
kernel underlying a computer system.
Common OS issues include managing and config
the memory, prioritizing tasks in allocating system resources, controlling i
devices, operating the network, and managing file systems. Additionall
interface for
users
to interact with systems.Smart wearables, TV boxes, servers, and
switching routers all have their own OSs.
Android, iOS,
Android,
Windows, RedFlag
Android, iOS, etc.
HarmonyOS, etc.
HarmonyOS, etc.
macOS, etc.
Mobile
Desktop
Smart home
Tablets
phones
computers
devices
69
Huawei Confidential
HUAWEI
PCs,

Origin of Linux
On October 5, 1991_Linus Torvalds officially announced the birth of the Linu
in the comp.os.minx newsgroup and open-sourced it.
Thanks to the open source community, the
Linux 1.0 kernel version
was officially
released in March 1994.
Linux
is
a
open
source
UNIX-like
OS.
It
is
a
multiuser ,multitasking,
multithreading, and multi-CPU OS based on POSIX and UNIX.
70
Huawei Confidential
HUAWEI
free,

Components of Linux
Components of Linux
Linux kernel
Application programs
Linux kernel project
Main author: Linus Torvalds (Finland)
In October 1991, Linux 0.02 (the first public version) was released.
In March 1994, Linux 1.0 was released.
a penguin; is the official mascot of the Linux kernel
71
Huawei Confidential
HUAWEI
Tux,

Common Linux OSs
Red Hat
Debian
Centos
Ubuntu
Fedora
Deepin
Linux OSs
Kaili Linux
Oracle Linux
DVL
Arch Linux
openEuler
NeoKylin
72
Huawei Confidential
HUAWEI

Centos
The CentOS Linux distribution is a stable, predictable; manageable; 
platform derived from the sources of Red Hat Enterprise Linux (RHE
from the RHEL source code under the GPL open source license.
After joining Red Hat in
2014, CentOS continued
to providefree
OS usage and
updates. CentOS is used in a wide range of applications and is espe
servers
On December 8, 2020, CentOS officially announced that the CentOS
came to
an end
Centos
users
now face challenges in updating, maintaining
migrating the OS after OS services stopped.
73
Huawei Confidential
HUAWEI

Debian
Debian is the
most GNU-compliant Linux OS50 far. It includes support for nearly
100 thousand
pieces of
open
source
software.
It
is stable and secure, and
is
compatible
with
various
kernel
architectures.
Free-of-charge
technical
support
makes Debian even
more popular.
Due to its excellent stability and
low
resource
overhead, Debian is widely used
in
virtual private servers
74
Huawei Confidential
HUAWEI

Ubuntu
Ubuntu
is built
on
Debian
It
is
an
open-source;
free
OS that targets desktop
applications; and is ideal for software emulation and cloud computing:
Ubuntu has a vibrant community to provide readily available suppor
75
Huawei Confidential
HUAWEI

Deepin
The Deepin OS is
a Linux distribution developed by Wuhan Deepin Tech
Ltd. It has in-house developedsoftware  features, including
the software center,
screenshotting; and music/video player, which are all presented in th
Deepin aims to
users with daily office work,
1 learning, and make entertainme
more
enjoyableIt
is
suitable
for laptops; desktopcomputers, and all-in-one
machines.
76
Huawei Confidential
HUAWEI
Co.,
help

NeoKylin
NeoKylin is aLinux release following the merging of COSIX Linux and K
It uses
an enhanced Linux kernel and is available in the desktop; general, adva
securityeditions.
It
has been widelyused in industries  suchas energy  finance;
transportation; and public sectors.
77
Huawei Confidential
HUAWEI

Common OSs Used in Each Industry
Industry
Common OSs
Telecom carrier
Centos
Banking and securities
CentOs, NeoKylin; Kylin
Internet
Enterprise-customized OS, Debian
Government and large
Centos, NeoKylin; Kylin, UOS
enterprises
Energy and electricity
CentOs, NeoKylin; Kylin; Ubuntu
Transportation
CentOS, NeoKylin
Public safety
Centos
Education and
CentOS, Kylin
healthcare
78
Huawei Confidential
HUAWEI

Kunpeng Processors' OS Compatibility
Common OSs
Deepin
Ubuntu
Kylin
Kunpeng
SUSE
Debian
Centos
NeoKylin
79
Huawei Confidential
HUAWEI

TaiShan Server's OS Compatibility
Specify the product type to query its OS compatibility .
Kunpeng Computing Compatibility Checker
Hone
EngEsh
Search OSs
Search Parts
Product Model
Part
CPU
Kunpeng 920 9230
DIMM
Disk
LOM
Mezz Card
OCP Card
PCle Card
RaID Card
[rpa Ycd
Epon [rel
Eopcri PDF
Hurh
Dtil
Eurtifcaton
Drivera
Noth
Ckoud Linn 7,6 [0l MRM
Updale
B0
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
D Kunpeng-Compatible OSs
openEuler OS
D Embedded OSs
5
openGauss Database
81
Huawei Confidential
HUAWEI

openEuler Overview
openEuler is an open-source version of EulerOS,
a server OS Huawei introduced in 2010. openE
one of the Linux distributions and is named after Leonhard Euler, a famous mathematician.
In September 2019, EulerOS was officially open-sourced and became known as 
The openEuler open
source
OS is an efficient, stable, and
secure OS based on the
Linux kernel
It
supports Kunpeng and other processors, and can maximize the computing power 
openEuler is suited for a wide range of
application scenarios such as databases, bi
computing, andAI. It is also
a global open source OS community that is built by contribu
across the world
82
Huawei Confidential
HUAWEI
chips.

openEuler Development History
September 25, 2021: openEuler
is released as an open source
digital infrastructure OS.
November 9, 2021: openEuler is
donated to the OpenAtom
2022
Foundation:
Used in all storage
products, wireless
2021
controllers, and Cloud
Edge management plane
openEuler is a recipient
Joint financial innovation
of the 2022 World
project in China
2019
Leading Internet Scientific
and Technological
Achieverents award.
2013
2010
2016-2019: EulerOS 2x is
in Huawei consumer
Initiates the
cloud, public/private cloud, NFV,
HPC project.
distributed storage; server, and
cloud core network solutions.
83
Huawei Confidential
HUAWEI
applied

openEuler-based Commercial Releases
iSoft
Kylin
iSoft Server OS V5.1 for Kunpeng
Kylin Server OS
OpenEuler
Linx
xFusion
Linx Secure OS V6.0
FusionOS 22
84
Huawei Confidential
HUAWEI

openEuler Technical Features: A-Tune (Automatic R
Optimization)
A-Tune is
an Al-driven automatic optimization system that
uses non-intrusive
system profiling to
sense service
workload, matching the optimal resource model for each service and responding to service c
Hadoop
AI
Sensing:
Generates profiles for
HPC
Database
mainstream service scenarios
of intelligent computing:
Web
Big data
System profiles foi seivice scenarios
A-Tune
Decision making:
Analyzes service models
Decision-making
4 Dynamic schedu ling
to dynamically schedule
resource models.
Exectitioni wvith optimal
confiquration
Execution:
05
Configures optimal parameters
across the full stack.
85
Huawei Confidential
HUAWEI
NginxKafka
M
y
S
Q
L
Apache
T
r
a
i
n
i
n
g
S
P
E
C
Inference
1
l
i
b
r
a
r
i
e
s
;
Base
Boot
system Kernel
Drivers

openEuler Technical Features: iSulad Container So
iSula is a general container engine solution; which boasts:
Fast bootup; various container patterns, and low resource consumption
Trusted and secure boot
Hitless upgrade
Enhanced security and commissioning
Application
Secure
System
container
container
container
iSulad
86
Huawei Confidential
HUAWEI

Kunpeng Hardware Feature: MPAM
Memory Partitioning and Monitoring (MPAM) is developed to control an
monitor
the allocation
and usage of the
L3 cache and memory bandwidth, benchmark
against the Resource Director Technology (RDT) feature of x86 h
openEuler
21.03 also supportsresource
management   using
the cache QoS and
memory bandwidth control technologies of AArch64.
87
Huawei Confidential
HUAWEI
chips.

Other openEuler Technical Features
System security
The openEuler 22.03 long term support (LTS)
System installation
version provides multiple security measures
openEuler 2203 LTS allows users to use
including identity authentication; security prot
the kickstart tool to automatically install
mandatory access control, integrity protection
the 05.
security audit, to ensure OS security for uppe
Multi-scenario convergence
applications.
openEuler 22.03 LTS is openEuler's first
System analysis and tuning
LTS version that supports multi-scenario
openEuler 22.03 LTS supports MySQL perfo
convergence. It allows various devices to
tuning and big data tuning; including Spark 
be deployed in server, cloud computing;
Hive tuning, and HBase tuning:
edge computing, and embedded scenarios.
Compiler
Innovation features
OpenEuler
openEuler 22.03 LTS supports the BiSheng C
openEuler 22.03 LTS has 23 million lines of
The Bisheng Compiler is a high-performanc
new code. It incorporates innovation
reliability , and easy-to-expand compiler too
features that have been commercially
developed by the Huawei Compiler Laboratory f
successful in the three innovation versions
general-purpose processor architectures, such as
of openEuler, and releases new features
KunpengIt introduces and enhances multiple
for four major scenarios.
compilation optimization technologies and s
different programming languages, such as C, C+
System management
and Fortran.
openEuler 22.03 LTS uses systemd to
Kernel
manage the 0S and services. systemd is
compatible with the init script of SysV and
openEuler 22.03 LTS is built based on Linux
Linux.
5.10. This kernel is an LTS version that provide
continuous updates to safeguard the Linux OS.
88
Huawei Confidential
HUAWEI

openEuler Open Source Community
Start Your Journey in openEuler
4 / sud0 yuM -Y vpaale
Your first
Lasi Melaqata eyphahon check 0 02,16 a0
On Wed Dec 22 09.0102 2021
coding experience
Dependencies [esolved
in openEuler
Kolhing [0 00.
Complexel
LET'S PLAY
01
02
03
04
Developers
Documents
Download
Community
Members
The openEuler code is hosted
On
On
on Gitee
https:/ /wwwopeneuler org/en, https:| /www openeuler org/en; All enterprises and organizations
Developers can submit bugs;developers can find all
developers can download theare welcome to join the
participate in discussions,
openEuler documents,
OS and related components.
openEuler open source
community, to build a vibrant
contribute code, and provide
including the Release Notes,
suggestions in the open
Installation Guide,
0S ecosystem together .
source community.
Administrator Guide; and
Feature Description.
89
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
D Kunpeng-Compatible OSs
D openEuler OS
Embedded OSs
5
openGauss Database
g0
Huawei Confidential
HUAWEI

Embedded OSs
An embedded OS is used in embedded systems. It is
9 type of system software suited for
a
wide range ofapplication scenarios; and generally includes the hardware-
driver software
a system kernel, device driver APIs, communication protocols,
a graphical
user interface,and
a standardized browser.An embedded
OS allocates
all hardware and
software
resources
of
embedded systems, schedules   tasks,
and
coordinates
concurrent
activities. It must reflect the characteristics of the embedded system where it is locate
can performthe functions   requiredthe embedded systemby loading and unloading
related
modules.
Popular embedded
OSs include HC/OS-II,embedded
Linux, Windows
Embedded, and VxWorks, as well as Android and iOS which are applied on
smartphones an
tablets.
91
Huawei Confidential
HUAWEI
by

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
Database Overview
openGauss Database
Basic Operations of openGauss
Application Development
92
Huawei Confidential
HUAWEI

Database
A database is a warehouse where data is organized, stored, and managed b
structure. It is a collection of a large amount of data that is stored in a comp
a long time; organized, shared, and managed in a unified manner.
Permanent
Organized
Can be shared
93
Huawei Confidential
HUAWEI

Relational Database Development History
Scale-up capability improvement
MPP technology of OLAP
In-memory database; hardware
Relational database
SQL specifications and
optimization, distributed deployment,
theory
optimization
enhanced reliability
and OLTPGOLAP convergence
19705
19805
19905
Database relation theories
SDL
RSI
Oracle
Oracle
Oracle
1970 EFCodd
1977-1979
1979-1983
1983 -
Exadata
System R
DBZ 9.7
System R
DBZ 1983-
Compatible with Oracle
IBM
1980-1982
1973-1977
Infomix 1984-
Infomix UE
IBM
Sybase 1984-
Sybase ASE
SAP
Ingres project
Ingres
SQL server 1992-
SQL server 2008
Microsoft
1974-?
1982-
China-developed database
Postgres 95
PostgreSQL
1995 -
1997 -
Enterprise DB
Green Plum
MySQL 5.5
Oracle
MySQL
1994 -
MySQL Cluster
Oracle
Maria DB
MySQL
Scale DB
replacement
Clustrix
H-store 2007 -
Volt DB 2010
94
Huawei Confidential
HUAWEI

Major Applications of Relational Databases
Service
Processing data
strategy
transactions
Business Processes
;
OLTP
8
OLAP
1
Business Data Warehouse
Analysis
On-Line Transaction Processing (OLTP)
On-Line Analytical Processing (OLAP)
OLTP is a typical
application of traditional relational databases. It OLAP is a typical
application of data warehouses. It support
is a highly-available online system that processes basic and
complex analysis and provides clear query results, helping
routine transactions, such as bank transactions, mainly with
companies make informed decisions. In the OLAP system; 
small transactions and queries.
quantity of the executed statements is not an evaluation
standard, because if the execution time of a statement is long
The OLTP system emphasizes on the database memory
the read data is huge:
efficiency. When evaluating an OLTP system; check the number
of transactions executed per second and the number of Execute
The OLAP system focuses on data analysis. The evaluation
SQL statements. It emphasizes the command rates of memory
standards are the throughput (bandwidth) of the disk
metrics, bound variables, and concurrent operations.
subsystem, SQL execution duration, disk I/0, and partitioning.
95
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
Database Overview
openGauss Database
Basic Operations of openGauss
Application Development
96
Huawei Confidential
HUAWEI

openGauss
As a leading enterprise-class database, openGauss is developed in collaboration with glo
core-oriented open-source relational database provides ultimate performance; full-link service and d
based tuning, and efficient O&M capabilities. openGauss is released under the Mulan Perm
v2 It deeply integrates Huawei's years of R&D experience in the database field and con
features based on enterprise-level scenario requirements.
openGauss
Robust
Superb
Rocksolid
Easy O&M
reliability
performance
security
97
Huawei Confidential
HUAWEI

openGauss Development History
Cloud & Open source Ecosystem
Productization
Internal use
openGauss
Incubation for
Joint innovation for
internal use
productization
Ecosystem building
2001-2011
2011-2019
2019-2020
2021-future
Enterprise-class in-
Bank G's core data warehouse and
GaussDB global release on15th, 2019.
Share enterprise-class data
memory database
commercial use of DWS on Huawei Cloud
Builds an ecosystem with global partners: management capabilities.
Lead ecosystem
Bank Z'5 core service system upgrade
Compatible with mainstream industry
construction:
from a commercial database.
ecosystems and complete interconnection with
industries such as finance.
Promote the development of
Helps with the comrercial use of 30,000+
database education.
sets of Huawei's more than 40 flagship
openGauss open source on June 30, 2020.
products, serving over 70 carriers and 2
billion users worldwide.
98
Huawei Confidential
HUAWEI
May
goes

Superb Performance
It provides the multi-core architecture-oriented concurrency control tec
hardware
optimization;and
achieves that
the
TPC-C benchmark performance
reaches
1,500,000 tpmC on Kunpeng 2-socket servers.
It uses NUMA-aware data structures
as the
kernel structures to adapt to the trend of
multi-core NUMA architecture on hardware.
It provides the SQL bypass intelligent engine technology.
99
Huawei Confidential
HUAWEI
key
using

Other Advantages
Constant Availability
Rocksolid Security
It supports multiple deployment modes, such
It supports security features such as fully -
a5 primary  standby synchronization,
encrypted computing; access control;
primary /standby asynchronization, and
encryption authentication; database
cascaded standby server deployment.
audit, and dynamic data masking to
It supports data page cyclic redundancy check
provide comprehensive end-to-end data
(CRC), and automatically restores damaged
security protection.
data pages through the standby node.
It recovers the standby node in parallel and
promotes it to primary to provide services
within 10 seconds.
Easy O&M
Simplified Development
It provides Al-based intelligent parameter
It adopts the Mulan Permissive
tuning and index recommendation to
Software License; allowing code to be
automatically recommend Al parameters.
freely modified, used, and referenced.
It provides slow SQL diagnosis and multi -
It fully opens database kernel
dimensional self-monitoring views to help
capabilities.
you understand system performance in real
It provides excessive partner
time.
certifications, training systems, and
It provides SQL time forecasting that
university courses.
supports online auto-learning:
100
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
Database Overview
openGauss Database
Basic Operations of openGauss
Application Development
101
Huawei Confidential
HUAWEI

SQL Definition
Wikipedia:
Structured Query Language (SQL) is a domain-specific language used in pro
It
is designed for managing data held in a relational database management system; 
stream processing in a relational data stream management system
SQL is based on relational algebra and tuple relational calculus; includin
definition language (DDL) and data manipulation language (DML). The sco
includes data insertion; query, update, and deletion, database schema creatio
modification; and data access control.
102
Huawei Confidential
HUAWEI

SQL Syntax
Data definition language (DDL)
DDL statements are used to define or modify objects in the database, such as tables, indexes, vie
sequences, users, roles; tablespaces, and stored procedures.
Data manipulation language (DML)
Performs operations on data in database tables, such as inserting; updating; and deleting dat
Data control language (DCL)
Sets or changes database transactions, performs authorization operations (such as granting
or roles, revoking permissions; creating roles; and deleting roles) , locks tables (supp
locks) , and stops services.
Data query language (DQL)
Queries data in a database; for example, querying data and combining the result s
statements.
103
Huawei Confidential
HUAWEI

Contents
1 . Kunpeng Ecosystem
2
Kunpeng Processors
3
TaiShan Servers
4
openEuler OS
5
openGauss Database
Database Overview
openGauss Database
Basic Operations of openGauss
Application Development
104
Huawei Confidential
HUAWEI

ODBC
OpenDatabase  Connectivity
(ODBC) is
an
open standard
API used
to
access
a
database in Windows. It is a component of the Windows Open Services A
(WOSA) and enables data sharing between heterogeneous database
ODBC is a unified API for accessing heterogeneous databases.
It allows applications
to
use
SQL
as
the
data
access
standard
to
access
data
in
different
database
management   systems.
Applicationscan
directly manipulatedata
in
a database
regardless of the database type. Through
ODBC youcan
access database files
on
various computers, and
even non-database objects such
as Excel tables and
ASCII
data files.
105
Huawei Confidential
HUAWEI

JDBC
The Java Database Connectivity (JDBC)
API provides universal data
access from the
Java programming language: It provides methods for querying and up
a
database.
JDBC is developedby Sun Microsystems.It
is used for
relational
databases.
106
Huawei Confidential
HUAWEI

Psycopg
Psycopgis
the
most
popularPostgreSQLdatabase adapterfor
the
Python
programming language.
Its main features are the complete implementation of the Python databa
specification and the thread safety (several threads can share the sam
The Psycopg package includes Zpsycopgda; a Zope database adapte
107
Huawei Confidential
HUAWEI

Quiz
1
(Single-answer question) Which of the following four groups of SQ
are DML commands?
A
CREATE, DROP, UPDATE
B
INSERT,
1 UPDATE, DELETE
C
INSERT,
1 DROP, ALTER
D. UPDATE, DELETE, ALTER
108
Huawei Confidential
HUAWEI

Summary
This course gave anoverview of the Kunpeng computing industry and Kunp
ecosystem; covering
Huawei Kunpeng processors; TaiShan servers, openE
and openGauss database.
Composition of the Kunpeng computing industry
Concepts of the Kunpeng ecosystem
Models,technologicalinnovations,and application
scenarios
of
Huawei
Kunpeng
processors
Models and specifications of TaiShan servers
D openEuler OS
openGauss database
109
Huawei Confidential
HUAWEI

Recommendations
openEuler open source community: https:/ /www.openeuler org /e
Kunpeng community: https:/ /www hikunpeng.com/en
openGauss open source community: https:/ lopengaussorg/en
110
Huawei Confidential
HUAWEI

Thank you-
0
Bring digital to every person, home; and
organization for a fully connected;
intelligent world.
Copyrlghto2023 Huawel Technologles Co., Ltd.
All Rights Reserved.
The information in this document may contain predictíve
statements including; without limitation; statements regarding
the future financial and operating results; future product
portfolio; new technology; etc There are @ number of factors
could causc actual results and developments to differ materially
from those expressed cr implied in the predictive statements.
Therefore, such information is provided for reference purpose
only and constitutes neither 2n offer nor an acceptance. Huawei
may change the information at any time without notice.
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deployment
12
Huawei Confidential
HUAWEI

Phase 1: Preparing the Porting Environment Based
on
a
Local TaiShan Server
Set up a local environment based on a TaiShan server
Local porting process
Arrival of
Tuning and
hardware
go-live
The server must be connected to the Internet.
Networking
Software
It takes time to configure physical servers and
configuration
porting
networking.
High device and O&M costs
Operating
0S installation
environment
deploym
