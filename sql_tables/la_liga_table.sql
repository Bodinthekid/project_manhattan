CREATE TABLE la_liga_table (
    `position` INT AUTO_INCREMENT PRIMARY KEY,  -- Posição na tabela do campeonato
    `internal_team_id` INT NOT NULL,            -- ID interno do time (vem de `la_liga_teams`)
    `team_name` VARCHAR(80) NOT NULL,           -- Nome do time
    `played` INT NOT NULL,                      -- Jogos disputados
    `wins` INT NOT NULL,                        -- Vitórias
    `draws` INT NOT NULL,                       -- Empates
    `losses` INT NOT NULL,                      -- Derrotas
    `goals_for` INT NOT NULL,                   -- Gols marcados
    `goals_against` INT NOT NULL,               -- Gols sofridos
    `goal_difference` INT NOT NULL,             -- Saldo de gols
    `points` INT NOT NULL,                      -- Pontuação
    `recent_form` VARCHAR(10) NOT NULL,         -- Últimos resultados (ex: "wdwldw"),
    FOREIGN KEY (`internal_team_id`) REFERENCES la_liga_teams (`internal_team_id`) ON DELETE CASCADE
);
