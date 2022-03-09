/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - attack_dos
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`attack_dos` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `attack_dos`;

/*Table structure for table `checkingtest` */

DROP TABLE IF EXISTS `checkingtest`;

CREATE TABLE `checkingtest` (
  `nameofattack` varchar(1000) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `checkingtest` */

insert  into `checkingtest`(`nameofattack`) values ('DOS');

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `user_id` varchar(250) default NULL,
  `name` varchar(250) default NULL,
  `address` varchar(250) default NULL,
  `email` varchar(250) default NULL,
  `mobile` varchar(250) default NULL,
  `password` varchar(250) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`user_id`,`name`,`address`,`email`,`mobile`,`password`) values (NULL,'asd','asd','asd@gmail.com','7894561230','asd');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
