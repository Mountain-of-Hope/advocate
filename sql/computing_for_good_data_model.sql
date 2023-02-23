/*
Create dimension tables for sponsors and time
*/

CREATE TABLE church_dim (
  church_id INT PRIMARY KEY,
  church_name VARCHAR(100) NOT NULL,
  church_address VARCHAR(200),
  church_email VARCHAR(100),
  church_phone VARCHAR(20)
);

CREATE TABLE time_dim (
  date_key INT PRIMARY KEY,
  date_actual DATE NOT NULL,
  year INT NOT NULL,
  quarter INT NOT NULL,
  month INT NOT NULL,
  day_of_month INT NOT NULL,
  day_of_week INT NOT NULL,
  week_of_year INT NOT NULL
);

CREATE TABLE sponsor_dim (
  sponsor_id INT PRIMARY KEY,
  church_id INT,
  sponsor_name VARCHAR(100) NOT NULL,
  sponsor_address VARCHAR(200),
  sponsor_email VARCHAR(100),
  sponsor_phone VARCHAR(20),
  FOREIGN KEY (church_id) REFERENCES church_dim(church_id)
);

CREATE TABLE student_dim (
  student_id INT PRIMARY KEY,
  sponsor_id INT,
  church_id INT,
  student_name VARCHAR(100) NOT NULL,
  student_address VARCHAR(200),
  student_email VARCHAR(100),
  student_phone VARCHAR(20),
  FOREIGN KEY (sponsor_id) REFERENCES sponsor_dim(sponsor_id),
  FOREIGN KEY (church_id) REFERENCES church_dim(church_id)
);

/*
Create a donation fact table to hold the details of each donation.
The fact table will include the foreign keys that link to the dimension tables
*/

CREATE TABLE donation_fact (
  donation_id INT PRIMARY KEY,
  student_id INT NOT NULL,
  sponsor_id INT NOT NULL,
  church_id INT,
  donation_amount DECIMAL(10, 2) NOT NULL,
  donation_date DATE NOT NULL,
  donation_type VARCHAR(50) NOT NULL,
  donation_note VARCHAR(500),
  FOREIGN KEY (sponsor_id) REFERENCES sponsor_dim(sponsor_id),
  FOREIGN KEY (church_id) REFERENCES church_dim(church_id)
);

/*
Populate the dimension tables with fake data
*/

INSERT INTO church_dim (church_id, church_name, church_address, church_email, church_phone)
VALUES (1, 'John Smith', '123 Main St, Anytown USA', 'johnsmith@email.com', '555-1234'),
      (2, 'Jane Doe', '456 Maple Ave, Somewhere USA', 'janedoe@email.com', '555-5678');

INSERT INTO sponsor_dim (sponsor_id, church_id, sponsor_name, sponsor_address, sponsor_email, sponsor_phone)
VALUES (1, 1, 'John Smith', '123 Main St, Anytown USA', 'johnsmith@email.com', '555-1234'),
       (2, 2, 'Jane Doe', '456 Maple Ave, Somewhere USA', 'janedoe@email.com', '555-5678');
     
INSERT INTO student_dim (student_id, sponsor_id, church_id, student_name, student_address, student_email, student_phone)
VALUES (1, 1, 1, 'John Smith', '123 Main St, Anytown USA', 'johnsmith@email.com', '555-1234'),
      (2, 1, 2, 'Jane Doe', '456 Maple Ave, Somewhere USA', 'janedoe@email.com', '555-5678');
     
INSERT INTO time_dim (date_key, date_actual, year, quarter, month, day_of_month, day_of_week, week_of_year)
VALUES (20220216, '2022-02-16', 2022, 1, 2, 16, 4, 7),
       (20220217, '2022-02-17', 2022, 1, 2, 17, 5, 7),
       (20220218, '2022-02-18', 2022, 1, 2, 18, 6, 7);

/*
Populate the donation fact table with fake data
*/
INSERT INTO donation_fact (donation_id, student_id, sponsor_id, church_id, donation_amount, donation_date, donation_type)
VALUES (1, 1, 1, 1, 100.00, '2022-02-16', 'General'),
       (2, 1, 1, 1, 50.00, '2022-02-17', 'General'),
       (3, 1, 2, 2, 75.00, '2022-02-18', 'General');
