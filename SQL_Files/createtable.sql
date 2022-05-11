DROP TABLE IF EXISTS districts;
CREATE TABLE districts (
    districtName TINYTEXT,
    districtType TINYTEXT,
    enrollment MEDIUMINT,
)

DROP TABLE IF EXISTS schools;
CREATE TABLE schools (
    isCharter TINYTEXT
    schoolName TINYTEXT
    schoolType TINYTEXT
    enrollment MEDIUMINT
)