INSERT INTO users (first_name, last_name, email)
VALUES ("JOHN","POTT","JOHN@codingdojo.com"),
("Mr. HART","JUSTIN","HART@HART.com"),
("DEANNA","PRALL","PRALL@gmail.com");


SELECT * FROM users;

SELECT * FROM users
WHERE email = 'JOHN@codingdojo.com';

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "HART"
WHERE users.id = 3;


DELETE FROM users
WHERE users.id = 2;

SELECT * FROM users
ORDER BY first_name DESC;