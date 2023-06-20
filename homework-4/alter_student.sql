-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE students
(
	student_id serial,
	first_name varchar(20),
	last_name varchar(20),
	birthday date,
	phone varchar(15)
)

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE students ADD COLUMN middle_name varchar(20);

-- 3. Удалить колонку middle_name
ALTER TABLE students DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE students RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE students ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO students (first_name, last_name, birth_date, phone) VALUES
('Dmitriy', 'Fedorov', '1983-04-22', '88005553535'),
('Sergey', 'Alekseev', '1976-05-07', '+74835553322'),
('Vladislav', 'Sergeev', '1972-01-23', '86787946123');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE students RESTART IDENTITY;