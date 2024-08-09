# Golang Trending Archive

Welcome to the Golang Trending Archive! This project aims to track and archive historical GitHub trending projects related to Go (Golang). <br>
This reposity reference from [aneasystone/github-trending](https://github.com/aneasystone/github-trending).

## Table of Contents

- [Golang Trending Archive](#golang-trending-archive)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Implementation](#implementation)
  - [Getting Started](#getting-started)
  - [All language](#all-language)
  - [Go](#go)
  - [Python](#python)
  - [Javascript](#javascript)
  - [C](#c)
  - [C++](#c-1)
  - [Typescript](#typescript)

## Introduction

The Golang Trending Archive is a project dedicated to preserving the historical records of trending GitHub projects related to the Go programming language. As GitHub's trending list is constantly changing, this repository helps in maintaining a historical archive of these projects.

## Features

- Archive of historical GitHub trending projects related to Go.
- Regular updates using GitHub Actions.
- No language restrictions, removing the Chinese query limitation.
- Monthly scheduled archiving tasks.

## Implementation

The main implementation of this project involves the following steps:

1. **Scraping GitHub Trending:** We use web scraping techniques to request and parse GitHub's trending page for Go projects. This allows us to extract information about trending projects.

2. **Data Storage:** Extracted data is stored in a structured format, such as md files, to maintain historical records.

3. **GitHub Actions:** We utilize GitHub Actions to automate the process of updating the archive on a regular basis. You can find the workflow configuration in the `.github/workflows` directory.

## Getting Started

To get started with the Golang Trending Archive, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/zengzzzzz/golang-trending-archive.git

# Daily Trending

## All language

* 【2024-08-07】[trailofbits / multiplier](https://github.com/trailofbits/multiplier) - Code auditing productivity multiplier.
* 【2024-08-07】[bghira / SimpleTuner](https://github.com/bghira/SimpleTuner) - A general fine-tuning kit geared toward Stable Diffusion 2.1, Stable Diffusion 3, DeepFloyd, and SDXL.
* 【2024-08-07】[ardalis / CleanArchitecture](https://github.com/ardalis/CleanArchitecture) - Clean Architecture Solution Template: A starting point for Clean Architecture with ASP.NET Core
* 【2024-08-06】[marticliment / UniGetUI](https://github.com/marticliment/UniGetUI) - UniGetUI: The Graphical Interface for your package managers. Could be terribly described as a package manager manager to manage your package managers
* 【2024-08-04】[mtdvio / every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) - A collection of (mostly) technical things every software developer should know about
* 【2024-08-04】[xvzc / SpoofDPI](https://github.com/xvzc/SpoofDPI) - A simple and fast anti-censorship tool written in Go
* 【2024-08-04】[apache / apisix](https://github.com/apache/apisix) - The Cloud-Native API Gateway
* 【2024-08-03】[teaxyz / white-paper](https://github.com/teaxyz/white-paper) - how will the protocol work?
* 【2024-08-01】[LibreHardwareMonitor / LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) - Libre Hardware Monitor, home of the fork of Open Hardware Monitor
## Python

* 【2024-08-09】[pytorch / rl](https://github.com/pytorch/rl) - A modular, primitive-first, python-first PyTorch library for Reinforcement Learning.
* 【2024-08-09】[statsmodels / statsmodels](https://github.com/statsmodels/statsmodels) - Statsmodels: statistical modeling and econometrics in Python
* 【2024-08-09】[jorhelp / Ingram](https://github.com/jorhelp/Ingram) - 网络摄像头漏洞扫描工具 | Webcam vulnerability scanning tool
* 【2024-08-08】[labmlai / annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) - 🧑‍🏫 60 Implementations/tutorials of deep learning papers with side-by-side notes 📝; including transformers (original, xl, switch, feedback, vit, ...), optimizers (adam, adabelief, sophia, ...), gans(cyclegan, stylegan2, ...), 🎮 reinforcement learning (ppo, dqn), capsnet, distillation, ... 🧠
* 【2024-08-08】[THUDM / CogVideo](https://github.com/THUDM/CogVideo) - Text-to-video generation: CogVideoX (2024) and CogVideo (ICLR 2023)
* 【2024-08-08】[hacksider / Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) - real time face swap and one-click video deepfake with only a single image (uncensored)
* 【2024-08-06】[CodeXBotz / File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot) - Telegram Bot to store Posts and Documents and it can Access by Special Links.
* 【2024-08-06】[Cog-Creators / Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - A multi-function Discord bot
* 【2024-08-05】[McGill-NLP / llm2vec](https://github.com/McGill-NLP/llm2vec) - Code for 'LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders'
* 【2024-08-04】[InternLM / lagent](https://github.com/InternLM/lagent) - A lightweight framework for building LLM-based agents
* 【2024-08-02】[pytorch / torchchat](https://github.com/pytorch/torchchat) - Run PyTorch LLMs locally on servers, desktop and mobile
* 【2024-08-02】[ohyicong / decrypt-chrome-passwords](https://github.com/ohyicong/decrypt-chrome-passwords) - 
* 【2024-08-02】[lucidrains / x-transformers](https://github.com/lucidrains/x-transformers) - A simple but complete full-attention transformer with a set of promising experimental features from various papers
* 【2024-08-01】[lucidrains / denoising-diffusion-pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch) - Implementation of Denoising Diffusion Probabilistic Model in Pytorch
* 【2024-08-01】[DAGWorks-Inc / burr](https://github.com/DAGWorks-Inc/burr) - Build applications that make decisions (chatbots, agents, simulations, etc...). Monitor, trace, persist, and execute on your own infrastructure.
* 【2024-08-01】[usnistgov / dioptra](https://github.com/usnistgov/dioptra) - Test Software for the Characterization of AI Technologies
## Java

* 【2024-08-09】[zongzibinbin / MallChat](https://github.com/zongzibinbin/MallChat) - mallchat的后端项目，是一个既能购物又能聊天的电商系统。以互联网企业级开发规范的要求来实现它，电商该有的购物车，订单，支付，推荐，搜索，拉新，促活，推送，物流，客服，它都必须有。持续更新ing。。（点个star，不迷路）
* 【2024-08-09】[pentaho / pentaho-kettle](https://github.com/pentaho/pentaho-kettle) - Pentaho Data Integration ( ETL ) a.k.a Kettle
* 【2024-08-09】[provectus / kafka-ui](https://github.com/provectus/kafka-ui) - Open-Source Web UI for Apache Kafka Management
* 【2024-08-09】[elunez / eladmin](https://github.com/elunez/eladmin) - eladmin jpa 版本：项目基于 Spring Boot 2.6.4、 Jpa、 Spring Security、Redis、Vue的前后端分离的后台管理系统，项目采用分模块开发方式， 权限控制采用 RBAC，支持数据字典与数据权限管理，支持一键生成前后端代码，支持动态路由
* 【2024-08-09】[netty / netty](https://github.com/netty/netty) - Netty project - an event-driven asynchronous network application framework
* 【2024-08-09】[androidx / media](https://github.com/androidx/media) - Jetpack Media3 support libraries for media use cases, including ExoPlayer, an extensible media player for Android
* 【2024-08-09】[JetBrains / JetBrainsRuntime](https://github.com/JetBrains/JetBrainsRuntime) - Runtime environment based on OpenJDK for running IntelliJ Platform-based products on Windows, macOS, and Linux
* 【2024-08-09】[alibaba / druid](https://github.com/alibaba/druid) - 阿里云计算平台DataWorks(https://help.aliyun.com/document_detail/137663.html) 团队出品，为监控而生的数据库连接池
* 【2024-08-08】[aws / aws-sdk-java-v2](https://github.com/aws/aws-sdk-java-v2) - The official AWS SDK for Java - Version 2
* 【2024-08-08】[software-mansion / react-native-svg](https://github.com/software-mansion/react-native-svg) - SVG library for React Native, React Native Web, and plain React web projects.
* 【2024-08-08】[debezium / debezium](https://github.com/debezium/debezium) - Change data capture for a variety of databases. Please log issues at https://issues.redhat.com/browse/DBZ.
* 【2024-08-08】[apache / druid](https://github.com/apache/druid) - Apache Druid: a high performance real-time analytics database.
* 【2024-08-08】[SeleniumHQ / selenium](https://github.com/SeleniumHQ/selenium) - A browser automation framework and ecosystem.
* 【2024-08-08】[checkstyle / checkstyle](https://github.com/checkstyle/checkstyle) - Checkstyle is a development tool to help programmers write Java code that adheres to a coding standard. By default it supports the Google Java Style Guide and Sun Code Conventions, but is highly configurable. It can be invoked with an ANT task and a command line program.
* 【2024-08-07】[google / gson](https://github.com/google/gson) - A Java serialization/deserialization library to convert Java Objects into JSON and back
* 【2024-08-07】[apache / pulsar](https://github.com/apache/pulsar) - Apache Pulsar - distributed pub-sub messaging system
* 【2024-08-07】[Activiti / Activiti](https://github.com/Activiti/Activiti) - Activiti is a light-weight workflow and Business Process Management (BPM) Platform targeted at business people, developers and system admins. Its core is a super-fast and rock-solid BPMN 2 process engine for Java. It's open-source and distributed under the Apache license. Activiti runs in any Java application, on a server, on a cluster or in the…
* 【2024-08-07】[alibaba / transmittable-thread-local](https://github.com/alibaba/transmittable-thread-local) - 📌 a missing Java std lib(simple & 0-dependency) for framework/middleware, provide an enhanced InheritableThreadLocal that transmits values between threads even using thread pooling components.
* 【2024-08-07】[OpenAPITools / openapi-generator](https://github.com/OpenAPITools/openapi-generator) - OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec (v2, v3)
* 【2024-08-07】[apache / fury](https://github.com/apache/fury) - A blazingly fast multi-language serialization framework powered by JIT and zero-copy.
* 【2024-08-07】[camunda / camunda](https://github.com/camunda/camunda) - Process Orchestration Framework
* 【2024-08-07】[preslavmihaylov / booknotes](https://github.com/preslavmihaylov/booknotes) - A collection of my book notes on various subjects, mainly computer science
* 【2024-08-07】[DataDog / dd-trace-java](https://github.com/DataDog/dd-trace-java) - Datadog APM client for Java
* 【2024-08-07】[apache / avro](https://github.com/apache/avro) - Apache Avro is a data serialization system.
* 【2024-08-07】[alibaba / spring-cloud-alibaba](https://github.com/alibaba/spring-cloud-alibaba) - Spring Cloud Alibaba provides a one-stop solution for application development for the distributed solutions of Alibaba middleware.
* 【2024-08-07】[thingsboard / thingsboard](https://github.com/thingsboard/thingsboard) - Open-source IoT Platform - Device management, data collection, processing and visualization.
* 【2024-08-06】[questdb / questdb](https://github.com/questdb/questdb) - QuestDB is an open source time-series database for fast ingest and SQL queries
* 【2024-08-06】[apache / rocketmq](https://github.com/apache/rocketmq) - Apache RocketMQ is a cloud native messaging and streaming platform, making it simple to build event-driven applications.
* 【2024-08-06】[cinit / QAuxiliary](https://github.com/cinit/QAuxiliary) - QNotified phoenix - To make OICQ great again
* 【2024-08-06】[google / guava](https://github.com/google/guava) - Google core libraries for Java
* 【2024-08-06】[FabricMC / fabric](https://github.com/FabricMC/fabric) - Essential hooks for modding with Fabric.
* 【2024-08-06】[jhy / jsoup](https://github.com/jhy/jsoup) - jsoup: the Java HTML parser, built for HTML editing, cleaning, scraping, and XSS safety.
* 【2024-08-06】[CaffeineMC / sodium-fabric](https://github.com/CaffeineMC/sodium-fabric) - A Fabric mod designed to improve frame rates and reduce micro-stutter
* 【2024-08-06】[LSPosed / LSPatch](https://github.com/LSPosed/LSPatch) - LSPatch: A non-root Xposed framework extending from LSPosed
* 【2024-08-05】[cabaletta / baritone](https://github.com/cabaletta/baritone) - google maps for block game
* 【2024-08-05】[LawnchairLauncher / lawnchair](https://github.com/LawnchairLauncher/lawnchair) - No clever tagline needed.
* 【2024-08-05】[spring-projects / spring-framework](https://github.com/spring-projects/spring-framework) - Spring Framework
* 【2024-08-05】[PlayPro / CoreProtect](https://github.com/PlayPro/CoreProtect) - CoreProtect is a blazing fast data logging and anti-griefing tool for Minecraft servers.
* 【2024-08-05】[microg / GmsCore](https://github.com/microg/GmsCore) - Free implementation of Play Services
* 【2024-08-05】[RikkaApps / Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - The API and the developer guide for Shizuku and Sui.
* 【2024-08-05】[xiaojieonly / Ehviewer_CN_SXJ](https://github.com/xiaojieonly/Ehviewer_CN_SXJ) - ehviewer，用爱发电，快乐前行
* 【2024-08-05】[xpipe-io / xpipe](https://github.com/xpipe-io/xpipe) - Your entire server infrastructure at your fingertips
* 【2024-08-05】[MinecraftForge / MinecraftForge](https://github.com/MinecraftForge/MinecraftForge) - Modifications to the Minecraft base files to assist in compatibility between mods. New Discord: https://discord.minecraftforge.net/
* 【2024-08-05】[libgdx / libgdx](https://github.com/libgdx/libgdx) - Desktop/Android/HTML5/iOS Java game development framework
* 【2024-08-04】[Blankj / AndroidUtilCode](https://github.com/Blankj/AndroidUtilCode) - 🔥 Android developers should collect the following utils(updating).
* 【2024-08-04】[trinodb / trino](https://github.com/trinodb/trino) - Official repository of Trino, the distributed SQL query engine for big data, formerly known as PrestoSQL (https://trino.io)
* 【2024-08-04】[alibaba / Sentinel](https://github.com/alibaba/Sentinel) - A powerful flow control component enabling reliability, resilience and monitoring for microservices. (面向云原生微服务的高可用流控防护组件)
* 【2024-08-04】[DataLinkDC / dinky](https://github.com/DataLinkDC/dinky) - Dinky is a real-time data development platform based on Apache Flink, enabling agile data development, deployment and operation.
* 【2024-08-04】[real-logic / aeron](https://github.com/real-logic/aeron) - Efficient reliable UDP unicast, UDP multicast, and IPC message transport
* 【2024-08-04】[alibaba / arthas](https://github.com/alibaba/arthas) - Alibaba Java Diagnostic Tool Arthas/Alibaba Java诊断利器Arthas
* 【2024-08-04】[krlvm / PowerTunnel](https://github.com/krlvm/PowerTunnel) - Powerful and extensible proxy server with anti-censorship functionality
* 【2024-08-04】[apache / dubbo](https://github.com/apache/dubbo) - The java implementation of Apache Dubbo. An RPC and microservice framework.
* 【2024-08-04】[apache / hertzbeat](https://github.com/apache/hertzbeat) - Apache HertzBeat(incubating) is a real-time monitoring system with agentless, performance cluster, prometheus-compatible, custom monitoring and status page building capabilities.
* 【2024-08-04】[scwang90 / SmartRefreshLayout](https://github.com/scwang90/SmartRefreshLayout) - 🔥下拉刷新、上拉加载、二级刷新、淘宝二楼、RefreshLayout、OverScroll，Android智能下拉刷新框架，支持越界回弹、越界拖动，具有极强的扩展性，集成了几十种炫酷的Header和 Footer。
* 【2024-08-03】[strimzi / strimzi-kafka-operator](https://github.com/strimzi/strimzi-kafka-operator) - Apache Kafka® running on Kubernetes
* 【2024-08-03】[redis / lettuce](https://github.com/redis/lettuce) - Advanced Java Redis client for thread-safe sync, async, and reactive usage. Supports Cluster, Sentinel, Pipelining, and codecs.
* 【2024-08-03】[apache / calcite](https://github.com/apache/calcite) - Apache Calcite
* 【2024-08-03】[keycloak / keycloak](https://github.com/keycloak/keycloak) - Open Source Identity and Access Management For Modern Applications and Services
* 【2024-08-03】[opensearch-project / OpenSearch](https://github.com/opensearch-project/OpenSearch) - 🔎 Open source distributed and RESTful search engine.
* 【2024-08-03】[mcastillof / FakeTraveler](https://github.com/mcastillof/FakeTraveler) - Fake where your phone is located (Mock location for Android).
* 【2024-08-03】[apolloconfig / apollo](https://github.com/apolloconfig/apollo) - Apollo is a reliable configuration management system suitable for microservice configuration management scenarios.
* 【2024-08-03】[apache / incubator-seata](https://github.com/apache/incubator-seata) - 🔥 Seata is an easy-to-use, high-performance, open source distributed transaction solution.
* 【2024-08-03】[kunal-kushwaha / DSA-Bootcamp-Java](https://github.com/kunal-kushwaha/DSA-Bootcamp-Java) - This repository consists of the code samples, assignments, and notes for the Java data structures & algorithms + interview preparation bootcamp of WeMakeDevs.
* 【2024-08-03】[raphw / byte-buddy](https://github.com/raphw/byte-buddy) - Runtime code generation for the Java virtual machine.
* 【2024-08-03】[OpenRefine / OpenRefine](https://github.com/OpenRefine/OpenRefine) - OpenRefine is a free, open source power tool for working with messy data and improving it
* 【2024-08-03】[eugenp / tutorials](https://github.com/eugenp/tutorials) - Just Announced - "Learn Spring Security OAuth":
* 【2024-08-03】[krlvm / PowerTunnel-Android](https://github.com/krlvm/PowerTunnel-Android) - Powerful and extensible proxy server with anti-censorship functionality for Android
* 【2024-08-02】[jeecgboot / JeecgBoot](https://github.com/jeecgboot/JeecgBoot) - 🔥「企业级低代码平台」前后端分离架构SpringBoot 2.x/3.x，SpringCloud，Ant Design&Vue3，Mybatis，Shiro，JWT。强大的代码生成器让前后端代码一键生成，无需写任何代码! 引领新的开发模式OnlineCoding->代码生成->手工MERGE，帮助Java项目解决70%重复工作，让开发更关注业务，既能快速提高效率，帮助公司节省成本，同时又不失灵活性。
* 【2024-08-02】[open-telemetry / opentelemetry-java-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation) - OpenTelemetry auto-instrumentation and instrumentation libraries for Java
* 【2024-08-02】[alibaba / COLA](https://github.com/alibaba/COLA) - 🥤 COLA: Clean Object-oriented & Layered Architecture
* 【2024-08-02】[elastic / logstash](https://github.com/elastic/logstash) - Logstash - transport and process your logs, events, or other data
* 【2024-08-02】[quarkusio / quarkus](https://github.com/quarkusio/quarkus) - Quarkus: Supersonic Subatomic Java.
* 【2024-08-02】[java-native-access / jna](https://github.com/java-native-access/jna) - Java Native Access
* 【2024-08-02】[apache / hive](https://github.com/apache/hive) - Apache Hive
* 【2024-08-02】[grpc / grpc-java](https://github.com/grpc/grpc-java) - The Java gRPC implementation. HTTP/2 based RPC
* 【2024-08-02】[openrewrite / rewrite](https://github.com/openrewrite/rewrite) - Automated mass refactoring of source code.
* 【2024-08-02】[flyway / flyway](https://github.com/flyway/flyway) - Flyway by Redgate • Database Migrations Made Easy.
* 【2024-08-02】[xkcoding / spring-boot-demo](https://github.com/xkcoding/spring-boot-demo) - 🚀一个用来深入学习并实战 Spring Boot 的项目。
* 【2024-08-02】[hibernate / hibernate-orm](https://github.com/hibernate/hibernate-orm) - Hibernate's core Object/Relational Mapping functionality
* 【2024-08-02】[apache / beam](https://github.com/apache/beam) - Apache Beam is a unified programming model for Batch and Streaming data processing.
* 【2024-08-01】[apache / hadoop](https://github.com/apache/hadoop) - Apache Hadoop
* 【2024-08-01】[devopshydclub / vprofile-project](https://github.com/devopshydclub/vprofile-project) - 
* 【2024-08-01】[obsidiandynamics / kafdrop](https://github.com/obsidiandynamics/kafdrop) - Kafka Web UI
* 【2024-08-01】[json-path / JsonPath](https://github.com/json-path/JsonPath) - Java JsonPath implementation
* 【2024-08-01】[apache / gravitino](https://github.com/apache/gravitino) - World's most powerful open data catalog for building a high-performance, geo-distributed and federated metadata lake.
* 【2024-08-01】[alibaba / DataX](https://github.com/alibaba/DataX) - DataX是阿里云DataWorks数据集成的开源版本。
* 【2024-08-01】[apache / pinot](https://github.com/apache/pinot) - Apache Pinot - A realtime distributed OLAP datastore
* 【2024-08-01】[TheAlgorithms / Java](https://github.com/TheAlgorithms/Java) - All Algorithms implemented in Java
* 【2024-08-01】[datahub-project / datahub](https://github.com/datahub-project/datahub) - The Metadata Platform for your Data Stack
* 【2024-08-01】[JetBrains / intellij-community](https://github.com/JetBrains/intellij-community) - IntelliJ IDEA Community Edition & IntelliJ Platform
* 【2024-08-01】[karatelabs / karate](https://github.com/karatelabs/karate) - Test Automation Made Simple
* 【2024-08-01】[apache / tomcat](https://github.com/apache/tomcat) - Apache Tomcat
* 【2024-08-01】[exadel-inc / CompreFace](https://github.com/exadel-inc/CompreFace) - Leading free and open-source face recognition system
* 【2024-08-01】[awsdocs / aws-doc-sdk-examples](https://github.com/awsdocs/aws-doc-sdk-examples) - Welcome to the AWS Code Examples Repository. This repo contains code examples used in the AWS documentation, AWS SDK Developer Guides, and more. For more information, see the Readme.md file below.
* 【2024-08-01】[WeiYe-Jing / datax-web](https://github.com/WeiYe-Jing/datax-web) - DataX集成可视化页面，选择数据源即可一键生成数据同步任务，支持RDBMS、Hive、HBase、ClickHouse、MongoDB等数据源，批量创建RDBMS数据同步任务，集成开源调度系统，支持分布式、增量同步数据、实时查看运行日志、监控执行器资源、KILL运行进程、数据源信息加密等。
* 【2024-08-01】[alibaba / jetcache](https://github.com/alibaba/jetcache) - JetCache is a Java cache framework.
## C

* 【2024-08-09】[openocd-org / openocd](https://github.com/openocd-org/openocd) - Official OpenOCD Read-Only Mirror (no pull requests)
* 【2024-08-07】[ataradov / usb-sniffer-lite](https://github.com/ataradov/usb-sniffer-lite) - A simple USB sniffer based on Raspberry Pi RP2040
* 【2024-08-05】[pr3y / Bruce](https://github.com/pr3y/Bruce) - Firmware for m5stack Cardputer, StickC and ESP32
* 【2024-08-04】[hufrea / byedpi](https://github.com/hufrea/byedpi) - Bypass DPI
* 【2024-08-03】[kiddin9 / openwrt-packages](https://github.com/kiddin9/openwrt-packages) - openwrt packages
* 【2024-08-02】[basil00 / Divert](https://github.com/basil00/Divert) - WinDivert: Windows Packet Divert
* 【2024-08-01】[open-sdr / openwifi](https://github.com/open-sdr/openwifi) - open-source IEEE 802.11 WiFi baseband FPGA (chip) design: driver, software
## C++

* 【2024-08-04】[cdcseacave / openMVS](https://github.com/cdcseacave/openMVS) - open Multi-View Stereo reconstruction library
* 【2024-08-04】[wwmm / easyeffects](https://github.com/wwmm/easyeffects) - Limiter, compressor, convolver, equalizer and auto volume and many other plugins for PipeWire applications
* 【2024-08-04】[introlab / rtabmap](https://github.com/introlab/rtabmap) - RTAB-Map library and standalone application
* 【2024-08-03】[microsoft / SEAL](https://github.com/microsoft/SEAL) - Microsoft SEAL is an easy-to-use and powerful homomorphic encryption library.
* 【2024-08-03】[AcademySoftwareFoundation / openvdb](https://github.com/AcademySoftwareFoundation/openvdb) - OpenVDB - Sparse volume data structure and tools
* 【2024-08-02】[AdaptiveCpp / AdaptiveCpp](https://github.com/AdaptiveCpp/AdaptiveCpp) - Implementation of SYCL and C++ standard parallelism for CPUs and GPUs from all vendors: The independent, community-driven compiler for C++-based heterogeneous programming models. Lets applications adapt themselves to all the hardware in the system - even at runtime!
* 【2024-08-02】[thedmd / imgui-node-editor](https://github.com/thedmd/imgui-node-editor) - Node Editor built using Dear ImGui
* 【2024-08-01】[randombit / botan](https://github.com/randombit/botan) - Cryptography Toolkit
## Go

* 【2024-08-09】[gabriel-vasile / mimetype](https://github.com/gabriel-vasile/mimetype) - A fast Golang library for media type and file extension detection, based on magic numbers
* 【2024-08-07】[encoredev / encore](https://github.com/encoredev/encore) - Encore is the Backend Development Platform for building distributed systems and event-driven applications.
* 【2024-08-07】[99designs / aws-vault](https://github.com/99designs/aws-vault) - A vault for securely storing and accessing AWS credentials in development environments
* 【2024-08-02】[KindlingProject / kindling](https://github.com/KindlingProject/kindling) - eBPF-based Cloud Native Monitoring Tool
## Javascript

* 【2024-08-07】[hackthedev / dcts-shipping](https://github.com/hackthedev/dcts-shipping) - A Chat Platform like Discord but self-hostable like TeamSpeak
* 【2024-08-06】[webtorrent / webtorrent](https://github.com/webtorrent/webtorrent) - ⚡️ Streaming torrent client for the web
* 【2024-08-04】[SadeghHayeri / GreenTunnel](https://github.com/SadeghHayeri/GreenTunnel) - GreenTunnel is an anti-censorship utility designed to bypass the DPI system that is put in place by various ISPs to block access to certain websites.
* 【2024-08-03】[CanadaHonk / porffor](https://github.com/CanadaHonk/porffor) - A from-scratch experimental AOT JS engine, written in JS
* 【2024-08-03】[pcottle / learnGitBranching](https://github.com/pcottle/learnGitBranching) - An interactive git visualization and tutorial. Aspiring students of git can use this app to educate and challenge themselves towards mastery of git!
* 【2024-08-02】[tailwindlabs / tailwindcss-typography](https://github.com/tailwindlabs/tailwindcss-typography) - Beautiful typographic defaults for HTML you don't control.
## Typescript

* 【2024-08-09】[certd / certd](https://github.com/certd/certd) - 免费通配符域名SSL证书全自动申请、更新、续期、部署安装，支持部署到阿里云、腾讯云、ssh主机。Automatically apply, renew and deploy free Generic domain SSL Certificates。
* 【2024-08-06】[Jigsaw-Code / outline-server](https://github.com/Jigsaw-Code/outline-server) - Outline Server, developed by Jigsaw. The Outline Server is a proxy server that runs a Shadowsocks instance and provides a REST API for access key management.
* 【2024-08-05】[electron-userland / electron-builder](https://github.com/electron-userland/electron-builder) - A complete solution to package and build a ready for distribution Electron app with “auto update” support out of the box
* 【2024-08-05】[keldaanCommunity / pokemonAutoChess](https://github.com/keldaanCommunity/pokemonAutoChess) - Pokemon Auto Chess Game. Made by fans for fans. Open source, non profit. All rights to the Pokemon Company.
* 【2024-08-05】[Jonghakseo / chrome-extension-boilerplate-react-vite](https://github.com/Jonghakseo/chrome-extension-boilerplate-react-vite) - Chrome Extension Boilerplate with React + Vite + Typescript
* 【2024-08-04】[Tonejs / Tone.js](https://github.com/Tonejs/Tone.js) - A Web Audio framework for making interactive music in the browser.
* 【2024-08-02】[ssoready / ssoready](https://github.com/ssoready/ssoready) - Open-source dev tools for enterprise SSO. Ship SAML support this afternoon.
* 【2024-08-02】[reduxjs / redux](https://github.com/reduxjs/redux) - A JS library for predictable global state management
* 【2024-08-02】[vue-mini / vue-mini](https://github.com/vue-mini/vue-mini) - 基于 Vue 3 的小程序框架。简单，强大，高性能。
* 【2024-08-02】[asyncapi / website](https://github.com/asyncapi/website) - AsyncAPI specification website
