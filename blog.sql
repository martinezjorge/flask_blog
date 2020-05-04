PRAGMA synchronous = OFF;
PRAGMA journal_mode = MEMORY;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` INTEGER NOT NULL,
  `username` VARCHAR(20) NOT NULL,
  `password` VARCHAR(20),
  `first_name` VARCHAR(30),
  `last_name` VARCHAR(30),
  `email` VARCHAR(60) NOT NULL UNIQUE,
  `image_file` BLOB,
  PRIMARY KEY (`username`)
);
INSERT INTO `user` VALUES
(1,'testing','testing','test','tester','test@test.com','default.jpg'),
(2,'coolguy','coolio','Jorge','Martinez','jorge@jorge.com','default.jpg'),
(3,'meanguy','meanie','Darlene','Martinez','meangirl@mean.com','default.jpg'),
(4,'rosegirl','roses','Rosa','Parks','parks@justice.com','default.jpg'),
(5,'liberator','carpetbagger','Frederick','Douglas','fdouglas@north.com','default.jpg'),
(6,'dreamer','ihadadream','Martin','King','mking@rights.com','default.jpg'),
(7,'pacifist','love','Mohatmad','Ghandi','mghandi@love.com','default.jpg'),
(8,'hater','killthemall','Adolf','Hitler','ahitler@gmail.com','default.jpg'),
(9,'groovyman','yeahbaby','Austin','Powers','apowers@shag.com','default.jpg'),
(10,'kleptomaniac','stealeverything','mr','stealie','mrstealie@randm.com','default.jpg'),
(11,'chemist','meth','Walter','White','whwhite@chem.com','default.jpg');

DROP TABLE IF EXISTS `hobbies`;
CREATE TABLE `hobbies` (
  `username` VARCHAR(20),
  `hobby` VARCHAR(50),
  PRIMARY KEY (`username`, 'hobby'),
  FOREIGN KEY ('username') REFERENCES `user`
);
INSERT INTO `hobbies` VALUES
('testing','testing stuff'),
('coolguy','chilling and stuff'),
('meanguy','being a jerk'),
('rosegirl','gardening'),
('liberator','fighting for rights'),
('dreamer','defending my people'),
('pacifist','solving conflicts without violence'),
('hater','hating'),
('groovyman','shagging'),
('kleptomaniac','stealing'),
('chemist','science shit');

DROP TABLE IF EXISTS `follows`;
CREATE TABLE `follows` (
  `leader` VARCHAR(20),
  `follower` VARCHAR(50),
  PRIMARY KEY (`leader`, 'follower'),
  FOREIGN KEY ('leader') REFERENCES `user` ('username'),
  FOREIGN KEY ('follower') REFERENCES `user` ('username')
);
INSERT INTO `follows` VALUES
('hater','coolguy'),
('hater','meanguy'),
('hater','rosegirl'),
('hater','liberator'),
('hater','dreamer'),
('hater','pacifist'),
('hater','hater'),
('hater','groovyman'),
('hater','kleptomaniac'),
('coolguy','testing'),
('meanguy','testing'),
('rosegirl','testing'),
('liberator','pacifist'),
('dreamer','pacifist'),
('pacifist','pacifist'),
('hater','chemist'),
('groovyman','rosegirl'),
('kleptomaniac','rosegirl');

DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `blog_id` INTEGER NOT NULL,
  `subject` VARCHAR(50),
  `description` VARCHAR(250),
  `user_id` VARCHAR(20) NOT NULL,
  `date_blogged` DATE,
  PRIMARY KEY (`blog_id`),
  FOREIGN KEY ('user_id') REFERENCES `user` ('id')
);
INSERT INTO `blog` VALUES
(1,'Gardening Roses','Here I will show you how to plant roses. First dig a hole. Put the roses in. Give them time.','rosegirl','2020-02-10 11:28:51.756825'),
(2,'Being Cool','Take it easy. Do not try too hard.','coolguy','2020-02-10 11:28:51.756825'),
(3,'Being Groovy','Behave! Do not make me come over there!','groovyman','2020-02-10 11:28:51.756825'),
(4,'Its my birthday','Happy birthday to me!','liberator','2020-02-10 11:28:51.756825'),
(5,'How to Steal Stuff','Just get anything that is in sight. Could be anything worthless or not just get it stuff it in your pocket.','kleptomaniac','2020-02-11 11:28:51.756825'),
(6,'Transferring Roses from Pots','This can be a very delicate process','rosegirl','2020-02-12 11:28:51.756825'),
(7,'Respecting Ourselves','Everyone is someone and worth something. Never forget it.','dreamer','2020-02-12 11:28:51.756825'),
(8,'How to Steal Stuff 2','Even if you do not really want that item. Just take it anyways and you will feel much better!','kleptomaniac','2020-02-12 11:28:51.756825'),
(9,'I told you I would go!','Now I am here and ready to teach you a lesson. Oh behave!','groovyman','2020-02-13 11:28:51.756825'),
(10,'Respecting Others!','Just like you are worth something. So are others. Its important that we face hate with pride and destroy it with kindess.','dreamer','2020-02-13 11:28:51.756825'),
(11,'Running from the Law','Its important that even as the law is closing in on you, you take as many things as possible. You dont know when you will get a chance to steal again.','kleptomaniac','2020-02-14 11:28:51.756825');

DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `blog_id` INTEGER NOT NULL,
  `tag` VARCHAR(20),
  PRIMARY KEY (`blog_id`, 'tag'),
  FOREIGN KEY ('blog_id') REFERENCES `blog`
);
INSERT INTO `tag` VALUES
(1,'gardening'),
(2,'coolness'),
(3,'grooviness'),
(4,'birthday'),
(5,'stealing'),
(6,'gardening'),
(7,'self-respect'),
(8,'stealing'),
(9,'grooviness'),
(10,'self-respect'),
(11,'stealing');

DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` INTEGER NOT NULL,
  `sentiment` VARCHAR(50),
  `description` VARCHAR(250),
  `date_commented` DATE,
  `blog_id` NOT NULL,
  `user_id` VARCHAR(20) NOT NULL,
PRIMARY KEY ('comment_id'),
FOREIGN KEY ('blog_id') REFERENCES `blog`,
FOREIGN KEY ('user_id') REFERENCES `user` ('id')
);
INSERT INTO `comment` VALUES
(1,'positive','this was a great blog. see you later!','2020-02-10',0,'coolguy'),
(2,'positive','youre so cool','2020-02-10',1,'rosegirl'),
(3,'negative','what a terrible blog','2020-02-12',6,'hater');