
CREATE TABLE la_liga_teams (
    `team_id` VARCHAR(20) PRIMARY KEY NOT NULL,       -- Identificador único para cada time
    `api_id` VARCHAR(10) NULL,                        -- ID do time na API de futebol
    `team_name` VARCHAR(80) NOT NULL,                 -- Nome do time
    `alternative_team_name` VARCHAR(80) NULL,
    `short_team_name` VARCHAR(7) NULL,                -- Nome curto do time
    `formed_year` VARCHAR(4) NULL,                    -- Ano de fundação do time
    `sport` VARCHAR(10) NULL,                         -- Tipo de esporte
    `location_team` VARCHAR(30) NULL,                 -- Localização do time
    `stadium_team` VARCHAR(30) NULL,                  -- Nome do estádio
    `description_team` VARCHAR(250) NULL,             -- Descrição do time em inglês
    `gender` VARCHAR(10) NULL,                        -- Gênero do time (masculino, feminino, etc.)
    `country_team` VARCHAR(10) NULL,                  -- País do time
    `badge_team` VARCHAR(250) NULL,                   -- URL do escudo do time
    `logo_team` VARCHAR(250) NULL                     -- URL do logo do time
);