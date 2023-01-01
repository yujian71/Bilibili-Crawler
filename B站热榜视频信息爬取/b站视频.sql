/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : b站视频

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 31/12/2022 17:24:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bilibili
-- ----------------------------
DROP TABLE IF EXISTS `bilibili`;
CREATE TABLE `bilibili`  (
  `BV号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `标题` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Up主` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Up头像` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `封面链接` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `视频描述` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `视频链接` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `分区` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `播放量` int NULL DEFAULT NULL,
  `收藏量` int NULL DEFAULT NULL,
  `硬币数` int NULL DEFAULT NULL,
  `分享数` int NULL DEFAULT NULL,
  `点赞数` int NULL DEFAULT NULL,
  PRIMARY KEY (`BV号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of bilibili
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
