-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 27, 2022 at 07:41 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chikun`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `id` int(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`id`, `username`, `password`) VALUES
(1, 'chikun', '123');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `in_time` time(4) NOT NULL,
  `out_time` time(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `name`, `date`, `in_time`, `out_time`) VALUES
(1, 'Rohan', '2022-05-13', '15:37:00.0000', '12:12:00.0000'),
(2, 'Rohan', '2022-05-13', '15:37:00.0000', '12:15:00.0000'),
(3, 'chikun', '2022-06-07', '09:52:00.0000', '12:15:00.0000'),
(4, 'chikun', '2022-06-15', '11:58:00.0000', '00:00:00.0000'),
(5, 'binayak', '2022-06-18', '11:38:00.0000', '12:12:00.0000'),
(6, '', '2022-06-20', '12:36:00.0000', '00:00:00.0000'),
(7, 'chikun', '2022-06-22', '10:27:00.0000', '10:27:00.0000');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(20) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `cmail` varchar(100) NOT NULL,
  `cwsite` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `cname`, `cmail`, `cwsite`, `city`, `country`) VALUES
(3, 'wipro', 'wipro@mail.com', 'wipro.in', 'bbsr', 'India'),
(4, 'mind trre', 'mindtree@mail.com', 'mindtree.in', 'bbsr', 'India'),
(5, 'tcs', 'tcs@mail.com', 'tcs.in', 'bbsr', 'India');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `id` int(100) NOT NULL,
  `dname` varchar(100) NOT NULL,
  `dhead` varchar(100) NOT NULL,
  `location` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`id`, `dname`, `dhead`, `location`) VALUES
(1, 'cse', 'satya', 'bam'),
(2, 'eee', 'srikant', 'bam'),
(3, 'mech', 'prabhu', 'bam'),
(4, 'cse', 'srikant', 'kolkata');

-- --------------------------------------------------------

--
-- Table structure for table `designation`
--

CREATE TABLE `designation` (
  `id` int(100) NOT NULL,
  `desname` varchar(100) NOT NULL,
  `depname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `designation`
--

INSERT INTO `designation` (`id`, `desname`, `depname`) VALUES
(1, 'developer', 'computer'),
(2, 'tester1', 'medical');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emp_code` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `role` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `bg` varchar(150) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `files` varchar(100) NOT NULL,
  `date_of_joining` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `emp_code`, `department`, `designation`, `role`, `gender`, `dob`, `bg`, `email`, `phone`, `files`, `date_of_joining`) VALUES
(11, 'Rohan', '234', 'cse', 'prof', 'Employee', 'Male', '', 'A-', 'wa@gmail.com', '99964446', '', ''),
(12, 'RKP3', '3237', 'mech', 'hod', 'Employee', 'Male', '', 'B+', 'ashishtripathy58@gmail.com', '549111698189', '', ''),
(16, 'binayak', '225', 'cse', 'prof', 'Employee', 'Male', '2022-06-13', 'B-', 'binu@mail.com', '1230456', '3.png', '2022-06-24'),
(17, 'deepak', '', 'Select Department', 'Select Designation', 'Select Role', 'Select Gender', '', 'Select Blood Group', '', '', '3.png', '');

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `id` int(50) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `lhead` varchar(100) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`id`, `lname`, `lhead`, `cname`, `city`, `country`) VALUES
(1, 'patia', 'rohan', 'tcs', 'bhubaneswar', 'India'),
(3, 'baramunda', 'jyoti', 'wipro', 'bbsr', 'India'),
(4, 'hawkins', 'hopper', 'capgemini', 'san', 'American Samoa');

-- --------------------------------------------------------

--
-- Table structure for table `payroll`
--

CREATE TABLE `payroll` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emp_code` varchar(200) NOT NULL,
  `salary` int(11) NOT NULL,
  `loan` int(11) NOT NULL,
  `hour` int(11) NOT NULL,
  `deduction` int(11) NOT NULL,
  `final_salary` int(11) NOT NULL,
  `pay_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payroll`
--

INSERT INTO `payroll` (`id`, `name`, `emp_code`, `salary`, `loan`, `hour`, `deduction`, `final_salary`, `pay_date`) VALUES
(8, 'rohan', '234', 2000, 0, 45, 500, 1500, '2022-05-13'),
(9, 'deepak', '596', 5000, 0, 0, 1300, 3700, '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `id` int(11) NOT NULL,
  `project_name` varchar(200) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `details` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`id`, `project_name`, `start_date`, `end_date`, `status`, `details`) VALUES
(1, 'Hrmm', '2022-04-27', '2022-04-19', 'process', ''),
(5, 'ERP', '2022-05-04', '2023-06-26', 'Process', ''),
(6, 'restrant', '2022-05-11', '2022-06-03', 'process', 'diusiudnluisdnpudincoud'),
(7, 'agri', '2022-06-01', '2022-06-20', 'Complete', 'hfjdshssjkjsfs;dsnsksndsndskjnsd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `designation`
--
ALTER TABLE `designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payroll`
--
ALTER TABLE `payroll`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_login`
--
ALTER TABLE `admin_login`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `designation`
--
ALTER TABLE `designation`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `payroll`
--
ALTER TABLE `payroll`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
