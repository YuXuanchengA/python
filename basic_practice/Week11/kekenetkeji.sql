-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2019-12-18 02:14:35
-- 服务器版本： 10.1.38-MariaDB
-- PHP 版本： 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `kekenet`
--

-- --------------------------------------------------------

--
-- 表的结构 `kekenetkeji`
--

CREATE TABLE `kekenetkeji` (
  `id` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `abstract` varchar(500) NOT NULL,
  `date` varchar(100) NOT NULL,
  `editor` varchar(50) NOT NULL,
  `sort` varchar(100) NOT NULL,
  `link` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `kekenetkeji`
--

INSERT INTO `kekenetkeji` (`id`, `title`, `abstract`, `date`, `editor`, `sort`, `link`) VALUES
(16, '小米推出智能手表Mi Watch', '小米已在国内市场推出第一款智能手表Mi Watch，外观和Apple Watch特别像。', '2019-11-18', 'Kelly', '智能手表 小米 双语新闻', 'http://www.kekenet.com/read/201911/599584.shtml'),
(17, '新型神经网络可以用快1亿倍速度解决\"三体问题\"', '三体问题是物理学中最复杂的计算题之一，但它在人工智能领域可能遇到了对手：一种新型神经网络有望以比现有技术快1亿倍的速度找出其解决方案。', '2019-11-14', 'Kelly', '双语新闻 神经网络 三体问题', 'http://www.kekenet.com/read/201911/599412.shtml'),
(18, '14岁女孩发明可替代抗生素的液体绷带', '一个14岁的科学家发明了一种可替代抗生素的液体绷带，在全国科学竞赛上赢得了25,000美元奖金。', '2019-11-13', 'Kelly', '双语新闻 液体绷带 抗生素', 'http://www.kekenet.com/read/201911/599335.shtml'),
(19, '特斯拉推出新版太阳能屋顶', '特斯拉推出了第三代家用太阳能光伏瓦。', '2019-11-07', 'Kelly', '双语新闻 特斯拉 太阳能屋顶', 'http://www.kekenet.com/read/201911/598810.shtml'),
(20, '苹果推出AirPods Pro无线降噪耳机', '苹果推出AirPods Pro无线降噪耳机，形似豌豆射手。', '2019-11-05', 'Kelly', '双语新闻 苹果 无线降噪耳机', 'http://www.kekenet.com/read/201911/598555.shtml'),
(21, '新的基因编辑技术诞生', '美国科学家已研发出强大的新的基因组编辑系统，显著提高目前CRISPR标准的精度和效率。', '2019-11-01', 'Kelly', '双语新闻 基因编辑 精准 风险', 'http://www.kekenet.com/read/201911/598372.shtml'),
(22, '特斯拉辟谣:没有推出悬浮滑板', '一段所谓特斯拉最新产品的视频被发布到了YouTube上，好像在社交媒体上引起了轩然大波。', '2019-10-31', 'Kelly', '双语新闻 特斯拉 辟谣 悬浮滑板', 'http://www.kekenet.com/read/201910/598297.shtml'),
(23, '基因检测结果呈阴性可能是\"虚假的安慰\"', '最新研究指出，即使基因检测结果呈阴性，人们也不能完全放松警惕，因为这可能是“虚假的安慰”。', '2019-10-29', 'Kelly', '双语新闻 基因检测 阴性 突变基因', 'http://www.kekenet.com/read/201910/597973.shtml'),
(24, '三星指纹传感曝出重大漏洞', '三星证实S10和Note 10智能手机上创新的屏下指纹阅读器存在问题，三天后该公司向数百万用户发出了更严肃的警告。', '2019-10-28', 'Kelly', '双语新闻 三星 指纹传感 漏洞', 'http://www.kekenet.com/read/201910/597902.shtml'),
(25, 'NASA工程师提出的引擎概念能达到光速的99%', 'NASA工程师David Burns提出了一个引擎概念，理论上可以加速到光速的99%，而且完全不用推进剂。', '2019-10-23', 'Kelly', '引擎概念 NASA 双语新闻 光速', 'http://www.kekenet.com/read/201910/597617.shtml'),
(26, '睡眠少身体棒的体质由基因决定', '白天时间不够用，晚上睡眠不好？但现实生活中，确实有些人每天睡眠时间很短，却精神饱满。为什么有些人每天只需要睡4、5个小时？这其实是由基因决定的。', '2019-10-23', 'Kelly', '双语新闻 睡眠 身体 基因', 'http://www.kekenet.com/read/201910/597616.shtml'),
(27, '波音和保时捷要联手开发飞行电动汽车', '波音和保时捷想要研发会飞的电动汽车。', '2019-10-21', 'Kelly', '双语新闻 波音 保时捷 飞行电动汽车', 'http://www.kekenet.com/read/201910/597349.shtml'),
(28, '3D打印机造出太空人造肉', '在宇宙飞船大口吃肉，享用完还可以自己3D打印一份留到下顿，这听着像不像科幻小说的情节？最近，科学家研制出的3D生物打印机就把这一梦想变为现实。', '2019-10-16', 'Kelly', '双语新闻 3D打印机 太空人造肉 宇航员', 'http://www.kekenet.com/read/201910/596906.shtml'),
(29, '全世界最黑的材料被研发出来了', '你可能认为你已经知道黑色，甚至是曾经科学已知的最黑的材料——特黑的Vantablack，但研究人员刚提出了一种材料，它把黑度提高到了一个新的层次。', '2019-10-11', 'Kelly', '双语新闻 黑色 材料', 'http://www.kekenet.com/read/201910/596457.shtml'),
(30, '瑞典搞出了面试机器人腾艾', '首席机器人腾艾被委托在瑞典乌普兰斯布罗市进行招聘。', '2019-10-10', 'Kelly', '双语新闻 瑞典 机器人 面试', 'http://www.kekenet.com/read/201910/596357.shtml');

--
-- 转储表的索引
--

--
-- 表的索引 `kekenetkeji`
--
ALTER TABLE `kekenetkeji`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `kekenetkeji`
--
ALTER TABLE `kekenetkeji`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
