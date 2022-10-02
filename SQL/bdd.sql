-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           5.7.33 - MySQL Community Server (GPL)
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour books-rating
CREATE DATABASE IF NOT EXISTS `books-rating` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `books-rating`;

-- Listage de la structure de la table books-rating. books
CREATE TABLE IF NOT EXISTS `books` (
  `id_books` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL DEFAULT '0',
  `author` varchar(50) DEFAULT '0',
  `category` varchar(50) DEFAULT '0',
  `rating` tinyint(1) unsigned DEFAULT '0',
  `comments` text,
  `status` varchar(50) DEFAULT NULL,
  `id_user` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_books`),
  KEY `FK_books_users` (`id_user`),
  CONSTRAINT `FK_books_users` FOREIGN KEY (`id_user`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

-- Listage des données de la table books-rating.books : ~4 rows (environ)
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` (`id_books`, `title`, `author`, `category`, `rating`, `comments`, `status`, `id_user`) VALUES
	(24, 'Les Trois Mousquetaires', 'Alexandre Dumas', 'Romans Historique', 7, 'Les aventures de D\'Artagnan, Athos, Porthos et Aramis, 4 mousquetaires au temps du Roi Louis XII. Ils déjouent les complots du Cardinal de Richelieu contre la reine Anne d\'Autriche.', 'progress', 9);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;

-- Listage de la structure de la procédure books-rating. sp_addBook
DELIMITER //
CREATE PROCEDURE `sp_addBook`(
	IN `p_title` varchar(45),
	IN `p_author` VARCHAR(45),
	IN `p_category` VARCHAR(45),
	IN `p_rating` TINYINT,
	IN `p_comments` TEXT(1000),
	IN `p_status` VARCHAR(50),
	IN `p_user_id` BIGINT
)
BEGIN
    INSERT INTO books (title, author, category, rating, comments, status, id_user) VALUES (
    p_title, p_author, p_category, p_rating, p_comments, p_status, p_user_id);
    
END//
DELIMITER ;

-- Listage de la structure de la procédure books-rating. sp_createUser
DELIMITER //
CREATE PROCEDURE `sp_createUser`(
	IN `p_name` VARCHAR(20),
	IN `p_username` VARCHAR(50),
	IN `p_password` VARCHAR(200)
)
BEGIN
    if ( select exists (select 1 from users where user_username = p_username) ) THEN
      
        select 'Username Exists !!';
      
    ELSE
      
        insert into users
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
      
    END IF;
END//
DELIMITER ;

-- Listage de la structure de la procédure books-rating. sp_deleteBook
DELIMITER //
CREATE PROCEDURE `sp_deleteBook`(
IN p_book_id bigint,
IN p_user_id bigint
)
BEGIN
delete from books WHERE id_books = p_book_id and id_user = p_user_id;
END//
DELIMITER ;

-- Listage de la structure de la procédure books-rating. sp_editBook
DELIMITER //
CREATE PROCEDURE `sp_editBook`(
	IN `p_title` varchar(45),
	IN `p_author` VARCHAR(45),
	IN `p_category` VARCHAR(45),
	IN `p_rating` TINYINT,
	IN `p_comments` TEXT(1000),
	IN `p_status` VARCHAR(50),
	IN `p_user_id` BIGINT,
	IN `p_id_book` BIGINT
)
BEGIN
    UPDATE books SET title = p_title, author = p_author, category = p_category, rating = p_rating, status = p_status, comments = p_comments
    WHERE id_books = p_id_book AND id_user = p_user_id;
    
END//
DELIMITER ;

-- Listage de la structure de la procédure books-rating. sp_getBookById
DELIMITER //
CREATE PROCEDURE `sp_getBookById`(
IN p_user_id BIGINT,
IN p_book_id BIGINT
)
BEGIN
    select * from books where id_user = p_user_id AND id_books = p_book_id;
END//
DELIMITER ;

-- Listage de la structure de la procédure books-rating. sp_getBooksByUser
DELIMITER //
CREATE PROCEDURE `sp_getBooksByUser`(
IN p_user_id bigint
)
BEGIN
    select * from books where id_user = p_user_id;
END//
DELIMITER ;

-- Listage de la structure de la procédure books-rating. sp_validateLogin
DELIMITER //
CREATE PROCEDURE `sp_validateLogin`(
	IN `p_username` VARCHAR(50)
)
BEGIN
    select * from users where user_username = p_username;
END//
DELIMITER ;

-- Listage de la structure de la table books-rating. users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_username` varchar(45) DEFAULT NULL,
  `user_password` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Listage des données de la table books-rating.users : ~9 rows (environ)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`user_id`, `user_name`, `user_username`, `user_password`) VALUES
	(9, 'Ulysse', 'ulysse.valdenairepro@gmail.com', 'pbkdf2:sha256:260000$67AvNNKKz6xAMQL6$3bb48832acbd6ece5d4b70cc4918e8c313689ef3b15f409ccb138f7949e87297');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
