CREATE TABLE course (
course_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
course_name VARCHAR (35),
pet_type CHAR(20),
course_level CHAR(15),
start_date DATE,
start_time TIME,
course_duration VARCHAR(30),
course_length VARCHAR(30),
trainer VARCHAR(30),
description VARCHAR(200)
) ENGINE=INNODB;

CREATE TABLE attendee (
attendee_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
course_id INT NOT NULL,
f_name VARCHAR(15),
l_name VARCHAR(20),
phone_number VARCHAR (15),
email VARCHAR(30),
date_of_birth DATE,
comment VARCHAR (50),
FOREIGN KEY (course_id) REFERENCES course(course_id)
) ENGINE=INNODB;


INSERT INTO course (course_id, course_name, pet_type, course_level, start_date, start_time, course_duration, course_length, trainer, description) VALUES
(1, "New Paws", "Dog", "Beginner", "2022-04-03", "09:00 AM", 45, 6, "Bill Gates","Nothing required, just bring your dog. And be prepared to hear barking!"),
(2,"Morning Obedience","Hamster","Intermediate", "2022-07-05","12:00 PM", 60, 4, "Patrick Star", "This course will train hamsters how to stay independent early in the mornings. Bring hamster cage and any other items the hamster may have."),
(3, "Glamour Photography for your Kitty", "Cat", "Advanced", "2022-09-12", "02:30 PM", 90, 8, "John Cena", "Your cat will learn how to become a model! Be sure to bring any props you like and an preferrenced camera."), 
(4, "Ferret Bueller's Day Off", "Ferret", "Beginner", "2022-10-31", "03:45 PM", 60, 6, "Barrack Obama", "This course will teach your ferret how to have a good time. Literally! Nothing necessary, just bring your ferret"),
(5, "Garfield's Training: Lazy Everyday", "Cat", "Beginner", "2022-11-23", "11:00 AM", 60, 6, "Garfield", "Learn how to make your cat even lazier. Trained by the greatest expert himself."),
(6, "How to find the Biggest Bones", "Dog", "Advanced", "2022/12/12", "8:30 AM", 45, 4, "Elon Musk", "Join the richest man in the world as he trains your dog how to find the biggest bones. Be prepared to take home dinosaur bones.");

SELECT FORMAT(CAST(start_time AS time), 'hh\:mm tt') 'time';


-- Used these to test functions

INSERT INTO course (course_name, pet_type, course_level, start_date, start_time, course_duration, course_length, trainer, description)  VALUES ("jonah", "dog", "beginner", "2022-11-07","9:00 AM", '9', 45, "Jonah", "This course suckksssssss");

UPDATE course 
SET course_name="meow", pet_type="cat", course_level="easy", start_date="2022-11-07", start_time="9:00 AM", course_duration='9', course_length=45, trainer="Jonah", description="Whats upppppppp" 
WHERE course_id= 7