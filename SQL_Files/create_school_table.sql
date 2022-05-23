DROP TABLE IF EXISTS schools;
CREATE TABLE schools (
    charter varchar(255),
    school_name varchar(255),
    school_type varchar(255),
    district_name varchar(255),
    enrollment SMALLINT,
    available_grades INT[13]
)