
#already maded queries

add = {
    'ADD USERS': "INSERT INTO users (name, username, password) VALUES (?,?,?)",
    'ADD SERIES': 'INSERT INTO serie (name, start_date, synopse, category_id) VALUES (?,?,?,?)',
    'ADD EPISODE': 'INSERT INTO episode (name, description, serie_id) VALUES (?,?,?)',
    'ADD CLASSIFICATION': 'INSERT INTO classification (initials, description) VALUES (?,?)',
    'ADD CATEGORY': 'INSERT INTO category(name, description) VALUES (?,?)'
}
#removes should be done by id, but not working for the timebeing
remove = {
    'REMOVE USERS': 'DELETE FROM users WHERE users.name = ?;',
    'REMOVE SERIE': 'DELETE FROM serie WHERE serie.name = ?;',
    'REMOVE EPISODE': 'DELETE FROM episode WHERE episode.name = ?;'
}

remove_all = {
    'REMOVE ALL USERS': 'DELETE FROM users;',
    'REMOVE ALL SERIES': 'DELETE FROM serie;',
    'REMOVE ALL EPISODES': 'DELETE FROM episode;'
}

show_all ={
    'SHOW ALL USERS': 'SELECT * FROM users;',
    'SHOW ALL SERIES': 'SELECT * FROM serie;',
    'SHOW ALL EPISODES': 'SELECT * FROM episode;',
    'SHOW ALL CATEGORY': 'SELECT * FROM category;',
    'SHOW ALL CLASSIFICATION': 'SELECT * FROM classification;'
}

update = {
    'UPDATE USER': 'UPDATE users SET users.name = ?, users.username = ?, users.password = ? WHERE (users.id = ?);',
    'UPDATE SERIE': 'UPDATE serie SET serie.synopse = ?  WHERE serie.id = ? AND serie.category_id = ?;'
}

showID = {
    'SHOW USER': 'SELECT * FROM users WHERE users.id=?;',
    'SHOW SERIE': 'SELECT * FROM serie where serie.id=?;',
    'SHOW EPISODE': 'SELECT * FROM episode where episode.id=?;',
}
