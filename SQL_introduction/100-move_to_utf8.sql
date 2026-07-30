-- converts hbtn_0c_0 database and first_table to utf8mb4/utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- selects the database so the table can be altered
USE hbtn_0c_0;

-- converts first_table and all its columns to utf8mb4/utf8mb4_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
