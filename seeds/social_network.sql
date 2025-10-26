-- file: social_network.sql

DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS posts CASCADE;

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email text,
  username text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  number_of_views int,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email, username) VALUES 
('superman@solitude.com', 'Superman'),
('batman@batcave.com', 'Batman'),
('aquaman@atlantis.com', 'Aquaman'),
('wonderwoman@amazon.com', 'Wonderwoman'),
('flash@flash.com', 'Barry');

INSERT INTO posts (title, content, number_of_views, user_id) VALUES
('Hello World', 'My first post on Earth!', 5, 1),
('I am Batman', 'I am rich and I am Batman', 12, 2),
('My favorite book', 'Just finished reading Waterworld', 8, 3),
('Weekend plans', 'Saving the world!', 3, 4),
('NEWS FLASH!', 'I want to run in the Olympics', 3, 5);