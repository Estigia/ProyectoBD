CREATE DATABASE  IF NOT EXISTS `PeriodicoBD` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `PeriodicoBD`;
-- MySQL dump 10.13  Distrib 5.7.9, for linux-glibc2.5 (x86_64)
--
-- Host: 127.0.0.1    Database: PeriodicoBD
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Armas_arma`
--

DROP TABLE IF EXISTS `Armas_arma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Armas_arma` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calibre` varchar(20) DEFAULT NULL,
  `marca` varchar(45) DEFAULT NULL,
  `categoria` varchar(2) NOT NULL,
  `serial` varchar(45) DEFAULT NULL,
  `objeto` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Armas_arma`
--

LOCK TABLES `Armas_arma` WRITE;
/*!40000 ALTER TABLE `Armas_arma` DISABLE KEYS */;
INSERT INTO `Armas_arma` VALUES (1,'.50','Colt','Fg','asdasdggdgfd','Escopeta');
/*!40000 ALTER TABLE `Armas_arma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Registros_actividad`
--

DROP TABLE IF EXISTS `Registros_actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Registros_actividad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actividad` varchar(45) NOT NULL,
  `Registro_id_id` int(11) NOT NULL,
  `Usuario_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Registros_actividad_d42349ca` (`Registro_id_id`),
  KEY `Registros_actividad_dc06fbee` (`Usuario_id_id`),
  CONSTRAINT `Registros_activ_Registro_id_id_8077cee2_fk_Registros_registro_id` FOREIGN KEY (`Registro_id_id`) REFERENCES `Registros_registro` (`id`),
  CONSTRAINT `Registros_actividad_Usuario_id_id_87fee64b_fk_home_usuario_id` FOREIGN KEY (`Usuario_id_id`) REFERENCES `home_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Registros_actividad`
--

LOCK TABLES `Registros_actividad` WRITE;
/*!40000 ALTER TABLE `Registros_actividad` DISABLE KEYS */;
INSERT INTO `Registros_actividad` VALUES (1,'Creado',1,2);
/*!40000 ALTER TABLE `Registros_actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Registros_registro`
--

DROP TABLE IF EXISTS `Registros_registro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Registros_registro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fiscal` varchar(60) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL,
  `descripcion` longtext NOT NULL,
  `movil` varchar(100) NOT NULL,
  `no_expediente` varchar(40) NOT NULL,
  `Arma_id` int(11) NOT NULL,
  `Municipio_id` int(11) NOT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `apellidos` varchar(55) NOT NULL,
  `cui` varchar(13),
  `edad` smallint(6),
  `muerto` tinyint(1) NOT NULL,
  `nombres` varchar(55) NOT NULL,
  `profesion` varchar(45),
  `sexo` varchar(2) NOT NULL,
  `ubicacion` longtext NOT NULL,
  `no_casquillos` smallint(6),
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Registros_registro_Arma_id_42fbd22d_fk_Armas_arma_id` (`Arma_id`),
  KEY `Registros_r_Municipio_id_f2a81b9d_fk_localizaciones_municipio_id` (`Municipio_id`),
  CONSTRAINT `Registros_r_Municipio_id_f2a81b9d_fk_localizaciones_municipio_id` FOREIGN KEY (`Municipio_id`) REFERENCES `localizaciones_municipio` (`id`),
  CONSTRAINT `Registros_registro_Arma_id_42fbd22d_fk_Armas_arma_id` FOREIGN KEY (`Arma_id`) REFERENCES `Armas_arma` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Registros_registro`
--

LOCK TABLES `Registros_registro` WRITE;
/*!40000 ALTER TABLE `Registros_registro` DISABLE KEYS */;
INSERT INTO `Registros_registro` VALUES (1,'asfseergtehryh','2016-02-14 23:55:00.000000','asdasfdsfsgdfhjgkhljk','asalto','12443756878',1,1,'2016-04-23 09:14:02.678540','xx','124234347668',34,1,'xx','asfdgdfgd','M','dsgfhgkjlk.dfsferhrthtyhfd',60,1);
/*!40000 ALTER TABLE `Registros_registro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add tipo_ usuario',6,'add_tipo_usuario'),(17,'Can change tipo_ usuario',6,'change_tipo_usuario'),(18,'Can delete tipo_ usuario',6,'delete_tipo_usuario'),(19,'Can add usuario',7,'add_usuario'),(20,'Can change usuario',7,'change_usuario'),(21,'Can delete usuario',7,'delete_usuario'),(22,'Can add arma',8,'add_arma'),(23,'Can change arma',8,'change_arma'),(24,'Can delete arma',8,'delete_arma'),(25,'Can add departamento',9,'add_departamento'),(26,'Can change departamento',9,'change_departamento'),(27,'Can delete departamento',9,'delete_departamento'),(28,'Can add municipio',10,'add_municipio'),(29,'Can change municipio',10,'change_municipio'),(30,'Can delete municipio',10,'delete_municipio'),(31,'Can add registro',11,'add_registro'),(32,'Can change registro',11,'change_registro'),(33,'Can delete registro',11,'delete_registro'),(34,'Can add actividad',12,'add_actividad'),(35,'Can change actividad',12,'change_actividad'),(36,'Can delete actividad',12,'delete_actividad');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_home_usuario_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_home_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `home_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-04-23 09:12:36.759056','1','Quetzaltenango',1,'Added.',9,2),(2,'2016-04-23 09:12:49.198285','1','Quetzaltenango',1,'Added.',10,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'Armas','arma'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'home','tipo_usuario'),(7,'home','usuario'),(9,'localizaciones','departamento'),(10,'localizaciones','municipio'),(12,'Registros','actividad'),(11,'Registros','registro'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Armas','0001_initial','2016-04-23 09:04:03.167570'),(2,'Armas','0002_auto_20160419_2300','2016-04-23 09:04:04.680446'),(3,'Armas','0003_auto_20160419_2321','2016-04-23 09:04:05.384013'),(4,'Armas','0004_auto_20160420_0006','2016-04-23 09:04:06.034373'),(5,'Armas','0005_auto_20160420_2351','2016-04-23 09:04:06.574160'),(6,'Armas','0006_auto_20160423_0113','2016-04-23 09:04:06.596829'),(7,'Armas','0007_auto_20160423_0552','2016-04-23 09:04:07.061217'),(8,'localizaciones','0001_initial','2016-04-23 09:04:09.669438'),(9,'home','0001_initial','2016-04-23 09:04:10.944560'),(10,'home','0002_auto_20160325_0011','2016-04-23 09:04:11.939232'),(11,'Registros','0001_initial','2016-04-23 09:04:18.287445'),(12,'Registros','0002_auto_20160421_0149','2016-04-23 09:04:20.329671'),(13,'Registros','0003_auto_20160421_0213','2016-04-23 09:04:25.348864'),(14,'Registros','0004_auto_20160421_0216','2016-04-23 09:04:25.469897'),(15,'Registros','0005_auto_20160422_0109','2016-04-23 09:04:26.668005'),(16,'Registros','0006_auto_20160422_0122','2016-04-23 09:04:28.620248'),(17,'Registros','0007_registro_no_casquillos','2016-04-23 09:04:29.191241'),(18,'Registros','0005_registro_is_active','2016-04-23 09:04:29.765120'),(19,'Registros','0007_merge','2016-04-23 09:05:16.697743'),(20,'contenttypes','0001_initial','2016-04-23 09:05:17.320873'),(21,'admin','0001_initial','2016-04-23 09:05:18.768585'),(22,'admin','0002_logentry_remove_auto_add','2016-04-23 09:05:18.902857'),(23,'contenttypes','0002_remove_content_type_name','2016-04-23 09:05:19.975661'),(24,'auth','0001_initial','2016-04-23 09:05:23.439762'),(25,'auth','0002_alter_permission_name_max_length','2016-04-23 09:05:23.997617'),(26,'auth','0003_alter_user_email_max_length','2016-04-23 09:05:24.075898'),(27,'auth','0004_alter_user_username_opts','2016-04-23 09:05:24.168302'),(28,'auth','0005_alter_user_last_login_null','2016-04-23 09:05:24.249825'),(29,'auth','0006_require_contenttypes_0002','2016-04-23 09:05:24.302119'),(30,'auth','0007_alter_validators_add_error_messages','2016-04-23 09:05:24.354509'),(31,'home','0003_auto_20160405_0546','2016-04-23 09:05:26.055936'),(32,'home','0004_auto_20160405_0550','2016-04-23 09:05:26.147773'),(33,'home','0005_auto_20160406_0435','2016-04-23 09:05:26.246369'),(34,'home','0006_auto_20160406_0457','2016-04-23 09:05:26.318953'),(35,'home','0007_auto_20160406_0525','2016-04-23 09:05:27.522829'),(36,'home','0008_auto_20160416_2230','2016-04-23 09:05:27.629733'),(37,'home','0009_auto_20160419_2303','2016-04-23 09:05:27.701428'),(38,'home','0010_auto_20160419_2321','2016-04-23 09:05:27.778315'),(39,'home','0011_auto_20160420_0006','2016-04-23 09:05:27.853748'),(40,'home','0012_auto_20160420_2352','2016-04-23 09:05:27.931081'),(41,'home','0013_auto_20160421_0149','2016-04-23 09:05:28.014608'),(42,'home','0014_auto_20160421_0213','2016-04-23 09:05:28.087499'),(43,'home','0015_auto_20160421_0216','2016-04-23 09:05:28.163489'),(44,'home','0016_auto_20160421_0511','2016-04-23 09:05:28.246417'),(45,'home','0017_auto_20160422_0109','2016-04-23 09:05:28.329411'),(46,'home','0018_auto_20160422_0122','2016-04-23 09:05:28.406999'),(47,'home','0019_auto_20160423_0113','2016-04-23 09:05:28.490396'),(48,'home','0020_auto_20160423_0552','2016-04-23 09:05:28.562070'),(49,'home','0017_auto_20160423_0058','2016-04-23 09:05:28.649211'),(50,'home','0018_auto_20160423_0214','2016-04-23 09:05:28.743088'),(51,'home','0017_auto_20160422_0153','2016-04-23 09:05:28.819717'),(52,'home','0019_merge','2016-04-23 09:05:28.873259'),(53,'home','0017_auto_20160423_0106','2016-04-23 09:05:29.526514'),(54,'home','0021_merge','2016-04-23 09:05:29.545718'),(55,'localizaciones','0002_auto_20160326_2300','2016-04-23 09:05:29.815745'),(56,'localizaciones','0003_auto_20160423_0903','2016-04-23 09:05:30.446501'),(57,'sessions','0001_initial','2016-04-23 09:05:30.959030');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('k2gmicu8wpxb9a88g1wmy7jhy42rleko','OGE4YmZjZTc2MjVjMWU0NjE5YmI5ZTI4ZWEyMmJjNTAyZmRhYzg4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImUwOWQ4Y2FhOTM3NTk3NzFjYWExMGVjMDQ0NDFkYmU3OTRkMGE4OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2016-05-07 09:10:15.512882');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_tipo_usuario`
--

DROP TABLE IF EXISTS `home_tipo_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_tipo_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_tipo_usuario`
--

LOCK TABLES `home_tipo_usuario` WRITE;
/*!40000 ALTER TABLE `home_tipo_usuario` DISABLE KEYS */;
INSERT INTO `home_tipo_usuario` VALUES (1,'Invitado');
/*!40000 ALTER TABLE `home_tipo_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_usuario`
--

DROP TABLE IF EXISTS `home_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(55) NOT NULL,
  `apellidos` varchar(55) NOT NULL,
  `institucion` varchar(30) NOT NULL,
  `ultima_conexion` datetime(6) NOT NULL,
  `nombre_usuario` varchar(20) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `Tipo_Usuario_id_id` int(11) NOT NULL,
  `last_login` datetime(6),
  `password` varchar(128) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_usuario_correo_0a61773a_uniq` (`correo`),
  UNIQUE KEY `home_usuario_nombre_usuario_50bfbd67_uniq` (`nombre_usuario`),
  KEY `home_usuario_Tipo_Usuario_id_id_261b13f1_uniq` (`Tipo_Usuario_id_id`),
  CONSTRAINT `home_usuario_Tipo_Usuario_id_id_261b13f1_fk_home_tipo_usuario_id` FOREIGN KEY (`Tipo_Usuario_id_id`) REFERENCES `home_tipo_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_usuario`
--

LOCK TABLES `home_usuario` WRITE;
/*!40000 ALTER TABLE `home_usuario` DISABLE KEYS */;
INSERT INTO `home_usuario` VALUES (2,'Root','Ruter','','2016-04-23 09:09:50.206851','Root','mail@mail.com',1,'2016-04-23 09:10:15.466520','pbkdf2_sha256$24000$yUU7J7hXsvrn$pfuxSNHQoCwkKf3kUx/ADcNAPlmr+iMU3bR/S8fijyQ=',1,1);
/*!40000 ALTER TABLE `home_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localizaciones_departamento`
--

DROP TABLE IF EXISTS `localizaciones_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `localizaciones_departamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `departamento` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localizaciones_departamento`
--

LOCK TABLES `localizaciones_departamento` WRITE;
/*!40000 ALTER TABLE `localizaciones_departamento` DISABLE KEYS */;
INSERT INTO `localizaciones_departamento` VALUES (1,'Quetzaltenango');
/*!40000 ALTER TABLE `localizaciones_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localizaciones_municipio`
--

DROP TABLE IF EXISTS `localizaciones_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `localizaciones_municipio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio` varchar(45) NOT NULL,
  `Departamento_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lo_Departamento_id_id_65e3ecc5_fk_localizaciones_departamento_id` (`Departamento_id_id`),
  CONSTRAINT `lo_Departamento_id_id_65e3ecc5_fk_localizaciones_departamento_id` FOREIGN KEY (`Departamento_id_id`) REFERENCES `localizaciones_departamento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localizaciones_municipio`
--

LOCK TABLES `localizaciones_municipio` WRITE;
/*!40000 ALTER TABLE `localizaciones_municipio` DISABLE KEYS */;
INSERT INTO `localizaciones_municipio` VALUES (1,'Quetzaltenango',1);
/*!40000 ALTER TABLE `localizaciones_municipio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-23  3:17:12
