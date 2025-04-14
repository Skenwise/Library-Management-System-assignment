-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: lms
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.24.04.1

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `isbn` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `year_published` int NOT NULL,
  `editor` varchar(100) NOT NULL,
  `genre` varchar(100) NOT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `language` varchar(100) DEFAULT NULL,
  `available` tinyint(1) DEFAULT '1',
  `author` varchar(100) DEFAULT NULL,
  `borrower_id` int DEFAULT NULL,
  PRIMARY KEY (`isbn`),
  KEY `fk_borrower` (`borrower_id`),
  CONSTRAINT `fk_borrower` FOREIGN KEY (`borrower_id`) REFERENCES `users` (`user_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (141439845,'Dracula',1897,'Nina Auerbach','Gothic Horror','Penguin Classic','English',1,'Bram Stoker',NULL),(142437220,'Inferno',1320,'Jean Hollander','Epic Poetry','Penguin Classic','English',1,'Dante Alighieri',NULL),(316769487,'The catcher in the Rye',1951,'E.L.Doctorow','Coming-of-Age Fiction','Little, Brown and Company','English',1,'J.D.Salinger',67),(451524934,'1984',1949,'Michael Turner','Dystopian Fiction','Signet Classic','English',1,'George Orwell',NULL),(486284735,'Pride and Prejudice',1813,'Vivien Jones','Romance','Dover Publication','English',1,'Jane Austen',NULL),(486415872,'Crime and Punishment',1866,'David McDuff','Psychologicol Fiction','Dover Publication','English',1,'Fyodor Dostoevsky',NULL),(486795748,'Wealth',1889,'James D. Wilson','Finance & Economics','Dover Publications','English',1,'Andrew Carnegie',NULL),(618260307,'The Hobbit',1937,'Douglas A. Anderson','Fantasy','Houghton Mifflin Harcourt','English',1,'J.R.R Tolkien',NULL),(743273567,'The Great Gatsby',1925,'Matthew J.Bruccoli','Classic Litterature','Scribner','English',1,'F. Scott Fitzgerald',NULL),(1503280780,'Moby-Dick',1851,'Harold Bloom','Adventure Fiction','CreateSpace Independent Publishing','English',1,'Herman Melville',NULL),(1590302257,'The Art of War',1851,'Thomas Cleargy','Military Strategy','Shambhala Publications','English',1,'Sun Tzu',NULL);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `book_code` varchar(20) NOT NULL,
  `borrower_id` int NOT NULL,
  `borrowed_book` varchar(255) NOT NULL,
  `borrower_name` varchar(100) NOT NULL,
  `transaction_date` datetime NOT NULL,
  `return_date` datetime DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1,'316769487',67,'The catcher in the Rye','Sage Kona','2025-04-13 17:16:39','2025-04-13 17:26:21');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `username` varchar(100) NOT NULL,
  `profession` varchar(100) DEFAULT NULL,
  `age` int NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `unique_constraint` (`user_id`,`username`),
  UNIQUE KEY `unique_user` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (4,'KP','Student',22,'KP2025@gmail.com'),(36,'Miriam','Student',21,'Miriam2025@gmail.com'),(61,'Hassan','Student',22,'hassan2023@gmail.com'),(67,'Sage Kona','Student',20,'skndream2023@gmail.com'),(93,'Skylar ','Business',21,'skymubanga12@gmail.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-14 11:15:17
