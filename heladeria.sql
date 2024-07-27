-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: heladeria
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `heladeria`
--

DROP TABLE IF EXISTS `heladeria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heladeria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `vender` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heladeria`
--

LOCK TABLES `heladeria` WRITE;
/*!40000 ALTER TABLE `heladeria` DISABLE KEYS */;
INSERT INTO `heladeria` VALUES (1,'Heladería El Sabor','Cerveza');
/*!40000 ALTER TABLE `heladeria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `precio` float NOT NULL,
  `calorias` int NOT NULL,
  `inventario` int NOT NULL,
  `es_vegetariano` tinyint(1) NOT NULL,
  `tipo_id` int NOT NULL,
  `sabor` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tipo_id` (`tipo_id`),
  CONSTRAINT `ingredientes_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_ingrediente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Chocolate',200,2000,10,1,1,'Dulce'),(2,'Menta',1000,200,12,0,2,'Mentolado'),(3,'Fresa',500,200,15,1,2,'Frutal');
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `precio_publico` float NOT NULL,
  `tipo_vaso` varchar(50) DEFAULT NULL,
  `volumen` float DEFAULT NULL,
  `heladeria_id` int NOT NULL,
  `tipo_producto` enum('Copa','Malteada') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `heladeria_id` (`heladeria_id`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`heladeria_id`) REFERENCES `heladeria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Copa de Chocolate',1500,'Copa de Plástico',NULL,1,'Copa'),(2,'Malteada de Vainilla',2000,NULL,500,1,'Malteada'),(3,'Helado de Fresa',1200,'Cono',NULL,1,'Copa'),(4,'Malteda chocoespacial',11000,NULL,500,1,'Malteada');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_ingredientes`
--

DROP TABLE IF EXISTS `producto_ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_ingredientes` (
  `producto_id` int NOT NULL,
  `ingrediente_id` int NOT NULL,
  PRIMARY KEY (`producto_id`,`ingrediente_id`),
  KEY `ingrediente_id` (`ingrediente_id`),
  CONSTRAINT `producto_ingredientes_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `producto_ingredientes_ibfk_2` FOREIGN KEY (`ingrediente_id`) REFERENCES `ingredientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_ingredientes`
--

LOCK TABLES `producto_ingredientes` WRITE;
/*!40000 ALTER TABLE `producto_ingredientes` DISABLE KEYS */;
INSERT INTO `producto_ingredientes` VALUES (1,1),(2,2),(1,3),(2,4);
/*!40000 ALTER TABLE `producto_ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_ingrediente`
--

DROP TABLE IF EXISTS `tipo_ingrediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_ingrediente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_ingrediente`
--

LOCK TABLES `tipo_ingrediente` WRITE;
/*!40000 ALTER TABLE `tipo_ingrediente` DISABLE KEYS */;
INSERT INTO `tipo_ingrediente` VALUES (1,'Base'),(2,'Complemento');
/*!40000 ALTER TABLE `tipo_ingrediente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-21 19:20:43
