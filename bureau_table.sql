-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Oct 19, 2020 at 10:27 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `a3_kit`
--

-- --------------------------------------------------------

--
-- Table structure for table `bureau`
--

DROP TABLE IF EXISTS `bureau`;
CREATE TABLE IF NOT EXISTS `bureau` (
  `index` bigint(20) DEFAULT NULL,
  `Loan_Selection` text,
  `Customer_Id` bigint(20) DEFAULT NULL,
  `Date_reported` datetime DEFAULT NULL,
  `Loan_type` text,
  `Loan_status` text,
  `Disbursed_amount` bigint(20) DEFAULT NULL,
  `Disbursed_amount_edited` int(11) DEFAULT NULL,
  `Disbursed_amount_user_edited` int(11) NOT NULL DEFAULT '0',
  `Disbursal_date` datetime DEFAULT NULL,
  `Tenure` double DEFAULT NULL,
  `Tenure_new` double DEFAULT NULL,
  `Tenure_edited` int(11) DEFAULT NULL,
  `Tenure_user_edited` int(11) NOT NULL DEFAULT '0',
  `ROI` double DEFAULT NULL,
  `ROI_new` double DEFAULT NULL,
  `ROI_edited` int(11) DEFAULT NULL,
  `ROI_user_edited` int(11) NOT NULL DEFAULT '0',
  `EMI` bigint(20) DEFAULT NULL,
  `EMI_new` double DEFAULT NULL,
  `EMI_user_edited` int(11) NOT NULL DEFAULT '0',
  `Current Balance` bigint(20) DEFAULT NULL,
  `DPD` double DEFAULT NULL,
  `DPD_month_new` text,
  `Overdue amount` double DEFAULT NULL,
  `Source` text,
  `extra_column` text,
  KEY `ix_bureau_index` (`index`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bureau`
--

INSERT INTO `bureau` (`index`, `Loan_Selection`, `Customer_Id`, `Date_reported`, `Loan_type`, `Loan_status`, `Disbursed_amount`, `Disbursed_amount_edited`, `Disbursed_amount_user_edited`, `Disbursal_date`, `Tenure`, `Tenure_new`, `Tenure_edited`, `Tenure_user_edited`, `ROI`, `ROI_new`, `ROI_edited`, `ROI_user_edited`, `EMI`, `EMI_new`, `EMI_user_edited`, `Current Balance`, `DPD`, `DPD_month_new`, `Overdue amount`, `Source`, `extra_column`) VALUES
(0, 'Yes', 945, '2017-10-31 00:00:00', 'Other', 'Active', 53851, NULL, 0, '2017-03-16 00:00:00', 6, 6, NULL, 0, 1, 1, NULL, 0, 22, 22, 0, 0, 3, 'Jun 2017', 0, 'crif', NULL),
(1, 'Yes', 945, '2017-12-31 00:00:00', 'Other', 'Active', 700000, NULL, 0, '2013-09-06 00:00:00', NULL, 60, NULL, 0, NULL, 13.81837738640629, NULL, 0, 0, 16221.93874583396, 0, 290161, NULL, NULL, 0, 'crif', NULL),
(2, 'Yes', 945, '2012-09-30 00:00:00', 'Two-wheeler Loan', 'Closed', 46117, NULL, 0, '2008-07-10 00:00:00', NULL, 24, NULL, 0, NULL, 27.45510425141249, NULL, 0, 0, 2518.505699646031, 0, 0, 620, 'Aug 2012', 0, 'equifax', NULL),
(3, 'Yes', 945, '2013-07-31 00:00:00', 'Other', 'Closed', 125000, NULL, 0, '2006-06-19 00:00:00', NULL, 12, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 11447.47940768336, 0, 0, NULL, NULL, 0, 'equifax', NULL),
(4, 'Yes', 945, '2017-12-31 00:00:00', 'Other', 'Active', 301731, NULL, 0, '2016-10-19 00:00:00', 36, 36, NULL, 0, 9.45, 9.45, NULL, 0, 0, 9658.28321399734, 0, 151053, 30, 'Oct 2017', 0, 'experian', NULL),
(5, 'Yes', 947, '2017-12-31 00:00:00', 'Other', 'Closed', 59907, NULL, 0, '2017-10-12 00:00:00', 9, 9, NULL, 0, 1, 1, NULL, 0, 26, 26, 0, 60000, 100, 'Dec 2017', 1717, 'cibil', NULL),
(6, 'Yes', 945, '2015-12-02 00:00:00', 'Credit Card', 'Closed', 15000, NULL, 0, '2006-08-04 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'Dec 2015', 0, 'cibil', NULL),
(7, 'Yes', 945, '2017-11-30 00:00:00', 'Credit Card', 'Closed', 18000, NULL, 0, '2006-05-27 00:00:00', NULL, NULL, NULL, 0, 42, 42, NULL, 0, 0, NULL, 0, 30237, 180, 'Nov 2017', 30237, 'cibil', NULL),
(8, 'Yes', 945, '2017-12-31 00:00:00', 'Other', 'Closed', 59907, NULL, 0, '2017-10-12 00:00:00', 9, 9, NULL, 0, 1, 1, NULL, 0, 26, 26, 0, 60000, 100, 'Dec 2017', 1717, 'cibil', NULL),
(9, 'Yes', 945, '2017-12-31 00:00:00', 'Other', 'Active', 56912, NULL, 0, '2017-10-14 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 29, 29, 0, 57000, NULL, NULL, 0, 'cibil', NULL),
(10, 'Yes', 945, '2017-10-31 00:00:00', 'Other', 'Closed', 59851, NULL, 0, '2017-03-16 00:00:00', 6, 6, NULL, 0, 1, 1, NULL, 0, 22, 22, 0, 0, 3, 'Jun 2017', 0, 'cibil', NULL),
(11, 'Yes', 945, '2017-12-31 00:00:00', 'Other', 'Active', 201731, NULL, 0, '2016-10-19 00:00:00', 36, 36, NULL, 0, 9.45, 9.45, NULL, 0, 0, 6457.325004864921, 0, 151053, 30, 'Oct 2017', 0, 'cibil', NULL),
(12, 'Yes', 945, '2016-06-30 00:00:00', 'Other', 'Closed', 109801, NULL, 0, '2016-04-08 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 57, 57, 0, 0, NULL, NULL, 0, 'cibil', NULL),
(13, 'Yes', 945, '2017-12-31 00:00:00', 'Other', 'Active', 600000, NULL, 0, '2013-09-06 00:00:00', NULL, 60, NULL, 0, NULL, 13.81837738640629, NULL, 0, 0, 13904.51892500053, 0, 290161, NULL, NULL, 0, 'cibil', NULL),
(14, 'Yes', 945, '2012-09-30 00:00:00', 'Two-wheeler Loan', 'Closed', 36117, NULL, 0, '2008-07-10 00:00:00', NULL, 18, NULL, 0, NULL, 27.45510425141249, NULL, 0, 0, 2470.494066138641, 0, 0, 620, 'Aug 2012', 0, 'cibil', NULL),
(15, 'Yes', 945, '2013-07-31 00:00:00', 'Other', 'Closed', 75000, NULL, 0, '2006-06-19 00:00:00', NULL, 12, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 6868.487644610015, 0, 0, NULL, NULL, 0, 'cibil', NULL),
(16, 'Yes', 945, '2010-05-30 00:00:00', 'Other', 'Closed', 398000, NULL, 0, '2006-03-08 00:00:00', NULL, 60, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 10061.06037189663, 0, 0, NULL, NULL, 0, 'cibil', NULL),
(17, 'Yes', 945, '2010-05-30 00:00:00', 'Other', 'Closed', 33500, NULL, 0, '2006-01-31 00:00:00', NULL, 4, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 8687.673100673434, 0, 0, NULL, NULL, 0, 'cibil', NULL),
(18, 'Yes', 945, '2017-05-31 00:00:00', 'Other', 'Closed', 89851, NULL, 0, '2016-01-21 00:00:00', 11, 11, NULL, 0, NULL, 13.38906857440143, NULL, 0, 44, 44, 0, 0, NULL, NULL, 0, 'cibil', NULL),
(19, 'Yes', 946, '2017-12-31 00:00:00', 'Other', 'Active', 899060, NULL, 0, '2013-05-15 00:00:00', 300, 300, NULL, 0, 11.25, 11.25, NULL, 0, 8994, 8994, 0, 863619, 30, 'Jan 2017', 0, 'cibil', NULL),
(20, 'Yes', 947, '2015-12-02 00:00:00', 'Credit Card', 'Closed', 15000, NULL, 0, '2008-08-04 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'Dec 2015', 0, 'cibil', NULL),
(21, 'Yes', 947, '2017-11-30 00:00:00', 'Credit Card', 'Closed', 18000, NULL, 0, '2009-05-27 00:00:00', NULL, NULL, NULL, 0, 42, 42, NULL, 0, 0, NULL, 0, 30237, 180, 'Nov 2017', 30237, 'cibil', NULL),
(22, 'Yes', 947, '2017-12-31 00:00:00', 'Other', 'Active', 56912, NULL, 0, '2017-10-14 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 29, 29, 0, 57000, NULL, NULL, 0, 'cibil', NULL),
(23, 'Yes', 945, '2014-02-28 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2007-09-24 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'May 2012', 0, 'cibil', 'emi and disbursed amount both are zero'),
(24, 'Yes', 945, '2017-04-10 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2006-05-10 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, NULL, NULL, 0, 'cibil', 'emi and disbursed amount both are zero'),
(25, 'Yes', 945, '2014-02-28 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2007-09-24 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'May 2012', 0, 'crif', 'emi and disbursed amount both are zero'),
(26, 'Yes', 945, '2017-04-10 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2006-05-10 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, NULL, NULL, 0, 'crif', 'emi and disbursed amount both are zero'),
(27, 'Yes', 945, '2014-02-28 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2007-09-24 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'May 2012', 0, 'equifax', 'emi and disbursed amount both are zero'),
(28, 'Yes', 945, '2017-04-10 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2006-05-10 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, NULL, NULL, 0, 'equifax', 'emi and disbursed amount both are zero'),
(29, 'Yes', 945, '2014-02-28 00:00:00', 'Credit Card', 'Closed', 0, NULL, 0, '2007-09-24 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'May 2012', 0, 'experian', 'emi and disbursed amount both are zero'),
(30, 'No', 945, '2015-12-02 00:00:00', 'Credit Card', 'Closed', 15000, NULL, 0, '2006-08-04 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'Dec 2015', 0, 'crif', NULL),
(31, 'No', 945, '2017-11-30 00:00:00', 'Credit Card', 'Closed', 18000, NULL, 0, '2006-05-27 00:00:00', NULL, NULL, NULL, 0, 42, 42, NULL, 0, 0, NULL, 0, 30237, 180, 'Nov 2017', 30237, 'crif', NULL),
(32, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Closed', 59907, NULL, 0, '2017-10-12 00:00:00', 9, 9, NULL, 0, 1, 1, NULL, 0, 26, 26, 0, 60000, 100, 'Dec 2017', 1717, 'crif', NULL),
(33, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 56912, NULL, 0, '2017-10-14 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 29, 29, 0, 57000, NULL, NULL, 0, 'crif', NULL),
(34, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 201731, NULL, 0, '2016-10-19 00:00:00', 36, 36, NULL, 0, 9.45, 9.45, NULL, 0, 0, 6457.325004864921, 0, 151053, 30, 'Oct 2017', 0, 'crif', NULL),
(35, 'No', 945, '2016-06-30 00:00:00', 'Other', 'Closed', 109801, NULL, 0, '2016-04-08 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 57, 57, 0, 0, NULL, NULL, 0, 'crif', NULL),
(36, 'No', 945, '2012-09-30 00:00:00', 'Two-wheeler Loan', 'Closed', 36117, NULL, 0, '2008-07-10 00:00:00', NULL, 18, NULL, 0, NULL, 27.45510425141249, NULL, 0, 0, 2470.494066138641, 0, 0, 620, 'Aug 2012', 0, 'crif', NULL),
(37, 'No', 945, '2013-07-31 00:00:00', 'Other', 'Closed', 75000, NULL, 0, '2006-06-19 00:00:00', NULL, 12, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 6868.487644610015, 0, 0, NULL, NULL, 0, 'crif', NULL),
(38, 'No', 945, '2010-05-30 00:00:00', 'Other', 'Closed', 398000, NULL, 0, '2006-03-08 00:00:00', NULL, 60, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 10061.06037189663, 0, 0, NULL, NULL, 0, 'crif', NULL),
(39, 'No', 945, '2010-05-30 00:00:00', 'Other', 'Closed', 33500, NULL, 0, '2006-01-31 00:00:00', NULL, 4, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 8687.673100673434, 0, 0, NULL, NULL, 0, 'crif', NULL),
(40, 'No', 945, '2017-05-31 00:00:00', 'Other', 'Closed', 89851, NULL, 0, '2016-01-21 00:00:00', 11, 11, NULL, 0, NULL, 13.38906857440143, NULL, 0, 44, 44, 0, 0, NULL, NULL, 0, 'crif', NULL),
(41, 'No', 945, '2015-12-02 00:00:00', 'Credit Card', 'Closed', 15000, NULL, 0, '2006-08-04 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'Dec 2015', 0, 'equifax', NULL),
(42, 'No', 945, '2017-11-30 00:00:00', 'Credit Card', 'Closed', 18000, NULL, 0, '2006-05-27 00:00:00', NULL, NULL, NULL, 0, 42, 42, NULL, 0, 0, NULL, 0, 30237, 180, 'Nov 2017', 30237, 'equifax', NULL),
(43, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Closed', 59907, NULL, 0, '2017-10-12 00:00:00', 9, 9, NULL, 0, 1, 1, NULL, 0, 26, 26, 0, 60000, 100, 'Dec 2017', 1717, 'equifax', NULL),
(44, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 56912, NULL, 0, '2017-10-14 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 29, 29, 0, 57000, NULL, NULL, 0, 'equifax', NULL),
(45, 'No', 945, '2017-10-31 00:00:00', 'Other', 'Closed', 59851, NULL, 0, '2017-03-16 00:00:00', 6, 6, NULL, 0, 1, 1, NULL, 0, 22, 22, 0, 0, 3, 'Jun 2017', 0, 'equifax', NULL),
(46, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 201731, NULL, 0, '2016-10-19 00:00:00', 36, 36, NULL, 0, 9.45, 9.45, NULL, 0, 0, 6457.325004864921, 0, 151053, 30, 'Oct 2017', 0, 'equifax', NULL),
(47, 'No', 945, '2016-06-30 00:00:00', 'Other', 'Closed', 109801, NULL, 0, '2016-04-08 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 57, 57, 0, 0, NULL, NULL, 0, 'equifax', NULL),
(48, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 600000, NULL, 0, '2013-09-06 00:00:00', NULL, 60, NULL, 0, NULL, 13.81837738640629, NULL, 0, 0, 13904.51892500053, 0, 290161, NULL, NULL, 0, 'equifax', NULL),
(49, 'No', 945, '2010-05-30 00:00:00', 'Other', 'Closed', 398000, NULL, 0, '2006-03-08 00:00:00', NULL, 60, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 10061.06037189663, 0, 0, NULL, NULL, 0, 'equifax', NULL),
(50, 'No', 945, '2010-05-30 00:00:00', 'Other', 'Closed', 33500, NULL, 0, '2006-01-31 00:00:00', NULL, 4, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 8687.673100673434, 0, 0, NULL, NULL, 0, 'equifax', NULL),
(51, 'No', 945, '2017-05-31 00:00:00', 'Other', 'Closed', 89851, NULL, 0, '2016-01-21 00:00:00', 11, 11, NULL, 0, NULL, 13.38906857440143, NULL, 0, 44, 44, 0, 0, NULL, NULL, 0, 'equifax', NULL),
(52, 'No', 946, '2017-12-31 00:00:00', 'Other', 'Active', 899060, NULL, 0, '2013-05-15 00:00:00', 300, 300, NULL, 0, 11.25, 11.25, NULL, 0, 8994, 8994, 0, 863619, 30, 'Jan 2017', 0, 'equifax', NULL),
(53, 'No', 945, '2015-12-02 00:00:00', 'Credit Card', 'Closed', 15000, NULL, 0, '2006-08-04 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'Dec 2015', 0, 'experian', NULL),
(54, 'No', 945, '2017-11-30 00:00:00', 'Credit Card', 'Closed', 18000, NULL, 0, '2006-05-27 00:00:00', NULL, NULL, NULL, 0, 42, 42, NULL, 0, 0, NULL, 0, 30237, 80, 'Nov 2017', 30237, 'experian', NULL),
(55, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Closed', 59907, NULL, 0, '2017-10-12 00:00:00', 9, 9, NULL, 0, 1, 1, NULL, 0, 26, 26, 0, 60000, 100, 'Dec 2017', 1717, 'experian', NULL),
(56, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 56912, NULL, 0, '2017-10-14 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 29, 29, 0, 57000, NULL, NULL, 0, 'experian', NULL),
(57, 'No', 945, '2017-10-31 00:00:00', 'Other', 'Active', 59851, NULL, 0, '2017-03-16 00:00:00', 6, 6, NULL, 0, 1, 1, NULL, 0, 22, 22, 0, 0, 3, 'Jun 2017', 0, 'experian', NULL),
(58, 'No', 945, '2016-06-30 00:00:00', 'Other', 'Closed', 109801, NULL, 0, '2016-04-08 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 57, 57, 0, 0, NULL, NULL, 0, 'experian', NULL),
(59, 'No', 945, '2017-12-31 00:00:00', 'Other', 'Active', 600000, NULL, 0, '2013-09-06 00:00:00', NULL, 60, NULL, 0, NULL, 13.81837738640629, NULL, 0, 0, 13904.51892500053, 0, 290161, NULL, NULL, 0, 'experian', NULL),
(60, 'No', 945, '2012-09-30 00:00:00', 'Two-wheeler Loan', 'Closed', 36117, NULL, 0, '2008-07-10 00:00:00', NULL, 18, NULL, 0, NULL, 27.45510425141249, NULL, 0, 0, 2470.494066138641, 0, 0, 620, 'Aug 2012', 0, 'experian', NULL),
(61, 'No', 945, '2013-07-31 00:00:00', 'Other', 'Closed', 75000, NULL, 0, '2006-06-19 00:00:00', NULL, 12, NULL, 0, NULL, 17.7894838974512, NULL, 0, 0, 6868.487644610015, 0, 0, NULL, NULL, 0, 'experian', NULL),
(62, 'No', 946, '2017-12-31 00:00:00', 'Other', 'Active', 899060, NULL, 0, '2013-05-15 00:00:00', 300, 300, NULL, 0, 11.25, 11.25, NULL, 0, 8994, 8994, 0, 863619, 30, 'Jan 2017', NULL, 'experian', NULL),
(63, 'No', 947, '2015-12-02 00:00:00', 'Credit Card', 'Closed', 15000, NULL, 0, '2008-08-04 00:00:00', NULL, NULL, NULL, 0, NULL, NULL, NULL, 0, 0, NULL, 0, 0, 900, 'Dec 2015', 0, 'experian', NULL),
(64, 'No', 947, '2017-11-30 00:00:00', 'Credit Card', 'Closed', 18000, NULL, 0, '2009-05-27 00:00:00', NULL, NULL, NULL, 0, 42, 42, NULL, 0, 0, NULL, 0, 30237, 180, 'Nov 2017', 30237, 'experian', NULL),
(65, 'No', 947, '2017-12-31 00:00:00', 'Other', 'Closed', 59907, NULL, 0, '2017-10-12 00:00:00', 9, 9, NULL, 0, 1, 1, NULL, 0, 26, 26, 0, 60000, 100, 'Dec 2017', 1717, 'experian', NULL),
(66, 'No', 947, '2017-12-31 00:00:00', 'Other', 'Active', 56912, NULL, 0, '2017-10-14 00:00:00', 11, 11, NULL, 0, 2, 2, NULL, 0, 29, 29, 0, 57000, NULL, NULL, 0, 'experian', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
