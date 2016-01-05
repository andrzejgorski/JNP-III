INSERT INTO posts (title, content, user_id) VALUES
    ( 'testing', 'cipka',   (SELECT id from users WHERE id=72) );
