DROP TABLE IF EXISTS weird_table;
CREATE TABLE weird_table(id INTEGER PRIMARY KEY, name VARCHAR(100), dislike INTEGER);
INSERT INTO weird_table VALUES (1001, 'Gxd', 0);
INSERT INTO weird_table VALUES (109, 'Damian', 3);
INSERT INTO weird_table VALUES (379, 'Magnus', 1);
INSERT INTO weird_table VALUES (28, 'Ronan', 2);
SELECT id FROM weird_table #shutuppp