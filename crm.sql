BEGIN;
CREATE TABLE `main_goods` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(30) NOT NULL,
    `price` numeric(10, 2) NOT NULL,
    `description` longtext NOT NULL
)
;
CREATE TABLE `main_operator` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(30) NOT NULL,
    `level` smallint UNSIGNED NOT NULL,
    `account` varchar(30) NOT NULL UNIQUE,
    `password` varchar(30) NOT NULL
)
;
CREATE TABLE `main_stock` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `extra` integer UNSIGNED NOT NULL,
    `goods_id` integer NOT NULL
)
;
ALTER TABLE `main_stock` ADD CONSTRAINT `goods_id_refs_id_382c9536` FOREIGN KEY (`goods_id`) REFERENCES `main_goods` (`id`);
CREATE TABLE `main_outer` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `number` integer UNSIGNED NOT NULL,
    `goods_id` integer NOT NULL,
    `operator_id` integer NOT NULL,
    `time` datetime NOT NULL
)
;
ALTER TABLE `main_outer` ADD CONSTRAINT `goods_id_refs_id_576520c2` FOREIGN KEY (`goods_id`) REFERENCES `main_goods` (`id`);
ALTER TABLE `main_outer` ADD CONSTRAINT `operator_id_refs_id_b858fb9b` FOREIGN KEY (`operator_id`) REFERENCES `main_operator` (`id`);
CREATE TABLE `main_inner` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `number` integer UNSIGNED NOT NULL,
    `goods_id` integer NOT NULL,
    `operator_id` integer NOT NULL,
    `time` datetime NOT NULL
)
;
ALTER TABLE `main_inner` ADD CONSTRAINT `goods_id_refs_id_9dd10ff7` FOREIGN KEY (`goods_id`) REFERENCES `main_goods` (`id`);
ALTER TABLE `main_inner` ADD CONSTRAINT `operator_id_refs_id_ed6a4ddc` FOREIGN KEY (`operator_id`) REFERENCES `main_operator` (`id`);
CREATE TABLE `main_customer` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(30) NOT NULL,
    `tele_phone` integer UNSIGNED NOT NULL,
    `mobile_phone` integer UNSIGNED NOT NULL,
    `email` varchar(75) NOT NULL,
    `address` varchar(60) NOT NULL,
    `account` varchar(30) NOT NULL UNIQUE,
    `password` varchar(30) NOT NULL
)
;
CREATE TABLE `main_order` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `customer_id` integer NOT NULL,
    `goods_id` integer NOT NULL,
    `number` integer UNSIGNED NOT NULL,
    `time` datetime NOT NULL
)
;
ALTER TABLE `main_order` ADD CONSTRAINT `customer_id_refs_id_2036e762` FOREIGN KEY (`customer_id`) REFERENCES `main_customer` (`id`);
ALTER TABLE `main_order` ADD CONSTRAINT `goods_id_refs_id_d7446ad9` FOREIGN KEY (`goods_id`) REFERENCES `main_goods` (`id`);
CREATE INDEX `main_stock_2b897762` ON `main_stock` (`goods_id`);
CREATE INDEX `main_outer_2b897762` ON `main_outer` (`goods_id`);
CREATE INDEX `main_outer_5e7ba3ec` ON `main_outer` (`operator_id`);
CREATE INDEX `main_inner_2b897762` ON `main_inner` (`goods_id`);
CREATE INDEX `main_inner_5e7ba3ec` ON `main_inner` (`operator_id`);
CREATE INDEX `main_order_09847825` ON `main_order` (`customer_id`);
CREATE INDEX `main_order_2b897762` ON `main_order` (`goods_id`);

COMMIT;
