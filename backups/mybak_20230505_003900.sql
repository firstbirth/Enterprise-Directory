-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `CityCode_ID` int NOT NULL AUTO_INCREMENT,
  `City_Name` varchar(128) NOT NULL,
  PRIMARY KEY (`CityCode_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,'Москва'),(2,'Петропавловск'),(3,'Актау'),(4,'Алматы'),(5,'Актобе'),(6,'Кокшетау');
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `Contact_ID` int NOT NULL AUTO_INCREMENT,
  `Email` varchar(128) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Inst_Username` varchar(30) NOT NULL,
  `WebSite` varchar(128) NOT NULL,
  PRIMARY KEY (`Contact_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,'newemail@gmail.com','87774043256','@newuser','https://abs.com'),(2,'sevkazenergo@mail.ru',' +77152500666','sevkazenergo','https://www.sevkazenergo.kz/ru/home.html'),(3,'kbm@kbm.kz','+77292473222','Karazhanbasmunai','http://kbm.kz/ru'),(4,'auz@mail.ru','+77272223300','auz.kz','http://auz.kz/'),(5,'office@arbz.kz','+77132744802','arbz.kz','http://arbz.kz'),(6,'ls-kokshetau@mail.ru','+77015033848','ls-kokshetau','https://ls.com.kz/pages/o-kompanii.html');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enterprises`
--

DROP TABLE IF EXISTS `enterprises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enterprises` (
  `Enterprise_ID` int NOT NULL AUTO_INCREMENT,
  `Enterprise_Name` varchar(128) NOT NULL,
  `Enterprise_City` int NOT NULL,
  `Industry_ID` int NOT NULL,
  `Address` varchar(256) NOT NULL,
  `Employee_Count` int NOT NULL,
  `Contact_ID` int NOT NULL,
  `Contact_Info_Manager` int NOT NULL,
  `Service_ID` int NOT NULL,
  `Description` text NOT NULL,
  PRIMARY KEY (`Enterprise_ID`),
  KEY `Enterprise_City` (`Enterprise_City`),
  KEY `Industry_ID` (`Industry_ID`),
  KEY `Contact_ID` (`Contact_ID`),
  KEY `Contact_Info_Manager` (`Contact_Info_Manager`),
  KEY `Service_ID` (`Service_ID`),
  CONSTRAINT `enterprises_ibfk_1` FOREIGN KEY (`Enterprise_City`) REFERENCES `city` (`CityCode_ID`),
  CONSTRAINT `enterprises_ibfk_2` FOREIGN KEY (`Industry_ID`) REFERENCES `industry` (`Industry_ID`),
  CONSTRAINT `enterprises_ibfk_3` FOREIGN KEY (`Contact_ID`) REFERENCES `contacts` (`Contact_ID`),
  CONSTRAINT `enterprises_ibfk_4` FOREIGN KEY (`Contact_Info_Manager`) REFERENCES `managers` (`Manager_ID`),
  CONSTRAINT `enterprises_ibfk_5` FOREIGN KEY (`Service_ID`) REFERENCES `services` (`Service_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enterprises`
--

LOCK TABLES `enterprises` WRITE;
/*!40000 ALTER TABLE `enterprises` DISABLE KEYS */;
INSERT INTO `enterprises` VALUES (1,'MyCompany',1,1,'asdasd',21,1,1,1,'test');
/*!40000 ALTER TABLE `enterprises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `industry`
--

DROP TABLE IF EXISTS `industry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `industry` (
  `Industry_ID` int NOT NULL AUTO_INCREMENT,
  `Industry_Name` varchar(128) NOT NULL,
  PRIMARY KEY (`Industry_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `industry`
--

LOCK TABLES `industry` WRITE;
/*!40000 ALTER TABLE `industry` DISABLE KEYS */;
INSERT INTO `industry` VALUES (1,'NewIndusty'),(2,'Новая деятельность'),(3,'Коммунальное хозяйство и электроэнергетика'),(4,'Добыча угля'),(5,' Ювелирная промышленность'),(6,'Металлургия'),(7,'Лесная промышленность');
/*!40000 ALTER TABLE `industry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `managers`
--

DROP TABLE IF EXISTS `managers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `managers` (
  `Manager_ID` int NOT NULL AUTO_INCREMENT,
  `Manager_Name` varchar(128) NOT NULL,
  `MgrPhone_Number` varchar(20) NOT NULL,
  `Start_Date` date DEFAULT NULL,
  PRIMARY KEY (`Manager_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `managers`
--

LOCK TABLES `managers` WRITE;
/*!40000 ALTER TABLE `managers` DISABLE KEYS */;
INSERT INTO `managers` VALUES (1,'asd','asdasdasd','2020-12-01'),(2,'Филипов С.А','+77711745587','2012-03-20'),(3,'Гумиров П.С','+77054584123','2001-05-20'),(4,'Садвакасов Д.А','+77088699421','2015-08-20'),(5,'Печенькин Г.В.','+77059453126','2031-02-20'),(6,'Чучман Л.Я.','+77080320568','2025-08-20');
/*!40000 ALTER TABLE `managers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_table`
--

DROP TABLE IF EXISTS `new_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_table` (
  `FirstColumb` int NOT NULL AUTO_INCREMENT,
  `AdditionalSettings` int DEFAULT NULL,
  PRIMARY KEY (`FirstColumb`)
) ENGINE=InnoDB AUTO_INCREMENT=223 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_table`
--

LOCK TABLES `new_table` WRITE;
/*!40000 ALTER TABLE `new_table` DISABLE KEYS */;
INSERT INTO `new_table` VALUES (1,2),(3,4),(5,6),(222,33333);
/*!40000 ALTER TABLE `new_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `Service_ID` int NOT NULL AUTO_INCREMENT,
  `Service_Name` varchar(128) NOT NULL,
  PRIMARY KEY (`Service_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (1,'TestService'),(2,'Передача теплоэнергии потребителям'),(3,'Добыча нефти и газа'),(4,'Производство изделий, посуды из серебра'),(5,'Производство проката из стали, чугуна и сплавов'),(6,'Переработка макулатуры, Сортировка и переработка твердых отходов');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05  0:39:00
